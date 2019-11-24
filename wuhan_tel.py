from phone import Phone
import csv
if __name__ == "__main__":
    #打开csv
    ff = open('tel.csv', 'a', newline='')
    writer = csv.writer(ff)
    # 打开txt
    with open('520.txt','r') as f:
        tel_list = []
        for num in f:
            # print(num.strip())
            #把号码放入函数转换成字典
            info = Phone().find(num.strip())
            print(info)
            try:
                phone = info['phone']
                province = info['province']
                city = info['city']
                zip_code = info['zip_code']
                area_code = info['area_code']
                phone_type = info['phone_type']
                # 把字典里的值放入元组添加到列表
                tel_list.append(
                    (phone,province,city,zip_code,area_code,phone_type)
                )
            except:
                print('none')
        # 遍历结束后,把列表写入到csv(一次性全部写入)
        writer.writerows(tel_list)
    f.close()
    ff.close()