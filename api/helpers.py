import zipfile
import os
from .validators import validate_package
from shutil import rmtree, move
from django.core.exceptions import ValidationError
import json
from .models import Package, SubmitPackage
from django.shortcuts import get_object_or_404


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
            return True


def handle_uploaded_files(zipRequest):

    createFolders()
    write(zipRequest)
    withoutExt = str(zipRequest).split('.')[0]
    unzip(withoutExt, os.path.join("uploads/", str(zipRequest)))
    validate = validate_package(withoutExt)
    moveIconsToStatic(withoutExt)
    new_json = reDefineJson(withoutExt)

    if validate:
        version = check_package_version(new_json)
        if bool(version["status"]):
            new_json["status"] = True
            return new_json
        else:
            return {"status": False, "message": version["message"]}
    else:
        cleanup(str(zipRequest))
        return ValidationError(
            "We could not validate you JSON file. Be sure you have generated file with the Choban Package Manager.")


def unzip(packageName, zip):
    folder = os.path.abspath(os.path.join("files", packageName))
    try:
        zf = zipfile.ZipFile(zip, "r")
        zf.extractall(folder)
        zf.close()
    except Exception as e:
        if e.errno == 17:
            return True


def validatePackage(packageName):
    return validate_package(packageName)


def write(zip):
    for chunk in zip.chunks():
        with open(os.path.join("uploads", str(zip)), "wb+") as f:
            f.write(chunk)
            f.close()


def cleanup(packageName):
    filesPath = os.path.join("files/", packageName)
    uploadsPath = os.path.join("uploads/")
    try:
        if os.path.exists(filesPath):
            rmtree(filesPath)
            os.remove(filesPath)
    except Exception as e:
        return False


def moveIconsToStatic(packageName):
    iconsPath = os.path.join("files/", packageName, "icons/")
    destPath = os.path.join("packages", "static",
                            "images", "packages", packageName)
    imageExtensions = ["png", "jpg", "jpeg", "svg"]

    for i in os.listdir(iconsPath):
        for ext in imageExtensions:
            if i.endswith(ext):
                image = i
                if os.path.exists(iconsPath) and not os.path.exists(destPath):
                    move(iconsPath, destPath)


def reDefineJson(packageName):
    validate = validate_package(packageName)
    imagePath = os.path.join("packages", "static",
                             "images", "packages", packageName)
    imageExtensions = ["png", "jpg", "jpeg", "svg"]
    if validate:
        for i in os.listdir(imagePath):
            for ext in imageExtensions:
                if i.endswith(ext):
                    validate['server'][
                        'icon'] = "/static/images/packages/{0}/{1}".format(packageName, i)
                    return validate


def validate_json(json_object):
    try:
        return json.loads(json_object)
    except json.JSONDecodeError as e:
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
