# def dispaly_message():
#     print("this chapter can teach us how to use def")

# dispaly_message()

# def favorite_book(title):
#     print(f"One of my book is {title}")

# favorite_book(1)    

# def descript_pet(pet_name, animal_type="dog"):
#     print(f"I have a {animal_type}")
#     print(f"It's named {pet_name}")

# descript_pet("willie")
# descript_pet(pet_name='harry', animal_type='hamster')


# def make_tshirt(size, logo="I love python"):
#     print(f"{size},{logo}")

# make_tshirt(42)
# make_tshirt(43, "yes")


# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)


# def city_country(city, country):
#     print(f"{city},{country}")

# city_country("taiwan", "zhongguo")
# city_country("niuyue", "meiguo")
# city_country("henei", "yuenan")


# the_album={}
# def make_album(singer,album,num=None):
#     the_album[singer]=album
#     if num:
#         the_album["num"]=num
#     print(the_album)

# make_album("lala","baima",3)


# the_album={}
# def make_album(singer,album):
#     the_album[singer]=album
#     return the_album

# while True :
#     print("input q to quit")
#     singer = input("singer").strip()
#     if singer == "q":
#         break
#     print("input q to quit")
#     album = input("album").strip()
#     if album == "q":
#         break
#     make_album(singer, album)
#     print(the_album)

# mylist = ["1", "2", "3", "4", "5"]
# mylist1 = mylist[:]
# sent_messages = []
# def show_messsages(mylist):
#     for i in mylist:
#         print(i)

# def send_messages(sendlsit,sentlist):
#     while sendlsit:
#         sent=sendlsit.pop()
#         print(sent)
#         sentlist.append(sent)
#     print(sendlsit)
#     print(sentlist)

# show_messsages(mylist)
# send_messages(mylist1,sent_messages)


# def show_sanwith(*toppings):
#     for topping in toppings:
#         print(topping)

# show_sanwith("1", "2", "3", "4")


# def send_car(car_subaru, car_outback, **cars):
#     cars["car_subaru"]=car_subaru
#     cars["car_outback"]=car_outback
#     return cars

# car = send_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)


