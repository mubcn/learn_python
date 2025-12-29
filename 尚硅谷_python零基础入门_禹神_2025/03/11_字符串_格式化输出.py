"""
按照预先定义的格式，将变量或计算结果，插入到字符串中并输出。
"""

name = '张三'
gender = '男'
weight = 65.2
age = 12

# 写法一:直接用加号进行拼接,写起来很麻烦,而且只能是字符串之间拼接.
info1 = '我叫' + name + ',我是' + gender + '生'
print(info1)

# 写法二:使用占位符,占位符使用%后添加数据类型.可以全部使用%s,解释器会转换为字符串
info2 = '我叫%s,我是%s生,我的体重是%f,我的年龄是%i岁' % (name, gender, weight, age)
print(info2)

info2 = '我叫%s,我是%s生,我的体重是%s,我的年龄是%s岁' % (name, gender, weight, age)
print(info2)

info2 = '我叫%s,我是%s生,我的体重是%i,我的年龄是%i岁' % (name, gender, weight, age)
print(info2)  # 转换过程会丢失精度

# %s占位字符串，%f占位浮点数，%1占位整数，%d占位十进制的整数，%s是万能的。

# 写法三:使用f-string,是目前python最推荐的方式.
info3 = f'我叫{name},我是{gender}生,我的体重是{weight},年龄是{age}'
print(info3)