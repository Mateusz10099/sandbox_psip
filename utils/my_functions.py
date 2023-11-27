from bs4 import BeautifulSoup
import requests
import re
import folium

def update_user(users_list: list [dict,dict]) -> None:
 nick_of_user = input("Prosze o podanie pseudnimu użytkownika którego chcesz zmodyfikować ")
 print(nick_of_user)
 for user in users_list:
    if user['nick'] == nick_of_user:
     print("FOUND")
     user['name'] = input('Podaj nowe imie: ')
     user['nick'] = input('Podaj nowy pseudonim: ')
     user['posts'] = int(input('Podaj liczbe postow: '))
     user['city'] = input('Podaj miasto')

def add_user_to(users_list: list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imie ?')
    posts = input('podaj liczbe postów ?')
    city = input('podaj miasto?')
    users_list.append({'name': name, 'posts': posts})

def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """
    tmp_list = []
    name = input('podaj imie użytkownika do usunięcia: ')
    for user in users_list:
        if user["name"] == name:
            tmp_list.append(user)
    print(f'Znaleziono użytkowników :')
    print('0. Usuń wszystkich znalezionych użytkowników')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek+1}. {user_to_be_removed}')
    numer = int(input(f'wybierz numer użytkownika do usunięcia: '))
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer-1])

def show_users_from(users_list: list) -> None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]}')


# ============ MAPA

def get_coordinates_of(city: str) -> list[float, float]:
    # pobrane strony internetowe

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    # pobranie współrzędnych z treści strony internetowej

    response_html_latitude = (response_html.select('.latitude')[1].text)  # . ponieważ class
    response_html_latitude = float(response_html_latitude.replace(',', '.'))
    response_html_longitude = (response_html.select('.longitude')[1].text)  # . ponieważ class
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    return [response_html_latitude, response_html_longitude]


# for item in nazwy_miejscowosci:
#    print(get_coordinates_of(item))

user = {"city": 'Hrubieszów', "name": "Agata", "nick": "AAA", "posts": 1_0_000}


# zwrócić mapę z pinezką odnoszącą się do wskazanego na podstawie nazwy użytkownika podanej z klawiatury
def get_map_of(user: str) -> None:
    city = get_coordinates_of(user['city'])
    map = folium.Map(
        location=city,
        tiles="OpenStreetMap",
        zoom_start=14,
    )
    folium.Marker(
        location=city,
        popup=f'TU RZĄDZI {user["name"]},'
              f'postów: {user["posts"]}'
    ).add_to(map)
    map.save(f'mapka_{user["name"]}.html')


# zwróci mapę z wszystkimi użytkownikami z danej listy (znajomymi)

### RYSOWANIE MAPY

def get_map_of(users: list[dict,dict]) -> None:
    map = folium.Map(
        location=[52.3, 21.0],
        tiles="OpenStreetMap",
        zoom_start=14,
    )

    for user in users:
        folium.Marker(
            location=get_coordinates_of(city=user['city']),
            popup=f'Użytkownik: {user["name"]} \n'
                  f'Liczba postów {user["posts"]}'
        ).add_to(map)
    map.save('mapka.html')

#======== END OF ELEMENT ======

def gui(users_list: list)-> None:
    while True:
        print(f'MENU: \n'
            f'0: Zakończ program \n'
            f'1: Wyświetl użytkowników \n'
            f'2: Dodaj użytkownika \n'
            f'3: Usuń użytkownika \n'
            f'4: Modyfikuj użytkownika \n'
            f'5: Wygeneruj mapę z użytkownikiem \n'
            f'6: Wygeneruj mapę z wszystkimi użytkownikami \n'
            )
        menu_option = input('Podaj funkcję do wywołania')
        print(f'Wybrano funkcję {menu_option}')

        match menu_option:
            case'0':
                print('Kończę prace')
                break
            case'1':
                print('Wyświetlam listę użytkowników')
                show_users_from(users_list)
            case'2':
                print('Dodawanie użytkownika')
                add_user_to(users_list)
            case'3':
                print('Usuwanie użytkownika')
                remove_user_from(users_list)
            case'4':
                print('Modyfikuję użytkownika')
                update_user(users_list)
            case'5':
                print('Rysuj mapę z użytkownikiem')
                user = input('podaj nazwę użytkownika do modyfikazji')
                for item in users_list:
                    if item['nick'] == user:
                        get_map_one_user(item)
            case '6':
                print('Rysyję mapę z wszystkimi użytkownikami')
                get_map_of(users_list)




