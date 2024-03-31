from json import loads,dumps
def read(path):
    with open(path,'r',encoding="utf-8") as f:
        data = f.read()
        f.close()
    re = loads(data)
    return re
def write(path,dictionary):
    with open(path,'w',encoding="utf-8") as f:
        f.write(dumps(dictionary))
        f.close()
