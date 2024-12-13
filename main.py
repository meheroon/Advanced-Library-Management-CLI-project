from book import lend_book, return_book, view_books, add_book, update_book
from datetime import datetime
def main():
    while True:
        print("\n---- Advanced Library Management System ----")
        print("1. View Books")
        print("2. Add Book") 
        print("3. Update Book Quantity") 
        print("4. Lend Book")
        print("5. Return Book")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            lend_book()
        elif choice == "5":
            return_book()
        elif choice == "0":
            print("\nExiting the system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()