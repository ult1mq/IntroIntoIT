class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def __getinfo(self):
        print("Название книги: " + self.title + ", Автор: " + self.author + ", Год издания: " + self.year)