import psycopg2

def fetch_books():
  conn = psycopg2.connect("dbname=library user=postgres password=password")
  cursor = conn.cursor()

  cursor.execute('SELECT id, title, author, review_points FROM books ORDER BY id')

  print(f'Temos {cursor.rowcount} livros cadastrados na nossa base:')

  books = cursor.fetchall()

  for book in books:
    print(f'{book[0]} - {book[1]} de {book[2]} - Nota: {book[3]}/10.0')

  cursor.close()
  conn.close()