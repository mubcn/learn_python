name = '张三'
gender = '男'
weight = 65.45
age = 12

# 1.字符串的最小宽度，位数不够会自动使用空格补全，位数小于字符串长度则不起作用
# 正数是右对齐，负数是左对齐
# 在 %m.ns 中,m为宽度,当输出的内容大于m,m则失效;n为精度,

info = '我叫%4.1s，性别是%4.2s,体重是%f,年龄是%d' % (name, gender, weight, age)
print(info)

# 在 %m.nf 中,m为