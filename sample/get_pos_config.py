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
    options = kCGWindowListOptionOnScreenOnly
    windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    for window in windowList:
        ownerName = window['kCGWindowOwnerName']
        geometry = window['kCGWindowBounds']
        if ownerName == "Hyperion":
            return geometry["X"], geometry["Y"]


def get_channel_config(unit):
    destop_x ,destop_y = get_win_pos()
    config_data = read_json_config(file)
    unit_data = config_data["Channel_" + unit]
    x1 = unit_data["X1"] + destop_x
    x2 = unit_data["X2"] + destop_x
    y1 = unit_data["Y1"] + destop_y
    y2 = unit_data["Y2"] + destop_y
    return int(x1), int(x2), int(y1), int(y2)
