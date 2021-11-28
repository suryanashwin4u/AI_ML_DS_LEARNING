# use ctrl+/ short cut key to comment out a line

# print("helloworld")
# print('helloworld')
# print('hello"my"world')
# print("hello'my'world")

# print("hello\"my\"world")
# print('hello\'my\'world')

# print('line A \n line B \n line C')
# print('line A \t line B \t line C')

# print('line A \ backslash')
# print('line A /\\/\\/\\/\\/\\ backslash')
# print('line A \ backslash\\ double \\\\')

# print('helll\bo')
# print('line A \\n line B \\n line C\\t')
# print('line A \\\' \\\" backslash')
# print('line A \\\' \\n \\t \\\" backslash')
# print(r'line A \\\' \\n \\t \\\" backslash')

# print("\U0001F602")
# print("\U0001F604")
# print("\U0001F618")

# print(2/4)  #float division
# print(2//4) #integer division
# print(5//4) #integer division

# print(2**4)
# print(2**0.5)
# print(2**4**2)

# print(round(2**0.5,2))

# print(2**3+5/2*6+(25/2+5))

# var1=23
# print(var1)

# var1="hello"
# print(var1) #this is due to dynamic programming 

# __var1="hello"
# print(__var1)

# hello_world="hw"    #this case used in python (snake case)
# print(hello_world) 

# helloWorld="hw"     #this case used in java(camel case)
# print(helloWorld)

# print("line A")
# print("line B")
# print("line A\nline B")

# fname="ashwani"
# lname="kumar"
# print(fname+" "+lname)

# fname=ashwani
# lname=kumar
# age=24
# print(fname+" "+lname+" "+str(lname) + age) #cant concatenate string with number so, convert int into string

# print(fname*5)

# myname=input("enter your name : ")
# print(myname * 5)

# myage=input("enter your age : ")
# print("my age is : " + myage)   #input function takes everything as string
# print(int(myage)+5)     #convert string to integer

# n1="52"
# n2="77"
# n3="5"
# print(float(n2)+float(n3)+float(n1))
# print(int(n2)+int(n3)+int(n1)+float(n2))

# name, age = "ashwani kumar" , 24
# print("my name is : "+" "+ name +" "+"and my age is : "+ str(age))

# x=y=z=a=b=c=1
# print(x+y+z+a+b+c)

# name,age=input("enter your name and age : ").split()
# print("my name is : " + name + " and my age is : " + age)

# name,age=input("enter your name and age : ").split(",")
# print("my name is : " + name + " and my age is : " + age)

# name,age=input("enter your name and age : ").split(",")
# print("hello my name is : {} and my age is : {}".format(name, age))
# print(f"hello my name is : {name} and my age is : {age}")
# print(f"hello my name is : {name} and my age is : {int(age)+10}")

# num1,num2,num3=input("enter 3 numbers : ").split(",")
# avg=(int(num1)+int(num2)+int(num3))/3
# print(f"average of three numbers is : {avg}")

# name="ashwani kumar"
# print(name[5]+name[7])
# print(name[5]+name[-7])
# print(name[0:10])
# print(name[:10])
# print(name[5:10])
# print(name[-5:5])
# print(name[:])
# print(name[2:])

# print("ashwani"[4:])
# print("ashwani"[0:5:2]) #step wise jump
# print("ashwani"[::2]) #step wise jump
# print("ashwani"[::-2]) #step wise jump
# print("ashwani"[::-1]) #step wise jump and reverse a string

# username=input("enter your name : ")
# print("reverse of username is : " + username[::-1])

# name="ashwani KUMAR"
# print(len(name))
# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.count("A"))

# username,character=input("enter username and a character : ").split(",")
# print(len(username))
# print(username.strip().lower().count(character))

# fname="     ashwani      "
# lname="     kumar             "
# print(fname+lname)
# print(fname.lstrip()+lname.rstrip())
# print(fname.strip()+" "+lname.strip())

# username="hello this is ashwani here and i am coding in python"
# print(username.replace(" ",""))
# print(username.replace(" ","_"))
# print(username.replace("is","was"))
# print(username.replace("is","was", 2)) #use no. to tell that only one will be replaced that comes first from left to right

# username="hello this is ashwani here and i am coding in python"
# print(username.find("this"))
# print(username.find("i", 20)) #use number to start finding from 15th position
# is_pos1=username.find("is")
# is_pos2=username.find("is", is_pos1+1)
# print("first found at : "+ str(is_pos1)+" "+" and second found at : " + str(is_pos2))

# name="ashwani"
# print(name.center(len(name)+2,"/"))

# name="ashwani"
# print(name.title())  #this will change first character of the coming string



# fname,lname=input("enter fname and lname : ").split(" ")
# fullname=fname+" "+lname
# print(fullname)
# print(fullname.center(len(fullname)+4,"%"))

# name="ashwani kumar" 
# name[2]='t' # it shows error bcz strings are immutable in nature
# newname=name.replace("ani","in") #but we can use old string to make a new string with different variable name
# print(newname)
# print(name)


# name="ashwani"
# name+=" kumar"  #noerror in this case bcz we cant change string characters but we can concatenate anything
# print(name)

# age=int(input("enter your age : "))
# age*=4
# age+=4
# age/=4
# age**=4
# age-=4
# print(age)

# age=input("enter your age :")
# if int(age)>=20:
#     print("you are 20+ ")
# else:
#     print("you are younger than 20")


# age=int(input("enter your age :"))
# if age==20:
#     pass
# else:
#     if age>20:
#         print("you are younger than 20")
#     else:
#         print("ok")

# name,age=input("enter your name and age :").split(",")
# age=int(age)
# if name=="ashwani" and age==25:
#     print("this is {} who is {} years old".format(name,age))
# else:
#     if name =="sumit" and age==20:
#         print("this is {} who is {} years old".format(name,age))
#     else:
#         print("sorry, we did not identify you")


# name,age,place=input("enter your name, age, place you live in :").split(",")
# age=int(age)
# if name=="ashwani" and age==25 and (place=="sagarpur" or place=="delhi"):
#     print("this is {} who is {} years old and you are living at {}".format(name,age,place)) 
# else:
#     if name =="sumit" and age==20 and (place=="sagarpur" or place=="delhi"):
#         print("this is {} who is {} years old and you are living at {}".format(name,age,place))
#     else:
#         print("sorry, we did not identify you")


# age=int(input("enter your age :"))
# if age==0 or age<0:
#     print("invalid input:please input age greater than 0")
# elif age>0 and age<=3:
#     print("ticket price: 0rs")
# elif age>3 and age<=10:
#     print("ticket price: 150rs")
# elif age>10 and age<=16:
#     print("ticket price: 250rs")    
# else:
#     print("ticket price: 200rs")


# age=int(input("enter your age :"))
# if age<=0:
#     print("invalid input:please input age greater than 0")
# elif 0<age<=3:
#     print("ticket price: 0rs")
# elif 3<age<=10:
#     print("ticket price: 150rs")
# elif 10<age<=16:
#     print("ticket price: 250rs")    
# else:
#     print("ticket price: 200rs")

# string=input("enter something into string : ")
# if string:
#     print(f"you have input:{string}")
# else:
#     print("you did not input anything into string")


# string,loop=input("enter something into string and loops number: ").split(",")
# loop=int(loop)
# i=0
# while 0<loop<=100:
#     i+=1
#     if string:
#         print(f"you have input:{string} and loop number is: {i}")
#         loop-=1
     
# number=input("enter your number: ")
# i=0
# sum=0
# l=len(number)-1
# while i<=l:
#     sum=sum+int(number[i])
#     i=i+1
# print("sum:" + str(sum))


# name=input("enter your name :")
# i=0
# while i<=(len(name)-1):
#     print(name.count(name[i]))
#     i+=1

# first,second=input("enter first and second number :").split(",")
# first=int(first)
# second=int(second)
# while first<=second:
#     print(f"{str(first)} * {str(second)} = {str(first*second)}")
#     first+=1
#     second+=1
#user control+c to break infinite loop

#while True:    #to run infinte loop   (T will be capital else it not works)
#while False:   (F will be capital else it not works)

# for i in range(10):
#     print("hi ashwani")
#     print(f"helloworld{i}")

# for i in range(1,11): #for i=1 to i=10
#     print("hi ashwani\n")
#     print(f"helloworld{i}")

# n=int(input("enter the number : "))
# total=0
# for i in range(1,n+1):
#     total+=i
#     print(f"sum is : {str(total)}")

# n=input("enter the number: ")
# total=0
# for i in range(0,len(n)):
#     total=total+int(n[i])
# print("total : " + str(total))

# name=input("enter the string : ")
# temp=""
# for i in range(len(name)):
#     if name[i] not in temp:
#     print(f"here is your name :{name[i]} and {str(name.count(name[i])})")
#     temp+= name[i]

# for i in range(1,11):
#     if i==5:
#         break
#     print(i)

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)


# number=int(input("guess a number between 1 and 100: "))
# winning_number=43
# guess=1
# game_over=False
# while not game_over:
#     if number==winning_number:
#         print(f"you win, and you guessed this number in {guess} times")
#         game_over=True
#     else:
#         if number<winning_number:
#             print("too low")

#         else:
#             print("too high")
    
#     guess +=1
#     number=int(input("guess again:"))

# import random
# number = int(input("Guess a number between 1 and 100:"))
# winning_number=random.randint(1,100)
# guess = 1
# game_over = False
# while not game_over:
#     if number == winning_number:
#         print(f"you win, and you guessed this number in {guess} times")
#         game_over = True
#     else:
#         if number < winning_number:
#             print("too low")

#         else:
#             print("too high")
    
#     guess += 1
#     number = int(input("guess again:"))

# num=input("enter a number : ")
# total=0
# for i in num:
#     total+= int(i)
# print(str(total))

# name=input("enter a number : ")
# for i in range(len(name)):
#     print(name[i])


# for i in "mohit":
#     print(i)

# def sum(p,q):
#     sum=p+q
#     return sum
# a,b=input("enter a and b : ").split(",")
# print(sum(a,b))

# def last_char(name):
#     return name[-1]
# print(last_char("ashwani kumar"))

# def odd_even(num):
#     if num%2==0:
#         print("even number")
#     else:
#         print("odd number")
# num=int(input("enter the number : "))
# odd_even(num)

# def odd_even(num):
#     if num%2==0:
#         return "even"
#     return "odd"
# num=int(input("enter the number :"))
# print(odd_even(num))

# def is_even(num):
#     return num%2==0
# print(is_even(10))

# def song():
#     return "helloWorld"
# print(song())

# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# bigger=greater(a,b)
# print(f"{bigger} is greater than")

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# def new_greatest(a,b,c):
#     return greater(greater(a,b), c)
# print(new_greatest(10,20,30))
# print(greatest(10,20,30))


# def is_palindrom(word):
#         return word == word[::-1]:
# print(is_palindrom("naman"))
# print(is_palindrom("horse"))

# for i in range(1,11):
#     print(i, end = " ")

# for i in range(1,11):
#     print(i, end = "\n")

# for i in range(1,11):
#     print(i, end = ",")

# def fibonacci_seq(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n==2:
#         print(a,b)
#     else:
#         print(a,b,end=" ")
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(b, end=" ")
# fibonacci_seq(10)

# def user_info(first_name,last_name,age=23):
#     print(f"{first_name}")
#     print(f"{last_name}")
#     print(f"{age}")
# user_info('harshit', 'vashista')


