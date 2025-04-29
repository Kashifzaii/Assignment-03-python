import json
import os

FILE_NAME = 'library.txt'

def read_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

def write_library(books):
    with open(FILE_NAME, 'w') as f:
        json.dump(books, f)

def input_book_details():
    return {
        "title": input("Book Title: "),
        "author": input("Author: "),
        "year": input("Year Published: "),
        "genre": input("Genre: "),
        "read": input("Read it? (yes/no): ").strip().lower() == "yes"
    }

def add_new_book(library):
    book = input_book_details()
    library.append(book)
    write_library(library)
    print(f'"{book["title"]}" added to your library.')

def delete_book(library):
    title = input("Enter title to delete: ").strip().lower()
    updated_library = [b for b in library if b["title"].lower() != title]
    if len(updated_library) != len(library):
        write_library(updated_library)
        print(f'"{title}" has been removed.')
    else:
        print(f'Book titled "{title}" not found.')

def search_library(library):
    key = input("Search by (title/author): ").strip().lower()
    value = input(f"Enter {key}: ").strip().lower()
    matches = [b for b in library if value in b.get(key, '').lower()]
    
    if matches:
        for b in matches:
            status = "Read" if b["read"] else "Unread"
            print(f'{b["title"]} - {b["author"]}, {b["year"]}, {b["genre"]} - {status}')
    else:
        print("No matching books found.")

def show_books(library):
    if not library:
        print("Library is empty.")
    for b in library:
        status = "Read" if b["read"] else "Unread"
        print(f'{b["title"]} - {b["author"]}, {b["year"]}, {b["genre"]} - {status}')

def show_stats(library):
    total = len(library)
    read_count = sum(1 for b in library if b["read"])
    percent = (read_count / total * 100) if total else 0
    print(f'Total Books: {total}')
    print(f'Read: {read_count} ({percent:.2f}%)')

def run_library_app():
    books = read_library()
    while True:
        print("\n📚 Library Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. Statistics")
        print("6. Quit")

        option = input("Select an option: ").strip()

        if option == '1':
            add_new_book(books)
        elif option == '2':
            delete_book(books)
            books = read_library()  # reload after delete
        elif option == '3':
            search_library(books)
        elif option == '4':
            show_books(books)
        elif option == '5':
            show_stats(books)
        elif option == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1–6.")

if __name__ == "__main__":
    run_library_app()

