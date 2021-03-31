# input english spanish french -> one word 
# output greet msg


# user input - your language
user_input = input("What's your language?\n").lower()

# languages storage -> e s f
dictionary = {
    "english": "Hello",
    "spanish": "Hola",
    "french": "Bonjour"
}

print(dictionary[user_input])







# condition to see if user input is exist in the storage 
# if yes - print greet msg
# if user_input not in language_storage:
#     print(f"Sorry I don't speak {user_input}")
# elif user_input == "english":
#     print("Hello")
# elif user_input == "spanish":
#     print("Hola")
# elif user_input == "french":
#     print("Bonjour")


    
    













# if not - Sorry I don't know how to speak {language}
