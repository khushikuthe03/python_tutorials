# Q1
# a=2
# b=9
# c=4
# if a>b and a>c: 
#     print("a")
# elif c>a and c>b:
#     print("c")
# else:
#     print("b")

# Q2.
# a=int(input("Enter ur age:"))
# if a>=18:
#     print("Ur are eligible for voting")
# else:
#     print("U cant vote.")
# if a>=21:
#     print("U can marry")
# else:
#     print("u cant marry")

# Q3.
# a=int(input("Enter ur income:"))
# tax=0
# if a<=250000:
#     print("No tax")
# elif 500000>=a>250000:
#     print("5% tax applied")
#     tax=(5/100)*(a-250000)
#     print("tax=",tax)
# elif 750000>=a>500000:
#     print("10% tax for above 5 lakhs and 5% tax for above 2.5 lakhs. ")
#     tax=((10/100)*(a-500000))+12500
#     print("tax=",tax)
# elif a>750000:
#     print("15% tax for above 7.5 lkhs and 10% tax for above 2.5 lkhs.")
#     tax=((15/100)*(a-750000))+12500+25000
#     print(tax)

# Q4.Fibonacci 
n=int(input("enter num"))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c

