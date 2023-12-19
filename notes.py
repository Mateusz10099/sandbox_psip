import sqlalchemy

db_params = sqlalchemy.URL.create(
    drivername="postgresql+psycopg2",
    username= "postgres",
    password= "Monika",
    host= "localhost",
    database= "postgres",
    port= 5433
)


engine = sqlalchemy.create_engine(db_params)
connection= engine.connect()

#sql_query_1=sqlalchemy.text("INSERT INTO public.my_table(name) VALUES('kepa');")
#sql_query_1=sqlalchemy.text("select * from public.my_table;")
#user = input('podaj nazwę zawodnika do usunięcia')
#sql_query_1=sqlalchemy.text(f"DELETE FROM public.my_table where name='{user}';")
#kogo_zmienic=input('podaj kogo zmienic')
#na_kogo=input('podaj na kogo zamienic')
#sql_query_1=sqlalchemy.text(f"update public.my_table set name='{na_kogo}' where name = '{kogo_zamienic}';")

def dodaj_uzytkownika(user:str):
    sql_query_1 = sqlalchemy.text(f"INSERT INTO public.my_table(name) VALUES '{user}';")
    connection.execute(sql_query_1)
    connection.commit()
cwok='stasiu'
dodaj_uzytkownika(cwok)

#connection.execute(sql_query_1)
#connection.commit()

