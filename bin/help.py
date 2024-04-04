def help(cmd):
    if not cmd:
        print("help 帮助")
        print("start 开始反控制")
        print("stop 停止反控制")
        print("exit 退出程序")
    elif cmd[0] == 'exit':
        print("exit 退出")
    elif cmd[0] == 'help':
        print("help [命令]")
    else:
        print(f"{cmd[0]}不是命令(可能是插件")
