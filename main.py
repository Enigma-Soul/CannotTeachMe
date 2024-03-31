from bin import config
from bin import *

def get_blacklist():
    ports = []
    exe = []
    json = config.read("./blacklist.json")
    for x in json["list"]:
        ports += json[x]["ports"]
        exe += json[x]["exe"]
    return ports , exe
get_blacklist()

