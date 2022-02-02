class Book:
    def __init__(self, title, year, published, genre, author, price):
        self.__title = title
        self.__year = year
        self.__published = published
        self.__genre = genre
        self.__author = author
        self.__price = price

    def get_title(self):
        return self.__title

    def set_model(self, title):
        self.__title = title

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_published(self):
        return self.__published

    def set_produced(self, published):
        self.__published = published

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __repr__(self):
        return f"Title:{self.__title}, year:{self.__year}, published:{self.__published}, genre:{self.__genre}, author:{self.__author}, price:{self.__price}"


book = Book('11/22/63', 2012, 'Charles Scribner"s Sons', 'science-fiction', 'Stephen King', '242 UAH')
print(book)
print(book.get_year())
book.set_year(year=2011)
print(book)
print(book.get_genre())
book.set_genre('science-fiction novel')
print(book)