# def user_info(first_name,last_name,age=23):
#     print(f"{first_name}")
#     print(f"{last_name}")
#     print(f"{age}")
# user_info('harshit', 'vashista', 24)

# def user_info(first_name,last_name='unknown',age=None):
#     print(f"{first_name}")
#     print(f"{last_name}")
#     print(f"{age}")

# user_info('harshit')

#default arguments only exists in the last


# def user_info(first_name=None,last_name=None,age=None):
#     print(f"{first_name}")
#     print(f"{last_name}")
#     print(f"{age}")

# user_info()

# def func():
#     x=7 #local variable
#     print(x)

# print(x)

# x=8 #global variable
# def func():
#     x=7 #local variable
#     print(x)
# func()
# print(x)

# x=8 #global variable
# def func():
#     global x
#     print(x)
# func()
# print(x)

# numbers=[1,2,3,4]
# print(numbers)

# words=['word1','word2','word3']
# print(words)

# words=["word1","word2","word3"]
# print(words)

# mixed=[1,2,3,4,"five","six", 2.3, None]
# print(mixed)

# mixed=[1,2,3,4,"five","six", 2.3, None]
# print(mixed[2])


# mixed=[1,2,3,4,"five","six", 2.3, None]
# print(mixed[:2])

# mixed=[1,2,3,4,"five","six", 2.3, None]
# print(mixed[:-1])

# mixed=[1,2,3,4,"five","six", 2.3, None]
# # print(mixed[-1])

# mixed[1:]=['two','three','four']
# print(mixed)

# fruits=['grapes','apples']
# fruits.append('mango')
# print(fruits)


# fruits=[]
# fruits.append('mango')
# print(fruits)


# fruits2.insert(2,"grapes")
# print(fruits1+fruits2)
# # fruits1.extend(fruits2)
# fruits1.append(fruits2) 
# fruits2.pop() 
# fruits1.pop(1) 
# del fruits1[1]
# fruits1=['hello','world','sonu']

# fruits2=['abc','def','ghi']
# fruits2.remove('abc') #it removes only first occurence of a particular keyword

# fruits1=['hello','world','sonu']
# if "hello" in fruits1:
#     print("hello is present in fruits1")
# else:
#     print("not present")


# print(fruits1.count('hello'))

# fruits1.sort()
# print(fruits1)        this will sort your list elements

# print(sorted(fruits1))  this will give only output in a sorted way without changing list elements
# fruits1.clear()
# fruits_copy=fruits1.copy() 
# print(fruits_copy)

# fruits1=['hello','world','sonu','ashwani','kumar']
# fruits2=['hello','world','sonu','ashwani','kumar']
# print(fruits1==fruits2)     #values are equal
# print(fruits1 is fruits2)   #different object references

# s="string"
# t=s.title()
# print(t)
# print(s)

# fruits=['a','b','c','d','e']
# for i in fruits:
#     print(i)
# i=0
# # while i<len(fruits):
# #     print(fruits[i])
#     i+=1

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0])
# for i in matrix:
#     print(i)

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for sublist in matrix:
#     for i in sublist:
#         print(i)

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0][0])
# print(matrix[1][1])
# print(matrix[2][2])
# print(type(matrix))

# s="string"
# print(type(s))


# numbers=list(range(1,11))
# print(numbers)
# popped_item=numbers.pop()
# print(popped_item)

# numbers=list(range(20,40))
# print(numbers.index(20))

# numbers=[1,2,3,4,1,3]
# print(numbers.index(1,2,5)) #start searching from 3rd positions and stop at 4th position

# def negative_list(l):
#     negative=[]
#     for i in l:
#         negative.append(-i)
#     return negative
# numbers=[1,2,3,4,1,3]
# print(negative_list(numbers))

# def square_list(l):
#     square=[]
#     for i in l:
#         square.append(i**2)
#     return square
# numbers=list(range(1,11))
# print(square_list(numbers))

# def reverse_list(l):
#     l.reverse()
#     return l

# def reverse_list(l):
#     return l[::-1]
# numbers=[1,2,3,4]
# print(reverse_list(numbers))

# def reverse_list(l):
#     r_list=[]
#     for i in range(len(l)):
#         popped_item=l.pop()
#         r_list.append(popped_item)
#     return r_list
# numbers=[1,2,3,4]
# print(reverse_list(numbers))


# def reverse_elements(l):
#     elements=[]
#     for i in l:
#         elements.append(i[::-1])
#     return elements
# words=['abc','tuv','xyz']
# print(reverse_elements(words))

# def filter_odd_even(l):
#     odd_nums=[]
#     even_nums=[]
#     for i in l:
#         if i%2==0:
#             even_nums.append(i)
#         else:
#             odd_nums.append(i)
#     output=[odd_nums, even_nums]
#     return output
# nums=[1,2,3,4,5,6,7]
# print(filter_odd_even(nums))

    # def common_finder(l1,l2):
    #     output=[]
    #     for i in l1:
    #         if i in l2:
    #             output.append(i)
    #     return output
    # print(common_finder([1,2,5,8],[1,2,7,6]))

# numbers=[6,4,3,2]
# numbers.extend([8,9])
# print(numbers)
# numbers.insert(1,"inserted")
# print(numbers)

# numbers=[6,4,3,2]
# print(min(numbers))
# print(max(numbers))
# def greatest_diff(l):
#     return max(l)-min(l)
# print(greatest_diff(numbers))

    # def sublist_counter(l):
    # 	count=0
    # 	for i in l:
    # 		if type(i)==list:
    # 			count+=1
    # 	return count
    # mixed=[1,2,3,[1,2],[3,4]]
    # print(sublist_counter(mixed))
#-------------------------

#tuples are faster than list but immutable

# example=('one','two','three')
# for i in example:
# 	print(i)

# l=(1)
# print(type(l))
# l=(1,)
# print(type(l))
# l=('words')
# print(type(l))
# l=('words',)
# print(type(l))

# guitars= 'hello', 'world', 'this'
# print(type(guitars))

# g=('ashwani','kumar','sonu')
# g1,g2,g3=(g)
# print(g1)

# f=('southern magnolia',['tokyo ghoul theme','landscape'])
# f[1].pop()
# f[1].append("we made it")
# print(f)

# l=(0,1,2,3)
# print(min(l))
# print(max(l))
# print(sum(l))
# print(len(l))

# def func(int1,int2):
# 	add=int1+int2
# 	mul=int1*int2
# 	div=int1/int2
# 	return add,mul,div
# print(func(8,4))
# add,multiply,divide=func(8,4)
# print(add)
# print(multiply)
# print(divide)

# nums1=tuple(range(1,11))
# nums2=list(range(1,11))
# print(nums1)
# print(nums2)

# nums=list(nums)
# nums=str(nums)
# print(nums)
# print(type(nums))

# numlist=str([1,2,3])
# print(numlist)
# print(type(numlist))

# mixed2=(1,2,3,4,5,[1,2,3])
# mixed2[5].pop()
# print(mixed2)

# user={'name':'harshit','age':24}
# print(user)
# print(type(user))

# user1=dict(name='harshit',age=24)
# print(user1)
# print(user1['name'])
# print(user1['age'])

# user_info={
# 	'name':'harshit',
# 	'age':24,
# 	'fav_movies':['hello','world'],
# 	'fav_tunes':['ashwani','kumar']
# 	}
# print(user_info)
# print(user_info['fav_movies'])

# users={
# 	info1={
# 	'name':'harshit',
# 	'age':24,
# 	'fav_movies':['hello','world'],
# 	'fav_tunes':['ashwani','kumar']
# 	},
	# info2={
	# 'name':'harshit',
	# 'age':24,
	# 'fav_movies':['hello','world'],
	# 'fav_tunes':['ashwani','kumar']
	# }
# }

# user_info={}
# user_info['name']='mohit'
# user_info['age']=19
# print(user_info)

# info2={
# 	'name':'harshit',
# 	'age':24,
# 	'fav_movies':['hello','world'],
# 	'fav_tunes':['ashwani','kumar']
# 	}
# if 'name' in info2:
# 	print('present')
# else:
# 	print('not present')

# info2={
# 	'name':'harshit',
# 	'age':24,
# 	'fav_movies':['hello','world'],
# 	'fav_tunes':['ashwani','kumar']
# 	}
# if 'harshit' in info2.values():
# 	print('present')
# else:
# 	print('not present')

# info2={
# 	'name':'harshit',
# 	'age':24,
# 	'fav_movies':['hello','world'],
# 	'fav_tunes':['ashwani','kumar']
# 	}
# if 24 in info2.values():
# 	print('present')
# else:
# 	print('not present')



# info2={
# 	'name':'harshit',
# 	'age':24,
# 	'fav_movies':['hello','world'],
# 	'fav_tunes':['ashwani','kumar']
# 	}

# if ['hello','world'] in info2.values():
# 	print('present')
# else:
# 	print('not present')

# for i in info2:
# 	print(i)
# for i in info2.values():
# 	print(i)

# user_values=info2.values()
# print(user_values)
# print(type(user_values))


# user_values=info2.keys()
# print(user_values)
# print(type(user_values))

# user_values=info2.items()
# print(user_values)
# print(type(user_values))

# info2={
# 	'name':'harshit',
# 	'age':24,
# 	'fav_movies':['hello','world'],
# 	'fav_tunes':['ashwani','kumar']
# 	}

# for key,value in info2.items():
# 	print(f"key is {key} and value is {value}")

# user_info={
# 	'name':'ashwani',
# 	'age':'24',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# print(user_info)
# user_info['skills']=['sass','csharp']
# print(user_info)
# user_info['hobbies']=['games','programming','songs','cricket']
# print(user_info)


# user_info={
# 	'name':'ashwani',
# 	'age':'24',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# skills=user_info.pop('skills')
# print(skills)
# print(type(skills))
# print(user_info)
# print(f"Here are my skills: {skills}")


# user_info={
# 	'name':'ashwani',
# 	'age':'24',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# popped_skills=user_info.popitem()
# print(user_info)
# print(popped_skills)
# print(type(popped_skills))

# user_info={
# 	'name':'ashwani',
# 	'age':'24',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# new_info={ 
# 	'name':'vikas',
# 	'age':'24',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# more_info={ 
# 'hobbies':['cricker','ludo']
# }
# user_info.update(new_info)
# print(user_info)
# user_info.update(more_info)
# print(user_info)
# user_info.update({})
# print(user_info)


# d=dict.fromkeys(['name','hobbies'],'unknown')
# print(d)

# d=dict.fromkeys(('name','hobbies'),'unknown')
# print(d)

# d=dict.fromkeys(('xyz'),'unknown')
# print(d)

# d=dict.fromkeys(range(1,11),'unknown')
# print(d)

# d=dict.fromkeys(['names','age'],['unknown','unknown'])
# print(d)

# new_info={ 
# 	'name':'ashwani',
# 	'age':'24',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# print(new_info.get('names')) #return None
# print(new_info.get('name')) #return None

# new_info={ 
# 	'name':'ashwani',
# 	'age':'24',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# if new_info.get('names'):
# 	print("present")
# else:
# 	print("it is not present")

# info={ 
# 	'name':'ashwani',
# 	'age':'24',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# info.clear()
# print(info)

# info1={ 
# 	'name':'ashwani',
# 	'age':'24',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# info2=info1.copy()
# print(info2)
# print(info1 is info2)

