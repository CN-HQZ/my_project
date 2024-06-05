from pathlib import Path
import json

# path = Path('chapter10\\pi_digits.txt')
# contents = path.read_text().rstrip()

# lines = contents.splitlines()
# pistring = ''
# for line in lines:
#     pistring += line.lstrip()
# print(pistring)
# print(len(pistring))
# print(contents)


# path = Path('chapter10\\zongjie.txt')
# readtxt = path.read_text()
# print(readtxt)

# for i in readtxt.splitlines():
#     i = i.replace("Python", "C")
#     print(i)


# contents = "I love programming.\n"
# contents += "I love creating new games.\n"
# contents += "I also love working with data.\n"

# path = Path('chapter10\\programming.txt')
# path.write_text(contents)


# name=input("Please input your name")

# path = Path('chapter10\\guest.txt')
# path.write_text(name)


# path=Path('chapter10\\guest_book.txt')
# names = ""

# while True:
#     name = input("Please input your name or input quit to quit")
#     if name.lower() == "quit":
#         break
#     else:
#         names += name+"\n"


# path.write_text(names)


# while True:
#     print("Give me two numbers, and I'll divide them.")
#     print("Enter 'q' to quit.")
#     first_number = input("\nFirst number: ")
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)


#10.7
# while True:
#     num1 = input("input a num1")
#     num2 = input("input a num2")
#     if num2 == "q":
#         break
#     try:
#         num = int(num1) +int(num2)
#         print(num)
#     except:
#         print("you must input a int num")
        

# try:
#     path = Path('chapter10\\cats.txt')
#     result = path.read_text()
#     print(result)
# except:
#     pass




# numbers = [2, 3, 5, 7, 11, 13]

# path = Path("chapter10\\numbers.json")
# contents = path.read_text()
# numbers = json.loads(contents)

# print(numbers )


