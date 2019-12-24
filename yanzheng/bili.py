
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from PIL import Image
from time import sleep
from functools  import reduce


# 初始化
def init():
    # 定义为全局变量，方便其他模块使用
    global url, browser, username, password, wait
    # 登录界面的url
    url = 'https://passport.bilibili.com/login'
    # 实例化一个chrome浏览器
    options = webdriver.ChromeOptions()
    options.binary_location = r"E:\Chrome\chrome.exe"
    browser = webdriver.Chrome(chrome_options=options)
    # 用户名
    username = '***********'
    # 密码
    password = '***********'
    # 设置等待超时
    wait = WebDriverWait(browser, 20)


# 登录
def login():
    # 打开登录页面
    browser.get(url)
    # 获取用户名输入框
    user = wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
    # 获取密码输入框
    passwd = wait.until(EC.presence_of_element_located((By.ID, 'login-passwd')))
    # 输入用户名
    user.send_keys(username)
    # 输入密码
    passwd.send_keys(password)
    # 获取打开滑块验证码页面的元素
    log = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="geetest-wrap"]/ul/li[5]/a[1]')))
    # 点击进入滑块验证码页面
    log.click()

# 构造滑动轨迹
def get_trace(distance):
    '''
    :param distance: (Int)缺口离滑块的距离
    :return: (List)移动轨迹
    '''

    # 创建存放轨迹信息的列表
    trace = []
    # 设置加速的距离
    faster_distance = distance * (4 / 5)
    # 设置初始位置、初始速度、时间间隔
    start, v0, t = 0, 0, 0.2
    # 当尚未移动到终点时
    while start < distance:
        # 如果处于加速阶段
        if start < faster_distance:
            # 设置加速度为2
            a = 2
        # 如果处于减速阶段
        else:
            # 设置加速度为-3
            a = -3
        # 移动的距离公式
        move = v0 * t + 1 / 2 * a * t * t
        # 此刻速度
        v = v0 + a * t
        # 重置初速度
        v0 = v
        # 重置起点
        start += move
        # 将移动的距离加入轨迹列表
        trace.append(round(move))
    # 返回轨迹信息
    return trace

def huadong():
    # 获取拖拽的圆球
    slideblock = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div[1]/div[2]/div[2]')))
    # 鼠标点击圆球不松开
    ActionChains(browser).click_and_hold(slideblock).perform()
    # 将圆球滑至相对起点位置的最右边
    print('准备拖')
    ActionChains(browser).move_by_offset(xoffset=180, yoffset=0).perform()
    print('拖完了')
    sleep(0.4)
    # 保存包含滑块及缺口的页面截图
    browser.save_screenshot('quekou.png')
    # 放开圆球
    ActionChains(browser).release(slideblock).perform()
    # 打开保存至本地的缺口页面截图
    quekouimg = Image.open('quekou.png')
    # 匹配本地对应原图
    sourceimg = match_source(quekouimg)

    # 获取缺口位置
    print('准备获取缺口位置')
    visualstack = get_diff_location(sourceimg, quekouimg)
    # 获取移动距离loc，827为滑块起点位置
    print('visua是',visualstack)
    loc = visualstack - 827 - 3
    print('滑动距离loc是',loc)
    if loc<=40:
        loc += 5
        print('loc+5现在是',loc)
    elif 40 < loc < 80:
        loc += 9
        print('loc+9',loc)
    elif 80 < loc < 100:
        loc += 2
        print('loc+2',loc)
    elif 115 < loc < 130 :
        loc -= 3
        print('loc-3现在是', loc)
    elif 130<= loc<150:
        loc -= 6
        print('loc-6现在是',loc)
    elif 150<loc <170:
        loc -= 9
        print('loc-9现在是',loc)
    elif 170 < loc <200:
        loc -= 12
        print('loc-12现在是', loc)
    # 生成拖拽移动轨迹，加3是为了模拟滑过缺口位置后返回缺口的情况
    track_list = get_trace(loc + 3)
    print(track_list,'list')
    sum = reduce(lambda x, y: x + y, track_list)
    print(sum,'list sum')
    sleep(2)
    ActionChains(browser).click_and_hold(slideblock).perform()
    sleep(0.2)
    # 根据轨迹拖拽圆球
    n = 0
    for i in range(len(track_list)-1,0,-1):
        ActionChains(browser).move_by_offset(xoffset=track_list[i], yoffset=0).perform()
        n += track_list[i]

        print('移动了%s' % n, track_list[i])
    # ActionChains(browser).move_by_offset(xoffset=sum, yoffset=0).perform()
    # 模拟人工滑动超过缺口位置返回至缺口的情况，数据来源于人工滑动轨迹，同时还加入了随机数，都是为了更贴近人工滑动轨迹
    imitate = ActionChains(browser).move_by_offset(xoffset=-1, yoffset=0)
    sleep(0.015)
    imitate.perform()
    sleep(random.randint(6, 10) / 10)
    imitate.perform()
    sleep(0.008)
    imitate.perform()
    sleep(0.012)
    imitate.perform()
    sleep(0.019)
    imitate.perform()
    sleep(0.013)
    ActionChains(browser).move_by_offset(xoffset=1, yoffset=0).perform()
    # 放开圆球
    sleep(0.5)
    ActionChains(browser).pause(random.randint(6, 14) / 10).release(slideblock).perform()
    sleep(random.random() * 5 + 0.5)

def match_source(image):
    image1 = Image.open('d://yuantu//source1.png')
    image2 = Image.open('d://yuantu//source2.png')
    image3 = Image.open('d://yuantu//source3.png')
    image4 = Image.open('d://yuantu//source4.png')
    image5 = Image.open('d://yuantu//source5.png')
    image6 = Image.open('d://yuantu//source6.png')
    image7 = Image.open('d://yuantu//source7.png')
    image8 = Image.open('d://yuantu//source8.png')
    image9 = Image.open('d://yuantu//source9.png')
    image10 = Image.open('d://yuantu//source10.png')
    list = [image1, image2, image3, image4,image5,image6,image7,image8,image9,image10]
    # 通过像素差遍历匹配本地原图
    for i in list:
        # 本人电脑原图与缺口图对应滑块图片横坐标相同，纵坐标原图比缺口图大88px，可根据实际情况修改
        pixel1 = image.getpixel((802, 350))
        pixel2 = i.getpixel((803, 350))
        # pixel[0]代表R值，pixel[1]代表G值，pixel[2]代表B值
        if abs(pixel1[0] - pixel2[0]) < 5:
            print('找到原图',i)
            return i

    print('返回了image',image)
    return image


# 计算滑块位移距离
def get_diff_location(image1,image2):
    print('准备计算滑块移动距离')
    #（825,1082）（335,463）为滑块图片区域，可根据实际情况修改
    for i in range(827,1082):
        for j in range(335,463):
            #遍历原图与缺口图像素值寻找缺口位置
            if is_similar(image1,image2,i,j)==False:
                # print('找到缺口位置',i)
                return i
    return -1


# 对比RGB值得到缺口位置
def is_similar(image1,image2,x,y):
    pixel1=image1.getpixel((x+1, y))
    pixel2=image2.getpixel((x, y))
    # 截图像素也许存在误差，50作为容差范围
    if abs(pixel1[0]-pixel2[0])>=50 and abs(pixel1[1]-pixel2[1])>=50 and abs(pixel1[2]-pixel2[2])>=50:
        return False
    return True

def main():
    # 初始化
    init()
    # 登录
    login()
    huadong()


# 程序入口
if __name__ == '__main__':
    main()