# info1={ 
# 	'name':'ashwani',
# 	'age':'24',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# info2=info1
# print(info1)
# print(info2)
# info1.clear()
# print(info1)
# print(info2)
# print(info2 is info1)

# info1={ 
# 	'name':'ashwani',
# 	'age':'24',
# 	'age':'23',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# print(info1.get('names','not found!'))
# print(info1.get('xuz','not found!'))


# info1={ 
# 	'name':'ashwani',
# 	'age':'24',
# 	'age':'23',
# 	'skills':['c','c++','java','python','html','css','bootstrap','php','sql']
# 	}
# print(info1)	#later key-value will overwrite first key value

# def word_counter(s):
# 	d={}
# 	for i in s:		#each character comes in i
# 		d[i]=s.count(i)	#count the character in string
# 	return d
# print(word_counter("ashwanikumar"))

# mydetails={}
# name=input("enter your name:")
# age=input("enter your age:")
# hobbies=input("enter your hobbies:").split(',')
# mydetails['name']=name
# mydetails['age']=age
# mydetails['hobbies']=hobbies
# print(mydetails)

# for key,value in mydetails.items():
# 	print(f"{key}:{value}")

# s={1,2,3,4,5,1,2,3,2}		#sets are unordered collection
# print(s)
# l=list(s)
# print(l)
# s=set(l)
# print(s)
# s=list(set(l))
# s=set(s)
# s.add(4)
# s.add(5)
# s.add(9)
# s.remove(9)
# s.remove(10)	#if key is not availabe then it will show error
# s.discard(4)    #it will not show errors  if keys not available


# s={1,2,3,4,5,1,2,3,2}		#sets are unordered collection
# # print(s.clear())
# # print(s)
# s1=s.copy()
# print(s1)

# s={1,1.0,2.3,'string'}	#order not matters
# print(s)

# s={'a','b','c'}
# if 'a' in s:
# 	print("present")
# else:
# 	print("not present")
# for i in s:
# 	print(i)

# s1={1,2,3,4,5}
# s2={4,5,65,6}
# union_set=s1|s2
# print(union_set)
# intersection_set=s1&s2
# print(intersection_set)
 
# squares=[]
# for i in range(1,11):
# 	squares.append(i**2)
# print(squares)

# square2=[i**2 for i in range(1,11)]
# print(square2)

# negative=[]
# for i in range(1,11):
# 	negative.append(-i)
# print(negative)

# new_negative=[-i for i in range(1,11)]
# print(new_negative)

# names=['harshit','mohit','rohit']
# new_list=['h','m','r']
# new_list=[]
# for name in names:
# 	new_list.append(name[0])
# print(new_list)
# new_list2=[name[0] for name in names]
# print(new_list2)


# def reverse_str(l):
# 	new_list=[]
# 	for name in l:
# 		new_list.append(name[::-1])
# 	return new_list
# print(reverse_strings(['abc','tuv','xyz']))


# def reverse_strings(l):
# 	return [name[::-1] for name in l]
# print(reverse_strings(['abc','tuv','xyz']))

# numbers=list(range(1,11))
# nums=[]
# for i in numbers:
# 	if i%2==0:
# 		nums.append(i)
# print(nums)
# print([i for i in numbers if i%2==0])
# print([i for i in range(1,11) if i%2==0])
# print([i for i in range(1,11) if i%2!=0])

# def num_to_string(l):
# 	return [str(i) for i in l if (type(i)==int or type(i)==float)]
# print(num_to_string([True, False, [1,2,3],1,1.0,3]))

# nums=[1,2,3,4,5]
# new_list=[]
# for i in nums:
# 	if i%2==0:
# 		new_list.append(i*2)
# 	else:
# 		new_list.append(-i)
# print(new_list)


# nums=[1,2,3,4,5,6,7,8,9]
# new_list2=[i*2 if (i%2==0) else -i for i in nums]
# print(new_list2)

# new_list=[]
# for j in range(3):
# 	new_list.append([1,2,3])
# print(new_list)

# print([[i for i in range(1,4)] for j in range(0,3)])

# square={num:num**2 for num in range(1,11)}
# print(square)

# square={f"square of {num} is":num**2 for num in range(1,11)}
# print(square)

# for k,v in square.items():
# 	print(f"{k}:{v}")

# string="ashwani"
# word_count={char:string.count(char) for char in string}
# print(word_count)

# odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
# print(odd_even)

# s={k**2 for k in range(1,11)}	#order does not matter in 
# print(s)

# names=['harshit','mohit','rohit']
# first={name[0] for name in names}
# print(first)

# def arguments(*args):
# 	print(args)
# 	print(type(args))
# arguments(1,2,3,4,5)

# def all_total(*args):
# 	total=0
# 	for num in args:
# 		total+=num
# 	return total
# print(all_total(1,2,3,4))

# def multiply_nums(num,*args):
# 	multiply=1
# 	print(num)
# 	print(args)
# 	for i in args:
# 		multiply*=i
# 	return multiply
# print(multiply_nums(1,3,2,2,2))	


# def multiply_nums(*args):
# 	multiply=1
# 	print(args)
# 	for i in args:
# 		multiply*=i
# 	return multiply
# print(multiply_nums())	

# def multiply_nums(n1,n2,*args):
# 	multiply=1
# 	print(n1+n2)
# 	print(args)
# 	for i in args:
# 		multiply*=i
# 	return multiply
# print(multiply_nums(1,1,))	


# def multiply_nums(n1,n2,*args):
# 	multiply=1
# 	print(n1+n2)
# 	print(args)
# 	for i in args:
# 		multiply*=i
# 	return multiply
# print(multiply_nums(1,1,3,4))	

# def multiply_nums(*args):
# 	multiply=1
# 	print(args)
# 	for i in args:
# 		multiply*=i
# 	return multiply
# nums=[2,3,4]
# print(multiply_nums(nums))
# print(multiply_nums(*nums)) #this star will unpack the list items


# def to_power(num,*args):
# 	if args:
# 		return[i**num for i in args]
# 	else:
# 		print("you didn't pass any args")
# nums=[2,3]
# print(to_power(2,*nums))
# print(to_power(2,*[2,3]))


# def func(**kwargs):
# 	print(kwargs)
# 	print(type(kwargs))
# func(first_name='harshit',last_name='vashistha')

# def fun(**kwargs):
# 	for k,v in kwargs.items():
# 		print(f"{k}:{v}")
# fun(first_name='ashwani',last_name='kumar')


# def fun(num, **kwargs):
# 	for k,v in kwargs.items():
# 		print(f"{k}:{v}:{num}")
# # fun('mohit',first_name='ashwani',last_name='kumar')
# d={'name':'harshit','age':24}
# fun('mohit',**d)	#unpack dictionary items

# def func(name='unknown',age=24):
# 	print(name)
# 	print(age)
# func('harshit',25)
# func()


# def func(name,*args,last_name='unknown',**kwargs):
# 	print(name)
# 	print(args)
# 	print(last_name)
# 	print(kwargs)
# func('harshit',1,2,3,a=1,b=2)

# def func(l,**kwargs):
# 	if kwargs.get('reverse_str')==True:
# 		return [name[::-1].title() for name in l]
# 	else:
# 		return [name.title() for name in l]
# names=['ashwani','kumar']
# print(func(names,reverse_str=True))

# def new_add(*args):
# 	total=0
# 	for num in args:
# 		total+=num
# 	return total
# # print(new_add(1,2,3,4,5,6,7,8,9))
# l=[1,2,3,4]
# print(new_add(*l))	#unpack

# add=lambda a,b,c:a+b+c
# print(add(1,2,3))
# multiply=lambda a,b,c:a*b*c
# print(multiply(1,2,3))
# divide=lambda a,b:a/b
# print(divide(4,2))

# is_even=lambda a:a%2==0
# print(is_even(6))

# last_char=lambda s:s[::-1]
# print(last_char('ashwani'))

# func=lambda s:True if len(s)>5 else False
# print(func('abcdefr'))
# func=lambda s:len(s)>5
# print(func('abcdefr'))

# for pos,name in enumerate(names):
# 	print(f"{pos}--->{name}")

# def find_pos(l, target):
# 	for pos,name in enumerate(l):
# 		if name==target:
# 			return pos
# 	return -1			
# name=['ashwin','ashwani kumar','ashwani']
# print(find_pos(name,'ashwani'))

# numbers=[1,2,3,4]
# def square(a):
# 	return a**2
# squares=list(map(square,numbers))
# print(squares)
# print(list(map(lambda a:a**2,[1,2,3,4])))

# numbers=[1,2,3,4]
# squares_new=[i**2 for i in numbers]
# print(squares_new)

# def square(n):
# 	return n**2

# numbers=[1,2,3,4]	

# new_list=[]
# for num in numbers:
# 	new_list.append(square(num))
# print(new_list)

# names=['abc','abcd','abcde']
# print(list(map(len,names)))
# print(map(len,names))	#return map object

# def is_even(a):
# 	return a%2==0
# numbers=[3,4,2,1,5,6,9,10]
# print(tuple(filter(is_even,numbers)))
# print(tuple(filter(lambda a:a%2==0,numbers)))
# print(filter(is_even,numbers))

# def is_even(a):
# 	return a%2==0
# numbers=[3,4,2,1,5,6,9,10]
# evens=filter(lambda a:a%2==0,numbers)
# for i in evens:
# 	print(i)
# for i in evens:
# 	print(i)  #only one time iterable

# def is_even(a):
# 	return a%2==0
# numbers=[3,4,2,1,5,6,9,10]
# evens=tuple(filter(lambda a:a%2==0, numbers))
# for i in evens:
# 	print(i)
# for i in evens:
# 	print(i)  #only one time iterable

#we can iterate map,filter only one time

# def is_even(a):
# 	return a%2==0
# numbers=[3,4,5,6,7,8,9]
# evens=filter(lambda a:a%2==0,numbers)
# new_evens=[i for i in numbers if i%2==0]
# print(list(evens))
# print(new_evens)

#for loop calls iter() and nex()

# numbers=[1,2,3,4]	
# squares=map(lambda a:a**2, numbers)
# number_iter=iter(numbers)
# print(iter(numbers))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))

#list,tuples,string are iterables
#map,filter are iterator

# numbers=[1,2,3,4]	
# squares=map(lambda a:a**2, numbers)
# print(iter(numbers))

# user_id=['user1','user2','user3']
# names=['ashwani','kumar','suryan']
# print(list(zip(user_id,names)))

# user_id=['user1','user2']
# fnames=['ashwani','sonu','sumit']
# lnames=['kumar','kumar','kumar']
# print(list(zip(user_id,fnames,lnames)))
# print(dict(zip(user_id,fnames)))

# l=[(1,2),(3,4),(4,5)]
# l1,l2=list(zip(*l))
# print(list(l1))
# print(list(l2))
 
# l1=[1,3,5,7]
# l2=[2,4,6,8]
# new_list=[]
# for pair in zip(l1,l2):
# 	new_list.append(max(pair))
# print(new_list)
# for pair in zip(l1,l2):
# 	new_list.append(min(pair))
# print(new_list)

# def average_finder(*args):
# 	average=[]
# 	for pair in zip(*args):
# 		average.append(sum(pair)/len(pair))
# 	return average
# print(average_finder([1,2,3],[4,5,6],[7,8,9]))

