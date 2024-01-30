print("Hello! I am StreetGlow's personal AI assistant. How may I assist you with a return or exchange?")

name = input("Please enter your name: ") 
# exchange or return ? 
print("What would you like to be assisted with today?")
print("1. Returns")
print("2. Exchanges")
print("3. Exit Chatbot ")
 
choose_option = input("Please enter the number of choice 1-3: ")
#return
if choose_option == "1":
 print("How many days has it been since your last purchase?")
 return_days = int(input("Please enter the number of days: "))
# return validation
 if return_days <= 30:
   print("Thank you for your patience. We will process your return within the next 24 hours.")
 else:
   print("Your order is invalid of being returned more than 30 days after purchase. Please contact our customer service for assistance.")
#exchange   
elif choose_option == "2":
  print("How many days has it been since your order has arrived?")
  exchange_days = int(input("Please enter the number of days: "))
  # exchange validation
  if exchange_days <= 30:
    print("Thank you for your patience. We will process your exchange within the next 24 hours.")
    
elif choose_option == "3":
  print(f"Thank you for using our chatbot, {name}! Have a great day!")
  exit()
else:
  print("Invalid option. Please try again.")

# ask for order number
order_number = input("Please enter your order number, a 10-digit number: ")