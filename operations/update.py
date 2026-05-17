import psycopg2
from operations.fetch import fetch_books

def update_book():
  fetch_books()

  try:
    id = int(input('\nDigite o id do livro que deseja editar: '))

    conn = psycopg2.connect("dbname=library user=postgres password=password")
    cursor = conn.cursor()
    cursor.execute(f'SELECT id, title, author, review_points FROM livros WHERE id = {id}')

    book = cursor.fetchone()

    nome = input(f"Digite um novo nome para esse livro ({book[1]}): ")
    if not nome: nome = book[1]

    autor = input(f"Digite um novo nome de autor para esse livro ({book[2]}): ")
    if not autor: autor = book[2]

    avaliacao_input = input(f"Digite uma nova nota para esse livro ({book[3]}): ")
    if not avaliacao_input: avaliacao = book[3]
    else: avaliacao = float(avaliacao_input)

    cursor.execute(f"UPDATE books SET title='{nome}', author='{autor}', review_points='{avaliacao}' WHERE id = {id};")
    conn.commit()

    print('Livro editado com sucesso!')

    cursor.close()
    conn.close()

  except Exception as err:
    print(f'Erro ao editar livro: {err}. Voltando ao Menu...')
