import json
from pathlib import Path


# path = Path('chapter10\\numbers.json')
# if path.exists():
#     jsonread = path.read_text()
#     jsonout = json.loads(jsonread)
#     print(f"I know your favorite number is {jsonout}")
# else:
#     num = input("show me your favorite num")
#     jsontext = json.dumps(num)
#     path.write_text(jsontext) 


def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
    
def get_new_username(path=Path('chapter10\\username.json')):
    """提示用户输入用户名"""
    user = {}
    username = input("What is your name? ")
    user["username"] = username
    age = input("What is your age? ")
    user["age"] = age
    contents = json.dumps(user)
    path.write_text(contents)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    path = Path('chapter10\\username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
#get_new_username()

