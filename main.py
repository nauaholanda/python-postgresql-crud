from operations import fetch_books, insert_book, update_book, delete_book

def main():
    print("Bem-vindo ao cadastro de livros!")
    while(True):
        print("Ações disponíveis: ")
        print("1 - Listar livros cadastrados")
        print("2 - Cadastrar novo livro")
        print("3 - Editar livro existente")
        print("4 - Excluir livro")
        print("(digite 999 ou pressione Ctrl+C para sair)")
        try:
            action_number = int(input("O que deseja fazer? (insira o número da ação): "))

            if (action_number == 999):
                break

            print('=========================================')
            print('\n\n\n')
            match action_number:
                case 1:
                    fetch_books()
                case 2: 
                    insert_book()
                case 3:
                    update_book()
                case 4:
                    delete_book()
                case _:
                    print("Ação desconhecida")
        

            print('\n\n\n')
            print('=========================================')

        except ValueError:
            print ("Informe apenas o número de uma ação.")
        except KeyboardInterrupt:
            break
    print("Até mais!")


if __name__ == "__main__":
    main()
