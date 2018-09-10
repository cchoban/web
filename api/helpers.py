import zipfile
import os
from .validators import validate_package, validate_files
from shutil import rmtree, move
from django.core.exceptions import ValidationError
import json
from .models import Package, SubmitPackage
from django.shortcuts import get_object_or_404
from . import Logger as log


class FolderNotFound(Exception):
    pass
class MissingIcons(Exception):
    pass


def createFolder(folderName):
    folder = "./files/" + folderName
    if not os.path.exists(folder):
        os.makedirs(folder)
        return "./files/" + folderName


def createFolders():
    folders = ["uploads", "files"]

    for i in folders:
        folder = os.path.join(i)
        try:
            if not os.path.exists(folder):
                os.makedirs(folder)
        except Exception as e:
            log.new(e).logInfo()
            return True


def handle_uploaded_files(zipRequest):
    withoutExt = str(zipRequest).split('.')[0]
    # write(zipRequest)
    unzip(withoutExt, zipRequest)
    validate = validate_package(withoutExt)
    if isinstance(validate, dict):
        moveIconsToStatic(withoutExt)
        new_json = reDefineJson(withoutExt)
        version = check_package_version(new_json)
        if bool(version["status"]):
            new_json["status"] = True
            return new_json
        else:
            return {"status": False, "message": version["message"]}
    else:
        cleanup(str(zipRequest))
        log.new(ValidationError(
            "We could not validate your JSON file. Be sure you have generated file with the Choban Package Manager.")).logError()
        raise ValidationError(
            "We could not validate your JSON file. Be sure you have generated file with the Choban Package Manager.")

def validateFiles(packageName):
    return validate_files()


def unzip(packageName, zip):
    folder = os.path.abspath(os.path.join("files", packageName))
    try:
        log.new('Extracting file. Package name: {}, Zip File: {}'.format(
            packageName, zip)).logInfo()
        zf = zipfile.ZipFile(zip, "r")
        zf.extractall(folder)
        zf.close()
    except Exception as e:
        log.new(e).logError()
        if e.errno == 17:
            return True


def validatePackage(packageName):
    return validate_package(packageName)


def write(zip):
    try:
        for chunk in zip.chunks():
            with open(os.path.join("uploads", str(zip)), "wb+") as f:
                f.write(chunk)
                f.close()
    except Exception as e:
        log.new(e).logError()
        return False


def cleanup(packageName):
    from django.conf import settings
    filesPath = os.path.join("files/", packageName)
    uploadsPath = os.path.join(settings.BASE_DIR, "uploads/", packageName)

    try:
        log.new('Cleaning up '+packageName).logInfo()
        if os.path.exists(filesPath):
            rmtree(filesPath)
            os.remove(filesPath)

        rmtree(uploadsPath)
        os.remove(uploadsPath)
    except Exception as e:
        log.new(e).logError()
        return False


def moveIconsToStatic(packageName):
    iconsPath = os.path.join("files/", packageName, "icons/")
    destPath = os.path.join("packages", "static",
                            "images", "packages", packageName)
    imageExtensions = ["png", "jpg", "jpeg", "svg"]

    if not os.path.exists(iconsPath):
        log.new('{} and {} does not exists'.format(
            iconsPath, destPath)).logInfo()
        log.new(FileNotFoundError(iconsPath)).logError()

    if len(os.listdir(iconsPath)) < 1:
        log.new(MissingIcons(
            'Missing icons under icons folder, please put one.')).logError()
        raise MissingIcons('Missing icons under icons folder as mentioned in your config file, please put one. ')


    try:
        for i in os.listdir(iconsPath):
            for ext in imageExtensions:
                if i.endswith(ext):
                    image = i
                    if os.path.exists(iconsPath) and not os.path.exists(destPath):
                        move(iconsPath, destPath)
    except Exception as e:
        log.new(e).logError()
        return False


def reDefineJson(packageName):
    validate = validate_package(packageName)
    imagePath = os.path.join("packages", "static",
                             "images", "packages", packageName)
    imageExtensions = ["png", "jpg", "jpeg", "svg"]
    if not os.path.exists(imagePath):
        log.new('{} does not exists '.format(imagePath)).logError()
        raise FileNotFoundError(imagePath)

    if isinstance(validate, dict):
        for i in os.listdir(imagePath):
            for ext in imageExtensions:
                if i.endswith(ext):
                    validate['server'][
                        'icon'] = "/static/images/packages/{0}/{1}".format(packageName, i)
                    return validate
    else:
        log.new(IsADirectoryError('Validated data is not dict!'))
        return False


def validate_json(json_object):
    try:
        return json.loads(json_object)
    except json.JSONDecodeError as e:
        log.new(e).logError()
        return False


def check_package_version(json_object):
    from distutils.version import LooseVersion
    js = json_object
    package_name = js["packageArgs"]["packageName"]
    package_version = LooseVersion(js["packageArgs"]["version"])

    repo = Package.objects.filter(
        packageName=package_name) or SubmitPackage.objects.filter(packageName=package_name)

    if repo.exists():
        repo_version = LooseVersion(repo.get().packageArgs["version"])
        if repo_version >= package_version:
            return {"status": False, "message": "We have never version of this package on system."}
        else:
            return {"status": True, "message": "Update on progress"}
    else:
        return {"status": True, "message": "Success"}
