# 练习 2.3：个性化消息 ⽤变量表⽰⼀个⼈的名字，并向其显⽰⼀条消息。显⽰的消息应⾮常简单，如下所⽰。
# Hello Eric, would you like to learn some Python today?
name = "Eric"
print(f"Hello {name},would you like to learn some some Python today?")

# 练习 2.4：调整名字的⼤⼩写 ⽤变量表⽰⼀个⼈的名字，再分别以全⼩写、全⼤写和⾸字⺟⼤写的⽅式显⽰这个⼈名。
print(name.lower())  # 全部小写
print(name.upper())  # 全部大写
print(name.title())  # 首字母大写

# 练习 2.5：名⾔ 1 找到你钦佩的名⼈说的⼀句名⾔，将这个名⼈的姓名和名⾔打印出来。输出应类似于下⾯这样（包括引号）。
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
print("Albert Einstein once said,\"A person who never made a mistake never tried anything new.\"")

# 练习 2.6：名⾔ 2 重复练习 2.5，但⽤变量 famous_person 表⽰名⼈的姓名，再创建要显⽰的消息并将其赋给变量 message，然后打印这条消息。
famous_person = "albert"
message = f"{famous_person.title()} Einstein once said,\"A person who never made a mistake never tried anything new.\""
print(message)

# 练习 2.7：删除⼈名中的空⽩ ⽤变量表⽰⼀个⼈的名字，并在其开头和末尾都包含⼀些空⽩字符。务必⾄少使⽤字符组合 "\t" 和 "\n" 各⼀次。
famous_person = "  albert  "
print(famous_person)
print(f"\t{famous_person.lstrip()}\n\t{famous_person.rstrip()}\n\t{famous_person.strip()}")

# 练习 2.8：⽂件扩展名 Python 提供了 removesuffix() ⽅法，其⼯作原理与 removeprefix() 很像。
# 请将值 'python_notes.txt'给变量 filename，再使⽤ removesuffix() ⽅法来显⽰不包含扩展名的⽂件名，就像⽂件浏览器所做的那样。
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
