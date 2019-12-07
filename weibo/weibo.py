import re
import openpyxl
import requests
import time,random
from lxml import etree # 导入xpath
from queue import Queue # 导入队列
from selenium import webdriver # 模拟登录
# from selenium.webdriver import ActionChains # 引入鼠标事件类
from selenium.webdriver.common.keys import Keys # 引入键盘事件类


class WeiboSpider(object):
    def __init__(self,obj):
        self.obj = obj
        self.url = 'https://s.weibo.com/weibo?q={}&Refer=SWeibo_box&page={}'
        self.q = Queue()
        self.f = open('cookies.txt',encoding='utf-8')
        self.headers ={
            "Cookie": self.f.read(),
            "Referer": self.url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400",}
        self.value = [["博主姓名", "微博正文", "评论数", "转发数", "点赞数","发布时间"],
                      ]
        # excel文件名
        self.path = self.obj + '.xlsx'
        # excel表1名
        self.sheet_name = '微博搜索' + self.obj

    # 获取页面
    def parse_html(self):
        while True:
            # 如果队列不是空
            if not self.q.empty():
                url = self.q.get()
                print('get url',url)
                try:
                    print('准备获取html')
                    html = requests.get(url=url,headers=self.headers,timeout=3).content.decode('utf-8','ignore')
                    # 如果有二级页面跳转
                    url_two = re.compile(r'location.replace\("(.*?)"\);')
                    url_two = url_two.findall(html)
                    if url_two:
                        print('走页面跳转-----------------')
                        html = requests.get(url=url_two[0], headers=self.headers, timeout=3).content.decode('utf-8','ignore')
                    # 执行解析函数
                    self.parse_content(html)
                    # 每页随机休眠
                    time.sleep(random.uniform(0.2,0.7))
                except Exception as e:
                    print('Retry')
                    exit()
            else:
                break

    # 模拟登录获取cookies
    def weibocookies(self):
        # 创建选项对象
        print('开始访问微博首页...')
        options = webdriver.ChromeOptions()
        # 无头模式
        # options.add_argument('--headless')
        # 添加路径
        options.binary_location = r"E:\Chrome\chrome.exe"
        # 创建浏览器对象
        browser = webdriver.Chrome(chrome_options=options)
        browser.get('https://weibo.com/login.php')
        print('页面渲染成功,准备登录')
        time.sleep(5)
        browser.find_element_by_id('loginname').send_keys('17607130551')
        time.sleep(0.5)
        browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('qq781124')
        time.sleep(0.5)
        browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(Keys.ENTER)
        print('登录中,页面渲染有点慢,请稍等片刻')
        time.sleep(10)
        print('登陆成功,准备获取cookies')
        with open('cookies.txt', 'w', encoding='utf-8') as f:
            for cook in browser.get_cookies():
                print(cook['name'], ':')
                print(cook['value'], ';')
                f.write(cook['name'] + '=' + cook['value'] + '; ')
            f.close()
            print('cookies写入成功,请重新启动本程序')
        # 关闭浏览器
        browser.quit()

    # 获取页数,url入队
    def url_in(self):
        pageurl = 'https://s.weibo.com/weibo?q={}&Refer=SWeibo_box'.format(self.obj)
        try:
            html = requests.get(url=pageurl, headers=self.headers, timeout=3).content.decode('utf-8', 'ignore')
            # 如果有二级页面跳转
            url_two = re.compile(r'location.replace\("(.*?)"\);')
            url_two = url_two.findall(html)
            if url_two:
                print('走页面跳转-----------------')
                html = requests.get(url=url_two[0], headers=self.headers, timeout=3).content.decode('utf-8', 'ignore')
            # print(html)
            p = etree.HTML(html)
            li_list = p.xpath('//ul[@class="s-scroll"]/li')
            # print(li_list,'页数')  # 获取所有页数对象
            # ['第44页'] -->44
            li = li_list.pop().xpath('.//text()')[0][1:-1]  # 获取最后一页
        except IndexError as e:
            print('登录状态过期,没有获取到页数,准备重新登录')
            self.f.close()
            self.weibocookies() # 微博模拟登录接口
            input('按回车退出')
            exit()
        except Exception as e:
            print(e)
            print('页数没拿到')
            exit()
        else:
            for page in range(1,int(li)+1):
                # 拼接所有页数,放入队列
                url = pageurl+'&page={}'.format(page)
                print(url)
                self.q.put(url)

    # 解析页面函数
    def parse_content(self,html):
        ######正文解析
        # 替换em标签
        htmlem = re.sub('<em class="s-color-red">.*?</em>', self.obj, html)
        # 替换img标签
        htmlimg = re.sub('<img.*?/>', '[图片]', htmlem)
        # 替换<br/>
        htmlbr = re.sub('<br/>', '\n', htmlimg)
        # 替换a标签前半部分
        pxa = re.compile('<a.*?>')
        htmla = pxa.sub('', htmlbr)
        # 替换</a>
        htmla = htmla.replace('</a>', '')
        # xpath解析
        pcon = etree.HTML(htmla)
        contentobj = pcon.xpath('//div[@class="card-wrap"]//div[@class="content"]/p[@node-type="feed_list_content"]')
        # print(contentobj)
        contentall = []
        for content in contentobj:
            # 看是否有展开全文
            zkqw = content.xpath('./text()')
            # 有展开全文
            if '展开全文' in ''.join(zkqw):
                zw = content.xpath('../p[@node-type="feed_list_content_full"]/text()')
                # print('有展开全文,if in',zw)
                # 极端情况,内容中含有展开全文这四个字的时候
                if not zw:
                    text = ''
                    for qw in zkqw:
                        text += qw
                    text = text.strip().replace('\u200b', '').strip()
                    contentall.append(text)
                # 遍历拼接文本内容
                textall = ''
                for qw in zw:
                    textall += qw
                textall = textall.strip().strip('收起全文').replace('\u200b','').strip()
                # print('有展开全文拼接str', textall)
                contentall.append(textall)
            # 没有展开全文
            else:
                # print('没有',zkqw)
                # 遍历拼接文本内容
                text = ''
                for qw in zkqw:
                    text += qw
                text = text.strip().replace('\u200b','').strip()
                contentall.append(text)
        # print(len(contentall))
        # print('listttt-----',contentall)
        ###### 拿到微博正文数量后,解析其他数据
        p = etree.HTML(html)
        bozhuidall = p.xpath('//div[@class="card-wrap"]//div[@class="content"]//a[@class="name"]/text()')  # 博主id
        n = 1
        pinglunall = []
        zhuanfaall = []
        dianzanall = []
        timeall = []
        for card in range(len(contentall)):
            pinglun = p.xpath('//div[@class="card-wrap"][{}]//div[@class="card-act"]/ul/li[3]/a/text()'.format(n))[0].strip()  # 评论数
            if pinglun == '评论':
                pinglun += '0'
            pinglunall.append(pinglun)
            zhuanfa = p.xpath('//div[@class="card-wrap"][{}]//div[@class="card-act"]/ul/li[2]/a/text()'.format(n))[0].strip()  # 转发数
            if zhuanfa == '转发':
                zhuanfa += '0'
            zhuanfaall.append(zhuanfa)
            dianzan = p.xpath('//div[@class="card-wrap"][{}]//div[@class="card-act"]/ul/li[4]/a/em/text()'.format(n))  # 点赞数
            # print(dianzan,'zheshi 点赞')
            if not dianzan:
                dianzan = ['0']
            dianzanall.append(dianzan[0])
            fabushijian = p.xpath('//div[@class="card-wrap"][{}]//div[@class="content"]//p[@class="from"]/a/text()'.format(n))  # 发布时间
            n += 1
            fabustr = ''
            for fabu in fabushijian:
                fabustr += fabu
            timeall.append(''.join(''.join(fabustr.split('\n')).split()))

        # 整合每条微博数据,添加到value
        for i in range(len(contentall)):
            val = [bozhuidall[i], contentall[i], pinglunall[i],zhuanfaall[i],dianzanall[i],timeall[i]]
            print(val)
            self.value.append(val)
        # print('博主id是:', bozhuidall, '\n正文是:', contentall, '\n评论是', pinglunall, '\n转发是', zhuanfaall, '\n点赞是', dianzanall,'\n发布时间是', timeall)
        # return contentall

    # 写入excel
    def write_excel_xlsx(self):
        print('准备写入xlsx------------')
        if len(self.value) == 1:
            print('没获取到内容,写入xlsx失败')
            return
        index = len(self.value)  # 获取需要写入数据的行数
        workbook = openpyxl.Workbook()  # 新建一个工作簿
        sheet = workbook.active
        sheet.title = self.sheet_name
        for i in range(0, index):
            for j in range(0, len(self.value[i])):
                sheet.cell(row=i + 1, column=j + 1, value=str(self.value[i][j]))
        workbook.save(self.path)
        print("xlsx格式表格写入数据成功！")

    # 走你
    def run(self):
        # 获取搜索关键字后的微博页数后将url入队列
        self.url_in()
        print('url全部入队,1秒后获取页面信息')
        time.sleep(1)
        # 页面解析
        self.parse_html()
        # 写入excel
        self.write_excel_xlsx()
        # 关闭cookies文本
        self.f.close()

if __name__ == '__main__':
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('微博搜索查询,自动写入excel工具')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    obj = input('输入微博搜索的关键字:')
    t1 = time.time()
    spider = WeiboSpider(obj)
    spider.run()
    print('运行时间:%.2f秒'%(time.time()-t1))
    input('运行结束owo,本程序仅供个人测试学习,请勿商用,谢谢合作!')
    print('按回车键退出')