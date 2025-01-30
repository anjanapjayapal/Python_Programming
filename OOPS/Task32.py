# TASK 32: Implement a class representing a Book

class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
        
    def getbookinfo(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"
        

obj=Book("It Ends With Us","Colleen Hoover",2016)
print(obj.getbookinfo())
