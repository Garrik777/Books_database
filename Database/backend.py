import sqlite3
from pathlib import Path

dBasePath = Path('./Database/books.db')


def create_table():
    conn = sqlite3.connect(dBasePath)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, '
                   'isbn integer)')
    conn.commit()
    cursor.close()
    conn.close()


def add_record(title, author, year, isbn):
    conn = sqlite3.connect(dBasePath)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO book VALUES (NULL,?,?,?,?)', (title, author, year, isbn))
    conn.commit()
    cursor.close()
    conn.close()


def view_table():
    conn = sqlite3.connect(dBasePath)
    cursor = conn.cursor()
    cursor.execute('SELECT * from book')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect(dBasePath)
    cursor = conn.cursor()
    cursor.execute('SELECT * from book WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def delete_record(id):
    conn = sqlite3.connect(dBasePath)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM book WHERE id=?', (id,))
    conn.commit()
    cursor.close()
    conn.close()


def update_record(id, title, author, year, isbn):
    conn = sqlite3.connect(dBasePath)
    cursor = conn.cursor()
    cursor.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_table()
    # add_record('Cippolino','Janny Rodary',1905,205677)
    # add_record('Сказка о царе Салтане','Пушкин А.С.',1815,105269)
    # delete_record(5)
    # print(search(author='Пушкин А.С.'))
    update_record(6, 'Стальная крыса', 'Гарри Гаррисон', 1975, 3254151)
    print(view_table())
