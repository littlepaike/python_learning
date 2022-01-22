# coding=utf-8
# trackback
import traceback

try:
    print("step1")
    num = 1 / 0
    
except:
    traceback.print_exc()
