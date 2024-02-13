print("Hello! I am StreetGlow's personal AI assistant. How may I assist you with a return or exchange?")

name = input("Please enter your name: ") 
# exchange or return ? 
print("What would you like to be assisted with today?")
print("1. Returns")
print("2. Exchanges")
print("3. Exit Chatbot ")
print("")
 
choose_option = input("Please enter the number of choice 1-3: ")
#return
if choose_option == "1":
 print("How many days has it been since your last purchase?")
 return_days = int(input("Please enter the number of days: "))
 print("")
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
    print("")
    
elif choose_option == "3":
  print(f"Thank you for using our chatbot, {name}! Have a great day!")
  exit()
else:
  print("Invalid option. Please try again.")
  print("")

# ask for order number
order_number = int(input("Please enter your order number, a 5-digit number: "))
if order_number > 9999 and order_number < 100000:
  print("Alright, thank you for your order number.")
  print("Processing........")
  print("Order number confirmed.")
  print("")
else: 
  print("Invalid order number. Please try again.")
  order_number = int(input("Please enter your order number, a 5-digit number: "))
  print("")

# Choose a reason fo return
print("Please choose a reason for your request:")
print("1. Item is defective")
print("2. Item is damaged")
print("3. Item is not as described")
print("4. Item is not the correct size")
print("5. Item is not the correct color")
print("6. Item is not the correct material")
print("7. Other")
print("")

reason_for_request = input("Please enter the number of choice 1-7: ")
print("")

if reason_for_request == "1":
  description = input("Please provide a description of the defective item.")
  print("Processing........")
  print("Thank you for your patience. We will process your request within the next 24 hours.")
  print("")
elif reason_for_request == "2":
  description = input("Please provide a description of the damaged item.")
  print("Processing........")
  print("Thank you for your patience. We will process your request within the next 24 hours.")
  print("")
elif reason_for_request == "3":
  description = input("Please provide a description of the item that is not as described.")
  print("Processing........")
  print("Thank you for your patience. We will process your request within the next 24 hours.")
  print("")
elif reason_for_request == "4":
  description = input("Please provide a description of the item that is not the correct size.")
  print("Processing........")
  print("Thank you for your patience. We will process your request within the next 24 hours.")
  print("")
elif reason_for_request == "5":
  description = input("Please provide a description of the item that is not the correct color.")
  print("Processing........")
  print("Thank you for your patience. We will process your request within the next 24 hours.")
  print("")
elif reason_for_request == "6":
  description = input("Please provide a description of the item that is not the correct material.")
  print("Processing........")
  print("Thank you for your patience. We will process your request within the next 24 hours.")
  print("")
elif reason_for_request == "7":
  description = input("Please provide a description of the other reason for your request.")
  print("Processing........")
  print("Thank you for your patience. We will process your request within the next 24 hours.")
  print("")
else:
  print("Invalid option. Please try again.")
  reason_for_request = input("Choose option from 1-7: ")
  print("")

# ask for contact information
print("Please enter the following information to contact you:")
email = input("Please enter your email address: ")
phone_number = input("Please enter your phone number: ")
print("")

# ask for payment information
payment_method = input("Are you going to use the same payment method? Answer yes or no")
if payment_method == "yes" or payment_method == "Yes":
  print("Okay, we'll proceed with your previous payment method.")
  print("")

elif payment_method == "no" or payment_method == "No":
  print("Please enter the following information to use for payment:")
  card_number = input("Please enter your card number: ")
  card_expiration_date = input("Please enter your card expiration date: ")
  card_cvv = input("Please enter your card CVV: ")
  print("Processing........")
  print("Thank you for re-confirming your payment information!")
  print("")

else:
  print("Invalid option. Please try again.")
  payment_method = input("Are you going to use the same payment method? Answer yes or no")

# step-by-step guide on returning/exchanging

if choose_option == "1":
  print("")
  print("******How to return a product: ******")
  print("1. Download or Print Return Label")
  print("Please print or download the return label provided by the online store. Attach it to the package securely.")
  print("")
  print("2. Pack the Item ")
  print("Pack the item securely in its original packaging if possible. Include any accessories, tags, or documentation that came with the product.")
  print("")
  print("3. Ship the Package")
  print("Ship the package to the store where you received it. Ensure that the package is in the correct condition and in.")
  print("4. Await Confirmation and Refund")
  print("")
  print("You should receive an email confirmation once the return is completed, and the refund should follow according to the store's policy.")
  print("Thank you for using our chatbot. Have a great day!")
  exit()

elif choose_option == "2":
  print("")
  print("******How to exchange a product: ******")
  print("1. Choose Replacement Item")
  print("Choose the item that you want to replace from the online store.")
  print("")
  print("2. Download or Print Return Label")
  print("Please print or download the return label provided by the online store. Attach it to the package securely.")
  print("")
  print("3. Pack the Item ")
  print("Pack the item securely in its original packaging if possible. Include any accessories, tags, or documentation that came with the product.")
  print("")
  print("4. Ship the Package")
  print("Ship the package to the store where you received it. Ensure that the package is in the correct condition and in.")
  print("")
  print("5. Receive the Replacement Item")
  print("Expect to receive the replacement item. Confirm that it meets your expectations.")
  print("")
  print("Thank you for using our chatbot. Have a great day!")
  

  
  
