from psutil import process_iter , net_connections
from re import match
def is_or_not(string,pattern):
    return bool(match(pattern,string))
def name_find(input_name):
    input_name += ".exe"
    input_name = input_name.replace("?",".*")
    pid_list = []
    # 遍历系统中所有进程
    for process in process_iter(['pid', 'name']):
        try:
            # 获取进程的名称
            name = process.info['name']
            # 如果进程名称与指定的进程名匹配，则返回对应的PID
            if is_or_not(name,input_name):
                pid_list += [process.pid]
        except Exception:
            pass
    return pid_list
def port_find(port):
    pid_list = []
    for conn in net_connections():
        if conn.laddr.port == port:
            pid_list += [conn.laddr]

    if len(pid_list) == 0:
        return None
    else:
        return pid_list