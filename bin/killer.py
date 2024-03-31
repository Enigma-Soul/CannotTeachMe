from os import kill as oskill
from psutil import Process

# 用Os库执行
def use_os(pid):
    try:
        oskill(pid,9)
        return True
    except Exception:
        return False
# 用Pusutil库执行
def use_process(pid):
    try:
        process = Process(pid)
        process.kill()
        return True
    except Exception:
        return False
# 是否活着
def die_or_not(pid):
    try:
        Process(pid)
        return False
    except Exception:
        return True
# 运行
def kill(pid):
    if not use_os(pid):
        if not use_process(pid):
            if  not die_or_not(pid):
                return False
            else:
                return True
        else:
            return False
    else:
        return True