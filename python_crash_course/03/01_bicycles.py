"""
这是第三章列表的代码
25-12-31
创建列表/输出列表/
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 3.1.1 访问列表元素
# 提取一个元素
# 提取第一款自行车

print(bicycles[0])  # 列表是从0 开始的,输出结果应该是trek
print(bicycles[0].title())  # 可以使用字符串方法,如title使首字母大写

# 3.1.2 索引从0而不是1开始
# 初始索引为0,所以提取第二个和第四个数据,应该一个是1,一个是3
print(bicycles[1])
print(bicycles[3])
# Python还有一种语法,比如提取最后一个和倒数第二个,可以使用-1和-2
print(bicycles[-1])
print(bicycles[-2])

# 3.1.3 使用列表中的各个值
message = f"我的第一辆自行车是{bicycles[0].title()}."
print(message)

# 练习3.1:姓名
# 将⼀些朋友的姓名存储在⼀个列表中，并将其命名为names。
# 依次访问该列表的每个元素，从⽽将每个朋友的姓名都打印出来。

names = ['磊哥', '建哥', '浩仔']

print(f'我的朋友有{names[0]}/{names[1]}/{names[2]}')

# 练习3.2:问候语
# 继续使⽤练习 3.1 中的列表，但不打印每个朋友的姓名，⽽是为每⼈打印⼀条消息。
# 每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
message = "早上好呀"
print(names[0] + message)
print(names[1] + message)
print(names[2] + message)

# 练习 3.3：⾃⼰的列表 想想你喜欢的通勤⽅式，如骑摩托⻋或开汽⻋，并创建⼀个包含多种通勤⽅式的列表。
# 根据该列表打印⼀系列有关这些通勤⽅式的陈述，如下所⽰。
# 我想拥有一辆本田摩托车

means_of_transportation = ['电动车', '自行车', '汽车']
print("我每天都会骑着" + means_of_transportation[0] + "去送孩子上学")
print("我有时会骑着" + means_of_transportation[1] + "去散散心")
print("在休息的时候,我会开着" + means_of_transportation[2] + "带着家人去旅行")