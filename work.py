from book_class import Book
from member import Member
book1=Book("Jane Eyre","Jane Astun",131231)
book2 = Book("Tale of two cities","charles dickens",312441)
customer1=Member("yassin","MI123")
book1.display_info()
customer1.borrow_book(book1)