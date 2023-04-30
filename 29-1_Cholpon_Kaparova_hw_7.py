import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection



connect = create_connection('hw.db')
sql_create_products_table = '''
CREATE TABLE products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title TEXT(200) NOT NULL,
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
)
'''
def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_products(conn, product):
    sql = '''
    INSERT INTO products(product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_products_by_quantity(conn, product):
    sql = '''
    UPDATE products SET quantity = ? WHERE id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_products_by_price(conn, product):
    sql = '''
    UPDATE products SET price = ? WHERE id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_products_by_id(conn, id):
    sql = '''
    DELETE FROM products WHERE id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_products(conn):
    sql = '''
    SELECT * FROM products
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_price_lessthan1500000_quntity_biggerthan100(conn):
    sql = '''
    SELECT * FROM products WHERE price < 1500000 and quantity > 100
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_producttitle(conn):
    sql = '''
    SELECT * FROM products WHERE product_title like 'Bed%'
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

if connect is not None:
    print('Connected successfully')
    # create_table(connect, sql_create_products_table)
    # insert_products(connect, ('Table Futuristic', 1000000.00, 500))
    # insert_products(connect, ('Shelf Futuristic', 200000.00, 550))
    # insert_products(connect, ('Wordrobe Futuristic', 2000000.00, 650))
    # insert_products(connect, ('Bed Futuristic', 1500000.00, 700))
    # insert_products(connect, ('Sofa Futuristic', 3000000.00, 300))
    # insert_products(connect, ('Table Barocco', 1000000.00, 100))
    # insert_products(connect, ('Shelf Barocco', 200000.00, 550))
    # insert_products(connect, ('Wordrobe Barocco', 2000000.00, 150))
    # insert_products(connect, ('Bed Barocco', 1500000.00, 200))
    # insert_products(connect, ('Sofa Barocco', 3000000.00, 300))
    # insert_products(connect, ('Table Renesans', 1000000.00, 100))
    # insert_products(connect, ('Shelf Renesans', 200000.00, 150))
    # insert_products(connect, ('Wordrobe Renesans', 2000000.00, 200))
    # insert_products(connect, ('Bed Renesans', 1500000.00, 100))
    # insert_products(connect, ('Sofa Renesans', 3000000.00, 100))
    # update_products_by_price(connect, (2000000, 31))
    # update_products_by_quantity(connect,(400,31))
    # delete_products_by_id(connect, 30)
    # select_products(connect)
    # select_products_price_lessthan1500000_quntity_biggerthan100(connect)
    select_products_producttitle(connect)
    connect.close()
