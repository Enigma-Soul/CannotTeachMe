from bin import *
from threading import Thread
from time import sleep
class shit(Thread):
    def __init__(self):
        super().__init__()
        self.running = True
    def start(self):
        while self.running:
            # 在这里执行循环的任务
            print("循环执行中...")
    def stop(self):
        self.running = False

def get_blacklist():
    ports = []
    exe = []
    json = config.read("./blacklist.json")
    for x in json["list"]:
        ports += json[x]["ports"]
        exe += json[x]["exe"]
    return ports , exe

def main():
    cmd = input(color("blue","/~ #"))


if __name__ == '__main__':
    main()