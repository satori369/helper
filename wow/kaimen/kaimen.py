import time
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
        print("报错", er, '次')

#######################################退队有宏了,弃用
#退队函数包
# def tuidui():
#     # 鼠标定位自身头像信息
#     win32api.SetCursorPos([120, 75])
#     time.sleep(0.5)
#     # 右键单击
#     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
#     time.sleep(0.5)
#     # 鼠标定位到离开队伍
#     win32api.SetCursorPos([120, 280])
#     time.sleep(0.5)
#     # 执行左单键击，若需要双击则延时几毫秒再点击一次即可
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#     # 退队后继续找客户
#     time.sleep(1)
#     win32api.keybd_event(27, 0, 0, 0)  # ESC
#     win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开ESC

pass
#如果有esc就取消esc界面 包
def escjc():
    window_capture("ESC2.jpg",200,400,860,320)
    image1 = Image.open('ESC.jpg')
    image2 = Image.open('ESC2.jpg')
    pixel1 = image1.getpixel((120, 300))  # ESC坐标
    pixel2 = image2.getpixel((120, 300))

    if abs(pixel1[0] - pixel2[0]) <=10 and abs(pixel1[1] - pixel2[1]) <=10 and abs(pixel1[2] - pixel2[2])<=10 :
        print('ESC打开了,再按ESC取消',pixel2)    #ESC界面打开了
        win32api.keybd_event(27, 0, 0, 0)  # ESC
        win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开ESC


