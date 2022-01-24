# coding=utf-8

import shutil
import zipfile

shutil.copyfile("a.txt", "a_copy.txt")
# shutil.copytree()

# 压缩 解压缩
# shutil.make_archive("电影/gg","zip","movie/港台")

# z1 = zipfile.ZipFile("zipfile.zip","w")
# z1.write("01.py")
# z1.write("os模块.py")
# z1.close()

z2 = zipfile.ZipFile("E:\paike\pycharm_workspace\python_learning\第二季\第八章 文件操作\zipfile.zip","r")
z2.extractall("电影")
z2.close()