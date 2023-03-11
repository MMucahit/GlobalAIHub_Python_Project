import sqlite3

import pandas as pd

## Veri tabanına bağlanma
def connection_db(db_name):
    con = sqlite3.connect(f'{db_name}.db')
    
    cursor = con.cursor()
    return cursor, con

## Bağlandığımız veri tabanında tablo oluşturma
def create_table(cursor, columns):
    try:
        cursor.execute(f"CREATE TABLE orders({', '.join(columns)})")
    except:
        pass

## Tabloya satır ekleme
def add_row(cursor,con, values:list, columns:list):
    results = cursor.execute(
        f'''INSERT INTO orders({', '.join(list(columns))}) 
        VALUES(?, ?, ?, ?, ?, ?)''', list(values))
    
    con.commit()
    
    return results

## Verileri okuma
def show_rows(cursor:sqlite3.Cursor, columns:list):
    result = cursor.execute('''SELECT * FROM orders''').fetchall()
    df = pd.DataFrame(result, columns=list(columns))
    return df