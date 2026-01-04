"""
4.1 历遍整个列表
26-01-02
循环
"""

# 4.1.1 认识循环
magicians = ['alice', 'david', 'carolina']  # 创建一个列表
for magician in magicians:  # for循环条件,不要忘记":"
    print(magician)  # 循环的语句,这里是将列表中每个元素分别关联到magician变量中,然后执行本行打印

# 不要使用魔术变量名称,应该使用有意义的名称,可帮我我判断代码段处理的是什么.

# 4.1.2 在for循环中执行更多的操作
magicians = ['alice', 'david', 'carolina']  # 创建一个列表
for magician in magicians:
    print(f"{magician.title()}那真是个绝妙的把戏！")
    print(f"我迫不及待想看看{magician.title()}接下来要表演的绝技.")  # 所有循环内的内容都需要缩进,Python使用缩进确定代码段

# 4.1.3 在for循环结束后执行一些操作

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}那真是一个绝妙的把戏!")
    print(f"我迫不及待想看看{magician.title()}接下来要表演的绝技.")
print("谢谢大家。这是一场非常精彩的魔术表演！")  # 这行代码不是循环的程序段了,因为没有使用相同的缩进.

# 练习 4.1：⽐萨 想出⾄少三种你喜欢的⽐萨，将其名称存储在⼀个列表中，
# 再使⽤ for 循环将每种⽐萨的名称打印出来。

pizzas = ['榴莲披萨', '烤肉披萨', '烤鸭披萨', '腊肠披萨']
for pizza in pizzas:
    print(pizza)
# 修改这个 for 循环，使其打印包含⽐萨名称的句⼦，⽽不仅仅是⽐萨的名称。
# 对于每种⽐萨都显⽰⼀⾏输出，如下所⽰。
for pizza in pizzas:
    print(f"我喜欢的披萨有:{pizza}.")
# 在程序末尾添加⼀⾏代码（不包含在 for 循环中），指出你有多喜欢⽐萨。
# 输出应包含针对每种⽐萨的消息，还有⼀个总结性的句⼦
print("我非常喜欢披萨.")

#练习 4.2：动物 想出⾄少三种有共同特征的动物，将其名称存储在⼀个列表中，
# 再使⽤ for 循环将每种动物的名称打印出来

small_animals = ['小猫', '小狗', '小兔子']
for small_animal in small_animals:
    print(f"一只{small_animal}会是个很棒的宠物")
print("这些动物中的任何一只都将成为绝佳的宠物！")