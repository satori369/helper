import random
from multiprocessing import Process
import os,time
# from woww.kaimen.kaimen import *
import win32gui, win32ui, win32con, win32api
from PIL import Image
import frozen

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
        # er += 1
        print("主进程跳跃检测截图报错")


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
    time.sleep(0.5)
    win32api.keybd_event(103, 0, 0, 0)  # 7
    win32api.keybd_event(103, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(103, 0, 0, 0)  # 7
    win32api.keybd_event(103, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(105, 0, 0, 0)  # 9
    win32api.keybd_event(105, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(100, 0, 0, 0)  # 4
    win32api.keybd_event(100, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(99, 0, 0, 0)  # 3
    win32api.keybd_event(99, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(98, 0, 0, 0)  # 2
    win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(98, 0, 0, 0)  # 2
    win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(96, 0, 0, 0)  # 0
    win32api.keybd_event(96, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(97, 0, 0, 0)  # 1
    win32api.keybd_event(97, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    # @
    win32api.keybd_event(16, 0, 0, 0)
    win32api.keybd_event(50, 0, 0, 0)
    win32api.keybd_event(50, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    # qq
    win32api.keybd_event(81, 0, 0, 0)  # q
    win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(81, 0, 0, 0)  # q
    win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    # .com
    win32api.keybd_event(110, 0, 0, 0)  # .
    win32api.keybd_event(110, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(67, 0, 0, 0)  # c
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(79, 0, 0, 0)  # o
    win32api.keybd_event(79, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(77, 0, 0, 0)  # m
    win32api.keybd_event(77, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)

    print('账号输入完毕')
    ###输入密码  先按table
    win32api.keybd_event(9, 0, 0, 0)  # tab
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(81, 0, 0, 0)  # q
    win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(81, 0, 0, 0)  # q
    win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(103, 0, 0, 0)  # 7
    win32api.keybd_event(103, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(104, 0, 0, 0)  # 8
    win32api.keybd_event(104, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(97, 0, 0, 0)  # 1
    win32api.keybd_event(97, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(97, 0, 0, 0)  # 1
    win32api.keybd_event(97, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(98, 0, 0, 0)  # 2
    win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(100, 0, 0, 0)  # 4
    win32api.keybd_event(100, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)

    print('密码输入完毕')
    # 回车
    win32api.keybd_event(13, 0, 0, 0)  # 回车
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(3)
    # 回车
    win32api.keybd_event(13, 0, 0, 0)  # 回车
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(8)
    win32api.keybd_event(13, 0, 0, 0)  # 回车
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(30)



cishu = 0
#运行开门子进程
def run_kaimen():
    global cishu
    while True:
        cishu += 1
        print('运行子进程开门接客~运行第%s次' % cishu)
        # str = ('python kaimen.py')  # python命令 + B.py
        str = ('kaimen.exe')
        os.system(str)



if __name__ == '__main__':
    #####为了在exe运行子进程,添加的包
    frozen.multiprocessing.freeze_support()
    print('--------------------------------------------------------------')
    print('wow开门测试版v0.1')
    print('说明:奥格小键盘9,幽暗8,雷霆7,大喊广告0,选取队友1,队伍喊话2,退队3')
    print('--------------------------------------------------------------')
    a = input('按回车键开始脚本')
    print('三秒后开始启动...请切换到魔兽窗口')
    time.sleep(3)
    duankai = 0
    time_start = time.time()
    p = Process(target=run_kaimen)
    print('子进程将开始')
    p.start()
    print('start运行')
    time1 = time.time()
#############################################
    while True:
        window_capture("duankai.jpg", 250, 250, 835, 520)
        image1 = Image.open('duankai.jpg')
        # 截图与素材原图对比(99, 7, 7) (100, 1, 1)  (120,17,10)
        pixel1 = image1.getpixel((20, 30))
        pixel2 = image1.getpixel((230, 30))
        pixel4 = image1.getpixel((180, 208))
        # 如果检测到断开连接,准备进行重连
        if abs(pixel1[0] - 100) <= 10 and abs(pixel1[1] - 7) <= 10 and abs(pixel1[2] - 7) <= 10 or \
                abs(pixel2[0] - 100) <= 10 and abs(pixel2[1] - 1) <= 10 and abs(pixel2[2] - 1) <= 10 or \
                abs(pixel4[0] - 120) <= 10 and abs(pixel4[1] - 17) <= 10 and abs(pixel4[2] - 10) <= 10:
            duankai += 1
            print('检测到断开连接,准备进行重连,断线第%s次'%duankai)
            time.sleep(1)
            login()


        else:
            print('父进程喊话+防掉线操作')
            win32api.keybd_event(96, 0, 0, 0)  # 小键盘0
            win32api.keybd_event(96, 0, win32con.KEYEVENTF_KEYUP, 0)  # 大喊喊话广告
            time.sleep(55)
            time2 = time.time()
            miaoshu = time2 - time1
            window_capture("shifazhong.jpg", 250, 50, 835, 820)
            image3 = Image.open('shifazhong.jpg')
            # 截图与素材原图对比(46, 43, 39)
            pixel3 = image3.getpixel((5, 30))
            # 如果在施法状态(46, 43, 39)
            if abs(pixel3[0] - 46) <= 10 and abs(pixel3[1] - 43) <= 10 and abs(pixel3[2] - 39) <= 10:
                # 在施法状态的话,等10秒施法结束后再跳
                print('正在施法,等待施法结束后再跳跃')
                time.sleep(12)

            if miaoshu > random.randint(240,420):
                win32api.keybd_event(65, 0, 0, 0)  # a
                time.sleep(0.5)
                win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开a
                win32api.keybd_event(68, 0, 0, 0)  # d
                time.sleep(0.5)
                win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开d
                time1 = time.time()
                # win32api.keybd_event(32, 0, 0, 0)  # 空格跳跃
                # win32api.keybd_event(32, 0, win32con.KEYEVENTF_KEYUP, 0)  # 空格防掉线
                # time.sleep(0.5)


            #计时
            time_new = time.time()
            seconds = time_new - time_start
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            print("运行了%02d时%02d分%02d秒" % (h, m, s))

        # p.join()
        # print('子进程结束')
