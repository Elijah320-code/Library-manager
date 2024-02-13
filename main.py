# library_manager.py

def add_book(title, author, year):
    with open('books.txt', 'a') as file:
        file.write(f"{title}, {author}, {year}\n")
    print("Book added successfully.")

def list_books():
    print("Listing all books:")
    with open('books.txt', 'r') as file:
        for line in file:
            print(line.strip())

def search_books(keyword):
    print(f"Searching for books with '{keyword}':")
    with open('books.txt', 'r') as file:
        for line in file:
            if keyword.lower() in line.lower():
                print(line.strip())

def main():
    while True:
        print("\nLibrary Manager")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter publication year: ")
            add_book(title, author, year)
        elif choice == "2":
            list_books()
        elif choice == "3":
            keyword = input("Enter search keyword: ")
            search_books(keyword)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
