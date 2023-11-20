print("Fun fact: The cracking sound a bullwhip makes when properly wielded is, in fact, a small sonic boom. The end of the whip, known as the cracker, moves faster than the speed of sound, thus creating a sonic boom. "
      "The whip is probably the first human invention to break the sound barrier.")
from dane import users_list

def update_user(users_list: list [dict,dict]) -> None:
 nick_of_user = input("Prosze o podanie pseudnimu użytkownika którego chcesz zmodyfikować ")
 print(nick_of_user)
 for user in users_list:
    if user['nick'] == nick_of_user:
     print("FOUND")
     user['name'] = input('Podaj nowe imie: ')
     user['nick'] = input('Podaj nowy pseudonim: ')
     user['posts'] = int(input('Podaj liczbe postow: '))

update_user(users_list)
for user in users_list:
         print(user)
