import psycopg2 as ps
from dane import users_list

db_params = ps.connect(
    database="postgres",
    user= "postgres",
    password= "Monika",
    host= "localhost",
    port= 5433
)

cursor = db_params.cursor()

def dodaj_uzytkownika(user:str):
    for nick in users_list:
        if user == nick['nick']:
            sql_query_1 = f"INSERT INTO public.snapchat(city, name, nick, posts) VALUES ('{nick['city']}', '{nick['name']}', '{nick['nick']}', '{nick['posts']}');"
            cursor.execute(sql_query_1)
            db_params.commit()
dodaj_uzytkownika(input('dodaj uzytkownika '))

# def usun_uzytkownika(user:str):
#     sql_query_1 = sqlalchemy.text(f"DELETE FROM public.my_table where name = '{user}';")
#     connection.execute(sql_query_1)
#     connection.commit()
# #cwok='stasiu'
# #usun_uzytkownika(cwok)
#
# def aktualizuj_uzytkownika(user_1:str,user_2:str):
#     sql_query_1 = sqlalchemy.text(f"UPDATE pulic.my_table set name = '{user_1}' where name = '{user_2}';")
#     connection.execute(sql_query_1)
#     connection.commit()
# aktualizuj_uzytkownika(
#     user_1=input('na kogo zamienic'),
#     user_2=input('kogo zamienic')
# )

#connection.execute(sql_query_1)
#connection.commit()

# ----------------------------------------------------------------------------------------------------------------------

# engine = sqlalchemy.create_engine(db_params)
# connection= engine.connect()
# sql_query_1=sqlalchemy.text("INSERT INTO public.my_table(name) VALUES('kepa');")
# sql_query_1=sqlalchemy.text("select * from public.my_table;")
# user = input('podaj nazwę zawodnika do usunięcia')
# sql_query_1=sqlalchemy.text(f"DELETE FROM public.my_table where name='{user}';")
# kogo_zmienic=input('podaj kogo zmienic')
# na_kogo=input('podaj na kogo zamienic')
# sql_query_1=sqlalchemy.text(f"update public.my_table set name='{na_kogo}' where name = '{kogo_zamienic}';")