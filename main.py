class Book:
    def __init__(self, name, author, book_id, copies):
        self.name = name
        self.author = author
        self.book_id=book_id
        self.copies = copies

    def display(self):
        print(f"book name : {self.name} \t author : {self.author} \t copies : {self.copies}")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.book_borrowed = []

class Libary:
    def __init__(self):
        self.books = []
        self.members = []

    def add(self):
        book_name = input("Enter book name : ")
        book_author = input("Enter book author : ")
        book_id = int(input("Enter book id : "))
        book_copies = int(input("Enter book copies : "))

        book= Book(book_name, book_author, book_id, book_copies)

        self.books.append(book)
        print("book added successfully")

    def viewBooks(self):
        for book in self.books:
            book.display()

    def searchBook(self):

        book_id=int (input("Enter book id :"))

        for book in self.books:
            if book.book_id ==book_id:
                book.display()
        print("found:")

    def addMember(self):

        name=input("Enter member name:")
        member_id=int(input("Enter member id :"))

        member=Member(name,member_id)
        self.members.append(member)
        print("member added successfully")

    def borrowBook(self):
        member_id = int(input("Enter member id: "))
        book_id = int(input("Enter book id: "))

        # 1. Find and validate the book
        target_book = None
        for book in self.books:
            if book.book_id == book_id:
                target_book = book
                break

        if not target_book:
            print("Book not found")
            return

        if target_book.copies <= 0:
            print("Book not available")
            return

        # 2. Find and validate the member
        target_member = None
        for member in self.members:
            if member.member_id == member_id:
                target_member = member
                break

        if not target_member:
            print("Member not found")
            return

        # 3. Process the transaction if both exist
        target_book.copies -= 1
        target_member.book_borrowed.append(book_id)
        print("Book borrowed successfully")

    def returnBook(self):
        member_id=int(input("enter member id:"))
        target_member=None

        for member in self.members:
            if member.member_id == member_id:
                target_member = member
                break

        if not target_member:
            print("Member not found")
            return

        book_id=int(input("enter book id:"))
        target_book=None
        for book in self.books:
            if book.book_id == book_id:
                target_book = book
                break

        if not target_book:
            print("Book not found")
            return

        target_book.copies +=1
        target_member.book_borrowed.remove(book_id)
        print("book returned successfully")

    def removeBook(self):
        book_id=int(input("enter book id:"))

        target_book=None

        for book in self.books:
            if book.book_id == book_id:
                target_book = book
                break

        if not target_book:
            print("Book not found")
            return

        self.books.remove(target_book)
        print("Book removed successfully")

    #write a function to prevent duplicate
    def isbookExists(self):
        pass


def main():
    l=Libary()

    for i in range(2):
        l.add()

    l.viewBooks()

    l.addMember()
    l.borrowBook()




if __name__=="__main__":
    main()