def zhaokehu():
    escjc()
    win32api.keybd_event(97, 0, 0, 0)  # 小键盘1 选取队友1
    win32api.keybd_event(97, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开1
    # 鼠标单击事件
    # 鼠标定位查看当前目标信息
    for y in range(96, 76,-1):
        time.sleep(0.01)
        win32api.SetCursorPos([280, y])
    time.sleep(0.5)
    #截图是否有选择队友1 选择则是在组队状态了
    window_capture("kehu.jpg",230,110,1590,830)
    image = Image.open('kehu.jpg')
    kh = mubiao_pipei(image)
    return kh

def mubiao_pipei(image):
    # image1 = Image.open('mubiaotu.jpg')
    #截图与素材原图对比2
    # for i in range(204, 208):
    for c in range(85, 102):
        pixel1 = image.getpixel((204, c))  # 目标坐标(白色边框)1
        # pixel2 = image1.getpixel((i, c))

        # pixel[0]代表R值，pixel[1]代表G值，pixel[2]代表B值  截图像素也许存在误差，10作为容差范围132, 129, 131,,,(55,20,60)
        if abs(pixel1[0] - 130) <= 15 and abs(pixel1[1] - 130) <= 15 and abs(pixel1[2] - 130) <= 15  or pixel1[0] == 0 and pixel1[2] == 0:
            print('来客户啦', pixel1, c)  # 客户上门,停止寻找客户,喊话等待客户交易
            # 有客户返回值1
            return 1
    # escjc()
    print('未匹配到目标,继续等待客户')
    time.sleep(1)
    # zhaokehu()  #没找到目标则调用自身继续寻找客户#####递归次数过多时不可取
    #没客户返回值0
    return 0


#确认交易函数包
def querenjiaoyi():
    # 鼠标定位交易按钮
    win32api.SetCursorPos([210, 505])
    time.sleep(0.5)
    # 执行左单键击，若需要双击则延时几毫秒再点击一次即可
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(1.5)
    # 鼠标定位确认交易按钮
    win32api.SetCursorPos([705, 220])
    time.sleep(0.5)
    # 左键单击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.5)

#开门函数包
def kaimen(n):
    li = ['奥格', '幽暗', '雷霆']
    print('n等于', n, '去往', li[n - 1])
    if li[n - 1] == '雷霆':
        win32api.keybd_event(103, 0, 0, 0)  # 7
        win32api.keybd_event(103, 0, win32con.KEYEVENTF_KEYUP, 0)
    elif li[n - 1] == '幽暗':
        win32api.keybd_event(104, 0, 0, 0)  # 8
        win32api.keybd_event(104, 0, win32con.KEYEVENTF_KEYUP, 0)
    elif li[n - 1] == '奥格':
        win32api.keybd_event(105, 0, 0, 0)  # 9
        win32api.keybd_event(105, 0, win32con.KEYEVENTF_KEYUP, 0)

def trade():
    s1 = 0
    s2 = 0
    s3 = 0
    while s1 <= 20:
        window_capture("jine.jpg", 50, 20, 333, 226)  # 截图交易金额函数
        image = Image.open('jine.jpg')
        pixel1 = image.getpixel((5, 10))# 交易界面坐标
        pixel2 = image.getpixel((40, 10))# 银币坐标
        print('截图交易界面(金额),组队等待%s秒,交易界面等待%s秒,确认交易等待%s秒'%(s1,s2,s3))
        # 在交易状态39, 36, 34  #RGB像素差小于5,表示在交易界面
        if abs(pixel1[0] - 39) <= 5 and abs(pixel1[1] - 36) <= 5 and abs(pixel1[2] - 34) <= 5:
            print('在交易状态')
            # 看到银币(163, 160, 163)##  小于5表示看到银币  (217, 193, 75)金币
            if abs(pixel2[0] - 163) <= 5 and abs(pixel2[1] - 160) <= 5 and abs(pixel2[2] - 163) <= 5or \
            abs(pixel2[0] - 217) <= 5 and abs(pixel2[1] - 193) <= 5 and abs(pixel2[2] - 75) <= 5:
                if pixel2[0]==163:
                    print('银币匹配')
                if pixel2[0]==217:
                    print('金币匹配')
                s3 += 1
                print('等待确认交易', s3)
                if s3 >= 20:
                    print('等待20秒还没确认交易,取消交易')
                    s3 = 0
                    # 10秒还没确认取消交易
                    win32api.keybd_event(27, 0, 0, 0)  # ESC
                    win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开ESC
                    win32api.keybd_event(98, 0, 0, 0)  # 小键盘2
                    win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)  # 队伍喊话广告
                    continue

                window_capture("jiaoyi2.jpg", 200, 500, 200, 146)
                # image11 = Image.open('querenjiaoyi.jpg')
                image12 = Image.open('jiaoyi2.jpg')

                # pixel11 = image11.getpixel((120, 300))  # 交易确认框坐标
                pixel12 = image12.getpixel((120, 300))
                # print('bug调试', pixel11, pixel12)
                # 对方交易确认,再检测金额 检测完毕就确认交易然后开门(52, 79, 47)
                if abs(pixel12[0] - 52) <= 10 and abs(pixel12[1] - 79) <= 10 and abs(pixel12[2] - 47) <= 10:
                    image1 = Image.open('aoge.jpg')
                    image2 = Image.open('youan.jpg')
                    image3 = Image.open('leiting.jpg')
                    list = [image1, image2, image3]
                    n = 0
                    # 通过像素差遍历匹配本地原图
                    for i in list:
                        n += 1
                        # 本人电脑原图与缺口图对应滑块图片横坐标相同，纵坐标原图比缺口图大88px，可根据实际情况修改
                        pixel3 = image.getpixel((15, 10))  # 金额1坐标 9
                        pixel4 = i.getpixel((15, 10))

                        pixel5 = image.getpixel((15, 3))  # 金额1坐标 9
                        pixel6 = i.getpixel((15, 3))

                        pixel7 = image.getpixel((23, 10))  # 金额2坐标 789
                        pixel8 = i.getpixel((23, 10))

                        pixel9 = image.getpixel((23, 3))  # 金额2坐标 789
                        pixel10 = i.getpixel((23, 3))

                        if n == 1:
                            print('正在匹配奥格中(99Y)')
                        elif n == 2:
                            print('正在匹配幽暗中(98Y)')
                        elif n == 3:
                            print('正在匹配雷霆中(97Y)')

                        # pixel[0]代表R值，pixel[1]代表G值，pixel[2]代表B值
                        if abs(pixel3[0] - pixel4[0]) == 0 and abs(pixel3[1] - pixel4[1]) == 0 and abs(
                                pixel3[2] - pixel4[2]) == 0:
                            print('金额1坐标1', n, pixel4)
                        else:
                            print('金额1坐标1没匹配上')
                            continue
                        if abs(pixel5[0] - pixel6[0]) == 0 and abs(pixel5[1] - pixel6[1]) == 0 and abs(
                                pixel5[2] - pixel6[2]) == 0:
                            print('金额1坐标2', n, pixel6)
                        else:
                            print('金额1坐标2没匹配上')
                            continue
                        if abs(pixel7[0] - pixel8[0]) == 0 and abs(pixel7[1] - pixel8[1]) == 0 and abs(
                                pixel7[2] - pixel8[2]) == 0:
                            print('金额2坐标1', n, pixel8)
                        else:
                            print('金额2坐标1没匹配上')
                            continue
                        if abs(pixel9[0] - pixel10[0]) == 0 and abs(pixel9[1] - pixel10[1]) == 0 and abs(
                                pixel9[2] - pixel10[2]) == 0:
                            print('金额2坐标2', n, pixel10)
                        else:
                            print('金额2坐标2没匹配上')
                            continue
                        print('金额匹配成功')
                        querenjiaoyi()
                        # 确认交易后,在开门
                        kaimen(n)
                        # TODO 开完门后,等人走了 我再退队  暂且用20秒退队
                        time.sleep(25)  # 等待传送门读条        20秒后 直接退队
                        print('完成一单')
                        # 退队宏设置3
                        win32api.keybd_event(99, 0, 0, 0)  # 小键盘3
                        win32api.keybd_event(99, 0, win32con.KEYEVENTF_KEYUP, 0)  # 小键盘3退队
                        win32api.keybd_event(27, 0, 0, 0)  # ESC
                        win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开ESC
                        win32api.keybd_event(39, 0, 0, 0)  # 方向键右
                        time.sleep(0.5)
                        win32api.keybd_event(39, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开方向键右
                        return 1

                    print('确认交易了,但是金额不对,取消交易')
                    win32api.keybd_event(27, 0, 0, 0)  # ESC
                    win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开ESC
                time.sleep(1)
                continue
            else:
                print('银币不匹配')
                if pixel2 == (179, 123, 88):
                    print('看到金币或铜币,取消交易')
                    win32api.keybd_event(27, 0, 0, 0)  # ESC
                    win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开ESC
                    win32api.keybd_event(98, 0, 0, 0)  # 小键盘2
                    win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)  # 队伍喊话广告
                    continue
                else:
                    print('还没给钱 等一会')
                    s2 += 1
                    print('等待交易金额', s2)
                    if s2 >= 20:
                        print('等待20秒还没给钱,取消交易')
                        # 清空计数
                        s2 = 0
                        win32api.keybd_event(27, 0, 0, 0)  # ESC
                        win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开ESC
                        # win32api.keybd_event(98, 0, 0, 0)  # 小键盘2
                        # win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)  # 队伍喊话广告
                    time.sleep(1)
                    continue

        # 不在交易状态
        else:
            s1 += 1
            print('不在交易状态,等待交易,等待20秒后退队', s1)
            ###todo 加入队伍广告说明
            win32api.keybd_event(98, 0, 0, 0)  # 小键盘2
            win32api.keybd_event(98, 0, win32con.KEYEVENTF_KEYUP, 0)  # 队伍喊话广告
            time.sleep(1)
            continue

    # 清空计数
    s1 = 0
    # 没顺利交易则退队
    print('循环结束,退队+esc')
    win32api.keybd_event(99, 0, 0, 0)  # 小键盘3
    win32api.keybd_event(99, 0, win32con.KEYEVENTF_KEYUP, 0)  # 小键盘3退队
    win32api.keybd_event(27, 0, 0, 0)  # ESC
    win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开ESC
    time.sleep(2)
    return 0


