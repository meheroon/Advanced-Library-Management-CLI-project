from book import lend_book, return_book, view_books
from datetime import datetime
def main():
    while True:
        print("\n---- Advanced Library Management System ----")
        print("1. View Books")
        print("2. Lend Book")
        print("3. Return Book")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_books()
        elif choice == "2":
            lend_book()
        elif choice == "3":
            return_book()
        elif choice == "0":
            print("\nExiting the system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()