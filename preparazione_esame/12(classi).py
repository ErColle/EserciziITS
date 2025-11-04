class Book: 
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title 
        self.author = author
        self.is_borrowed = False
        
    def borrow(self):
        if self.is_borrowed is False:
            self.is_borrowed = True 
            
    def return_book(self):
        if self.is_borrowed is True:
            self.is_borrowed = False
            
class Member:
    def __init__(self, member_id:str, name: str):
        self.member_id = member_id 
        self.name = name 
        self.borrowed_books: list[Book] = [] 
        
    def borrow_book(self, book: Book):
        if book not in self.borrowed_books:
            book.borrow()
            self.borrowed_books.append(book)
    
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            
class Library: 
    def __init__(self):
        self.books: dict[str, Book] = {} # chiave id libro - valore oggetto Book 
        self.members: dict[str, Member] = {} # chiave id member - valore oggetto Member
        
    def add_book(self, book_id: str, title: str, author: str):
        self.books[book_id] = Book(book_id, title, author)
    
    def register_member(self, member_id: str, name: str):
        self.members[member_id] = Member(member_id, name)
    
    def borrow_book(self, member_id, book_id):
                        
        if book_id not in self.books:
            raise ValueError("Book not found")
        
        if member_id not in self.members:
            raise ValueError("Member not found")
        
        book = self.books[book_id]
        
        if book.is_borrowed:
            raise ValueError("Book is already borrowed")
        else:
            self.members[member_id].borrow_book(self.books[book_id])
        
    def return_book(self, member_id, book_id):
        book = self.books[book_id]
        member = self.members[member_id]
        
        if book not in member.borrowed_books:
            raise ValueError("Book not borrowed by this member") 
        self.members[member_id].return_book(self.books[book_id])
        
    def get_borrowed_books(self, member_id: str):
        if member_id in self.members:
            return [book.title for book in self.members[member_id].borrowed_books]
        return []

    


