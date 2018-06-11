import os, json
from os.path import splitext
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = splitext(value.name)[1]
    valid_extensions = ['.zip']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


def validate_package(packageName):
    for i in os.listdir(os.path.join("files", packageName)):
        if i.lower().endswith('.cb'):
            try:
                with open(os.path.join("./files/{0}/{1}".format(packageName, i)), "r") as f:
                    js = json.load(f)
                    f.close()

                js["packageArgs"]
                js["packageUninstallArgs"]
                js["server"]

                return js
            except Exception as e:
                print(e)
                return False
