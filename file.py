from tkinter import *
import os,sys,time,hashlib
from datetime import datetime
#导入模块

process_name=['RCServer.exe','RCClient.exe','RCMonitor.exe','RCUpdate.exe','RCData.exe','RCAudio.exe','StudentMain.exe']
try:
    Verify_file=open('Verify.txt','r')
except FileNotFoundError:
    print('Verify.txt丢失,无法运行.')
    input('请按Enter键退出...')
    sys.exit()
Verify_code=Verify_file.read()
Verify_file.close()
year_now=datetime.now().year
month_now=datetime.now().month
time_now='Verify_code:'+str(year_now)+'.'+str(month_now)
time_hash=hashlib.sha256(time_now.encode('utf-8')).hexdigest()
if time_hash != Verify_code:
    print('效验码已过期,请前往您购买的渠道更换效验码.')
    input('请按Enter键退出...')
    sys.exit()
#效验码

window=Tk()
screen=Canvas(window,width=150,height=100)
window.attributes('-topmost',1)
screen.pack()
window.title('file.exe显示:')
#配置窗口

screen.create_text(75,50,text='反极域系统\n请点击控制键:')
def control(do_code):
    if do_code == '1':
        for _ in range(2):
            for i in process_name:
                os.system('taskkill /f /im '+str(i))
    elif do_code == '2':
        os .system('ipconfig /flushdns')
    elif do_code == '3':
        window.destroy()
    return 0
button1=Button(window,width=20,text='解除老师控制',command=lambda:control('1'))
button2=Button(window,width=20,text='刷新DNS缓存',command=lambda:control('2'))
button3=Button(window,width=20,text='关闭此页面',command=lambda:control('3'))
button1.pack()
button2.pack()
button3.pack()
#功能按键

while True:
    try:
        window.attributes('-topmost',1)
        time.sleep(0.01)
        window.update()
    except TclError:
        sys.exit()
#主循环
