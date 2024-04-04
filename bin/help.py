def help(cmd):
    if cmd[0] == 'help':
        print("help [命令]")
    elif not cmd:
        print("help 帮助")
        print("start 开始反控制")
        print("stop 停止反控制")
        print("renew 更新黑名单")
    else:
        print(f"{cmd[0]}不是命令(可能是插件")