# average_finder=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
# print(average_finder([1,2,3],[4,5,6],[7,8,9]))

# numbers1=[2,3,4,5,6,6]
# evens1=[]
# for num in numbers1:
# 	evens1.append(num%2==0)
# print(all(evens1))	
# print(all([True,False,True,False]))	#all function works like 'and' operator

# numbers1=[2,3,4,5,6,6]
# print(all([num%2==0 for num in numbers1]))	#it works like AND GATE
# print(any([num%2==0 for num in numbers1])) #it works like OR GATE

# def func(item):
# 	return len(item)
# names=['harshit','Mohit','ab']
# print(max(names,key=func))

# def func(item):
# 	return len(item)
# names=['harshit','Mohit','ab']
# print(min(names,key=func))

# names=['harshit','Mohit','ab']
# print(min(names,key= lambda item:len(item)))

# students2=[
# 	{'name':'harshit','score':90,'age':24},
# 	{'name':'mohit','score':70,'age':19},
# 	{'name':'sonu','score':90,'age':19}
# 	]
# print(max(students2,key=lambda item:item.get('score')))
# print(max(students2,key=lambda item:item.get('score'))['name'])
# print(max(students2,key=lambda item:item.get('age'))['score'])

# students={
# 	'harshit':{'score':90,'age':24},
# 	'mohit':{'score':75,'age':19},
# 	'rohit':{'score':76,'age':23}
# 	}
# print(max(students,key=lambda item:students[item]['age']))
# print(min(students,key=lambda item:students[item]['score']))

# fruits=['grapes','mango','apple']
# fruits.sort()
# print(fruits)

# fruits1=('grapes','mango','apple')
# fruits5=sorted(fruits1)
# print(fruits1)
# print(fruits5)

# fruits1={'grapes','mango','apple'}
# fruits2=sorted(fruits1)
# print(fruits1)
# print(fruits2)

# guitars=[
# {'model':'yamaha f223','price':8400},
# {'model':'honda f223','price':2200},
# {'model':'apache f223','price':8200}
# ]
# print(sorted(guitars,key=lambda d:d['price'],reverse=True))
# print(sorted(guitars,key=lambda d:d['price']))
# sort_models=sorted(guitars,key=lambda d:d['model'])
# print(sort_models)

# def add(a,b):
# 	'''this function takes 2 arguments and return their sum'''
# 	return a+b
# print(add.__doc__)

# print(len.__doc__)

# print(sum.__doc__)

# print(help(sum))

# def square(a):
# 	return a**2
# s=square
# print(s(7))

# print(s.__name__)
# print(square.__name__)
# print(s)
# print(square)

# def square(a):
# 	return a**2
# l=[1,2,3,4]
# print(list(map(square,l)))

# l=[1,2,3,4]
# def square(a):
# 	return a**2
# def my_map(func,l):
# 	new_list=[]
# 	for item in l:
# 		new_list.append(func(item))
# 	return new_list
# print(my_map(square,l))

# l=[1,2,3,4]
# def my_map(func,l):
# 	new_list=[]
# 	for item in l:
# 		new_list.append(func(item))
# 	return new_list
# print(my_map(lambda a:a**3,l))

# l=[1,2,3,4]
# def my_map2(func,l):
#  return [func(item) for item in l]
# print(my_map2(lambda a:a**2,l))

# def outer_func():
# 	def inner_func():
# 		print('inside func')
# 	return inner_func
# var=outer_func()
# var()

# def outer_func():
# 	def inner_func():
# 		print('inside func')
# 	return inner_func()
# outer_func()

# def outer_func2(msg):
# 	def inner_func2():
# 		print(f"message is {msg}")
# 	return inner_func2
# var=outer_func2("old")
# var()

# def to_power(x):
# 	def calc_power(n):
# 		return n**x
# 	return calc_power
# cube=to_power(3)
# print(cube(2))
# square=to_power(2)
# print(square(4))

# def decorator_function(any_function):
# 	def wrapper_function():
# 		print("this is awesome function")
# 		any_function()
# 	return wrapper_function

# def func1():
# 	print("this is function 1")
# def func2():
# 	print("this is function 2")

# func1=decorator_function(func1)
# func1()
# func2=decorator_function(func2)
# func2()

# def decorator_function(parameter):
# 	def wrapper_function():
# 		print("this is awesome function")
# 		parameter()
# 	return wrapper_function

# @decorator_function
# def func1():
# 	print('this is function 1')
# func1()

# @decorator_function
# def func2():
# 	print('this is function 2')
# func2()



# def decorator_function(parameter):
# 	def wrapper_function(*args,**kwargs):
# 		print("this is awesome function")
# 		parameter(*args,**kwargs)
# 	return wrapper_function

# @decorator_function
# def func1(a):
# 	print(f'this is function 1 with argument {a}')
# func1(7)




# def decorator_function(parameter):
# 	def wrapper_function(*args,**kwargs):
# 		print("this is awesome function")
# 		return parameter(*args,**kwargs)
# 	return wrapper_function

# @decorator_function
# def func1(a):
# 	print(f'this is function 1 with argument {a}')
# func1(7)
# @decorator_function
# def add(a,b):
# 	return a+b
# print(add(2,3))



# def decorator_function(parameter):
# 	def wrapper_function(*args,**kwargs):
# 		"""this is wrapper function"""
# 		print("this is awesome function")
# 		return parameter(*args,**kwargs)
# 	return wrapper_function

# @decorator_function
# def add(a,b):
# 	return a+b
# print(add.__doc__)
# print(add.__name__)

# from functools import wraps
# def decorator_function(any_function):
# 	@wraps(any_function)
# 	def wrapper_function(*args,**kwargs):
# 		"""this is wrapper function"""
# 		print("this is awesome function")
# 		return any_function(*args,**kwargs)
# 	return wrapper_function

# @decorator_function
# def adds(a,b):
# 	'''this is add function'''
# 	return a+b

# print(adds.__doc__)
# print(adds.__name__)

# from functools import wraps
# def print_function_data(function):
# 	@wraps(function)
# 	def wrapper(*args,**kwargs):
# 		print(f"you are calling{function.__name__}function")
# 		print(f"{function.__doc__}")
# 		return function(*args,**kwargs)
# 	return wrapper

# @print_function_data
# def addition(a,b):
# 	"""This function takes two numbers as arguments and return their sum"""
# 	return a+b

# print(addition(4,5))

# import time
# t1=time.time()
# print(t1)
# print('this is line one')
# x=5
# if x==5:
# 	print('x is equal to 5')
# print('this is line two')
# print('this is line two')
# print('this is line two')
# print('this is line two')
# t2=time.time()
# print(t2-t1)

# from functools import wraps
# import time
# def calculate_time(function):
# 	@wraps(function)
# 	def wrapper(*args,**kwargs):
# 		t1=time.time()
# 		returned_value=function(*args,**kwargs)
# 		t2=time.time()
# 		total_time=t2-t1
# 		print(f'this function took {total_time} seconds')
# 		return returned_value
# 	return wrapper

# @calculate_time
# def square_finder(n):
# 	return [i**2 for i in range(1,n+1)]

# square_finder(1000)


# from functools import wraps
# def only_int_allow(function):
# 	@wraps(function)
# 	def wrapper(*args,**kwargs):
# 		if all([type(arg)==int for arg in args]):
# 			return function(*args,**kwargs)
# 		print("Invalid arguments")
# 	# 	data_types=[]
# 	# 	for arg in args:
# 	# 		data_types.append(type(arg)==int)
# 	# 	if all(data_types):
# 	# 		return function(*args,**kwargs)
# 	# 	else:
# 	# 		print("Invalid arguments")
# 	return wrapper

# @only_int_allow
# def add_all(*args):
# 		total=0
# 		for i in args:
# 			total+=i
# 		return total

# print(add_all(1,2,3,4,5,'harshit'))
# print(add_all(1,2,3,4,5))



# from functools import wraps
# def only_data_type_allow(data_type):
# 	def decorator(function):
# 		@wraps(function)
# 		def wrapper(*args,**kwargs):
# 			if all([type(arg)==data_type for arg in args]):
# 				return function(*args,**kwargs)
# 			print("invalid arguments")
# 		return wrapper
# 	return decorator

# @only_data_type_allow(str)
# def string_join(*args):
# 	string=''
# 	for i in args:
# 		string = string + " " + i 
# 	print(string)

# string_join('harshit','vishu',21)
# string_join('harshit','vishu')


# i=iter([1,2,3])
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# l=[1,2,3,4,5]
# for num in map(lambda a:a**2,l):
# 	print(num)


# def nums(n):
# 	for i in range(1,n+1):
# 		yield i

# for number in nums(10):
# 	print(number)

# def nums(n):
# 	for i in range(1,n+1):
# 		yield i
# numbers=nums(10)
# for num in numbers:
# 	print(num)
# for num in numbers:	# this will not work because we are using generators
# 	print(num)


# def nums(n):
# 	for i in range(1,n+1):
# 		yield i
# numbers=list(nums(10))
# for num in numbers:
# 	print(num)
# for num in numbers:
# 	print(num)

# def even_generator(n):
# 	for num in range(2,n+1,2):
# 		yield(num)

# even_nums=even_generator(20)
# for num in even_nums:
# 	print(num)


# def even_generator(n):
# 	for num in range(1,n+1):
# 		if num%2==0:
# 			yield(num)

# even_nums=even_generator(20)
# for num in even_nums:
# 	print(num)

# square=(i**2 for i in range(1,11)) #for generator list using compression
# for num in square:
# 	print(num)


# square=(i**2 for i in range(1,11)) #for generator list using compression
# #generator is much efficient than list as it only generates 1 number at a time thats why it is memory efficient
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))


# import time
# t1=time.time()
# l=[i**2 for i in range(1000000)]	#using list
# print(time.time()-t1)


# import time
# t1=time.time()
# l=(i**2 for i in range(1000000))	#using generator
# print(time.time()-t1)


# class Person:
# 	def __init__(self, first_name,last_name,age):
# 		self.first_name=first_name
# 		self.last_name=last_name
# 		self.age=age
# p1=Person('harshit','kumar',23)
# p2=Person('mohit','kumar',19)
# print(p1.first_name)
# print(p1.last_name)
# print(p1.age)
# print(p2.first_name)
# print(p2.last_name)
# print(p2.age)



# class Person:
# 	def __init__(this, first_name,last_name,age): #we can use any name in place of first argument here to represent the name of object instance
# 		this.first_name=first_name
# 		this.last_name=last_name
# 		this.age=age

# p1=Person('harshit','kumar',23)
# p2=Person('mohit','kumar',19)

# print(p1.first_name)
# print(p1.last_name)
# print(p1.age)

# print(p2.first_name)
# print(p2.last_name)
# print(p2.age)


# class Laptop:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.name=model_name
# 		self.price=price
# 		self.laptop_name=brand+' '+model_name

# laptop1=Laptop('hp','au114tx',63000)
# print(laptop1.laptop_name)

# class Person:
# 	def __init__(self,first_name,last_name,age):
# 		self.first_name=first_name
# 		self.last_name=last_name
# 		self.age=age

# 	def full_name(self):
# 		return f"{self.first_name} {self.last_name}"

# 	def is_above_18(self):
# 		return self.age>18

# p1=Person('ashwani','kumar',24)
# p2=Person('sumit','kumar',22)

# print(p1.full_name())
# print(Person.full_name(p1))
# print(p1.is_above_18())

