from bin import *

def get_blacklist():
    ports = []
    exe = []
    json = config.read("./blacklist.json")
    for x in json["list"]:
        ports += json[x]["ports"]
        exe += json[x]["exe"]
    return ports , exe
def kill_all():
    ports, exe = get_blacklist()

    for port in ports:
        for pid in port_find(port):
            try:
                kill(pid)
            except Exception:
                pass
    for ex in exe:
        for pid in name_find(ex):
            try:
                kill(pid)
            except Exception:
                pass
