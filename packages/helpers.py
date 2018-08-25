import os
import json
from api.models import Setting
from api import helpers as api_helpers


class CacheDirectoryNotFound(Exception):
    pass


def __check_for_cached_repo():
    path = os.path.join("cache", "repo.json")
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                js = api_helpers.validate_json(f.read())
                f.close()
                if not isinstance(js, bool) and len(js) > 0:
                    return js
                else:
                    return {}
        except Exception as e:
            raise CacheDirectoryNotFound(e)
    else:
        return {}


def __write_cache(json_key):
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
