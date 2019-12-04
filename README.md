##脚本工具箱

    - 1.excel写入数据库脚本
        * 提供excel文件名,库名,表名即可运行
    
    - 2.批量筛选电话号码地区
        * 提供要打开的号码txt文件名即可

##生成exe文件



```cmd

可选参数	  格式举例	       			   功能说明
-F			pyinstaller -F demo.py		只在dist中生产一个demo.exe文件。
-D			pyinstaller -D demo.py		默认选项，除了demo.exe外，还会在在dist中生成很多依赖文件，推荐使用。
-c			pyinstaller -c demo.py		默认选项，只对windows有效，使用控制台，就像编译运行C程序后的黑色弹窗。
-w			pyinstaller -w demo.py		只对windows有效，不使用控制台。
-p			pyinstaller -p E:\python\Lib\site-packages demo.py		设置导入路径，一般用不到。
-i			pyinstaller -i D:\file.icon demo.py		将file.icon设置为exe文件的图标，推荐一个icon网站:https://tool.lu/tinyimage/



pyinstaller --onefile --nowindowed --icon="D:\stu\xcx\favicon.ico" wuhan_tel.py
pyinstaller -F wuhan_tel.py
```





​    



​	