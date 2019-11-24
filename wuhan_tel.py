from phone import Phone
import csv
if __name__ == "__main__":
    #打开csv
    ff = open('tel.csv', 'a', newline='')
    writer = csv.writer(ff)
    with open('520.txt','r') as f:
        tel_list = []
        for num in f:
            # print(num.strip())
            info = Phone().find(num.strip())
            print(info)
            try:
                phone = info['phone']
                province = info['province']
                city = info['city']
                zip_code = info['zip_code']
                area_code = info['area_code']
                phone_type = info['phone_type']
                tel_list.append(
                    (phone,province,city,zip_code,area_code,phone_type)
                )

            except:
                print('none')
        writer.writerows(tel_list)
    f.close()
    ff.close()