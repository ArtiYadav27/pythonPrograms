class library:
    def __init__(self):
        self.books=[]
        self.no_of_books=0
        
    def add_books(self,book_name):
        self.books.append(book_name)
        self.no_of_books +=1

    def check_books(self):
        if(self.no_of_books==len(self.books)):
            print(f"everything seems good..\nlibrary has total {self.no_of_books} books.." )
        else:
            print("books no has been mismatched...")
    def show_details(self):
        print(f"books in the library are...{self.books}..")
l1=library()
l1.add_books("chintamani")
l1.check_books()
l1.show_details()
l1.add_books("harry potter")
