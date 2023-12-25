class Library:
    def __init__(self, listOfBooks):
        # Constructor to initialize the Library object with a list of books
        self.books = listOfBooks

    def displayAvailableBooks(self):
        # Method to display the available books in the library
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        # Method to borrow a book from the library
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            # Remove the borrowed book from the list
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        # Method to return a borrowed book to the library
        self.books.append(bookName)  # Add the returned book back to the list
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class Student:
    def requestBook(self):
        # Method for a student to request a book
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        # Method for a student to return a borrowed book
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centraLibrary = Library(
        ["Algorithms", "Physics", "Maths", "Biology", "Computer Science"])
    student = Student()

    # Menu-driven interface for the library system
    while (True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))

        # Menu options
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
