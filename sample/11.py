import sys


if sys.platform == "darwin":
    from Quartz import (
        CGWindowListCopyWindowInfo,
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID
    )


win_name = []
options = kCGWindowListOptionOnScreenOnly
windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
for window in windowList:
    ownerName = window['kCGWindowOwnerName']
    geometry = window['kCGWindowBounds']
    win_name.append(ownerName)
    if ownerName == "Hyperion":
        print(geometry["X"], geometry["Y"])
if "Hyperion" not in win_name:
    print(1)



# if ownerName == "Hyperion":
#     return geometry["X"], geometry["Y"]

