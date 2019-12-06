'''
号码筛选小程序
'''
import time
from phone import Phone

import csv

def shaixuan():
    # 打开csv
    print('-----------------------------------------------------------------------------------------')
    print('号码筛选小程序使用说明:\n(1)将号码保存到txt文件,每个号码一行;\n(2)将txt文件放到本程序当前目录下;\n(3)程序运行结束后将创建csv文件到当前目录下;\n')
    print('接下来请输入你要打开的txt文件名,如"xxx.txt",输入xxx即可')
    print('-----------------------------------------------------------------------------------------')
    xxx = input('文件名是:')
    # 打开txt
    t1 = time.time()
    try:
        with open(xxx + '.txt', 'r', encoding='UTF-8') as f:
            tel_list = []
            n = 0
            nn = 0
            for num in f:
                # print(num.strip())
                # 把号码放入函数转换成字典

                try:
                    info = Phone().find(num.strip())
                    print(info)
                    phone = info['phone']
                    province = info['province']
                    city = info['city']
                    zip_code = info['zip_code']
                    area_code = info['area_code']
                    phone_type = info['phone_type']
                    # 把字典里的值放入元组添加到列表
                    tel_list.append(
                        (phone, province, city, zip_code, area_code, phone_type)
                    )
                    n += 1
                except Exception as e:
                    print(e)
                    print(num+ '无法识别')
                    nn += 1
    except Exception as e:
        input('应该是文件名输错了,请检查后重试')
    else:
        # 遍历结束后,把列表写入到csv(一次性全部写入)
        ff = open(xxx + '.csv', 'a', newline='')
        writer = csv.writer(ff)
        writer.writerows(tel_list)
        f.close()
        ff.close()
        print('成功查找%s条数据,有%s条没找到'%(n,nn))
        return t1


if __name__ == "__main__":

    t1 = shaixuan()
    print('运行时间:%.2f'% (time.time()-t1)+'秒')
    input('运行结束')