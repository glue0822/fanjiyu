import os
print('反极域系统启动中...\n启动完成。\n@CopyRight 235工作室版权所有')
while True:
    print('1:解除老师控制\n2:退出')
    do_code=input('请输入控制码:')
    if do_code == '1':
        error_code=os.system('taskkill /f /im StudentMain.exe')
        if error_code != 128:
            print('操作成功!')
        print('可能需要再次输入1')
    elif do_code == '2':
        break
