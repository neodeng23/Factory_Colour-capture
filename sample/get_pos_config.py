import sys
import json
import getpass

current_user = getpass.getuser()
file = "/Users/" + current_user + "/PycharmProjects/Factory_Colour-capture/sample/ui_config.json"


def read_json_config(file):
    with open(file) as json_file:
        config = json.load(json_file)
    return config


if sys.platform == "darwin":
    from Quartz import (
        CGWindowListCopyWindowInfo,
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID
    )


def get_win_pos():
    win_name = []
    options = kCGWindowListOptionOnScreenOnly
    windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    for window in windowList:
        ownerName = window['kCGWindowOwnerName']
        geometry = window['kCGWindowBounds']
        win_name.append(ownerName)
        if ownerName == "Hyperion":
            return geometry["X"], geometry["Y"]
    if "Hyperion" not in win_name:
        return 9999, 9999


def get_channel_config(unit, destop_x, destop_y):
    if destop_x is not None and destop_y is not None:
        config_data = read_json_config(file)
        for i in config_data["Current resolution"]:
            if config_data["Current resolution"][i] == 1:
                unit_data = config_data[i]["Channel_" + unit]
        n = config_data[i]["magnification"]
        x1 = unit_data["X1"] + destop_x * n
        x2 = unit_data["X2"] + destop_x * n
        y1 = unit_data["Y1"] + destop_y * n
        y2 = unit_data["Y2"] + destop_y * n
        return int(x1), int(x2), int(y1), int(y2)
    else:
        return None
