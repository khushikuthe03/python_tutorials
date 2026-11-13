# atm_pin="1234"
# count=3

# while count>0:
#     pin=input("Enter your pin:")
#     if pin!=atm_pin:
#         print("Incorrect pin.")
#         count=count-1
#     else:
#         print("Pin verified.")
#         break
# if count==0:
#     print("Your card has been blocked.")
    
# balance=2000
# atm_pin=1234

# print("======ATM MENU======")
# print("1.Balance Enquiry")
# print("2.Cash Withdrawal")
# print("3.Deposit Money")
# print("4.Change pin")
# print("5.Exit")

# choice=int(input("Enter your choice:"))
# if choice==1:
#     print("Balance amount=",balance)
# elif choice==2:
#     amount=int(input("Enter your withdrawal amount:"))
#     if amount>0:
#         if amount<=balance:
#                 balance=balance-amount
#                 print("Withdrawal successful.")
#                 print("Remaining balance=",balance)
#         else:
#                 print("Amount insufficient.")
#     else:
#           print("Invalid amount.")

# elif choice==3:
#         amount=int(input("Enter amount to be deposited:"))
#         if amount>0:
#             balance=balance+amount
#             print("Deposit successful.")
#             print("Updated balance=",balance)
#         else:
#               print("Invalid amount.")

# elif choice==4:
#     pin=int(input("Enter new pin:"))
#     if 10000>pin>999:
#         atm_pin=pin
#         print("Your new pin is set successfully.")

#     else:
#          print("Invalid pin.")

# elif choice==5:
#     print("Thank you")

atm_pin="123"
count=3

while count>0:
    pin=input("Enter pin:")
    if pin!=atm_pin:
        print("Incorrect pin")
        count=count-1
    else:
        print("Pin verified")
        break
if count==0:
    print("Ur card has been blocked.")

balance=5000

print("=====ATM MENU=====")
print("1.Balance Inquiry")
print("2.Cash Withdrawal")
print("3.Deposit Money")
print("4.Change pin")
print("5.Exit")

choice=int(input("Enter choice from 1-4:"))

if choice==1:
    print("Available balance:",balance)
elif choice==2:
    amount=input("Enter amount to be withdrawn:")
    if amount>0:
        if amount<=balance:
            balance=balance-amount
            print("The remaining balance=",balance)
        else:
            print("Invalid amount")
elif choice==3:

        
     



