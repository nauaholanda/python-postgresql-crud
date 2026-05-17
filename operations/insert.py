import psycopg2

def insert_book():
  try:
    nome = input("Digite o nome do novo livro: ")
    autor = input("Digite o nome do autor desse livro: ")
    avaliacao = float(input("Digite a nota desse livro: "))

    conn = psycopg2.connect("dbname=library user=postgres password=password")
    cursor = conn.cursor()

    sql = f"INSERT INTO books(title, author, review_points) values('{nome}', '{autor}', {avaliacao});"

    cursor.execute(sql)
    conn.commit()

    print(f"Livro {nome} salvo com sucesso!")

    cursor.close()
    conn.close()

  except Exception as err:
    print(f'Erro ao inserir livro: {err}. Voltando ao Menu...')