import psycopg2
from operations.fetch import fetch_books

def delete_book():
  fetch_books()

  try:
    id = int(input('\nDigite o id do livro que deseja excluir: '))

    conn = psycopg2.connect("dbname=teste_python user=postgres password=password")
    cursor = conn.cursor()
    cursor.execute(f'SELECT id, nome, autor, avaliacao FROM livros WHERE id = {id}')

    book = cursor.fetchone()

    confirmation = input(f'Confirmar a exclusão do livro {book[1]} de {book[2]} (id {book[0]})? (s/n) ')

    if confirmation == 's':
      cursor.execute(f"DELETE FROM livros WHERE id = {id};")
      conn.commit()
      print('Livro excluído com sucesso!')

    cursor.close()
    conn.close()

  except Exception as err:
    print(f'Erro ao excluir livro: {err}. Voltando ao Menu...')