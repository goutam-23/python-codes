class library:
    def __init__(self,lst1,library):
        self.lst1=lst1
        self.library=library

    def display_books(self):
        return f"these are the books present in the library{lst1}"

    def lend_book(self):
        numbers=int(input("enter the book you want:\nenter 1 for c\nenter 2 for java.\nenter 3 for python.\nenter 4 for html\nenter:"))
        lst1.pop(numbers)
        print("the book is given to the reader..")
        print("books are present in the library NOW!!",lst1)

    def add_book(self):
        add=input("enter which book you want to add in the library:")
        lst1.append(add)
        print("your book is added successfully.")
        print("books are present in the library NOW!!", lst1)

    def return_book(self):
        return1=input("which book you want to return:")
        lst1.append(return1)
        print("done!! the book is restored in the library.")
        print("books are present in the library NOW!!", lst1)

lst1=["c","java","python","html"]
GoutamLibrary = library(lst1, "Goutam's Library")

while 1:
    print("enter 1 for display books.\nenter 2 for lend a book.\nenter 3 for add a book.\nenter 4 for return a book.\nenter 5 to exit from the library\nenter the choice:")
    entry=int(input())
    if entry==1:
        print(GoutamLibrary.display_books())
    elif entry==2:
        print(GoutamLibrary.lend_book())
    elif entry==3:
        print(GoutamLibrary.add_book())
    elif entry==4:
        print(GoutamLibrary.return_book())
    elif entry==5:
        break