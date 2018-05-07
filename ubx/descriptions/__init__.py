import os
import importlib

default = []

for name in os.listdir(os.path.dirname(__file__)):
    if name.startswith("_") or not name.endswith(".py"):
        continue
    name = name[:-3]
    importlib.import_module("." + name, "ubx.descriptions")
    default.append(globals()[name].description)
