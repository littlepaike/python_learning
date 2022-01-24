import os

print(os.name)  # windows->nt  linux unix->posix
print(os.sep)  # windows->\   linux unix->/
print(repr(os.linesep))  # windows->\r\n linux ->\n

data_dir = os.sep.join(['hello', 'world'])
print(data_dir)

print(os.stat('01.py'))
#########关于工作目录的操作###########
print(os.getcwd())
# os.mkdir()
# os.chdir("d:")

# os.makedirs("s/e/q")
# os.removedirs("s/e/q")    #只能删除空目录

