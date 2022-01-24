with open("a.txt",'r',encoding="utf-8") as f:
    print("文件名是：{0}".format(f.name))
    print(f.tell())
    print(f.readline())
    print(f.tell())
a