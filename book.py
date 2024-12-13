from file import load_books, save_books, load_lends, save_lends
from datetime import datetime, timedelta
# View the available books
def view_books():
    books = load_books()
    print("\n---- Available Books ----")
    for book in books:
        print(f"Title: {book['title']}, Quantity: {book['quantity']}")


# Lend a book
def lend_book():
    print("\n---- Lend a Book ----")
    books = load_books()
    lends = load_lends()
    book_title = input("Enter the title of the book to lend: ").strip()
    matching_book = next((book for book in books if book["title"].lower() == book_title.lower()), None)

    if not matching_book:
        print("\nError: Book not found.")
        return

    if int(matching_book["quantity"]) <= 0:
        print("\nThere are not enough books available to lend.")
        return

    borrower_name = input("Enter the borrower's name: ").strip()
    phone_number = input("Enter the borrower's phone number: ").strip()
    due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")  # 2 weeks due

    lends.append({
        "borrower_name": borrower_name,
        "phone_number": phone_number,
        "book_title": matching_book["title"],
        "due_date": due_date
    })

    matching_book["quantity"] = str(int(matching_book["quantity"]) - 1)
    save_books(books)
    save_lends(lends)
    print(f"\nBook '{book_title}' lent to {borrower_name} successfully. Due date: {due_date}")


# Return a book
def return_book():
    print("\n---- Return a Book ----")
    books = load_books()
    lends = load_lends()
    book_title = input("Enter the title of the book to return: ").strip()
    borrower_name = input("Enter the borrower's name: ").strip()

    matching_lend = next(
        (lend for lend in lends if lend["book_title"].lower() == book_title.lower() and lend["borrower_name"].lower() == borrower_name.lower()), 
        None
    )

    if not matching_lend:
        print("\nError: No matching lend record found.")
        return

    matching_book = next((book for book in books if book["title"].lower() == book_title.lower()), None)
    if matching_book:
        matching_book["quantity"] = str(int(matching_book["quantity"]) + 1)

    lends.remove(matching_lend)
    save_books(books)
    save_lends(lends)
    print(f"\nBook '{book_title}' returned successfully by {borrower_name}.")