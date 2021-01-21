import sys
import json
import getpass

current_user = getpass.getuser()
file = "/Users/" + current_user + "/PycharmProjects/Factory_Colour-capture/sample/ui_config.json"


def read_json_config(file):
    with open(file) as json_file:
        config = json.load(json_file)
    return config


config_data = read_json_config(file)
for i in config_data["Current resolution"]:
    if config_data["Current resolution"][i] == 1:
        print(config_data[i])
