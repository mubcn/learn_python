'''
| 类型名称 | 英文名 | 举例 | 备注 |
| --- | --- | --- | --- |
| 字符串 | string | 张三 ‘李四' | 用引号包起来 |
| 整型 | int | 18 22 | 不带小数点的数 |
| 浮点型 | float | 65.2 74.6 | 带小数点的数 |
|  |  |  |  |
'''

test = type('张三')
print(test)  # <class 'str'>
print(type('张三'))  # <class 'str'>
print(type(18))  # <class 'int'>
print(type(52.5))  # <class 'float'>

# 注意：在Python中：变量无类型数据有类型

print('*' * 16)  # 分割
print(type('18'))  # <class 'str'>
print(type(18))  # <class 'int'>
print(type('65.2'))  # <class 'str'>
print(type(65.2))  # <class 'float'>
