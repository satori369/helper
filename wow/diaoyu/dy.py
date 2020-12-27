import os
import subprocess
from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框
import time
# import dy_run
# from multiprocessing import Process

class CanvasDemo:
    def __init__(self):
        self.root = Tk()
        self.root.title("海王秘籍")
        self.canvas = Canvas(self.root, width=440, height=200, bg="White")
        self.canvas.pack()
        self.time_start = time.time()       #起始时间
        self.label = Label(text="")         #时间文本对象
        self.a = 0
        self.tetle = '''----------------------------------
wow钓鱼脚本v5.0(通用版)
说明:9键钓鱼,8开蚌壳，0键上鱼饵(请设置好宏),每钓鱼10分钟,自动上鱼饵
-----------------------------------
'''
        self.text_start = "3秒钟后开始钓鱼"
        self.text_start = self.tetle + self.text_start

        self.frame = Frame(self.root)
        self.frame.pack()
        self.btString = Button(self.frame, text="开 始", command=self.start)
        self.btClear = Button(self.frame, text="结 束", command=self.over)
        self.btString.grid(row=1, column=1)
        self.btClear.grid(row=1, column=2)
        self.label.pack()

        # self.p = Process(target=dy_run.dyrun)   #打开进程
        # self.str1 = ('python dy_run.py')    #测试环境
        self.str1 = ('dy_run.exe')          #exe环境



    def start(self):
        self.time_start = time.time()       #起始时间
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")

        self.canvas.create_text(220, 50, text=self.text_start, font="Tine 10 bold", tags="string")
        self.a = 1
        self.p = subprocess.Popen(self.str1, shell=True)    #进程启动

        return self.a,self.p

    #结束按钮
    def over(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")
        self.label.configure(text="运行了00时00分00秒")   #初始界面显示的文本
        self.tetle_over = self.tetle + self.over_time()
        self.canvas.create_text(220, 50, text=self.tetle_over, font="Tine 10 bold", tags="string")
        self.a = 0
        self.time_start = time.time()
        # self.p.kill()  # 终止子进程            //windows下不好使
        os.system('taskkill /t /f /pid {}'.format(self.p.pid))      ##shell命令 结束进程

        return self.a,self.time_start

    #计算用时
    def over_time(self):
        time_new = time.time()
        timestamp = time_new - self.time_start
        m, s = divmod(timestamp, 60)
        h, m = divmod(m, 60)
        over_time = "程序一共运行了%02d时%02d分%02d秒" % (h, m, s)
        return over_time


    def update_clock(self):
        time_new = time.time()
        timestamp = time_new - self.time_start
        m, s = divmod(timestamp, 60)
        h, m = divmod(m, 60)
        shijian = "运行了%02d时%02d分%02d秒" % (h, m, s)

        if self.a == 1:
            self.label.configure(text=shijian)
        self.root.after(50, self.update_clock)

    def run(self):
        self.update_clock()
        self.canvas.create_text(220, 50, text=self.tetle, font="Tine 10 bold", tags="string")
        self.root.mainloop()






# frame10=Frame(root)
# frame10.pack()
# group=LabelFrame(frame10,text='特别鸣谢',padx=5,pady=5)
# group.grid()
# w=Label(group,text='容器框')
# w.pack()
'''

'''

if __name__ == '__main__':
    CanvasDemo().run()


# root.mainloop()



