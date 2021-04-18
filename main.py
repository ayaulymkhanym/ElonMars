#Hello world
# print("Hello world")
# """print ("I am learning python with Elon Mars team")"""
# print("Hi")


# DATA TYPE
# string
# "asd"

# # int
# a = 1123

# # float
# a = 23.123

# data types

# string
# a = 'asdasd'
# b = "asdasdasd"
# c = '''asdasdasd'''

# # int
# a = 1123

# # # float
# # a = 23.123

# # a1 = [1,2,3, '223']

# d = {
#    'asd': 123,
#   '23': 233
# }

# # boolean
# a = True
# a = False

# print(type(123))
# print(type(d))
# Преобразования из одного data type
# a = '123'
# a = str(a)
# print(a)
# print(type(a))
# x = range(5, 6)
# print(x)
# a = 757+2*2/2
# print(a)
# a = 1
# a = float(a)
# b = 1
# b = float(b)
# c = 1.14
# c = float(c)
# print(type(a))
# d = a+b+c
# print(d)
# print(round(d, 2))
# print(c)
# a = input("Введи первое число\n")
# b = input("Введи второе число\n")
# a = int(a)
# b = int(b)
# c = input("Введи третье число\n")
# c = int(c)
# d = a * b * c
# print(d)
# a = input("Введи первое число\n")
# b = input("Введи второе число\n")
# a = int(a)
# b = int(b)
# c = input("Введи третье число\n")
# c = int(c)
# d = a * b * c
# print(d)
# a = input("Радиус\n")
# S = float(a)**2 * 3.14
# print(float(S))
# name = input("Введи имя")
# a = f"Привет{name}"
# print(a)

# a = '''Входные данные текст
# банан заменить на большие буквы 
# Example: ПРивет банан Банан яблоко груши банАн БАНАН'''

# b = a.upper()

# # print(b) 

# c = b.replace('БАНАН', "Яблоко")
# print(c)

# password1 = '2222'#Jack
# password2 = '3333'#Nick

# user_input = input("Введи пароль")

# if user_input == password1:
#   print('Hello Jack')
# elif user_input == password2:
#   print('hello Nick')
# else:
#   print('wrong password!')

# a = input("Введите первое число\n")

# b = input("Введите второе число\n")

# action = input("Введите действие + , - , *, /")

# if action == "+":
# 	print(int(a)+int(b))
# elif action == "-":
# 	print(int(a)-int(b))
# elif action == "*":
# 	print(int(a)*int(b))
# elif action == "/":
# 	print(int(a)/int(b))	

# Sex = input("Input your sex (female, male):")
# Age = input("Input your age:\n")
# Age = int(Age)
# if Sex == "female" and Age >= 18:
# 	print("Come in")
# elif Sex == "male" and Age >= 21:
# 	print("Come in")
# elif (Sex == "male" and Age <0) or (Sex == "female" and Age<0):
# 	print ("Error")
# else:
# # 	print("Go home!")
# d = {
#   'name' : 'Egor',
#   'surname': 'EgorUlyKotiBar',
#   'pas': 123123,
#   'WW': True,
#   'array': [12,2,3,24,3],
#   'dd': {
#     '2level': 'Egor2',
#     '2pas': 21312
#   }
# }

# a = input("vvedite a")
# b = input("vvedite b")


# a = int(a)+int(b)
# b = int(a) - int(b)
# a = int(a) - int(b)

# print(a)
# print(b)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])
# # ['apple', 'banana', 'cherry', 'orange']

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[4:])
# # ["kiwi", "melon", "mango"]

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[2] = 'KKKKK'
# fruit = thislist[3]
# print(thislist)
# print(fruit)
# gen = input("Choose your gender\n")
# age = input("What is your age\n")
# if int(age) <= 0:
#   print("Write the correct age")
#   age = input("What is your age\n")

# gen = str(gen).upper()
# if (gen == "W" and int(age) >= 18) or (gen == "M" and int(age) >= 21):
#   print("Ote ber")
# else:
#   print("Kait uine")
# a = [5,4,3,2,8,6,7]
# a.sort()
# print(a)

# b = ['c','b','y','d']
# b.sort()
# print(b)

# c = ["gy", "yud", "abc", "rys"]
# c.sort()
# print(c)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# i = 0
# while i < len(thislist):
#   # print(thislist[i])

#   if thislist[i] == 'cherry':
#     print(thislist[i])
#   else:
#     print('other fruit')
#   i += 1#i = i + 1

#   i = 0
# while i < 2:
#   j = 0
#   while j < 2:
#     print('this is I', i)
#     print('this is J', j)
#     j += 1
#   i += 1
# print(j)

# thislist = ["apple", "banana", "cherry", mango"]

# fruits = ["apple", "banana", "cherry", "apple", "banana", "cherry", "mango"]
# for fruit in fruits:
	# print(fruit)

# mylist = '''asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA'''
# mylist2 = mylist
# mylist2 = mylist2.upper()
# mylist = mylist.split(' ')
# mylist2 = mylist2.split(' ')

# for i in range(0,len(mylist)):
# 	if mylist2[i] == "BANANA":
# 		mylist[i]="BANANA"
# mylist = " ".join(mylist)
# print(mylist)

# i = 0
# a = a.split()
# while i < len(a):
#   if a[i].lower() == 'banana':
#     a[i] = 'BANANA'
#   i += 1
# a = ' '.join(a)
# print(a)


# for i in range (0,11):
# # 	if i/3 != 3  and i >0:
# # 		print (i)

# a = [1,2,3,4,5]
# b = [1,2,10]
# for i in range (0, len(a)):
# 	for x in range (0, len(b)):
# 		if a[i] == b[x]:
# 			y = b[x]
			# print(y)= 1 
# a  = input("Write number") 
# try: 
# 	a = int(a)
# 	print(a*10)
# except Exception as e:
# 	print(e, "Please write number")