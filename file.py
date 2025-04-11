#github地址:https://www.github.com/glue0822/no_config
#开源项目,欢迎参加!
import os,sys
process_name=['RCServer.exe','RCClient.exe','RCMonitor.exe','RCUpdate.exe','RCData.exe','RCAudio.exe','StudentMain.exe']
print('反极域系统启动中...\n启动完成。')
while True:
    print('1:解除老师控制\n2:退出')
    do_code=input('请输入控制码:')
    if do_code == '1':
        for _ in range(2):
            for i in process_name:
                os.system('taskkill /f /im '+str(i))
    elif do_code == '2':
        sys.exit()
