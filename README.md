##脚本工具箱

    - 1.excel写入数据库脚本-ex_sql
        * 提供excel文件名,库名,表名即可运行
    - 2.批量筛选电话号码地区工具-telctiy
        * 提供要打开的号码txt文件名即可
    - 3.爬取微博搜索关键字信息,自动写入excel工具-weibo
    	* 输入关键字即可
    	* cookies过期时,模拟登录获取cookies
    - 4.列表助手类-listhelper
        * 查询工具箱
        * 快排
        * 二分查找
    - 5.滑动验证破解-yanzheng
    	* 获取原图,修改打开原图路径即可
    - 6.ww用-ww
    - 7.wow钓鱼以及开门-wow

##生成exe文件



```cmd

可选参数	  格式举例	       			   功能说明
-F			pyinstaller -F demo.py		只在dist中生产一个demo.exe文件。
-D			pyinstaller -D demo.py		默认选项，除了demo.exe外，还会在在dist中生成很多依赖文件，推荐使用。
-c			pyinstaller -c demo.py		默认选项，只对windows有效，使用控制台，就像编译运行C程序后的黑色弹窗。
-w			pyinstaller -w demo.py		只对windows有效，不使用控制台。
-p			pyinstaller -p E:\python\Lib\site-packages demo.py		设置导入路径，一般用不到。
-i			pyinstaller -i D:\file.icon demo.py		将file.icon设置为exe文件的图标，推荐一个icon网站:https://tool.lu/tinyimage/



pyinstaller --onefile --nowindowed --icon="D:\stu\xcx\favicon.ico" weibo.py
pyinstaller -F wuhan_tel.py
```





​    



​	