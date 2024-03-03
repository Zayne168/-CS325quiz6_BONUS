from abc import ABC, abstractmethod


class BookCatalog(ABC):
    @abstractmethod
    def search_by_title(self, title):
        #print("Search for a book by title")
        pass

    @abstractmethod
    def search_by_author(self, author):
        #print("Search for a book by author")
        pass

    @abstractmethod
    def search_by_genre(self, genre):
        #print("Search for a book by genre") this is so that the abstract method is    
        #actually abstract.
        pass
class BookManagement(ABC):
    @abstractmethod
    def add_book(self, book):
        print("Add a book to the catalog")

    @abstractmethod
    def remove_book(self, book):
        print("Remove a book from the catalog")

    @abstractmethod
    def generate_reports(self):
        print("Generate library reports")
class BookBorrowing(ABC):
    @abstractmethod
    def borrow_book(self, book, user):
        #print("Allow a user to borrow a book")
        pass
    @abstractmethod
    def return_book(self, book, user):
        #print("Handle the return of a borrowed book")
        pass
class Library(BookCatalog, BookManagement, BookBorrowing):
    def __init__(self):
        self.catalog = {}
        self.borrowed_books = {}
    def search_by_title(self, title):
        print(f"Searching for the book with title: {title}")
    def search_by_author(self, author):
        print(f"Searching for books by author: {author}")
    def search_by_genre(self, genre):
        print(f"Searching for books in genre: {genre}")
    def add_book(self, book):
        print(f"Adding book: {book} to the catalog")
    def remove_book(self, book):
        print(f"Removing book: {book} from the catalog")
    def generate_reports(self):
        print("Generating library reports")
    def borrow_book(self, book, user):
        print(f"User {user} borrowing book: {book}")
    def return_book(self, book, user):
        print(f"User {user} returning book: {book}")
#This shows ISP because it does not allow the client/user to utilize any un-wanted 
#functionality if this program was fully implemented. SImilar functions are grouped
#into classes so that the front-end deveoloper can decide what functionalities each 
#type of user(customer, librarian, etc) get access to. A standard user would only be 
#able to use the catalog and borrow classes 

def main():
  library = Library()
  # Simulating the actions of different users
  print("\nGuest User:")
  guest_user = "Guest"
  library.search_by_title("Python Programming")
  library.search_by_author("John Smith")
  print("\nRegistered User:")
  registered_user = "John Doe"
  library.search_by_genre("Fantasy")
  library.borrow_book("Harry Potter", registered_user)
  print("\nLibrarian:")
  librarian = "Jane Smith"
  library.add_book("Python Programming")
  library.remove_book("Machine Learning Basics")
  library.generate_reports()
if __name__ == "__main__":
  main()