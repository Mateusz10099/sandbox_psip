# BEAUTIFULSOUP4

from bs4 import BeautifulSoup
import requests
import re
import folium

#-*- coding: utf-8 -*- TO JEST KOD NA ZAMIANĘ ZNAKÓW POLSKICH

nazwy_miejscowosci = ['Opoczno','Lublin','Gdańsk']
def get_coordinates_of(city:str)->list[float,float]:
    # pobrane strony internetowe

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    # pobranie współrzędnych z treści strony internetowej

    response_html_latitude = (response_html.select('.latitude')[1].text) # . ponieważ class
    response_html_latitude = float(response_html_latitude.replace(',','.'))
    response_html_longitude = (response_html.select('.longitude')[1].text) # . ponieważ class
    response_html_longitude = float(response_html_longitude.replace(',','.'))

    return [response_html_latitude, response_html_longitude]

#for item in nazwy_miejscowosci:
#    print(get_coordinates_of(item))

# zwrócić mapę z pinezką odnoszącą się do wskazanego na podstawie nazwy użytkownika podanej z klawiatury

# zwróci mapę z wszystkimi użytkownikami z danej listy (znajomymi)

### RYSOWANIE MAPY

city= get_coordinates_of(city='Zamość')
map = folium.Map(
    location=city,
    tiles="OpenStreetMap",
    zoom_start=14,
    )

for item in nazwy_miejscowosci:
    folium.Marker(
        location=get_coordinates_of(city=item),
        popup='GEOINFORMATYKA RZĄDZI OU YEEEEEEAAAAH'
    ).add_to(map)
map.save('mapka.html')