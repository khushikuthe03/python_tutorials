# Armstrong no.      153=1^3 + 5^3 +3^3=153
#  star pattern 5star,4 star,...

# factorial
# fact=1
# i=1
# num=int(input("Enter a number:"))
# while i<=num:
#     fact=fact*i
#     i=i+1
# print("Factorial=",fact)

# Armstrong
# num=int(input("Enter a number:"))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10
# if sum==num:
#     print("Armstrong no.")
# else:
#     print("Not armstrong no.")

num=int(input("Enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==num:
    print("Armstrong no.")
else:
    print("Not")

    


