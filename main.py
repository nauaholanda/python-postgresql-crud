from operations.books import fetch_books, insert_book, update_book, delete_book
from operations.reviews import list_reviews, insert_review

def main():
    print("Welcome to the book registry!")
    while(True):
        print("Available actions: ")
        print("1 - List registered books")
        print("2 - Register a new book")
        print("3 - Edit an existing book")
        print("4 - Delete a book")
        print("5 - List the reviews of a book")
        print("6 - Insert a review of a book")
        print("(type 999 or press Ctrl+C to exit)")
        try:
            action_number = int(input("What would you like to do? (enter the action number): "))

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
                case 5:
                    list_reviews()
                case 6:
                    insert_review()
                case _:
                    print("Unknown action")
        

            print('\n\n\n')
            print('=========================================')

        except ValueError:
            print("Please enter a valid action number.")
        except KeyboardInterrupt:
            break
    print("Goodbye!")


if __name__ == "__main__":
    main()