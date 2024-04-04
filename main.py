from bin.color import color
from bin.help import help
from threading import Thread
from time import sleep
from sys import exit , executable
from os import listdir , system
from kernel import kill_all

class shit(Thread):
    def __init__(self):
        super().__init__()
        self.running = False
    def run(self):
        self.running = True
        while self.running:
            kill_all()
            sleep(0.5)
    def stop(self):
        self.running = False



def main():
    while True:
        cmd = input(color("blue", "/~ #")).split()
        plus_in = []
        for i in listdir("./plus-in"):
            if i[-3:] == ".py":
                plus_in += [i[:-3]]
        if cmd[0] == "help":
            help(cmd[1:])
        elif cmd[0] == "exit":
            runner.stop()
            exit(0)
        elif cmd[0] == "start":
            runner.start()
        elif cmd[0] == "stop":
            runner.stop()
        elif cmd[0] in plus_in:
            plus__in = ""
            for temp in cmd:
                if cmd.index(temp) == int(len(cmd) - 1):
                    plus__in += temp
                else:
                    plus__in += temp
                    plus__in += " "
            system(f"{executable} ./plus-in/{plus__in}.py")
        else:
            print(f"{cmd[0]}并不是一个命令或插件")




if __name__ == '__main__':
    # 初始化程序
    runner = shit()
    main()