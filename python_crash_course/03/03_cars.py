"""
3.3 管理列表
25-12-31
排序列表元素
"""

# 3.3.1 使用使⽤ sort() ⽅法对列表进⾏永久排序 reverse=True 逆序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # 永久排序
print(cars)
cars.sort(reverse=True)
print(cars)

# 3.3.2使⽤ sorted() 函数对列表进⾏临时排序 reverse=True 逆序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"原始值为{cars}")
print(f"临时排序后为{sorted(cars)}")
print(f"临时排序后为{sorted(cars, reverse=True)}")
print(f"再次观察现有列表{cars}")

# 3.3.3 反向打印列表 reverse() 方法
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()  # 反方向排序,并不会按顺序排列，只是交换方向
print(cars)
cars.reverse()  # 反方向排序,可以再次使用该方法,恢复方向
print(cars)  # 继续打印

# 3.3.4 确定列表长度 len() 函数
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"cars列表元素为{cars},共{len(cars)}个.")

# 练习 3.8：放眼世界 想出⾄少 5 个你想去旅游的地⽅。
# 将这些地⽅存储在⼀个列表中，并确保其中的元素不是按字⺟顺序排列的。
# 按原始排列顺序打印该列表。不要考虑输出是否整洁，只管打印原始 Python 列表就好。
# 使⽤ sorted() 按字⺟顺序打印这个列表，不要修改它。再次打印该列表，核实排列顺序未变。
# 使⽤ sorted() 按与字⺟顺序相反的顺序打印这个列表，不要修改它。
# 再次打印该列表，核实排列顺序未变。
# 使⽤ reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
# 使⽤ reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
# 使⽤ sort() 修改该列表，使其元素按字⺟顺序排列。打印该列表，核实排列顺序确实变了。
# 使⽤ sort() 修改该列表，使其元素按与字⺟顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。

tourist_city =['shanghai', 'chongqing', 'qingdao', 'dalian', 'beijing']
print(f"原始列表为{tourist_city}")
print(f"临时按字母从小到大排序输出{sorted(tourist_city)}")
print(f"临时按字母从大到小排序输出{sorted(tourist_city, reverse=True)}")
print(f"确认排序没有改变,{tourist_city}")
tourist_city.reverse()
print(f"反方向输出列表{tourist_city}")
tourist_city.reverse()
print(f"再次反方向列表还原列表,{tourist_city}")
tourist_city.sort()
print(f"按照字母从小到大排序{tourist_city}")
tourist_city.sort(reverse=True)
print(f"按照字母从大到小排序{tourist_city}")

# 练习 3.9：晚餐嘉宾 选择你为完成练习 3.4〜练习 3.7 ⽽编写的⼀个程序，
# 在其中使⽤ len() 打印⼀条消息，指出你邀请了多少位嘉宾来共进晚餐。

# 练习 3.4：嘉宾名单
inviters = ['小艾', '小王', '小李']
print(f"我需要邀请{inviters[0]}/{inviters[1]}和{inviters[2]}来一起吃饭.")
print(f"我当前邀请了{len(inviters)}人")
# 练习 3.5：修改嘉宾名单
unattended_personnel = '小艾'
new = '小赵'
inviters.remove(unattended_personnel)
inviters.append(new)
print(f"因为{unattended_personnel}不能到来,我将在邀请{new}.")
print(f"现在我邀请的有{inviters[0]}/{inviters[1]}和{inviters[2]}")
print(f"我当前邀请了{len(inviters)}人")
# 练习 3.6：添加嘉宾 你刚找到了⼀张更⼤的餐桌，可容纳更多的嘉宾就座。请想想你还想邀请哪三位嘉宾。
print("我找到了一个更大的桌子")  # 提示信息
print("我将继续邀请小宋/小周和小天的到来")  # 提示新人
inviters.insert(0, '小宋')  # 头部添加小宋
inviters.insert(2, '小周')  # 中间添加小周
inviters.append('小天')  # 尾部添加小天
print(f"我本次一共邀请了,{inviters[0]}/{inviters[1]}/{inviters[2]}/{inviters[3]}/{inviters[4]}和{inviters[5]}")  # 打印所有数据
print(f"我当前邀请了{len(inviters)}人")
# 练习 3.7：缩短名单 你刚得知新购买的餐桌⽆法及时送达，因此只能邀请两位嘉宾。
print("我的天,桌子到不了了,我只能邀请两个人了")
pop_up = inviters.pop()
print(f"非常不好意思{pop_up},只能下次邀请你了")
print(f"我当前邀请还有{len(inviters)}人")
pop_up = inviters.pop()
print(f"非常不好意思{pop_up},只能下次邀请你了")
print(f"我当前邀请还有{len(inviters)}人")
pop_up = inviters.pop()
print(f"非常不好意思{pop_up},只能下次邀请你了")
print(f"我当前邀请还有{len(inviters)}人")
pop_up = inviters.pop()
print(f"非常不好意思{pop_up},只能下次邀请你了")
print(f"我当前邀请还有{len(inviters)}人")
print(f"{inviters[0]}记得我们的宴会,我等你")
print(f"{inviters[1]}记得我们的宴会,我等你")
del inviters[0]
del inviters[0]
print(inviters)
print(f"列表中还有{len(inviters)}人")