# Code with Shinas 
# while loops in python
# while loop executes a set of statements as long as a condition is true.
# print 1 to 5 using while loop 


# n=1
# while n<=5:
#     print(n)
#     n+=1


# ask to inputh name until user inputs something 


# name=""
# while len(name)==0:
#     name=input("Enter your name? ")
# print("Hello",name)

# name=None
# while not name:
#        name=input("Enter your name? ")
# print("Hello",name)

# Write a program that asks the user to enter numbers continuously until they enter a negative 
# number. Then, the program should print the sum of all the entered numbers.

sum=0
num=0
while True:
    num=int(input("Enter Number: "))
    if num<0:
        break
    sum+=num
print("Sun of numbers:",sum)

# Write a program to find the factorial of a number using a while loop.
# num=int(input("Enter Value:"))
# f=1
# i=1
# while i<=num:
#     f*=i
#     i+=1

# print("!{} = {}".format(num,f))