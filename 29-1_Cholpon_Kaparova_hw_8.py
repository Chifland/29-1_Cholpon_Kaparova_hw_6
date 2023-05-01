import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

connect = create_connection('org.db')
sql_create_countries_table = '''
CREATE TABLE countries(
id INTEGER PRIMARY KEY AUTOINCREMENT,
country_title VARCHAR(100) NOT NULL
)
'''
def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def select_cities_id(conn):
    sql = '''
    SELECT * FROM cities
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

# def select_cities(conn, city):
#
#     sql = '''
#
#     SELECT * FROM select_employees_all(conn) WHERE c_id = ?
#
#     '''
#     try:
#         cursor = conn.cursor()
#         cursor.execute(sql,(city,))
#
#         rows = cursor.fetchall()
#
#
#         for row in rows:
#             print(row)
#     except sqlite3.Error as e:
#         print(e)

def select_employees_all(conn, city):
    sql = '''
    select  e.first_name, e.last_name, c.title, cn.country_title from employees as e, cities as c, countries as cn
    
    where c.city_id = e.city_id and cn.country_id = c.country_id and c.city_id = ?

    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,(city,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)



if connect is not None:
    print('Connected successfully')
    # create_table(connect,sql_create_countries_table)
    print(f'Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже')
    select_cities_id(connect)
    while True:
        a = int(input(f'Choose id of city: '))
        select_employees_all(connect, a)

        answer = input(f'Для выхода из программы нажмите "0": ')
        if answer == '0':
            break


    connect.close()

