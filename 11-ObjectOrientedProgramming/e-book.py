class Book():
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False
        self.price = price

    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
    
    def change_page(self,page):
        self.current_page = page
