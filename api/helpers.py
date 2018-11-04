import os, json
from .models import Package, SubmitPackage, Setting


class CacheDirectoryNotFound(Exception):
    pass


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


def check_for_cached_repo():
    path = os.path.join("cache", "repo.json")
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                js = validate_json(f.read())
                f.close()
                if not isinstance(js, bool) and len(js) > 0:
                    return js
                else:
                    return {}
        except Exception as e:
            raise CacheDirectoryNotFound(e)
    else:
        return {}


def write_cache(json_key):
    path = os.path.join("cache", "repo.json")
    print(os.path.abspath(path))
    try:
        with open(path, "w") as f:
            f.write(json.dumps(json_key))
            f.close()

            Setting.objects.filter(do_update_packages=True).update(
                do_update_packages=False)
            return json.dumps(json_key)
        return False
    except Exception as e:
        create_cache_folder()
        raise CacheDirectoryNotFound(e)


def create_cache_folder():
    path = os.path.abspath(os.path.join('cache'))

    try:
        os.makedirs(path)
    except Exception as e:
        print(e)
