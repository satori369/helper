import time, random
import win32gui, win32ui, win32con, win32api
from PIL import Image


#截图函数
def window_capture(filename,w,h,x,y):
    global er
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
        er += 1
        f = open('text.txt', 'a')
        p = '报错' + str(er) + '次\n'
        f.writelines(p)
        f.close()


def diaoyu(yuantu):
    #钓鱼按键
    time.sleep(0.3)
    win32api.keybd_event(57, 0, 0, 0)  # 9
    win32api.keybd_event(57, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开9
    time.sleep(0.1)
    # 鼠标定位鱼漂 410,220
    win32api.SetCursorPos([410, 220])
    time.sleep(1)

    window_capture("yupiao.jpg", 280, 170, 410, 205)
    yupiao = Image.open('yupiao.jpg')
    pixel1 = yuantu.getpixel((155, 97))  #
    #遍历区域RGB颜色,更准确
    for i in range(150,160):
        for c in range(92,102):
            pixel2 = yupiao.getpixel((i,c))
            # 目标黄字RGB163,146,25,目标灰底50,55,6799
            if abs(163 - pixel2[0]) <= 20 and abs(146 - pixel2[1]) <= 20 and abs(25 - pixel2[2]) <= 20:
                # print('获取鱼漂,等待鱼上钩,RGB色%s' % str(pixel2))
                f = open('text.txt', 'a')
                p13 = '获取鱼漂,等待鱼上钩\n'
                f.writelines(p13)
                f.close()

                time.sleep(2)
                # shengyin = Image.open('shengyin.jpg')
                for s in range(300):
                    time.sleep(0.05)
                    window_capture("shengyin2.jpg", 140, 270, 1610, 680)  # 声音截图检测
                    time.sleep(0.02)
                    shengyin2 = Image.open('shengyin2.jpg')
                    # pixel3 = shengyin.getpixel((58, 233))
                    pixel4 = shengyin2.getpixel((58, 233))
                    if s >=290:
                        # print('超时了，没有鱼上钩,重新抛竿')
                        f = open('text.txt', 'a')
                        p11 = '超时了，没有鱼上钩,重新抛竿\n'
                        f.writelines(p11)
                        f.close()
                        return
                    # pixel[0]代表R值，pixel[1]代表G值，pixel[2]代表B值  截图像素也许存在误差，10作为容差范围
                    elif abs(51 - pixel4[0]) >= 10 and abs(51 - pixel4[2]) >= 10:
                        # print('s是%s'%s)
                        continue

                    else:
                        # print('上钩了,收杆')
                        f = open('text.txt', 'a')
                        p12 = '上钩了,收杆\n'
                        f.writelines(p12)
                        f.close()
                        # 右键单击
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                        time.sleep(4)
                        return
            else:
                # print('未找到鱼漂,RGB色%s' % str(pixel2))  #999
                pass

def run():
    #首先截图原图以作对比     ###暂时不用
    window_capture("yuantu.jpg", 280, 170, 410, 205)
    yuantu = Image.open('yuantu.jpg')
    time_start = time.time()
    while True:
        diaoyu(yuantu)
        time_new = time.time()
        s = time_new - time_start
        # print('过去了%s秒'%s)
        if s > 600:
            return

if __name__ == '__main__':

    er = 0
    run()
    pass