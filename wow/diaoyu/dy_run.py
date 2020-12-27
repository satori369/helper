import os
import subprocess
import time
import win32gui, win32ui, win32con, win32api
from PIL import Image

cccc = 22
duankai = 0 #断开连接次数


#截图函数
def window_capture(filename,w,h,x,y):
    # global er
    try:
        hwnd = 0 # 窗口的编号，0号表示当前活跃窗口88
        # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
        hwndDC = win32gui.GetWindowDC(hwnd)
        # 根据窗口的DC获取mfcDC
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        # mfcDC创建可兼容的DC
        saveDC = mfcDC.CreateCompatibleDC()
        # 创建bigmap准备保存图片
        saveBitMap = win32ui.CreateBitmap()
        # 获取监控器信息
        # MoniterDev = win32api.EnumDisplayMonitors(None, None)
        # w = MoniterDev[0][2][2]
        # h = MoniterDev[0][2][3]
        # print(w,h)  #图片大小
        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        # 高度saveDC，将截图保存到saveBitmap中
        saveDC.SelectObject(saveBitMap)
        # 截取从左上角（0，0）长宽为（w，h）的图片  (x,y)截图范围大小
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (x, y), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, filename)
        # 释放内存，不然会造成资源泄漏
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
    except Exception:
        ## er += 1
        # print("run截图报错")
        p5 = "run截图报错\n"
        print_text(p5)

