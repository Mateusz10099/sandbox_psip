import psycopg2 as ps
import requests as rq
from bs4 import BeautifulSoup
import folium

db_params = ps.connect(
    database="postgres",
    user= "postgres",
    password= "Monika",
    host= "localhost",
    port= 5433
)
cursor = db_params.cursor()

def add_user_to() -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    city = input('podaj miasto: ')
    name = input('podaj imie: ')
    nick = input('podaj nick: ')
    posts = input('podaj liczbe postów: ')
    sql_query_1 = f"INSERT INTO public.snapchat(city, name, nick, posts) VALUES ('{city}', '{name}', '{nick}', '{posts}');"
    cursor.execute(sql_query_1)
    db_params.commit()

def remove_user_from() -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imie użytkownika do usunięcia: ')
    sql_query_1 = f"SELECT * FROM public.snapchat WHERE name='{name}';"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    print(f'Znaleziono użytkowników :')
    print('0. Usuń wszystkich znalezionych użytkowników')
    for numerek, user_to_be_removed in enumerate(query_result):
        print(f'{numerek+1}. {user_to_be_removed}')
    numer = int(input(f'wybierz numer użytkownika do usunięcia: '))
    if numer == 0:
        sql_query_2 = f"DELETE * FROM public.snapchat;"
        cursor.execute(sql_query_2)
        db_params.commit()
    else:
        sql_query_2 = f"DELETE FROM public.snapchat WHERE id='{query_result[numer - 1][0]}';"
        cursor.execute(sql_query_2)
        db_params.commit()

def show_users_from() -> None:
    sql_query_1 = f"SELECT * FROM public.snapchat;"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    for row in query_result:
        print(f'Twoj znajomy {row[2]} opublikowal {row[4]} postow')

def update_user() -> None:
    nick_of_user = input("Prosze o podanie pseudnimu użytkownika którego chcesz zmodyfikować ")
    sql_query_1 = f"SELECT * FROM public.snapchat WHERE nick='{nick_of_user}';"
    cursor.execute(sql_query_1)
    print('Odnaleziono')
    city = input('podaj nowe miasto: ')
    name = input('podaj nowe imie: ')
    nick = input('podaj nowy nick: ')
    posts = input('podaj liczbe postow: ')
    sql_query_2 = f"UPDATE public.snapchat SET city='{city}', name='{name}', nick='{nick}', posts='{posts}' WHERE nick='{nick_of_user}';"
    cursor.execute(sql_query_2)
    db_params.commit()

# ========================================= MAPA ============================================ #
def get_coordinates_of(city:str) -> list[float, float]:
    # pobranie strony internetowe
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'
    response = rq.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    # pobranie współrzędnych z treści strony internetowej
    response_html_latitude = (response_html.select('.latitude')[1].text)  # . ponieważ class
    response_html_latitude = float(response_html_latitude.replace(',', '.'))
    response_html_longitude = (response_html.select('.longitude')[1].text)  # . ponieważ class
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    return [response_html_latitude, response_html_longitude] # zwrócić mapę z pinezką odnoszącą się do wskazanego na podstawie nazwy użytkownika podanej z klawiatury

def get_map_one_user() -> None:
    city = input('Podaj miasto uzytkownika: ')
    sql_query_1 = f"SELECT * FROM public.snapchat WHERE city='{city}';"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    if not query_result:
        print(f'Nie ma tego miasta w bazie')
        return
    city = get_coordinates_of(city)
    map = folium.Map(location=city,
                     tiles="OpenStreetMap",
                     zoom_start=14,
    ) # location to miejsce wycentrowania mapy
    for user in query_result:
        folium.Marker(location=city,
                      popup=f"Użytkownik: {user[2]}\n"
                      f'Liczba postow: {user[4]}'
    ).add_to(map)
    map.save(f'mapka_{query_result[0][1]}.html') # zwróci mapę z wszystkimi użytkownikami z danej listy (znajomymi)

### RYSOWANIE MAPY
def get_map_of() -> None:
    map = folium.Map(location=[52.3, 21.0],
                     tiles="OpenStreetMap",
                     zoom_start=7,
    ) # location to miejsce wygenerowania mapy
    sql_query_1 = f"SELECT * FROM public.snapchat;"
    cursor.execute(sql_query_1)
    query_result=cursor.fetchall()
    for user in query_result:
        folium.Marker(location=get_coordinates_of(city=user[1]),
                      popup=f'Użytkownik: {user[2]}\n'
                      f'Liczba postów: {user[4]}'
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
        menu_option = input('Podaj funkcję do wywołania: ')
        print(f'Wybrano funkcję {menu_option}')

        match menu_option:
            case'0':
                print('Kończę prace')
                break
            case'1':
                print('Wyświetlam listę użytkowników')
                show_users_from()
            case'2':
                print('Dodawanie użytkownika')
                add_user_to()
            case'3':
                print('Usuwanie użytkownika')
                remove_user_from()
            case'4':
                print('Modyfikuję użytkownika')
                update_user()
            case'5':
                print('Rysuj mapę z użytkownikiem')
                get_map_one_user()
            case '6':
                print('Rysyję mapę z wszystkimi użytkownikami')
                get_map_of()

def pogoda_z(miasto: str):
    url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
    return rq.get(url).json()

class User:
    def __init__(self, city, name, nick, posts):
        self.city = city
        self.name = name
        self.nick = nick
        self.posts = posts
    def pogoda_z(self, miasto:str):
        url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
        return rq.get(url).json()

npc_1 = User(city='Sopot', name='krzysiek', nick='krycha', posts=200)
npc_2 = User(city='Koszalin', name='basia', nick='bara', posts=500)
print(npc_1)
print(npc_2)
print(npc_1.pogoda_z(npc_1))
print(npc_2.pogoda_z(npc_2))