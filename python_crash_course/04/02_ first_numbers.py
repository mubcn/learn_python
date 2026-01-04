"""
4.3 创建数值列表
26-01-02
使用函数range()生成数据
"""

# 4.3.1 使⽤ range() 函数
numbers = []
for value in range(1, 5):  # range(1, 5) 是指从1到4
    print(value)
for value in range(1, 5):
    numbers.append(value)
print(numbers)

# 4.3.2 使⽤ range() 创建数值列表
# 使用list()直接转换为列表,类似于下方程序段
# for value in range(1, 5):
#     numbers.append(value)
# print(numbers)
numbers = list(range(1,6))
print(numbers)