# print(p2.full_name())
# print(Person.full_name(p2))
# print(p2.is_above_18())


# class Laptop:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.name=model_name
# 		self.price=price
# 		self.laptop_name=brand+' '+model_name

# 	def apply_discount_percent(self,num):
# 		off_price=(num/100)*self.price
# 		return self.price-off_price

# laptop1=Laptop('hp','au114tx',63000)
# laptop2=Laptop('apple','macbook pro',23000)
# print(laptop1.apply_discount_percent(5))
# print(laptop2.apply_discount_percent(5))


# class Circle:
# 	def __init__(self,raidus,pi):
# 		self.raidus=raidus
# 		self.pi=pi
	
# 	def calc_circumference(self):
# 		return 2*self.pi*self.raidus

# c1=Circle(4,3.14)
# c2=Circle(5,3.14)
# print(c1.calc_circumference())
# print(c2.calc_circumference())


# class Circle:
# 	pi=3.14
# 	def __init__(self,raidus):
# 		self.raidus=raidus
	
# 	def calc_circumference(self):
# 		return 2*self.pi*self.raidus

# c1=Circle(4)
# c2=Circle(5)
# print(c1.calc_circumference())
# print(c2.calc_circumference())


# class Laptop:
# 	discount=4
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.name=model_name
# 		self.price=price
# 		self.laptop_name=brand+' '+model_name

# 	def apply_discount_percent(self):
# 		off_price=(Laptop.discount/100)*self.price
# 		return self.price-off_price

# laptop1=Laptop('hp','au114tx',63000)
# laptop2=Laptop('apple','macbook pro',23000)
# print(laptop1.apply_discount_percent())
# print(laptop2.apply_discount_percent())



# class Laptop:
# 	discount=4
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.name=model_name
# 		self.price=price
# 		self.laptop_name=brand+' '+model_name

# 	def apply_discount_percent(self):
# 		off_price=(Laptop.discount/100)*self.price
# 		return self.price-off_price

# Laptop.discount=100	#change the class variable outside class
# laptop1=Laptop('hp','au114tx',63000)
# laptop2=Laptop('apple','macbook pro',23000)
# print(laptop1.apply_discount_percent())
# print(laptop2.apply_discount_percent())
# print(laptop1.__dict__)
# print(laptop2.__dict__)


# class Laptop:
# 	discount=0
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.name=model_name
# 		self.price=price
# 		self.laptop_name=brand+' '+model_name

# 	def apply_discount_percent(self):
# 		off_price=(self.discount/100)*self.price
# 		return self.price-off_price


# laptop1=Laptop('hp','au114tx',1000)
# laptop1.discount=50
# print(laptop1.apply_discount_percent())
# print(laptop1.__dict__)

# laptop2=Laptop('apple','macbook pro',1000)
# laptop2.discount=100
# print(laptop2.apply_discount_percent())
# print(laptop2.__dict__)


# class Person:
# 	count_instance=0	#class variable

# 	def __init__(self,name,age):
# 		Person.count_instance+=1	#class variable increment
# 		self.name=name
# 		self.age=age

# p1=Person("ashwani",24)		
# p2=Person("sumit",20)		
# p3=Person("neelam",23)		
# p4=Person("shewta",22)		
# p5=Person("monika",21)		
# p6=Person("pinku",25)		
# p7=Person("ankit",26)		

# print(Person.count_instance)	#calling class variable


# class Person:
# 	count_instance=0	#class variable

# 	def __init__(self,name,age):	#self used for instance reference
# 		Person.count_instance+=1	#class variable increment
# 		self.name=name
# 		self.age=age

# @classmethod
# def count_instance_func(cls):		#cls used for class reference
# 	return print(f"You have created {cls.count_instance} instances of {cls.__name__}")

# p1=Person("ashwani",24)		
# p2=Person("sumit",20)		
# p3=Person("neelam",23)		
# p4=Person("shewta",22)		
# p5=Person("monika",21)		
# p6=Person("pinku",25)		
# p7=Person("ankit",26)		

# print(Person.count_instance)		#calling class variable
# Person.count_instance_func()


# class Person:
# 	@classmethod
# 	def from_string(cls,string):
# 		    first,age=string.split(',')
# 		    return cls(first,age)

# p1=Person.from_string('ashwanikumar,24')	#making an object using string arguments 



# class Person:
# 	@staticmethod
# 	def hello():
# 			print('hello,static method called')

# Person.hello()




# class Person:
# 	def __init__(self,name,age):	#this is a dunder/magic method that starts with '__'
# 		self._name=name
# 		self._age=age 				#every variable is public in python but we can use '_' to show developer that this variable should be considered as private variables




# class Phone:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.model_name=model_name
# 		self._price=price     

# phone1=Phone('nokia','1100',1000)
# print(phone1._price)	#underscrore is just a convention to represent any private variable to a class but actually it remains public to that class
# phone1._price=-1000
# print(phone1._price)




# class Phone:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.model_name=model_name
# 		self.__price=price     

# phone1=Phone('nokia','1100',1000)
# print(phone1.__price)
# print(phone1.__dict__)	#name mangling
# print(phone1._Phone__price)
# phone1._Phone__price=-1000
# print(phone1._Phone__price)



# class Phone:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.model_name=model_name
# 		self._price=max(price,0)	#for positive values
		
# 	@property
# 	def complete_specification(self):
# 		return f"brand:{self.brand}, model name:{self.model_name} and model price:{self._price}"

# p1=Phone('nokia','1100',-10000)	#let users dont pass -ve value

# print(p1.brand)
# print(p1.model_name)
# print(p1._price)
# print(p1.complete_specification)	#we can call this function as property using property decorator above



# class Phone:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.model_name=model_name
# 		self._price=price
		
# 	@property
# 	def price(self):
# 		return self._price

# 	@price.setter
# 	def price(self,new_price):
# 		self._price=max(new_price,0)

# p1=Phone('nokia','1100',-10000)	#let users dont pass -ve value
# p1.price=-500
# print(p1.price)


# class Phone:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.model_name=model_name
# 		self._price=max(price,0)

# 	def full_name(self):
# 		return f"Brand name:{self.brand} and model name:{self.model_name}"

# 	def make_a_call(self,number):
# 		return f"calling{self.number}...."	

# class Smartphone(Phone):
# 	def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
# 		# Phone.__init__(self,brand,model_name,price) #will work same as super()
# 		super().__init__(brand,model_name,price)
# 		self.ram=ram
# 		self.internal_memory=internal_memory
# 		self.rear_camera=rear_camera

# phone=Phone('nokia','1100',1000)
# print(phone.full_name())
	
# smartphone=Smartphone('oneplus','5',30000,'6 GB','64 GB','20 MP')
# print(smartphone.full_name()+f" and price is: {smartphone._price}")



#multiple inheritence
# class Phone:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.model_name=model_name
# 		self._price=max(price,0)

# 	def full_name(self):
# 		return f"Brand name:{self.brand} and model name:{self.model_name}"

# 	def make_a_call(self,number):
# 		return f"calling{self.number}...."	

# class Smartphone1(Phone):
# 	def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
# 		# Phone.__init__(self,brand,model_name,price) #will work same as super()
# 		super().__init__(brand,model_name,price)
# 		self.ram=ram
# 		self.internal_memory=internal_memory
# 		self.rear_camera=rear_camera

# class Smartphone2(Phone):
# 	def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
# 		# Phone.__init__(self,brand,model_name,price) #will work same as super()
# 		super().__init__(brand,model_name,price)
# 		self.ram=ram
# 		self.internal_memory=internal_memory
# 		self.rear_camera=rear_camera

# phone=Phone('nokia','1100',1000)
# print(phone.full_name())
# smartphone1=Smartphone1('motorola','5',30000,'6 GB','64 GB','20 MP')
# print(smartphone1.full_name()+f" and price is: {smartphone1._price}")
# smartphone2=Smartphone2('nokia','5',30000,'6 GB','64 GB','20 MP')
# print(smartphone2.full_name()+f" and price is: {smartphone2._price}")


#multilevel inheritence
# class Phone:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.model_name=model_name
# 		self._price=max(price,0)

# 	def full_name(self):
# 		return f"Brand name:{self.brand} and model name:{self.model_name}"

# 	def make_a_call(self,number):
# 		return f"calling{self.number}...."	

# class Smartphone(Phone):
# 	def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
# 		# Phone.__init__(self,brand,model_name,price) #will work same as super()
# 		super().__init__(brand,model_name,price)
# 		self.ram=ram
# 		self.internal_memory=internal_memory
# 		self.rear_camera=rear_camera

# class tablet(Smartphone):
# 	def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
# 		super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
# 		self.front_camera=front_camera
# 		self.ram=ram
# 		self.internal_memory=internal_memory
# 		self.rear_camera=rear_camera

# phone=Phone('nokia','1100',1000)
# print(phone.full_name())

# smartphone=Smartphone('motorola','5',30000,'6 GB','64 GB','20 MP')
# print(smartphone.full_name()+f" and price is: {smartphone._price}")

# tablet=tablet('lenevo','5',20000,'3 GB','64 GB','20 MP','10MP')
# print(tablet.full_name()+f" and price is: {tablet._price}")


#method resolution order, method overriding , isinstance() and issubclass()
# class Phone:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.model_name=model_name
# 		self._price=max(price,0)

# 	def full_name(self): 
# 		return f"calling function from phone class--->Brand name:{self.brand},model name:{self.model_name},price:{self._price}"

# class Smartphone(Phone):
# 	def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
# 		super().__init__(brand,model_name,price)
# 		self.ram=ram
# 		self.internal_memory=internal_memory
# 		self.rear_camera=rear_camera

# 	def full_name(self): 	#method overiding
# 		return f"calling function from smartphone class--->Brand name:{self.brand},model name:{self.model_name},price:{self._price},ram:{self.ram},internal_memory:{self.internal_memory},rear_camera:{self.rear_camera}"

# class tablet(Smartphone):
# 	def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
# 		super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
# 		self.front_camera=front_camera

# 	def full_name(self):	#method overiding
# 		return f"calling function from tablet class--->Brand name:{self.brand},model name:{self.model_name},price:{self._price},ram:{self.ram},internal_memory:{self.internal_memory},rear_camera:{self.rear_camera},front_camera:{self.front_camera}"

# phone_obj=Phone('nokia','1100',10000)
# print(phone_obj.full_name())
# print(help(Phone))	#method resolution order
# print(isinstance(phone_obj,Phone))	#isinstance function(object name , class name)

# smartphone_obj=Smartphone('motorola','5',30000,'6 GB','64 GB','20 MP')
# print(smartphone_obj.full_name())
# print(help(Smartphone))	#method resolution order
# print(isinstance(smartphone_obj,Phone))		#isinstance function(object name , class name)
# print(isinstance(smartphone_obj,Smartphone))		#isinstance function(object name , class name)

# print(isinstance(phone_obj,Smartphone))

# tablet_obj=tablet('lenevo','5',20000,'3 GB','64 GB','20 MP','10MP')
# print(tablet_obj.full_name())
# print(help(tablet))	#method resolution order
# print(isinstance(tablet_obj,Phone))			#isinstance function(object name , class name)
# print(isinstance(tablet_obj,Smartphone))		#isinstance function(object name , class name)
# print(isinstance(tablet_obj,tablet))			#isinstance function(object name , class name)

