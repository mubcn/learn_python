separate = "****************\n"
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# 要在字符串中插入变量的值,可先在左引号前加上字母f,再将要产褥的变量放在花括号内.这样,Python在显示字符串时,将把每个变量投替换为其值.
# 这种字符串成为 f 字符串. f是format(设置格式)的简写
print(f"{separate}hello\n\t{full_name.title()}!\n\t这是使用print打印的")
# 显示为 hello,Ada Lovelace!
# 相同的,可以使用变量存储
message = f"{separate}hello,\n\t{full_name.title()}!!!\n这是使用变量存储的"
print(message)

# 2.3.4 删除空白
print(separate,f"2.3.4 删除空白")
favorite_language = "Python "
print(f"原始数据为:{favorite_language},\n使用\"rstrip\"的方法后为:{favorite_language.rstrip()}.")
print(f"或者将{favorite_language}数据使用该方法重新关联使用favorite_language = favorite_language.rstrip()")
favorite_language = favorite_language.rstrip()
print(f"重新打印结果为{favorite_language}.")
print("删除右侧空格")
