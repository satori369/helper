import time

import win32api
import win32con
import win32gui


n = 1
yeshu = input('输入要循环的页数')
# time.sleep(2)
print('5秒后启动，请切换好窗口')
time.sleep(5)
# 鼠标单击事件
yeshu = int(yeshu)
# #执行左单键击，若需要双击则延时几毫秒再点击一次即可



def quanxuanfuzhi():
    win32api.SetCursorPos([320, 280])
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # #右键单击
    # win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    time.sleep(0.3)
    win32api.SetCursorPos([1520, 680])
    time.sleep(0.3)
    win32api.keybd_event(16, 0, 0, 0)  # shift
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.3)
    win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    time.sleep(0.3)
    ###复制
    win32api.keybd_event(17, 0, 0, 0)  # ctrl
    win32api.keybd_event(67, 0, 0, 0)  # c
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    time.sleep(0.3)

def qiehuanchuangkou():
    ###切换窗口
    win32api.keybd_event(18, 0, 0, 0)  # c
    win32api.keybd_event(9, 0, 0, 0)  # c
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    time.sleep(0.3)

def zhantie():
    ###粘贴
    win32api.keybd_event(17, 0, 0, 0)  # ctrl
    win32api.keybd_event(86, 0, 0, 0)  # ctrl
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    time.sleep(0.3)
    win32api.keybd_event(13, 0, 0, 0)  # enter
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    time.sleep(0.3)
###全选
while n<=yeshu:
    quanxuanfuzhi()
    qiehuanchuangkou()
    zhantie()
    win32api.SetCursorPos([1550,720])
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(3)
    n+=1

