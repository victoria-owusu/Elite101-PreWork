print("Hello! I am StreetGlow's personal AI assistant. How may I assist you with a return or exchange?")

name = input("Please enter your name: ") 

print("What would you like to be assisted with today?")
print("1. Returns")
print("2. Exchanges")
print("3. Exit Chatbot ")

while True: 
  choose_option = input("Please enter the number of choice 1-3: ")
  
  if choose_option == "1":
   print("How many days has it been since your last purchase?")
   return_days = int(input("Please enter the number of days: "))
  elif choose_option == "2":
    exchange_days = print("How many days has it been since your last purchase?")
  elif choose_option == "3":
    print(f"Thank you for using our chatbot, {name}! Have a great day!")
    break
  else:
    print("Invalid option. Please try again.")
  