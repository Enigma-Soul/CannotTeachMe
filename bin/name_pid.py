from psutil import process_iter

def find(input_name):
    input_name += ".exe"
    pid_list = []
    # 遍历系统中所有进程
    for process in process_iter(['pid', 'name']):
        try:
            # 获取进程的名称
            name = process.info['name']
            # 如果进程名称与指定的进程名匹配，则返回对应的PID
            if name == input_name:
                pid_list += [process.pid]
            return pid_list
        except Exception:
            return None