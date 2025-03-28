import os
import json

# reads all the cargo grid models from the grid3DViewer folder.
#
# Be sure to be careful regarding naming, the files NEED to have the exact same name as what
# we get from the log files, else we have to write a mapping function (please don't)
def loadCargoGrids() -> dict:
    grids = {}
    for file in os.listdir("/"):
        if not file.endswith(".json"):
            continue
        else:
            with open(os.path.join("/", file), "r") as f:
                entry = json.load(f)
            grids[file[:-5].lower()] = entry

    return grids

#print(loadCargoGrids())