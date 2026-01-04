# 练习 4.3：数到 20 使⽤⼀个 for 循环打印数 1〜20（含）。

print("4.3数20")
numbers = list(range(1, 21))  # 创建一个1-20的数组
for number in numbers:  # 循环打印数字
    print(number)

# 练习 4.4：100 万 创建⼀个包含数 1〜1 000 000 的列表，再使⽤⼀个 for 循环将这些数打印出来。
# （如果输出的时间太⻓，按 Ctrl + C 停⽌输出，或关闭输出窗⼝。）
print("4.4 一百万")
numbers = list(range(1, 1_000_001))
for number in numbers:
    print(number)

# 练习 4.5：100 万求和 创建⼀个包含数 1〜1 000 000 的列表，再使⽤min() 和 max() 核实该列表确实是从 1 开始、到 1 000 000 结束的。
# 另外，对这个列表调⽤函数 sum()，看看 Python 将 100 万个数相加需要多⻓时间。
print("4.5 100万求和")
numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 练习 4.6：奇数 通过给 range() 函数指定第三个参数来创建⼀个列表，其中包含 1〜20 的奇数；
# 再使⽤⼀个 for 循环将这些数打印出来。
print("4.6 奇数")
numbers = list(range(1, 21, 2))
for number in numbers:
    print(number)

# 练习 4.7：3 的倍数 创建⼀个列表，其中包含 3〜30 内能被 3 整除的数，再使⽤⼀个 for 循环将这个列表中的数打印出来。

print("4.7 3的倍数")
numbers = list(range(3,31,3))
for number in numbers:
    print(number)

# 练习 4.8：⽴⽅ 将同⼀个数乘三次称为⽴⽅。例如，在 Python 中，2的⽴⽅⽤ 2**3 表⽰。
# 创建⼀个列表，其中包含前 10 个整数（1〜10）的⽴⽅，再使⽤⼀个 for 循环将这些⽴⽅数打印出来。
numbers = []
print("4.8 立方")
for number in range(1,11):
    numbers.append(number ** 3)
# 可简化为 列表推导式直接创建立方数列表，替代第一个for循环
# numbers = [number ** 3 for number in range(1, 11)]

for number in numbers:
    print(number)

# 练习 4.9：⽴⽅推导式 使⽤列表推导式⽣成⼀个列表，其中包含前 10个整数的⽴⽅。
print("4.9 立方推导式")
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)