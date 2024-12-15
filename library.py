
class Book:
    def __init__(self,book_id,book_name,book_title,book_author,book_availability):
        self.book_id=book_id
        self.book_name=book_name
        self.book_title=book_title
        self.book_author=book_author
        self.book_availability=book_availability
        
    def book_borrow(self):
        if self.book_availability:
            self.book_availability=False
            return True
        else:
            return False
        
    def book_return(self):
        self.book_availability=True
    
    def __repr__(self):
        self.status = ""
        if self.book_availability:
            self.status="Available"
        else:
            self.status="Not available"
            
        return  f"{self.book_id:<13} | {self.book_name:<22} | {self.book_title:<22} | {self.book_author:<22} |  {self.status:<13}"
        
class Library:
    book_list=[]
    
    @classmethod
    def add_book(self,new_book):
        self.book_list.append(new_book)
        print("\n--------- New Book Added Successfully !! ----------\n")
        
    @classmethod
    def show_book(self):
        if self.book_list:
             print(f"\n{'Book ID':<13} | {'Book name':<22} | {'Boot title':<22} | {'Book author':<22} | {'Status':<11}")
             print("="*101)
             for book in self.book_list:
                 print(book)
             print()
             
        else:
            print("\n >> No book added till now in our library\n")
    
    @classmethod
    def borrow_book_from_library(self,book_id):
        for book in self.book_list:
            if book_id == book.book_id:
                    if book.book_borrow():
                     print("\n-------- Congratulations successfully book borrowed !! --------")       
                    else:
                     print("\n-------- Sorry book is already borrowed !! ---------")
            else:
                print("\n------- Sorry book is not available ----------")
    
    @classmethod
    def book_return_to_library(self,book_id):
            for book in self.book_list:
                if book.book_id == book_id:
                    if not book.book_availability:
                        book.book_return()
                        print("\n------ Book return successfully -------")
                    else:
                        print("\n-------- Book was not borrowed --------")
                else:
                    print("\n >> Book is not available !!\n")
                    
                
while True:
        print()
        print("1. Insert book to library") 
        print("2. Display book from library") 
        print("3. Borrow book from library") 
        print("4. Return book to library") 
        print("5. Exit from library") 
        
        choice = int(input("Enter your option:"))
        
        if choice==1:
            print()
            book_id = int(input(">> Enter your book id: "))
            book_name=input(">> Enter your book name: ")
            book_title=input(">> Enter your book title: ")
            book_author=input(">> Enter your book author: ")
            book_availability=True
            
            new_book = Book(book_id, book_name, book_title,book_author,book_availability)
            
            Library.add_book(new_book)
            
        elif choice==2:   
            Library.show_book()
            
        elif choice==3:
         book_id = input("\n>> Enter your book ID: ")
         int_book_id = int(book_id)
         Library.borrow_book_from_library(int_book_id)
         
        elif choice==4:
           book_id = input("\n>> Enter your book ID: ")
           int_book_id = int(book_id)
           Library.book_return_to_library(int_book_id)
           
        elif choice==5:
            print("\n >> Good bye from library !!")
            break
        
        else:
            print("\n >> Enter valid option from 1 to 5 ") 
       