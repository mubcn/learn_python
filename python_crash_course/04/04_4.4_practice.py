# 练习 4.10：切⽚ 选择你在本章编写的⼀个程序，在末尾添加⼏⾏代码，以完成如下任务。
# 打印消息“清单中的前三项内容如下:”，再使⽤切⽚来打印列表的前三个元素。
# 打印消息“列表中间位置的 3 项内容如下:”，再使⽤切⽚来打印列表中间的三个元素。
# 打印消息“清单中最后三项内容如下:”，再使⽤切⽚来打印列表末尾的三个元素。
print("4.10 切片")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("清单中的前三项内容如下")
for player in players[:3]:
    print(player.title())
print("列表中间位置的3项内容如下:")
for player in  players[1:4]:
    print(player.title())
print("清单中最后三项内容如下")
for player in players[-3:]:
    print(player.title())

# 练习 4.11：你的⽐萨，我的⽐萨 在你为练习 4.1 编写的程序中，创建⽐萨列表的副本，并将其赋给变量 friend_pizzas，再完成如下任务。
# 在原来的⽐萨列表中添加⼀种⽐萨。
# 在列表 friend_pizzas 中添加另⼀种⽐萨。
# 核实有两个不同的列表。为此，打印消息“我最喜欢的披萨是:”，再使⽤⼀个 for 循环来打印第⼀个列表；
# 打印消息“我朋友最喜爱的披萨是:”，再使⽤⼀个 for 循环来打印第⼆个列表。核实新增的⽐萨被添加到了正确的列表中。
print("4.11 你的披萨,我的披萨")
pizzas = ['榴莲披萨', '烤肉披萨', '烤鸭披萨', '腊肠披萨']
friend_pizzas = pizzas[:]
pizzas.append("肘子披萨")
friend_pizzas.append("麻酱披萨")
print("我最喜欢的披萨是:")
for pizza in pizzas:
    print(pizza)
print("\n我朋友最喜欢的披萨是:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

# 练习 4.12：使⽤多个循环 在本节中，为节省篇幅，程序 foods.py 的每个版本都没有使⽤ for 循环来打印列表。
# 请选择⼀个版本的foods.py，在其中编写两个 for 循环，将各个⾷品列表都打印出来。
print("4.12 使⽤多个循环")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)
print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)