# print(isinstance(phone_obj,tablet))
# print(isinstance(smartphone_obj,tablet))


#multiple inheritence
# class A:

# 	def hello(self):
# 		print("this is class A")

# class B:

# 	def hello(self):
# 		print("this is class B")

# class C(A,B):
# 	pass

# class D(B,A):
# 	pass

# class_c_obj=C()
# class_c_obj.hello()
# print(help(C))		#method resolution order
# print(C.mro())		#method resolution order
# print(C.__mro__)	#method resolution order

# class_d_obj=D()
# class_d_obj.hello()
# print(help(D))		#method resolution order
# print(D.mro())	    #method resolution order
# print(D.__mro__)	#method resolution order


# class Phone:
# 	def __init__(self,brand,model,price):
# 		self.brand=brand
# 		self.model=model
# 		self.price=price

# 	def phone_name(self):
# 		return f'{self.brand}{self.model}'

# 	def __str__(self):
# 		return f'{self.brand}{self.model}'
	
# Phone_obj=Phone('nokia','1100',1000)	
# print(Phone_obj) #now it will use __str__function


# class Phone:
# 	def __init__(self,brand,model,price):
# 		self.brand=brand
# 		self.model=model
# 		self.price=price

# 	def phone_name(self):
# 		return f'{self.brand}{self.model}'

# 	def __repr__(self):
# 		return f'{self.brand}{self.model}'
	
# Phone_obj=Phone('nokia','1100',1000)	
# print(Phone_obj) #now it will use __repr__ function


# class Phone:
# 	def __init__(self,brand,model,price):
# 		self.brand=brand
# 		self.model=model
# 		self.price=price

# 	def phone_name(self):
# 		return f'{self.brand}{self.model}'

# 	def __str__(self):
# 		return f'{self.brand}{self.model}'
	
# 	def __repr__(self):
# 		return f'{self.brand}{self.model}{self.price}'
	
# Phone_obj=Phone('nokia','1100',1000)	
# print(Phone_obj) #now it will only use __str__ function not the next one after it


# class Phone:

# 	def __init__(self,brand,model,price):
# 		self.brand=brand
# 		self.model=model
# 		self.price=price

# 	def phone_name(self):
# 		return f'{self.brand}{self.model}'

# 	def __str__(self):
# 		return f'{self.brand}{self.model}'
	
# 	def __repr__(self):
# 		return f'{self.brand}{self.model}{self.price}'
	
# Phone_obj=Phone('nokia','1100',1000)	
# print(str(Phone_obj))		#it will call __str__
# print(repr(Phone_obj))	#it will call __repr__


# class Phone:
# 	def __init__(self,brand,model,price):
# 		self.brand=brand
# 		self.model=model
# 		self.price=price

# 	def phone_name(self):
# 		return f'{self.brand}{self.model}'

# 	def __str__(self):
# 		return f'{self.brand}{self.model}{self.price}'
	
# 	def __repr__(self):
# 		return f'Phone(\'{self.brand}\',\'{self.model}\',{self.price})'
	
# Phone_obj=Phone('nokia','1100',1000)	
# print(str(Phone_obj))		#it will call __str__
# print(repr(Phone_obj))	#it will call __repr__ and return object copy
# print(Phone_obj.__repr__())


#operator overloading or polymorphism
# class Phone:
# 	def __init__(self,price):
# 		self.price=price

# 	def __add__(self,other):
# 		return self.price+other.price

# 	def __mul__(self,other):
# 		return self.price*other.price

# phone1=Phone(2000)
# phone2=Phone(5000)
# print(phone1+phone2)	#object addition due to operator overloading
# print(phone1*phone2)	#object multiplication due to operator overloading

#polymorphism of len()
# l=[1,2,3,4,5]
# print(len(l))
# l={1,2,3,4,5}
# print(len(l))
# l=(1,2,3,4,5)
# print(len(l))


#polymorphism with method overriding

# class Phone:
# 	def __init__(self,brand,model_name,price):
# 		self.brand=brand
# 		self.model_name=model_name
# 		self._price=max(price,0)

# 	def full_name(self):
# 		return"calling function through class phone"

# class Smartphone1(Phone):
# 	def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
# 		# Phone.__init__(self,brand,model_name,price) #will work same as super()
# 		super().__init__(brand,model_name,price)
# 		self.ram=ram
# 		self.internal_memory=internal_memory
# 		self.rear_camera=rear_camera
	
# 	def full_name(self):
# 		return f"calling overriding function through class smartphone1"


# phone=Phone('nokia','1100',1000)
# print(phone.full_name())

# smartphone1=Smartphone1('motorola','5',30000,'6 GB','64 GB','20 MP')
# print(smartphone1.full_name())


#errors handling in python
# def add(a,b):
# 	if (type(a) is int) and (type(b) is int):
# 	# if (type(a)==int) and (type(b)==int): #this is alternative to upper syntax
# 		return a+b
# 	raise TypeError("wrong arguments passed") 
# 	# raise ValueError("wrong arguments passed") 

# print(add(2,3))
# print(add('2','3'))



# class Animal:
# 	def __init__(self,name):
# 		self.name=name

# 	def sound(self):	
# 		raise NotImplementedError("define this function in child class")

# class Dog(Animal):
# 	def __init__(self,name,breed):
# 		super().__init__(name)
# 		self.breed=breed

# 	def sound(self):
# 		return "bow bow"	#overriding

# class Cat(Animal):
# 	def __init__(self,name,breed):
# 		super().__init__(name)
# 		self.breed=breed

# 	def sound(self):	
# 		return "meow meow"	#overriding

# doggy=Dog('boony','pug')
# print(doggy.sound())

# cat=Cat('caty','catee')
# print(cat.sound())

# animal=Animal('animals')
# print(animal.sound())		#raise error of type NotImplementedError



# class Mobile:
# 	def __init__(self,name):
# 		self.name=name

# class MobileStore:
# 	def __init__(self):
# 		self.mobiles=[]

# 	def add_mobile(self,new_mobile):
# 		self.mobiles.append(new_mobile)

# oneplus=Mobile("one plus 5")
# samsung="samsung galaxy s8"
# mobostore=MobileStore()
# print(mobostore.mobiles)
# mobostore.add_mobile(samsung)
# print(mobostore.mobiles)

# class Mobile:
# 	def __init__(self,name):
# 		self.name=name

# class MobileStore:
# 	def __init__(self):
# 		self.mobiles=[]
# 	def add_mobile(self,new_mobile):
# 		if isinstance(new_mobile,Mobile):
# 			self.mobiles.append(new_mobile)
# 		else:
# 			raise TypeError('new mobile should be object of Mobile class')

# oneplus=Mobile('one plus 6')
# samsung='samsung galaxy s8'
# mobostore=MobileStore()
# mobostore.add_mobile(oneplus)
# mobo_phones=mobostore.mobiles
# print(mobo_phones[0].name)




# while True:
# 	try:
# 		age=int(input("enter your age:"))
# 		break
# 	except ValueError: #use this argument if you know type of error
# 		print("invalid input...")
# 	except:	#use this if you dont know type of error
# 		print("invalid input...")

# if age<18:
# 	print("you cant play this game")
# else:
# 	print("you can play this game")




# while True:
# 	try:
# 		number=int(input("enter your number:"))		
# 	except ValueError: #use this argument if you know type of error
# 		print("invalid input...")
# 	except:	#use this if you dont know type of error
# 		print("unexpected error...")
# 	else:
# 		print(f'user input ={number}')
# 		break
# 	finally:
# 		print("finally always runs............")


# def divide(a,b):
# 	try:
# 		return a/b
# 	except zeroDivisionError as err:
# 		print(err)
# 	except TypeError as err:
# 		print(err)
# 	except:
# 		print("unexpected error")

# a,b=input('enter a,b:').split(',')
# print(f'your inputs are a:{a} and b:{b}')
# print(divide(int(a),int(b)))



# def validate(name):
# 	if len(name)<8:
# 		raise ValueError('name is too short')

# username=input('enter your name:')
# validate(username)
# print(f'hello {username}')


# class NameTooShort(ValueError):
# 	pass

# def validate(name):
# 	if len(name)<8:
# 		raise NameTooShort("name is too short")

# username=input('enter your name:')
# validate(username)
# print(f'hello {username}')

#debugging
# import pdb
# pdb.set_trace()
# name=input('enter name:')
# age=input('enter age:')
# print(f'hello{name} your age is {age}')
# age2=age+5
# print(f'{name} you will be {age2} in next five years')



#file operations
# f=open('file1.txt') # to open a file

# f=open(r'C:\Users\HP\Desktop\python\file1.txt') # use r to open a file using given path else it shows errors

# print(f.readline(),end='') #end is used to skip space between next lines

# print(f.readline()) #read one line at a time

# print(f.read())	#read whole file at once

# print(f'cursor position:{f.tell()}') 	#it tells that

# f.seek(50)	#it transfer curson to specific position

# lines=f.readlines() #it returns list
# print(lines)
# print(len(lines))

# for line in lines:
# 	print(line,end='')

# print(f.name)

# for line in f:	#use this to print all the data in a given file
# 	print(line,end='')

# for line in f.readlines()[:3]:	#to print only 3 lines
# 	print(line, end='')
# f.close()

# print(f.closed)


#context manager manages all things and close the files automatically at the end
# with open('file1.txt') as f:
# 	print(f.read())
# print(f.closed)


# with open('file1.txt','r') as f:	#'r' is used for read mode and it is bydefault
# 	print(f.read())


# with open('file1.txt','w') as f:	#'w' is used for write mode...
# 	f.write('helloworld\nagainhellworld\nagain helloworld')	# overwrite old data 


# with open('file2.txt','w') as f:	#if file not found then it creates a new file
# 	f.write('this is file2.txt')


# with open('file2.txt','a') as f:	#to append a text at the end of the file
# 	f.write(' this is file2.txt\n')


# with open('file3.txt','a') as f:	#it can create a new file as well
# 	f.write(' this is file3 created with append argument\n')


#for r+ mode we have to create the file first then we can work in it
#first create file using gitbash command prompt: echo -e "helloworld">>file.txt
#with r+ mode we can read and write both together
# with open('file33.txt','r+') as f:
# 	f.seek(len(f.read()))
# 	f.write('please do it\n')
# 	f.write('hello do it \n')
# 	f.seek(len(f.read()))


#read from one file and write to another file
# with open('file11.txt','r') as rf:
# 	with open('file22.txt','a') as wf:
# 		wf.write(rf.read())

#read from one file and write to another file in a formated way
# with open('salary.txt','r') as rf:
# 	with open('output.txt','a') as wf:
# 		for line in rf.readlines():
# 			name,salary=line.split(',')
# 			wf.write(f"name:{name} and salary:{salary}")


#read links from a html files and write into another file
# with open('index.html','r') as webpage_file:
# 	with open('output.txt','a') as output_file:
# 		for line in webpage_file.readlines():
# 			if '<a href=' in line:
# 				pos=line.find('<a href=')
# 				first_quote=line.find('\"',pos)
# 				second_quote=line.find('\"',first_quote+1)
# 				url=line[first_quote+1 : second_quote]
# 				output_file.write(url+'\n')


