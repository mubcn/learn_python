name = "ada lovelace"
print(name.title())
"""
title 方法是Python可对数据执行的操作,title()函数不需要额外的信息,因此它后面的括号是空的.
title()方法以首字母大写的方式显示每个单词,即将每个单词的首字母都改为大写
Ada Lovelace

"""
name = name.title()  # 将name转换为首字母大写后保存到他自己内
print(name)  # 打印新的name数据
print(name.upper())  # 全部大写
print(name.lower())  # 全部小写
