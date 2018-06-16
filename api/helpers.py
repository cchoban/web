import zipfile
import os
from .validators import validate_package
from shutil import rmtree, move
from django.core.exceptions import ValidationError


def createFolder(folderName):
    folder = "./files/" + folderName
    if not os.path.exists(folder):
        os.makedirs(folder)
        return "./files/" + folderName


def createFolders():
    folders = ["uploads", "files"]

    for i in folders:
        try:
            os.makedirs(os.path.join(i))
        except Exception as e:
            return True


def unzip(packageName, zip):
    folder = os.path.join("files", packageName)
    print(folder)
    try:
        zf = zipfile.ZipFile(zip, "r")
        zf.extractall(folder)
        zf.close()
    except OSError as e:
        if e.errno == 17:
            # Already exists
            return True
        print(e)


def validatePackage(packageName):
    return validate_package(packageName)


def handle_uploaded_files(zipRequest):
    createFolders()
    write(zipRequest)
    withoutExt = str(zipRequest).split('.')[0]
    unzip(withoutExt, os.path.join("uploads/", str(zipRequest)))
    validate = validate_package(withoutExt)
    moveIconsToStatic(withoutExt)
    if validate:
        return validate
    else:
        cleanup(str(zipRequest))
        return ValidationError(
            "We could not validate you JSON file. Be sure you have generated file with the Choban Package Manager.")


def write(zip):
    for chunk in zip.chunks():
        with open(os.path.join("uploads", str(zip)), "wb+") as f:
            f.write(chunk)
            f.close()


def cleanup(packageName):
    filesPath = os.path.join("files/", packageName)
    uploadsPath = os.path.join("uploads/", packageName+".zip")

    if os.path.exists(filesPath) and os.path.exists(uploadsPath):
        try:
            rmtree(filesPath)
            os.remove(uploadsPath)
            os.removedirs(filesPath, uploadsPath)
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
                print(image)
                if os.path.exists(iconsPath):
                    move(iconsPath, destPath)
