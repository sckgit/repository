#coding:utf-8
import os

name = 'John Doe'
print('你好')
newstr=name.capitalize()
new_str=newstr.upper()
newstr_swapped=newstr.swapcase()
new_len=new_str.zfill(10)
print(new_len)
print(new_str)
print(newstr_swapped)
print(os.getcwd())