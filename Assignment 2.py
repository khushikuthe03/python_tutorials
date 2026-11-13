# Q1.
# a=int(input("Enter first number :"))
# b=int(input("Enter second number :"))
# c=int(input("Enter third number :"))
# if a>b and a>c:
#     print("a is greater.")
# elif b>a and b>c:
#     print("b is greater.")
# else:
#     print("c is greater.")

# Q2.
# year=int(input("Enter the year: "))
# if year%400==0 or (year%4==0 and year%100!=0):
#     print("It is a leap year.")
# else:
#     print("It is not a leap year.")

#Q3.
# year=int(input("Enter the year: "))
# month=int(input("Enter the month: "))
# day=int(input("Enter the date:"))
# valid=False
# if 0<month<=12:
#     if month in[1,3,5,7,8,10,12] and 0<day<=31:
#         valid=True
#     elif month in[4,6,9,11] and 0<day<=30:
#         valid=True
#     elif month==2:
#         if year%400==0 or (year%4==0 and year%100!=0):
#          if 0<day<=29:
#           valid=True
#         else:
#            if 0<day<=28:
#             valid=True
# if valid==True:
#     print("Valid date.")
# else:
#     print("Invalid date.")
 
# Q4.
# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))
# c=int(input("Enter value of c: "))
# D=(b*b)-(4*a*c)
# print("Discriminant= ",D)
# if D>0:
#     print("Root 1=",(-b-(D**(1/2)))/(2*a))
#     print("Root 2=",(-b+(D**(1/2)))/(2*a))
# elif D==0:
#     print("Root=",(-b)/(2*a))
# elif D<0:
#     print("Root 1=",(-b-(D**(1/2)))/(2*a))
#     print("Root 2=",(-b+(D**(1/2)))/(2*a))

# Q5.
# a="ABCDEFGH"
# result=""
# for i in range(len(a)): 
#  if i%3!=0:
#     result=result+a[i]
# print("Result=",result)

# Q6.
# current=0
# maximum=0
# previous=None
# while True:
#     a=int(input())
#     if a==0:
#         break
#     if a==previous:
#         current=current+1
#     else:
#         current=1
#     if current>maximum:
#         maximum=current
#     previous=a
# print("Maximum times the number occured=",maximum)

# Q7.
# N,K=map(int,input().split())
# pins=["I"]*N
# for i in range(K):
#     start,stop=map(int,input().split())
#     for j in range(start-1,stop):
#         pins[j]="."
# print("".join(pins))

# Q8.
h1=int(input("Enter time in hours:"))
m1=int(input("Enter time in minutes:"))
s1=int(input("Enter time in seconds:"))
h2=int(input("Enter time in hours:"))
m2=int(input("Enter time in minutes:"))
s2=int(input("Enter time in seconds:"))
t1=(h1*3600)+(m1*60)+(s1)
t2=(h2*3600)+(m2*60)+(s2)
print("Difference in seconds=",t2-t1)