"""
关于range的用法
"""

"""练习4-4：一百万
创建一个包含数1~1000000的列表，再使用一个for循环将这些数打印出来。
(如果输出的时间太长，按CtrL+C停止输出或关闭输出窗口。)"""

s = 0
number_list = []
for i in range(1, 1_000_001):
    number_list.append(i)
    # print(i)
"""练习4-5：一百万求和
创建一个包含数1~1000000的列表，再使用min()和max()
核实该列表确实是从1开始、到1000000结束的。
另外，对这个列表调用函数sUm(),看看Python将一百万个数相加需要多长时间。"""

print(min(number_list))
print(max(number_list))
print(sum(number_list))