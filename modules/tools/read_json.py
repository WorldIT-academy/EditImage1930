import os
import json
def read_json(fd: str) -> dict:
    path_to_file = os.path.abspath(os.path.join(__file__, "..", "..", "..", "static", "json", fd))
    with open(path_to_file, "r") as data_json:
        return json.load(data_json)




