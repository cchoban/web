import os
import json
from os.path import splitext
from django.core.exceptions import ValidationError
from . import Logger as log


class MissingIconsFolder(Exception):
    pass


class MissingInstallationScript(Exception):
    pass


def validate_file_extension(value):
    ext = splitext(value.name)[1]
    valid_extensions = ['.zip']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


def validate_package(packageName, skipCheckingIcons):
    if validate_files(packageName, skipCheckingIcons):
        for i in os.listdir(os.path.join("files", packageName)):
            if i.lower().endswith('.cb'):
                try:
                    with open(os.path.join("./files/{0}/{1}".format(packageName, i)), "r") as f:
                        js = json.load(f)
                        f.close()

                        validate_keys(js)

                    return js

                except Exception as e:
                    log.new(e).logError()
                    return False


def validate_keys(js):
    neededKeys = ["packageArgs", "packageUninstallArgs", "server"]

    for i in neededKeys:
        if not i in js:
            return False


def validate_files(packageName, skipCheckingIcons):
    from .models import Package

    folder = os.path.abspath(os.path.join("files", packageName))
    folders = [
        'icons',
    ]

    for i in folders:
        if i in os.listdir(folder):
            return True
        else:
            if i == 'icons':
                if skipCheckingIcons:
                    return True
                else:
                    return False
            log.new(MissingIconsFolder(i)).logError()
            raise MissingIconsFolder(i)
