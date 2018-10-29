# import zipfile
import os
# from .validators import validate_package, validate_files
# from shutil import rmtree, move
# from django.core.exceptions import ValidationError
# import json
from .models import Package, SubmitPackage
# from django.shortcuts import get_object_or_404
# from . import Logger as log


# class FolderNotFound(Exception):
#     pass
# class MissingIcons(Exception):
#     pass


# def createFolder(folderName):
#     folder = "./files/" + folderName
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#         return "./files/" + folderName


# def createFolders():
#     folders = ["uploads", "files"]

#     for i in folders:
#         folder = os.path.join(i)
#         try:
#             if not os.path.exists(folder):
#                 os.makedirs(folder)
#         except Exception as e:
#             log.new(e).logInfo()
#             return True


# def handle_uploaded_files(zipRequest):
#     withoutExt = str(zipRequest).split('.')[0]
#     isUpgrade = is_upgrade(withoutExt)
#     unzip(withoutExt, zipRequest)
#     validate = validate_package(withoutExt, isUpgrade)

#     if isinstance(validate, dict):
#         moveIconsToStatic(withoutExt, isUpgrade)
#         new_json = reDefineJson(withoutExt, validate, isUpgrade)
#         compress_icon(new_json)
#         version = check_package_version(new_json)
#         if bool(version["status"]):
#             new_json["status"] = True
#             return new_json
#         else:
#             return {"status": False, "message": version["message"]}
#     else:
#         cleanup(withoutExt)
#         log.new(ValidationError(
#             "We could not validate your JSON file. Be sure you have generated file with the Choban Package Manager.")).logError()
#         raise ValidationError(
#             "We could not validate your JSON file. Be sure you have generated file with the Choban Package Manager.")

# def validateFiles(packageName):
#     return validate_files()


# def unzip(packageName, zip):
#     folder = os.path.abspath(os.path.join("files", packageName))
#     try:
#         log.new('Extracting file. Package name: {}, Zip File: {}'.format(
#             packageName, zip)).logInfo()
#         zf = zipfile.ZipFile(zip, "r")
#         zf.extractall(folder)
#         zf.close()
#     except Exception as e:
#         log.new(e).logError()
#         if e.errno == 17:
#             return True


# def validatePackage(packageName):
#     return validate_package(packageName)


# def write(zip):
#     try:
#         for chunk in zip.chunks():
#             with open(os.path.join("uploads", str(zip)), "wb+") as f:
#                 f.write(chunk)
#                 f.close()
#     except Exception as e:
#         log.new(e).logError()
#         return False


# def cleanup(packageName):
#     from django.conf import settings
#     filesPath = os.path.join("files", packageName)
#     uploadsPath = os.path.join(settings.BASE_DIR, "uploads", packageName+'.zip')

#     try:
#         if os.path.exists(filesPath):
#             rmtree(filesPath)
#             os.remove(filesPath)
#         if os.path.exists(uploadsPath):
#             os.remove(uploadsPath)
#     except Exception as e:
#         log.new(e).logError()
#         return False


# def moveIconsToStatic(packageName, skipCheckingOfIcons):

#     if skipCheckingOfIcons:
#         return True

#     iconsPath = os.path.join("files/", packageName, "icons/")
#     destPath = os.path.join("packages", "static",
#                             "images", "packages", packageName)
#     imageExtensions = ["png", "jpg", "jpeg", "svg"]

#     if skipCheckingOfIcons:
#         return True

#     iconsPath = os.path.join("files/", packageName, "icons/")
#     destPath = os.path.join("packages", "static",
#                             "images", "packages", packageName)
#     imageExtensions = ["png", "jpg", "jpeg", "svg"]

#     if not os.path.exists(iconsPath):
#         log.new('{} and {} does not exists'.format(
#             iconsPath, destPath)).logInfo()
#         log.new(FileNotFoundError(iconsPath)).logError()

#     if len(os.listdir(iconsPath)) < 1:
#         log.new(MissingIcons(
#             'Missing icons under icons folder, please put one.')).logError()
#         raise MissingIcons('Missing icons under icons folder as mentioned in your config file, please put one. ')


#     try:
#         for i in os.listdir(iconsPath):
#             for ext in imageExtensions:
#                 if i.endswith(ext):
#                     if os.path.exists(iconsPath) and not os.path.exists(destPath):
#                         move(iconsPath, destPath)
#         return True
#     except Exception as e:
#         log.new(e).logError()
#         return False


# def reDefineJson(packageName, validated_data, skipCheckingOfIcons):

#     if skipCheckingOfIcons:
#         validated_data['server']['icon'] = Package.objects.get(packageName=packageName).server['icon']
#         return validated_data

#     imagePath = os.path.join("packages", "static",
#                              "images", "packages", packageName)
#     imageExtensions = ["png", "jpg", "jpeg", "svg"]
#     if not os.path.exists(imagePath):
#         log.new('{} does not exists '.format(imagePath)).logError()
#         raise FileNotFoundError(imagePath)

#     if isinstance(validated_data, dict):
#         for i in os.listdir(imagePath):
#             for ext in imageExtensions:
#                 if i.endswith(ext):
#                     validated_data['server'][
#                         'icon'] = "/static/images/packages/{0}/{1}".format(packageName, i)
#                     return validated_data
#     else:
#         log.new(IsADirectoryError('Validated data is not dict!'))
#         return False


# def validate_json(json_object):
#     try:
#         return json.loads(json_object)
#     except json.JSONDecodeError as e:
#         log.new(e).logError()
#         return False


# def is_upgrade(package_name):
#     find_package = Package.objects.filter(packageName=package_name)

#     if find_package.exists():
#         return True
#     else:
#         return False

def check_package_version(json_object):
    from distutils.version import LooseVersion

    js = json_object
    package_name = js["packageName"]
    package_version = LooseVersion(js["version"])

    repo = Package.objects.filter(
        packageName=package_name) or SubmitPackage.objects.filter(packageName=package_name)

    if repo.exists():
        repo_version = repo.get().packageArgs["version"]
        if repo_version and package_version:
            if LooseVersion(repo_version) >= package_version:
                return {"status": False, "message": "We have never version of this package on system."}
            else:
                return {"status": True, "message": "Update on progress"}
        else:
            return {
                "status": False,
                "message": "We could not verify version number, please check it."
            }
    else:
        return {"status": True, "message": "Success"}


def compress_icon(image, package_name):
    from PIL import Image
    from django.conf import settings

    image_name = str(image)
    path = os.path.join(settings.BASE_DIR, 'media', 'packages', package_name, image_name)

    if os.path.exists(path):
        return str(image)

    im = Image.open(image)
    newImage = im.resize((200, 200))


    if image_name.endswith('.png'):
        file_format = 'png'
    elif image_name.endswith('.jpg') or image_name.endswith('.jpeg'):
        file_format = 'jpg'


    if not os.path.exists(path):
        os.makedirs(path)

    sea = newImage.save(os.path.join(path, image_name), format=file_format, quality=70)
    return image_name


def handle_uploaded_files():
    pass

def validate_json(json_object):
    import json
    try:
        js = json.loads(json_object)
        return True
    except Exception as e:
        return False

def dump_json(json_object):
    import json
    try:
        js = json.loads(json_object)
        return js
    except Exception as e:
        print(e)
        return False
