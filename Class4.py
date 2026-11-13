# Q1.Reverse
# n=int(input("Enter a number:"))
# while n>=1:
#     print(n)
#     n-=1
# OR
# for i in range(n,0,-1):
#     print(i)
# OR
# while True:
#     if n<1:
#         break
#     print(n)
#     n=n-1

# Q2.Prime
# n=int(input("Enter a number:"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print("Prime number")
# else:
#     print("Not a prime number.")

# Q3.sum n avg
# n=int(input("Enter a number:"))
# sum=0
# i=0
# while i<=n:
#     sum=sum+i
#     i=i+1
#     average=sum/n
# print("Sum=",sum)
# print("Average=",average)

# Q4.multiple 
# num=int(input("Enter a number:"))
# n=int(input("Enter the number of multiples:"))
# i=1
# while i<=n:
#     mul=num*i
#     i=i+1
#     print(mul)

# Q5.Fibonacci
# n=int(input("Enter a number: "))
# a=0
# b=1
# i=1
# while i<=n:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     i=i+1
# OR
# n=int(input("Enter a number:"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c
# OR
# n=int(input("Enter a number:"))
# previous=0
# next=1
# for i in range(n):
#     print(previous)
#     temp=previous+next
#     previous=next
#     next=temp

# Q6.sum of digits
n=int(input("Enter a number:"))
i=0
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("Sum of digits=",sum)
