from bin import *

def get_blacklist():
    ports = []
    exe = []
    json = config.read("./blacklist.json")


