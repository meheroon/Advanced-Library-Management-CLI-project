import csv
import os

BOOKS_FILE = "books.csv"
LENDS_FILE = "lends.csv"

# Load books from file
def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r", encoding="utf-8") as file:
        return [row for row in csv.DictReader(file)]

# Save books to file
def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "quantity"])
        writer.writeheader()
        writer.writerows(books)

# Load lend records from file
def load_lends():
    if not os.path.exists(LENDS_FILE):
        return []
    with open(LENDS_FILE, "r", encoding="utf-8") as file:
        return [row for row in csv.DictReader(file)]

# Save lend records to file
def save_lends(lends):
    with open(LENDS_FILE, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["borrower_name", "phone_number", "book_title", "due_date"])
        writer.writeheader()
        writer.writerows(lends)
