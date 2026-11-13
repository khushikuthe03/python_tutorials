# Q1:
# r=float(input("Enter the radius of circle: "))
# b=float(input("Enter the base of triangle: "))
# h=float(input("Enter the height of triangle: "))

# print("Area of circle =",3.14*r*r) 
# print("Area of triangle =",0.5*b*h)

# Q2:
# a=10
# b=20
# # print("a: ",a,"b: ",b)
# # a,b=b,a
# # print("a: ",a,"b: ",b)

# a=10
# b=20
# def swap(a,b):
#     print(f"a before swap= {a} and b before swap= {b}")
#     temp=a
#     a=b
#     b=temp
#     print(f"a after swap= {a} and b after swap= {b}")
# swap(a,b)

# Q3:
# import random
# a=random.randint(1,50)
# print("Random number:",a) 

# Q4:
# 1km=0.62 miles
# 1mile=1.6 km
# km=float(input("Enter distance in km:"))
# miles=km*0.621
# print("Distance in miles is:",miles) 

# Q5:
# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))

# if a>b:
#     print("a is greater.")
# elif a<b:
#     print("b is greater.")
# else:
#     print("both are equal")


# # Q6:
# a=int(input("Enter the number: "))
# if a%2==0:
#     print("The number is even.")
# else:
#     print("The number is odd.") 

# Q7:
# a=float(input("Enter the number:"))
# if a>0:
#     print("The number is positive.")
# elif a<0:
#     print("The number is negative.")
# else:
#     print("The number is zero.") 

# Q8:
# c1=int(input("Enter students in class1: "))
# c2=int(input("Enter students in class2: "))
# c3=int(input("Enter students in class3: "))
# a=(c1+1) //2
# b=(c2+1) //2
# c=(c3+1) //2
# print(f"The total number of desks are {a+b+c}.")

# print("Number of desks required in c1 are:",a)
# print("Number of desks required in c2 are:",b)
# print("Number of desks required in c3 are:",c)

# #Q9:
# h=int(input("Enter time in hours: "))
# m=int(input("Enter time in minutes: "))
# s=int(input("Enter time in seconds: "))
# angle= (h*30) + (m*(1/2)) + (s*(1/120))
# print(angle)

# Q10:
# x1=int(input("x1:"))
# x2=int(input("x2:"))
# x3=int(input("x3:"))
# y1=int(input("y1:"))
# y2=int(input("y2:"))
# y3=int(input("y3:"))
# if x1==x2:
#     x4=x3
# elif x1==x3:
#     x4=x2
# else:
#     x4=x1
# if y1 == y2:
#      y4 = y3
# elif y1 == y3:
#       y4 = y2
# else:
#     y4 = y1
# print(f"Fourth vertex:({x4},{y4})")

#Q11:
N = int(input("Enter number of cards: "))
sum = 0
for i in range(N - 1):
    num = int(input("Enter remaining number on card: "))
    sum = sum + num
total = (N * (N + 1)) // 2
lost = total - sum
print("Lost number is:",lost)


