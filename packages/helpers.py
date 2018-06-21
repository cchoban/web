import os
import json
from api.models import Setting
from api import helpers as api_helpers


def __check_for_cached_repo():
    path = os.path.join("cache", "repo.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            js = api_helpers.validate_json(f.read())
            f.close()
            if not isinstance(js, bool) and len(js) > 0:
                return js
            else:
                return {}
    else:
        return {}


def __write_cache(json_key):
    path = os.path.join("cache", "repo.json")
    with open(path, "w") as f:
        f.write(json.dumps(json_key))
        f.close()

        Setting.objects.filter(do_update_packages=True).update(
            do_update_packages=False)
        return json.dumps(json_key)
    return False
