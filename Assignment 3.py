# Q1.
# n=int(input("Enter a number:"))
# i=1
# while i<=n:
#     print(i)
#     i=i+1

# Q2.
# n=int(input("Enter a number:"))
# fact=1
# i=1
# while i<=n:
#     fact=fact*i
#     i=i+1 
# print("Factorial=",fact)

# Q3.
# n=int(input("Enter a number:"))
# while n>=1:
#     print(n)
#     n=n-1

# Q4.
# n=int(input("Enter a number:"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print("Prime number")
# else:
#     print("Not a prime number.")

# Q5.
# n=int(input("Enter a number:"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
#     average=sum/n
# print("Sum=",sum)
# print("Average=",average)

# Q6.
# num=int(input("Enter the number:"))
# n=int(input("Enter the number of multiples:"))
# i=1
# while i<=n:
#     mul=num*i
#     print(mul)
#     i=i+1

# Q7.
# n=int(input("Enter a number:"))
# previous=0
# next=1
# for i in range(n):
#     print(previous)
#     temp=previous+next
#     previous=next
#     next=temp

# Q8.
n=int(input("Enter the number:"))
sum=0

while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("Sum of digits=",sum)