#read links from html files and write into another text file
# with open('index.html','r') as webpage_file:
# 	with open('output.txt','a') as output_file:
# 		page=webpage_file.read()
# 		link_exist=input("link available? (type True or False):")
# 		while link_exist:
# 			pos=page.find('<a href=')
# 			if pos==-1 or pos==0:
# 				link_exist=False
# 			else:
# 				first_quote=page.find('\"',pos)
# 				second_quote=page.find('\"',first_quote+1)
# 				url=page[first_quote+1 : second_quote]
# 				output_file.write(url + '\n')
# 				page=page[second_quote:]


#to read a different file encoding
# with open('love_story.txt','r',encoding='utf-8') as f:
# 	print(f.encoding)
# 	print(f.read())


#read only 100 characters and print output
# with open('file.txt','r') as f:
# 	print(f.read(100))

#read only 100 characters at a time using loop
# with open('file.txt','r') as f:
# 	data=f.read(100)
# 	while len(data)>0:
# 		print(data)
# 		data=f.read(100)


# from csv import reader 
# with open('file.csv','r') as f:
# 	# print(reader(f)) #returns object location, reader is iterator
# 	# print(type(reader(f)))	#return class name
# 	next(reader(f))	#it is used to jump at the next line
# 	for row in reader(f):
# 		print(row)




# from csv import DictReader
# with open('file.csv','r') as f:
# 	# csv_reader=DictReader(f)
# 	csv_reader=DictReader(f,delimiter='|') #this is used when we use '|' in csv files as delimiter
# 	for row in csv_reader:
# 		print(row['email'])


# from csv import writer
# with open('file.csv','w',newline='') as f:	#newline is used to skip newlines
# 	csv_writer=writer(f,delimiter='@')					#object created to write in csv files
# 	csv_writer.writerow(['name','country'])	#print new rows in csv files
# 	csv_writer.writerow(['ashwani','india'])	
# 	csv_writer.writerow(['ashwani','india'])
# 	csv_writer.writerow(['ashwani','india'])
# 	csv_writer.writerow(['ashwani','india'])
# 	csv_writer.writerows([['name','country'],['mohit','INDIA'],['harshit','INDIA']]) # to write in csv files only using one line



# from csv import DictWriter
# with open('file.csv','w',newline='') as f: #newline='' is used to skip newlines
# 	csv_writer=DictWriter(f,fieldnames=['firstname','lastname','age'],delimiter='|')	#fieldnames is for header and delimiter for separating with '|'
# 	csv_writer.writeheader()	#it writes header things
# 	csv_writer.writerow({		#it will print individual dictionary items
# 		'firstname':'harshit',
# 		'lastname':'vashistha',
# 		'age':500
# 		})
# 	csv_writer.writerow({
# 		'firstname':'mohit',
# 		'lastname':'vashistha',
# 		'age':500
# 		})

# 	csv_writer.writerows(	#to print all dictionary items in one go
# 		[
# 		{'firstname':'ashwani','lastname':'kumar','age':500},
# 		{'firstname':'ashwani','lastname':'kumar','age':500},
# 		{'firstname':'ashwani','lastname':'kumar','age':500},
# 		{'firstname':'ashwani','lastname':'kumar','age':500}
# 		]
# 		 )



# from csv import DictReader,DictWriter
# with open('file1.csv','r') as rf:
# 	with open('file2.csv','w', newline='') as wf:
# 		csv_reader=DictReader(rf)
# 		csv_writer=DictWriter(wf,fieldnames=['first_name','last_name','age'])
# 		csv_writer.writeheader()
# 		for row in csv_reader:
# 			fname,lname,age=row['firstname'],row['lastname'],row['age']
# 			csv_writer.writerow({
# 				'first_name':fname.upper(), #formatted outputs
# 				'last_name':lname.upper(),	#formatted outputs
# 				'age':age.upper()			#formatted outputs
# 				})



import os

# print(os.getcwd()) 						    #print current working directory

# os.mkdir('newfolder1')					    #make a directory in same folder

# print(os.path.exists('newfolder1'))		    #check and return true or false whether file exists

# if os.path.exists('newfolder1'):			
# 	print('folder already exists')
# else:
# 	os.mkdir('newfolder1')			

# open('index.html','a').close() 			    #open or create a new file

# os.chdir(r'C:\Users\HP\Desktop')				#change location of current working directory

# os.mkdir(r'C:\Users\HP\Desktop\newfolder2')   #r is used to ignore escape sequences

# print(os.listdir())								#print list of folders in a current directory in the form of list

# print(os.listdir(r'C:\Users\HP\Desktop'))		#print list of folders in a directories if given path

# for item in os.listdir():
# 	 print(r'C:\Users\HP\Desktop\python'+'\\'+item)	#to print paths of different files or folders inside a current working directory

# for item in os.listdir():  								#print paths of all files or folder in a current working directory
# 	path=os.path.join(os.getcwd(),item)
# 	print(path)


# for item in os.listdir(r'C:\Users\HP\Desktop'):  			#print paths of all files or folders from a different directory
# 	path=os.path.join(os.getcwd(r'C:\Users\HP\Desktop'),item)
# 	print(path)

# fileiteration=os.walk(r'C:\Users\HP\Desktop\python')		#it will walk through all folders and files in a directory and their subdirectories
# for current_path,folder_names,file_names in fileiteration:
# 	print(f'current path:{current_path}')
# 	print(f'folder names:{folder_names}')
# 	print(f'file names:{file_names}')

# os.rmdir('deleteit')									 #only used to remove empty directory

# os.makedirs(r'new\movies') 							 #used to make directory and subdirectories simultanously

# import shutil
# shutil.rmtree('new') 									 #it permanently deletes directory and its subdirectories containing files or folders inside
# shutil.copytree('new','helloworld')			 		 #it copies only tree structured files or folders to another directory present in current working directory
# shutil.copytree('new','newfolder/helloworld') 		 #copies tree inside helloworld folder
# shutil.copy('file.txt','documents') 		  			 #copy file into given directory
# shutil.copy('file.txt','documents/file1.txt') 			 #copy and rename file into given directory
# shutil.move('file.txt','documents/file2.txt')


# from PIL import Image
# img1=Image.open('../mypic.jpg')	#open an image
# img1.save('../mypic.png') 		#save pic with new name and location
# img1.show()						#show pic
# img1.thumbnail((50,50)) 			#change pic size
# img1.save('../mypicsized.jpg')	
# img1.show()


# import os
# from PIL import Image
# for item in os.listdir():
# 	img1=Image.open('../mypic.jpg')
# 	filename,extension=os.path.splitext(item) #split the folder name into name and extension
# 	img1.save(f'{filename}.png')



# import os
# from PIL import Image,ImageEnhance
# img1=Image.open('../mypic.jpg')
# enhancer=ImageEnhance.Sharpness(img1)
# enhancer.enhance(5).save('../mysharp.jpg')
# img1.show()
#0:blurry,1:original,2:image sharp...



# import os
# from PIL import Image,ImageEnhance
# img1=Image.open('../mypic.jpg')
# enhancer=ImageEnhance.Color(img1)	#making color object
# enhancer.enhance(4).save('../mycoloredpic.jpg')	#enhancecolor function
# img2=Image.open('../mycoloredpic.jpg')
# img2.show()



# import os
# from PIL import Image,ImageEnhance
# img1=Image.open('../mypic.jpg')
# enhancer=ImageEnhance.Brightness(img1)			#making brightness object
# enhancer.enhance(3.5).save('../mybrightpic.jpg')	#enhance brightnesss function
# img2=Image.open('../mybrightpic.jpg')
# img2.show()


# import os
# from PIL import Image,ImageEnhance
# img1=Image.open('../mypic.jpg')
# enhancer=ImageEnhance.Contrast(img1)			#making contrast object
# enhancer.enhance(1.5).save('../mycontrastpic.jpg')	#enhance contrast function
# img2=Image.open('../mycontrastpic.jpg')
# img2.show()



# import os
# from PIL import Image,ImageEnhance,ImageFilter
# img1=Image.open('../mypic.jpg')
# img1.filter(ImageFilter.GaussianBlur(raidus=4)).save('../myfilterpic.jpg')	#it will filter
# img2=Image.open('../myfilterpic.jpg')
# img2.show()



# import tkinter as tk 
# win=tk.Tk()

# from tkinter import *
# win=Tk()


# import os  													 #import module for accesing system files
# from csv import DictWriter									 #import module for accessing csv files
# import tkinter												 #import module to work on gui application	
# from tkinter import ttk 									 #import ttk for better gui applictions

# win=tkinter.Tk()											 #created object of tk class
# win.title('mywindow') 										 #write title in gui window

# #name_label=ttk.Label(win,text='enter your name:')			 #setting label properties	 
# #name_label.pack()											 #create label in middle

# name_label=ttk.Label(win,text='enter your name:')  			 #setting label properties
# name_label.grid(row=0,column=0,sticky=tkinter.W)			 #create label in left side
# name_variable=tkinter.StringVar()										 #store variable
# name_entrybox=ttk.Entry(win,width=16,textvariable=name_variable)	 	 #setting an input field and stores input into variable
# name_entrybox.grid(row=0,column=1)										 #create input field gui
# name_entrybox.focus()

# email_label=ttk.Label(win,text='enter your email:')  		 #setting label properties
# email_label.grid(row=1,column=0,sticky=tkinter.W)			 #create label in left side
# email_variable=tkinter.StringVar()										 #store variable
# email_entrybox=ttk.Entry(win,width=16,textvariable=email_variable)	 	 #setting an input field and stores input into variable
# email_entrybox.grid(row=1,column=1)										 #create input field gui

# age_label=ttk.Label(win,text='enter your age:')  			 #setting label properties
# age_label.grid(row=2,column=0,sticky=tkinter.W)				 #create label in left side
# age_variable=tkinter.StringVar()										 #store variable
# age_entrybox=ttk.Entry(win,width=16,textvariable=age_variable)	 	 #setting an input field and stores input into variable
# age_entrybox.grid(row=2,column=1)										 #create input field gui

# gender_label=ttk.Label(win,text='select your gender:')  			 #setting label properties
# gender_label.grid(row=3,column=0,sticky=tkinter.W)				 #create label in left side
# gender_variable=tkinter.StringVar()
# gender_combobox=ttk.Combobox(win,width=14,textvariable=gender_variable,state='readonly')
# gender_combobox['values']=('Male','Female','Other')	#values inside selection bar
# gender_combobox.current(0)	#it will show default value in the combobox which depends on argument number passed
# gender_combobox.grid(row=3,column=1)

# profession_variable=tkinter.StringVar()
# radiobtn1=ttk.Radiobutton(win,text='Student',value='Student',variable=profession_variable)
# radiobtn1.grid(row=4,column=0)
# radiobtn2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=profession_variable)
# radiobtn2.grid(row=4,column=1)

# checkbtn_variable=tkinter.IntVar()
# checkbtn=ttk.Checkbutton(win,text='check if you want to subscribe to our newsletter',variable=checkbtn_variable)
# checkbtn.grid(row=5,columnspan=3)

# def button_function():
# 	print(f'name : {name_variable.get()},\nage : {age_variable.get()},\nemail_id : {email_variable.get()}\n')	#print on screen

# 	if checkbtn_variable.get()==0:
# 		subscribed='NO'
# 	else:
# 		subscribed='YES'

