from tkinter import *
import os,sys
process_name=['RCServer.exe','RCClient.exe','RCMonitor.exe','RCUpdate.exe','RCData.exe','RCAudio.exe','StudentMain.exe']

window=Tk()
screen=Canvas(window,width=150,height=100)
screen.pack()
screen.create_text(75,50,text='反极域系统\n1:解除老师控制\n2:刷新DNS缓存\n3:退出\n请点击控制键:')
window.title('file.exe')

def control(do_code):
    if do_code == '1':
        for _ in range(2):
            for i in process_name:
                os.system('taskkill /f /im '+str(i))
    elif do_code == '2':
        os .system('ipconfig /flushdns')
    elif do_code == '3':
        sys.exit()
    return 0
button1=Button(window,width=20,text='1',command=lambda:control('1'))
button2=Button(window,width=20,text='2',command=lambda:control('2'))
button3=Button(window,width=20,text='3',command=lambda:control('3'))
button1.pack()
button2.pack()
button3.pack()
window.mainloop()
