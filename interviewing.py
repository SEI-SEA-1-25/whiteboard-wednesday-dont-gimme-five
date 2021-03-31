user_input = input('Choose a language: english, spanish and french').lower()

languages = {
    'english': 'Hello!🤟🏼', 
    'spanish': 'Hola!🌸',
    'french': 'Bonjour!🍭'
}

for language in languages:
    if(user_input == language):
        print(languages[language])


# if user_input == 'english':
#     print('Hello!')
# elif user_input == 'spanish':
#     print('Hola!🌸')
# elif user_input == 'french':
#     print('Bonjour!🍭')
# else:
#     print('invalid input 🙅🏼‍♀️')