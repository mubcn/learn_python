"""
3.2 修改/添加和删除元素
会用到几个方法或函数?
添加/删除/弹出
25-12-31
"""

# 3.2.1 修改列表元素
# 使用索引可以直接修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']  # 创建一个列表
print(motorcycles)  # 打印列表

motorcycles[0] = 'ducati'  # 修改索引0的元素
print(motorcycles)  # 打印列表

# 3.2.2 在列表添加元素

# 在列表末尾添加元素 使用append('元素')
motorcycles = ['honda', 'yamaha', 'suzuki']  # 重新初始化列表
motorcycles.append('ducati')  # 使用append 在列表尾部添加 ducati
print(motorcycles)  # 打印列表

motorcycles = []  # 再次初始化  # 重新初始化列表
motorcycles.append('honda')  # 使用 append 添加元素
motorcycles.append('yamaha')  # 使用 append 添加元素
motorcycles.append('suzuki')  # 使用 append 添加元素
print(motorcycles)  # 打印列表

# 在列表插入元素,使用insert(索引,'元素')
motorcycles = ['honda', 'yamaha', 'suzuki']  # 重新初始化列表
motorcycles.insert(0, 'ducati')  # 在索引0 插入元素,现有元素向右移动一位
print(motorcycles)  # 打印元素

# 3.2.3 从列表删除元素
# 1. 从列表中删除元素 del 列表[索引]
motorcycles = ['honda', 'yamaha', 'suzuki']  # 重新初始化列表
print(motorcycles)  # 打印元素
del motorcycles[0]  # 删除索引0的元素
print(motorcycles)  # 打印元素

motorcycles = ['honda', 'yamaha', 'suzuki']  # 重新初始化列表
print(motorcycles)  # 打印元素
del motorcycles[2]  # 删除索引2的元素
print(motorcycles)

# 2. 从列表删除元素 列表.pop(索引) 没有索引删除最后一个
motorcycles = ['honda', 'yamaha', 'suzuki']  # 重新初始化列表
popped_motorcycle = motorcycles.pop()  # 索引默认值是-1
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']  # 重新初始化列表
last_owned = motorcycles.pop()
print(f"我拥有的最后一辆摩托车是{last_owned}.")

# 也可以移除任意索引位置的元素
motorcycles = ['honda', 'yamaha', 'suzuki']  # 重新初始化列表
first_owned = motorcycles.pop(1)  # 移除第二个元素
print(f"我最喜欢的摩托车是{first_owned.title()}.")

# 如果要从列表中删除⼀个元素，且不再以任何⽅式使⽤它，就使⽤ del 语句；
# 如果要在删除元素后继续使⽤它，就使⽤ pop() ⽅法。

# 根据值删除元素,使用remove('元素')方法
motorcycles = ['honda', 'yamaha', 'suzuki']  # 重新初始化列表
print(motorcycles)
motorcycles.remove('yamaha')  # 如果元素不存在会报错.
print(motorcycles)

# 使用变量导入,用于提示删除的值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']  # 重新初始化列表
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"删除{too_expensive}成功.")
print(f"当前还存在{motorcycles}")

# 练习 3.4：嘉宾名单
# 如果你可以邀请任何⼈⼀起共进晚餐（⽆论是在世的还是故去的），你会邀请哪些⼈？
# 请创建⼀个列表，其中包含⾄少三个你想邀请的⼈，然后使⽤这个列表打印消息，邀请这些⼈都来与你共进晚餐。

inviters = ['小艾', '小王', '小李']
print(f"我需要邀请{inviters[0]}/{inviters[1]}和{inviters[2]}来一起吃饭.")

# 练习 3.5：修改嘉宾名单
# 你刚得知有位嘉宾⽆法赴约，因此需要另外邀请⼀位嘉宾。
# 以完成练习 3.4 时编写的程序为基础，在程序末尾添加函数调⽤print()，指出哪位嘉宾⽆法赴约。
# 修改嘉宾名单，将⽆法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印⼀系列消息，向名单中的每位嘉宾发出邀请。

unattended_personnel = '小艾'
new = '小赵'
inviters.remove(unattended_personnel)
inviters.append(new)
print(f"因为{unattended_personnel}不能到来,我将在邀请{new}.")
print(f"现在我邀请的有{inviters[0]}/{inviters[1]}和{inviters[2]}")

# 练习 3.6：添加嘉宾 你刚找到了⼀张更⼤的餐桌，可容纳更多的嘉宾就座。请想想你还想邀请哪三位嘉宾。
# 以完成练习 3.4 或练习 3.5 时编写的程序为基础，在程序末尾添加函数
# 调⽤ print()，指出你找到了⼀张更⼤的餐桌。
# 使⽤ insert() 将⼀位新嘉宾添加到名单开头。
# 使⽤ insert() 将另⼀位新嘉宾添加到名单中间。
# 使⽤ append() 将最后⼀位新嘉宾添加到名单末尾。
# 打印⼀系列消息，向名单中的每位嘉宾发出邀请。

print("我找到了一个更大的桌子")  # 提示信息
print(f"我将继续邀请小宋/小周和小天的到来")  # 提示新人
inviters.insert(0, '小宋')  # 头部添加小宋
inviters.insert(2, '小周')  # 中间添加小周
inviters.append('小天')  # 尾部添加小天
print(f"我本次一共邀请了,{inviters[0]}/{inviters[1]}/{inviters[2]}/{inviters[3]}/{inviters[4]}和{inviters[5]}")  # 打印所有数据

# 练习 3.7：缩短名单 你刚得知新购买的餐桌⽆法及时送达，因此只能邀请两位嘉宾。
# 以完成练习 3.6 时编写的程序为基础，在程序末尾添加⼀⾏代码，打印⼀条你只能邀请两位嘉宾共进晚餐的消息。
# 使⽤ pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为⽌。
# 每次从名单中弹出⼀位嘉宾时，都打印⼀条消息，让该嘉宾知道你很抱歉，⽆法邀请他来共进晚餐。
# 对于余下两位嘉宾中的每⼀位，都打印⼀条消息，指出他依然在受邀之列。
# 使⽤ del 将最后两位嘉宾从名单中删除，让名单变成空的。打印
# 该名单，核实名单在程序结束时确实是空的。

print("我的天,桌子到不了了,我只能邀请两个人了")
pop_up = inviters.pop()
print(f"非常不好意思{pop_up},只能下次邀请你了")
pop_up = inviters.pop()
print(f"非常不好意思{pop_up},只能下次邀请你了")
pop_up = inviters.pop()
print(f"非常不好意思{pop_up},只能下次邀请你了")
pop_up = inviters.pop()
print(f"非常不好意思{pop_up},只能下次邀请你了")
print(f"{inviters[0]}记得我们的宴会,我等你")
print(f"{inviters[1]}记得我们的宴会,我等你")
del inviters[0]
del inviters[0]
print(inviters)