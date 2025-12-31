"""
第三章,列表
开始时间25-12-30
"""
"""
练习3-1姓名
将一些朋友的姓名存储在一个列表中，并将其命名为names。
依次访问该列表中的每个元素，从而将每个朋友的姓名打印出来。
"""
print("**************************")
print("练习3-1")
names = ["小余", "小陈", "小曾"]
print(names[0])
print(names[1])
print(names[2])

"""
练习3-2：问候语
继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。
每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
"""
print("**************************")
print("练习3-2")
names = ["小余", "小陈", "小曾"]
print(f"holle {names[0]}, 你好呀")
print(f"holle {names[1]}, 你好呀")
print(f"holle {names[2]}, 你好呀")
"""
练习3-4：嘉宾名单
如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？
请创建一个列表，其中包含至少三个你想邀请的人，然后使用这个列表打印消息，
邀请这些人来与你共进晚餐。
"""
print("**************************")
print("练习3-4")
names = ["小余", "小陈", "小曾"]
message = "一起吃饭啊"
print(f"holle {names[0]}, {message}")
print(f"holle {names[1]}, {message}")
print(f"holle {names[2]}, {message}")

"""
练习3-5：修改嘉宾名单
你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
以完成练习3-4时编写的程序为基础，在程序末尾添加一条print语句
指出哪位嘉宾无法赴约。
修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
再次打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
print("**************************")
print("练习3-5")
names = ["小余", "小陈", "小曾"]
message = "一起吃饭啊"
print(f"holle {names[0]}, {message}")
print(f"holle {names[1]}, {message}")
print(f"holle {names[2]}, {message}")
print(f"{names[2]},来不了")
names[2] = "小王"
message = "来吃饭了"
print(f"holle {names[0]}, {message}")
print(f"holle {names[1]}, {message}")
print(f"holle {names[2]}, {message}")

"""
练习3-6：添加嘉宾
你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
-以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print语句
指出你找到了一个更大的餐桌。
使用insert()将一位新嘉宾添加到名单开头。
使用insert()将另一位新嘉宾添加到名单中间。
使用append()将最后一位新嘉宾添加到名单末尾。
打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
print("**************************")
print("练习3-6")
print("找到了更大的餐桌")
names.insert(0, "小林")
names.insert(2, "小张")
names.append("小邓")
print(f"holle {names[0]}, {message}")
print(f"holle {names[1]}, {message}")
print(f"holle {names[2]}, {message}")
print(f"holle {names[4]}, {message}")
print(f"holle {names[5]}, {message}")
print("改造为历遍")
for name in names:
    print(f"你好, {name},{message}")