# 断线重连函数,点击确认,然后输入账号密码
def login():
    # 鼠标定位确认按钮
    # win32api.SetCursorPos([740, 435])
    # time.sleep(0.5)
    # # 左键点击
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(1)

    # 回车
    win32api.keybd_event(13, 0, 0, 0)  # 回车
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)

    # 鼠标定位确认按钮
    win32api.SetCursorPos([440, 267])
    time.sleep(0.5)
    # 左键点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(1)

    # 默认就在输入账号窗口,全选然后退格即可
    win32api.keybd_event(17, 0, 0, 0)  # Ctrl
    win32api.keybd_event(65, 0, 0, 0)  # a
    win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开a
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开Ctrl
    time.sleep(0.5)
    win32api.keybd_event(8, 0, 0, 0)  # Backspace 退格键 摁住
    win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开退格键
    time.sleep(0.5)

    # 输入账号
    win32api.keybd_event(97, 0, 0, 0)  # 1
    win32api.keybd_event(97, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(103, 0, 0, 0)  # 7
    win32api.keybd_event(103, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(103, 0, 0, 0)  # 7
    win32api.keybd_event(103, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(105, 0, 0, 0)  # 9
    win32api.keybd_event(105, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(100, 0, 0, 0)  # 4
    win32api.keybd_event(100, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(99, 0, 0, 0)  # 3
    win32api.keybd_event(99, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(98, 0, 0, 0)  # 2
    win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(98, 0, 0, 0)  # 2
    win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(96, 0, 0, 0)  # 0
    win32api.keybd_event(96, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(97, 0, 0, 0)  # 1
    win32api.keybd_event(97, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    # @
    win32api.keybd_event(16, 0, 0, 0)
    win32api.keybd_event(50, 0, 0, 0)
    win32api.keybd_event(50, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    # qq
    win32api.keybd_event(81, 0, 0, 0)  # q
    win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(81, 0, 0, 0)  # q
    win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    # .com
    win32api.keybd_event(110, 0, 0, 0)  # .
    win32api.keybd_event(110, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(67, 0, 0, 0)  # c
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(79, 0, 0, 0)  # o
    win32api.keybd_event(79, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(77, 0, 0, 0)  # m
    win32api.keybd_event(77, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)

    # print('账号输入完毕')
    p6 = '账号输入完毕\n'
    print_text(p6)
    ###输入密码  先按table
    win32api.keybd_event(9, 0, 0, 0)  # tab
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(81, 0, 0, 0)  # q
    win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(81, 0, 0, 0)  # q
    win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(103, 0, 0, 0)  # 7
    win32api.keybd_event(103, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(104, 0, 0, 0)  # 8
    win32api.keybd_event(104, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(97, 0, 0, 0)  # 1
    win32api.keybd_event(97, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(97, 0, 0, 0)  # 1
    win32api.keybd_event(97, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(98, 0, 0, 0)  # 2
    win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(100, 0, 0, 0)  # 4
    win32api.keybd_event(100, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)

    # print('密码输入完毕')
    p7 = '密码输入完毕\n'
    print_text(p7)
    # 回车
    win32api.keybd_event(13, 0, 0, 0)  # 回车
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(8)
    # 回车
    win32api.keybd_event(13, 0, 0, 0)  # 回车
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(8)
    win32api.keybd_event(13, 0, 0, 0)  # 回车
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(30)

#断线检测函数
def duankai_jiance():
    n = 0  #
    global duankai
    window_capture("duankai.jpg", 150, 60, 470, 405)
    yupiao = Image.open('duankai.jpg')
    for i in range(0, 150):
        for c in range(0, 60):
            pixel1 = yupiao.getpixel((i, c))
            if abs(pixel1[0] - 100) <= 10 and abs(pixel1[1] - 7) <= 10 and abs(pixel1[2] - 7) <= 10:
                duankai += 1
                n = 1
                print('检测到断开连接,准备进行重连,断线第%s次' % duankai)
                p4 = '检测到断开连接,准备进行重连,断线第%s次\n' % duankai
                print_text(p4)
                time.sleep(1)
                login()
                win32api.keybd_event(48, 0, 0, 0)  # 0上鱼饵
                win32api.keybd_event(48, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开0
                # print('上鱼饵')
                p3 = '上鱼饵\n'
                print_text(p3)
                time.sleep(7)
                break
        if n == 1:
            break


#日志写入
def print_text(p):
    f = open('text.txt', 'a')
    f.writelines(p)
    f.close()

def dyrun():
    # print('--------------------------------------------------------------')
    # print('wow钓鱼脚本v4.0(断线自动重连)')
    # print('说明:9键钓鱼,8开蚌壳,0键上鱼饵(请设置好宏),每钓鱼10分钟,自动上鱼饵')
    # print('钓鱼操作优化，断线重连优化')
    # print('--------------------------------------------------------------')
    # a = input('按回车键开始钓鱼')
    print('三秒后开始启动...请切换到魔兽窗口')

    f = open('text.txt', 'w')
    xieru = '''print('----------------)\n'''
    f.writelines(xieru)
    f.close()



    time.sleep(3)

    time_start = time.time()
    while True:
        ###断线检测
        # duankai_jiance()  //断线重连开启这个
        ###测试环境用这个
        # str = ('python dy_code.py')  # python命令 + B.py
        ###exe文件环境用这个
        str = ('dy_code.exe')
        p = os.system(str)
        # print(p.pid, '看这里')
        # os.system('taskkill /F /IM dy_code.py')        #关闭进程----不需要
        time.sleep(1)
        # 计时
        time_new = time.time()
        seconds = time_new - time_start
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        # print("运行了%02d时%02d分%02d秒" % (h, m, s))
        p1 = "运行了%02d时%02d分%02d秒\n" % (h, m, s)
        print_text(p1)

        win32api.keybd_event(8, 0, 0, 0)  # 空格跳
        win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开空格
        for i in range(5):
            win32api.keybd_event(56, 0, 0, 0)  # 8打开蚌壳
            win32api.keybd_event(56, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开8
            time.sleep(0.5)
        time.sleep(2)
        win32api.keybd_event(48, 0, 0, 0)  # 0上鱼饵
        win32api.keybd_event(48, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开0
        # print('上鱼饵')
        p2 = '上鱼饵\n'
        print_text(p2)
        time.sleep(7)


if __name__ == '__main__':
    dyrun()