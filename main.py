users_list:list = [
    {"name":"Marek", "nick":"major","posts":100},
    {"name":"Mateusz", "nick":"świetlik","posts":60},
    {"name":"Bartosz", "nick":"Baran","posts":31231},
    {"name":"Kamil", "nick":"Koc","posts":123},
    {"name":"Marek", "nick":"Wisse","posts":0},
    {"name":"Wiktoria", "nick":"Witka","posts":34},
    {"name":"Wiktoria", "nick":"Wiki","posts":360},
    {"name":"Monika", "nick":"Monia","posts":100_000_000},
    {"name":"Kasia", "nick":"Kkk","posts":1_500}
]

for user in users_list:
    print(f'Twój znajomy {user["name"]} dodał {user["posts"]} postów')

#print(f'Twój znajomy {users_list[0]["nick"]} opublikował {users_list[0]["posts"]}!!!')