# For Loop----

# for i in range(0,11):
#     print(i)

# for i in range(1,21):
#     if i %2 ==0:
#         print(i)

# for i in range(1,21):
#     if i %2 !=0:
#         print(i)

# num = 5

# for i in range(1,11):
#     print(num, "x", i, "=", num*i)

# total = 0

# for i in range(1,11):
#     total = total + i

# print("Total: ",total)

# num = 5
# fact = 1

# for i in range(1,num + 1):
#     fact = fact * i

# print("Factorial: ", fact)

# chars = "Python"

# for char in chars:
#     print(char)

# names = ["Aarti","Suraj","Tejas","Om","Yash","Yash"]

# for name in names:
#     print(name)

# num = [10,30,20,45,40,200,60,202,756]

# largest = num[0]

# for i in num:
#     if i > largest:
#         largest = i

# print("The Largest number: ", largest)

# text = "python programming"
# count = 0

# for char in text:
#     if char in "aeiou":
#         count += 1

# print("Number of vowels: ",count)

# While Loop-----

# i = 1
# while i <= 10:
#     print(i)
#     i+=1


# i = 1
# total = 0

# while i <=10:
#     total += i
#     i += 1

# print("Total: ",total)

# num = 12345
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num //= 10

# print("Reverse number: ", reverse)

# num = 123456

# count = 0

# while num > 0:
#     num //= 10
#     count += 1

# print("The nummber of digits: ", count)

# correct_number = 4

# guess = int(input("Enter a number: "))

# while guess != correct_number:
#     print("Wrong Number!!")

#     guess = int(input("Enter a number: "))

# print("Correct Guess!!")

# Loop Control Statements

# for i in range(20):
#     if i == 12:
#         break
#     print(i)

# for i in range(20):
#     if i == 12:
#         continue
#     print(i)


# x = 0
# while x < 5:
#     print(x)
#     x+=1

# def greet():
#     print("Hello Mister/Miss!!")

# greet()


# def greet():
#     name=input("Enter your name!: ")
#     print(f"Hello! {name}! How are you?")

# greet()

# def greet(name):
#     print(f"Hello! {name}! How are you?")

# greet("Veena")

# def greet(name="Guest"):
#     print(f"Hello! {name}! How are you?")

# greet("Veena")

# def welcome():
#     print("Welcome to the Professional Course!!")
#     print("Lets Learn Data Science!!")

# welcome()

# def age_verification():
#     age = int(input("Enter your age: "))

#     if age>=18:
#         print("Applicable for the License!!")
#     else:
#         print("Try Again Next Time")

# age_verification()

# def login(user_name):
#     password=input("Enter your Password: ")
#     while password != "Veen0000":
#         print("Wrong Password!")
#         password = input("Enter Your Password!: ")
        
#     else:
#         print(f"Hello! {user_name}")
# login("Veena")


# def add(a,b):
#     return a+b

# def multiply(x,y):
#     print(x*y)

# add(2,3)
# multiply(2,3)

# print("Add: ",add(2,3))
# print("Multiply: ", multiply(2,3))


# def student(name,age):
#     print(f"{name} is {age} years old!")

# student(age=27,name="Veena")

# def total_score(*marks):
#     print("Marks: ",marks)
#     print("Total Score: ",sum(marks))
#     import numpy as np
#     print("Percentage: ",np.mean(marks))
# total_score(85,97,99)


# def employee_details(**details):
#     for key,value in details.items():
#         print(key,":",value)

# employee_details(
#     Emp_name="Veena",
#     Age = 27,
#     Department="IT",
#     Salary = "10K"
# )