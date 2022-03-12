class book: # this is a class
    def __init__(self, title, author, pages):  
        self.title = title 
        self.author = author
        self.pages = pages
    def display(self): 
        print(f"The book is {self.title}, the author is {self.author}, and the number of pages is {self.pages}")