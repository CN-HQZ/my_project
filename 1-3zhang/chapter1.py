message = "hello word"
message1 = " python "
nostarch_url = 'https://nostarch.com'
filename='python_notes.txt'
print(message.title()) #首字母大写
print(message.upper()) #全大写
print(message.lower()) #全小写
print(message1.rstrip()) #删除右侧空白
print(message1.lstrip()) #删除左侧空白
print(message1.strip())  #删除空白
print(nostarch_url.removeprefix('https://')) #删除前缀
print(filename.removesuffix(".txt")) #删除后缀