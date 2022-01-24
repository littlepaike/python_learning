# coding=utf-8
# 使用递归计算n的阶乘
import os


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))


def getAllFiles(path):
    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            getAllFiles(filepath)
        print(filepath)

getAllFiles("movie")