# 	print(f'gender : {gender_variable.get()},\nprofession : {profession_variable.get()},\nsubscribed(yes or no)? : {subscribed}')

	
# 	with open('file.txt', 'w') as f:																				#write from application into a text file
# 		f.write(f'name : {name_variable.get()},\nage : {age_variable.get()},\nemail_id : {email_variable.get()}\ngender : {gender_variable.get()},\nprofession : {profession_variable.get()},\nsubscribed(yes or no)? : {subscribed}')

	
# 	with open('file.csv','w',newline='') as fcsv:																	#writing into csv files
# 		dict_writer=DictWriter(fcsv, fieldnames=['UserName','User Email Id','User Age','User Gender','User Profession','Subscribed'])
# 		if os.stat('file.csv').st_size==0:
# 			dict_writer.writeheader()
# 		else:
# 			dict_writer.writerow({
# 			'UserName':name_variable.get(),
# 			'User Email Id':email_variable.get(),
# 			'User Age':age_variable.get(),
# 			'User Gender':gender_variable.get(),
# 			'User Profession':profession_variable.get(),
# 			'Subscribed':subscribed
			
# 			})


# 	name_entrybox.delete(0,tkinter.END)	#to delete field values on submit
# 	age_entrybox.delete(0,tkinter.END)	
# 	email_entrybox.delete(0,tkinter.END)

# 	name_label.configure(foreground='Green')	#to change color of labels after submission
# 	email_label.configure(foreground='#b388ff')
# 	age_label.configure(foreground='Red')

# 	submit_button.configure(foreground='red')	#change button color after submission


# submit_button=ttk.Button(win,text='Submit',command=button_function)					#setting a button with text
# # submit_button=tkinter.Button(win,text='Submit',command=button_function)			#setting a button with text
# submit_button.grid(row=6,column=1)													#create a gui button 

# win.mainloop()																	     #create a gui window to infinite time until user close using cross button



# import tkinter as tk
# from tkinter import ttk
# win=tk.Tk()

# win.title('Loop Labels')

# labels=['name:','age:','gender:','country:','state:','city:']

# for i in range(len(labels)):
# 	cur_label=ttk.Label(win,text=labels[i])
# 	cur_label.grid(row=i,column=0,sticky=tk.W,padx=40,pady=10)
# name_var=tk.StringVar()

# user_info={
# 	'name':tk.StringVar(),
# 	'age':tk.StringVar(),
# 	'gender':tk.StringVar(),
# 	'country':tk.StringVar(),
# 	'state':tk.StringVar(),
# 	'city':tk.StringVar()
# 	}

# counter=0
# for i in user_info:
# 	cur_entrybox=ttk.Entry(win,width=16,textvariable=user_info[i])
# 	cur_entrybox.grid(row=counter,column=1,padx=40,pady=10)
# 	counter+=1

# def submit_function():
# 	for i in user_info:
# 		print(user_info[i].get())
	

# submit_btn=ttk.Button(win,text='Submit',command=submit_function)
# submit_btn.grid(row=6,columnspan=2)

# win.mainloop()



#create label frame
# import tkinter as tk
# from tkinter import ttk
# win=tk.Tk()

# win.title('Label Frame')

# label_frame=ttk.LabelFrame(win,text='enter your details below')	#used to create label frame
# label_frame.grid(row=0,column=0,padx=40,pady=40)

# labels=['name:','age:','gender:','country:','state:','city:']

# for i in range(len(labels)):
# 	cur_label=ttk.Label(label_frame,text=labels[i])
# 	# cur_label.grid(row=i,column=0,sticky=tk.W,padx=2,pady=2)
# 	cur_label.grid(row=i,column=0,sticky=tk.W)
# name_var=tk.StringVar()

# user_info={
# 	'name':tk.StringVar(),
# 	'age':tk.StringVar(),
# 	'gender':tk.StringVar(),
# 	'country':tk.StringVar(),
# 	'state':tk.StringVar(),
# 	'city':tk.StringVar()
# 	}

# counter=0

# for i in user_info:
# 	cur_entrybox=ttk.Entry(label_frame,width=16,textvariable=user_info[i])
# 	# cur_entrybox.grid(row=counter,column=1,padx=40,pady=10)
# 	cur_entrybox.grid(row=counter,column=1)
# 	counter+=1

# def submit_function():
# 	for i in user_info:
# 		print(user_info[i].get())
	
# submit_btn=ttk.Button(win,text='Submit',command=submit_function)
# submit_btn.grid(row=6,columnspan=2)

# for child in label_frame.winfo_children():
# 	child.grid_configure(padx=4,pady=4)

# win.mainloop()





#create notebook inside window
# import tkinter as tk
# from tkinter import ttk

# window=tk.Tk()

# window.title("Tab control")

# notebook=ttk.Notebook(window)		#create notebook object

# page1=ttk.Frame(notebook)			#create frame using notebook object
# notebook.add(page1,text='One')		#add frame 

# page2=ttk.Frame(notebook)
# notebook.add(page2,text='Two')

# #notebook.grid(row=0,column=0)					#create notebook grid
# notebook.pack(expand=True,fill='both')			#create pack that cover whole window

# label1=ttk.Label(page1,text='label:')	#add label
# label1.grid(row=0,column=0)
# entry1=ttk.Entry(page1,width=26)		#add input field
# entry1.grid(row=0,column=1)

# label2=ttk.Label(page2,text='label:')	#add label
# label2.grid(row=0,column=0)
# entry2=ttk.Entry(page2,width=26)		#add input field
# entry2.grid(row=0,column=1)

# window.mainloop()



#menu bar and dropdown with separator line
# import tkinter as tk
# from tkinter import ttk
# win=tk.Tk()
# win.title("menubar")

# menubar=tk.Menu(win)		#create menu object

# file_menu=tk.Menu(menubar,tearoff=0)	#create submenu using menu object
# def new_file():
# 	print('new file func called')
# file_menu.add_command(label='new file',command=new_file)  #add links to submenu
# def new_window():
# 	print('new window called')
# file_menu.add_command(label='new window',command=new_window)	
# file_menu.add_separator()										#add a line that separates upper menu contents
# def save_file():
# 	print('save file called')
# file_menu.add_command(label='save file',command=save_file)
# menubar.add_cascade(label='File', menu=file_menu)		#add popup menu cascade


# edit_menu=tk.Menu(menubar,tearoff=0)
# def undo_func():
# 	print('help func called')
# edit_menu.add_command(label='Undo',command=undo_func)
# edit_menu.add_separator()										#add a line that separates upper menu contents
# def redo_func():
# 	print('help func called')
# edit_menu.add_command(label='Redo',command=redo_func)
# menubar.add_cascade(label='Edit', menu=edit_menu)


# selection_menu=tk.Menu(menubar,tearoff=0)
# def new_file():
# 	print('new file func called')
# selection_menu.add_command(label='new file',command=new_file)
# def new_window():
# 	print('new window called')
# selection_menu.add_command(label='new window',command=new_window)
# selection_menu.add_separator()										#add a line that separates upper menu contents
# def save_file():
# 	print('save file called')
# selection_menu.add_command(label='save file',command=save_file)
# menubar.add_cascade(label='Selection', menu=selection_menu)


# view_menu=tk.Menu(menubar,tearoff=0)
# def new_file():
# 	print('new file func called')
# view_menu.add_command(label='new file',command=new_file)
# def new_window():
# 	print('new window called')
# view_menu.add_command(label='new window',command=new_window)
# view_menu.add_separator()										#add a line that separates upper menu contents
# def save_file():
# 	print('save file called')
# view_menu.add_command(label='save file',command=save_file)
# menubar.add_cascade(label='View', menu=view_menu)


# go_menu=tk.Menu(menubar,tearoff=0)
# def new_file():
# 	print('new file func called')
# go_menu.add_command(label='new file',command=new_file)
# def new_window():
# 	print('new window called')
# go_menu.add_command(label='new window',command=new_window)
# go_menu.add_separator()										#add a line that separates upper menu contents
# def save_file():
# 	print('save file called')
# go_menu.add_command(label='save file',command=save_file)
# menubar.add_cascade(label='Go', menu=go_menu)



# def debug_func():
# 	print('debug func called')
# menubar.add_command(label='Debug',command=debug_func)

# def terminal_func():
# 	print('terminal func called')
# menubar.add_command(label='Terminal',command=terminal_func)

# def help_func():
# 	print('help func called')
# menubar.add_command(label='Help',command=help_func)

# win.config(menu=menubar)			#add whole config into window
# win.mainloop()					#will run untill clicked on window cross button




#warning message box and exception handling
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox as m_box

# win=tk.Tk()

# label_frame=ttk.LabelFrame(win,text='Enter your details here')		#create labelframe border with text 
# label_frame.grid(row=0,column=0,padx=40,pady=20)

# name_label=ttk.Label(label_frame,text='Enter your name :', font=('',10))
# name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
# name_var=tk.StringVar()
# name_entry=ttk.Entry(label_frame,width=36,textvariable=name_var)
# name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)

# age_label=ttk.Label(label_frame,text='Enter your age :', font=('',10))
# age_label.grid(row=2,column=0,padx=5,pady=5,sticky=tk.W)
# age_var=tk.StringVar()
# age_entry=ttk.Entry(label_frame,width=36,textvariable=age_var)
# age_entry.grid(row=3,column=0,padx=5,pady=5,sticky=tk.W)

# def submit_func():
# 	name=name_var.get()
# 	age=age_var.get()

# 	if name=='' or age=='':
# 		m_box.showerror('Error','please enter the values')
# 	else:
# 		try:
# 			age=int(age)
# 		except ValueError:
# 			m_box.showerror('title','only numbers are allowed in age field')
# 		else:
# 			if age<18:
# 				m_box.showwarning('warning','you are not 18, visit this content on your own risk')
# 			print(f'your name is: {name} and age is : {age}')

# submit_btn=ttk.Button(win,text='Submit',command=submit_func)
# submit_btn.grid(row=1,columnspan=2,padx=40)

# win.mainloop()




#database operations using xammp control panel
# import mysql.connector			#package for database connections

# conn=mysql.connector.connect(host='localhost',username='root',password='', database='pythondb')	#to make database connections

# print(conn) 								#to check connection object

# my_cursor=conn.cursor()						#use cursor to traverse through data in the table

# query="CREATE DATABASE pythondb"			#sql query to create database

# query="SHOW DATABASES"					#sql query to show database

# query="CREATE TABLE test(name VARCHAR(255),age INT)"		#sql query to create a table

# query="INSERT INTO test(name,age) VALUES(%s,%s)"		#we use '?' in case of sqllite

# values=('ashwani',24)					#if wants to insert 1 value

# values=[								#if wants to insert many values at a time into table
# ('ashwani',20),	
# ('amit',21),
# ('rahul',22),
# ('pinky',23),
# ('monika',24)
# ]

# my_cursor.execute(query,values)				#to insert one row into table at once
# my_cursor.executemany(query,values)		#to insert many rows into table at once

# query="select * from test"

# my_cursor.execute(query)


# for database_name in my_cursor:		#to print all database names
# 	print(database_name)

# print(my_cursor.fetchall())			# print list of all database names inside

# my_cursor.execute(query)			#to execute query

# conn.commit()						#not necessery but it is a good practice to use it

# conn.close()						#to close the connection


#accessing arguments from command line
# import sys
# print(f"number of command line arguments:{len(sys.argv)} \n and list of command line arguments passed:{str(sys.argv)}")


#use of del keyword to delete variables
# var1=var2=var3="helloworld"
# print(var1)
# print(var2)
# print(var3)	
# del var1,var2,var3
# print(var1)
# print(var2)
# print(var3)


