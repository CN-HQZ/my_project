# age={"zhangsan":18, "lisi":20}
# print(age["lisi"])
# age["wangwu"]=17
# print(age)
# age["wangwu"]=19
# print(age)
# del age["wangwu"]
# print(age)


# people={"first_name":"hou", "last_name":"zhao", "age":22, "city":"heilong" }
# print(people["first_name"])
# print(people["last_name"])
# print(people["age"])
# print(people["city"])


# people={"first_name":"hou", "last_name":"zhao", "age":22, "city":"heilong",  "zs":1, "lisi":2}
# print(f"'first_name':\n{people['first_name']}")
# for key, value in people.items():
#     print(f"\nkey:{key}")
#     print(f"value:{value}")
# for key in people:
#     print(key)


# favo_langu={"zs":1, "lisi":2}
# firend=["zs", "lisi"]
# for i in firend:
#     print("hi"+i)
#     if i in favo_langu:
#         print(f"{i}like{favo_langu[i]}")


# rivers={"nile":"egypt", "songhuajiang":"china", "blackriver":"china"}
# for key, values in rivers.items():
#     print(f"The {key.title()} runs through {values.title()}")

# for key in rivers:
#     print(key)

# for values in rivers.values():
#     print(values)


# current_users=["Zs", "lisi", "ww", "zl", "sq"]
# current_users_lower=[ i.lower() for i in current_users]
# finishusers={"zs":"ok", "Lisi":"ok"}
# finishusers_lower=[i.lower() for i in finishusers.keys()]

# for i in current_users_lower:
#     if i in finishusers:
#         print(f"thanks{i}")
#     else:
#         print(f"come{i}")


# people1={"first_name":"xiao", "last_name":"hu", "age":26, "city":"heilong" }
# people2={"first_name":"lao", "last_name":"mo", "age":40, "city":"heilong" }
# people3={"first_name":"xiao", "last_name":"long", "age":32, "city":"heilong" }
# peoples=[people1, people2, people3]
# for i in peoples:
#     for key,values in i.items():
#         print(f"key:{key}\nvalues:{values}")
    
#     print("\n --------------------- \n")


# pet1={"type":"dog", "owner":"xiaoming"}
# pet2={"type":"cat", "owner":"lili"}
# pets=[pet1 , pet2]
# for i in pets:
#     for values in i.values():
#         print(values)


