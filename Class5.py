# import random
# print("=====ROCK,PAPER,SCISSORS=====")
# print("1.Rock")
# print("2.Paper")
# print("3.Scissors")
# comp=random.randint(1,3)
# user=int(input("Enter ur choice from 1-3:"))
# print("Computer's choice:",comp)

# if user==1 and comp==2:
#     print("Computer wins")
# elif user==1 and comp==3:
#     print("User wins")
# elif user==2 and comp==1:
#     print("User wins")
# elif user==2 and comp==3:
#     print("Computer wins")
# elif user==3 and comp==1:
#     print("User wins")
# elif user==3 and comp==2:
#     print("User wins")
# elif user==comp:
#     print("Tie")
# else:
#     print("Invalid input")

# Q.Star
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# Q.1.
# yr=int(input("Enter the year:"))
# if yr%400==0 or (yr%4==0 and yr%100!=0):
#     print("Leap year.")
# else:
#     print("Not a leap year.")

# Q2.
# time=float(input("Enter number of hours browsed:"))
# bill=0
# if time<=0:
#     bill=0
# elif time<=0.5:
#     bill=10
# elif time<=1:
#     bill=20
# else:
#     bill=100
# print("Bill=",bill)

# Q3.
temp=input("Enter temp in warm or cold:")
humidity=input("Enter humidity in humid or dry:")
if temp=="Warm":
    if humidity=="Dry":
        print("Play Basketball")
    elif humidity=="Humid":
        print("Play Tennis")
if temp=="Cold":
    if humidity=="Dry":
        print("Play cricket")
    elif humidity=="Humid":
        print("Swim")

# Q4.
# n=int(input("Enter a number:"))
# if n%10==5:
#     square=n*n
#     print("Square=",square)
# else:
#     print("Significant figure is not 5.")

# Q5.
# age=int(input("Enter your age:"))
# if age<18 and age>15:
#     print("U can enroll.")
# else:
#     print("U can't enroll.")



    