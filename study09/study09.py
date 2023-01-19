#多文件学习


import test_file_1,test_file_2
from test_file_3 import fun
from test_file_3 import var

#调用两个文件的同名函数
"""
print('fun() form 1:')
test_file_1.fun()

print('fun() form 2:')
test_file_2.fun()
"""


#调用两个文件的同名变量
"""
print('var from 1:')
print(f'var = {test_file_1.var}')

print('var from 1:')
print(f'var = {test_file_2.var}')
"""


#局部引入的调用方式
"""
print('fun_3_test:')
fun()

print('var_3:')
print(f'var = {var}')
"""


#查看py的包含路径
"""
import sys
for path in sys.path:
    print (path)
"""


#尝试调用网站接口
"""
import requests

ret = requests.get('http://www.baidu.com')
print('ret.text = ')
print(ret.text)

ret = requests.get(
    'http://hq.sinajs.cn/list=sh601006',        #大秦铁路（股票代码：sh601006）
    # 现在一定要加上下面这个消息头
    headers ={'Referer':'http://finace.sina.com.cn'}
)

"""



