class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books are present in the library are: ")
        for book in self.books: 
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("sorry, this book is either been issued or it is not available in the library ")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("thanks for returning the book! Hope you enjoyed reading it. have a great day ahead!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")                
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["python", "django", "uxdesigning", "drawingguide", "autobiographies"])
    student = Student()
    #centrallibrary.displayavailablebook()
    while(True):
        welcomeMessage = """\n ======== welcome to central library =========
        plese choose an Option:
        1.List all the books
        2.request a book
        3.Add/return a book
        4.exit the library"""
        
        print(welcomeMessage)
        a = int(input("enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()

        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())

        
        elif a== 3:
            centralLibrary.returnBook(student.returnBook())

        elif a== 4:
            print("thanks for using the library. have a great day ahead.")
            exit()

        
        else:
            print("Invalid Choice!")




