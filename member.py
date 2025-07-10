from book_class import Book

class Member:
    def __init__(self,name,membership_id):
        self.name =name
        self.membership_id =membership_id
        self.borrow =[]
    def borrow_book(self,book):
        if book.available:
            self.borrow.append(book)
            book.available =False
            print(f"{self.name}borrwed'{book.title}'")
        else:
             print("'{book.title}'not available")
    def return_book(self,book):
         if book in self.borrow:
              book.avaialble = True
              print(f"{self.name} returned '{book.title}'")
              

        

    