def run():
    time_start = time.time()
    while True:
        time.sleep(1)
        kh = zhaokehu()
        #如果kh有值 则表明来客户了,进入交易函数
        if kh:
            dan = trade()  # 交易函数
            print('总共完成%s单'%dan)

        image1 = Image.open('duankai.jpg')
        # 截图与素材原图对比(99, 7, 7) (100, 1, 1)
        pixel1 = image1.getpixel((20, 30))
        pixel2 = image1.getpixel((230, 30))
        pixel4 = image1.getpixel((180, 208))
        # 如果检测到断开连接,准备进行重连
        if abs(pixel1[0] - 100) <= 10 and abs(pixel1[1] - 7) <= 10 and abs(pixel1[2] - 7) <= 10 or \
                abs(pixel2[0] - 100) <= 10 and abs(pixel2[1] - 1) <= 10 and abs(pixel2[2] - 1) <= 10 or \
                abs(pixel4[0] - 120) <= 10 and abs(pixel4[1] - 17) <= 10 and abs(pixel4[2] - 10) <= 10:

            print('检测到断开连接,暂停寻找客户120s')
            time.sleep(120)
            return

        time_new = time.time()
        s = time_new - time_start
        # print('过去了%s秒'%s)
        if s > 60000:
            return
        if er >= 10:
            print('截图报错10次,结束循环')
            return

if __name__ == '__main__':
    er = 0
    run()