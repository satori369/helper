import time
# import re
# import requests
# from lxml import etree
import openpyxl
from selenium import webdriver # 模拟登录
# from selenium.webdriver import ActionChains # 引入鼠标事件类
from selenium.webdriver.common.keys import Keys # 引入键盘事件类


# print('hello world')

class ZhuaquSpider():
    def __init__(self,):
        self.value = [["客户电话"],]
        # excel文件名
        # self.path = '号码本' + riqi + '.xlsx'
        # excel表1名
        self.sheet_name = '号码本'
        # self.f = open('name.txt', encoding='utf-8')

    def parse_html(self):
        print('开始访问首页...')
        # options = webdriver.ChromeOptions()
        # 无头模式
        browser = webdriver.Chrome(executable_path=r'D:\Python\Scripts\chromedriver.exe')
        browser.get('https://login.aihujing.com/#/login')
        time.sleep(5)
        print('页面渲染成功,准备登录')
        #user定位
        ###获取txt文档里的第一行
        user = self.f.readline()
        browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/p[2]/input').send_keys(user)
        #password定位
        time.sleep(1)
        ###获取txt文档里的第二行
        password = self.f.readline()
        browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/p[3]/input').send_keys(password)
        self.f.close()
        #登录确认定位
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/button').click()
        time.sleep(3)
        #手机管理定位
        browser.find_element_by_xpath('//*[@id="aside"]/div[1]/div/ul/li[3]/div').click()
        time.sleep(1)
        #通话数据定位
        #//*[@id="aside"]/div[1]/div/ul/li[3]/ul/li/ul/li/span
        browser.find_element_by_xpath('//*[@id="aside"]/div[1]/div/ul/li[3]/ul/li/ul/li[2]/span').click()
        #//*[@id="watermark"]/div[1]/div[1]/div/span[3]
        time.sleep(2)
        #详单定位
        browser.find_element_by_xpath('//*[@id="watermark"]/div[1]/div[1]/div/span[3]').click()
        print('为保证数据抓取不丢失，总页数限制80页内')
        riqi = input('请手动选择日期，并输入到此处(用于表格命名),然后按回车')
        # excel文件名
        self.path = '号码本' + riqi + '.xlsx'
        time.sleep(3)
        #总共页数定位
        max_str = browser.find_element_by_xpath('//*[@id="watermark"]/div[1]/div[2]/div[2]/div[3]/div/div[3]/ul/li[2]').text
        max = max_str.split(' ')[1]
        print('总共有%s页' % max)
        max_num = int(max)
        # 获取号码函数
        print('2秒后开始抓取号码---')
        time.sleep(2)

        for i in range(2,max_num+1):
            time.sleep(1)
            #抓取号码函数
            self.parse_content(browser)
            print('第%s页抓取完毕'%(i-1))
            #输入下一页的页数，然后回车
            browser.find_element_by_xpath('//*[@id="watermark"]/div[1]/div[2]/div[2]/div[3]/div/div[3]/ul/li[2]/input').clear()
            browser.find_element_by_xpath('//*[@id="watermark"]/div[1]/div[2]/div[2]/div[3]/div/div[3]/ul/li[2]/input').send_keys(str(i))
            time.sleep(0.5)
            browser.find_element_by_xpath('//*[@id="watermark"]/div[1]/div[2]/div[2]/div[3]/div/div[3]/ul/li[2]/input').send_keys(Keys.ENTER)
            time.sleep(3)
        print('全部抓取完毕，写入到excel文档')
        # input('a')
        # return self.path

    #获取号码
    def parse_content(self, browser):
        # 遍历手机号节点
        for i in range(1, 31):
            try:
                phone = browser.find_element_by_xpath('//*[@id="watermark"]/div[1]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[%s]/td[5]/div/div/p' % i).text
                print(phone)
                self.value.append([phone])
                ###TODO
            #最后一页不满30个时，就错误处理退出循环
            except:
                print('未找到字符串')
                if i <= 5:
                    time.sleep(1)
                    continue
                print('抓取完毕')
                break

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

    def run(self):
        self.parse_html()
        self.write_excel_xlsx()


if __name__ == '__main__':
    # riqi = input('请输入搜索日期，用于表格文档命名')
    spider = ZhuaquSpider()
    spider.run()
    #//*[@id="watermark"]/div[1]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/div/div/p
    #//*[@id="watermark"]/div[1]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[4]/td[5]/div/div/p

    #//*[@id="watermark"]/div[1]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[30]/td[5]/div/div/p
    #//*[@class="el-table_7_column_114  "]//p/text()