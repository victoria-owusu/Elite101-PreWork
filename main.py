print("Hello! How may I assist you today?")

name = input("Please enter your name: ") 

age = input("What a special name! How old are you? ")

print("Oh what a wonderful age! What would you like to be assisted with today?")
print("1. Placeholder Option 1 ")
print("2. Placeholder Option 2 ")
print("3. Placeholder Option 3 ")
print("4. Exit Chatbot ")

while True: 
  choose_option = input("Please enter the number of choice 1-4: ")
  
  if choose_option == "1":
    print("Placeholder Option 1")
  elif choose_option == "2":
    print("Placeholder Option 2")
  elif choose_option == "3":
    print("Placeholder Option 3")
  elif choose_option == "4":
    print(f"Thank you for using our chatbot, {name}! Have a great day!")
    break
  else:
    print("Invalid option. Please try again.")
  