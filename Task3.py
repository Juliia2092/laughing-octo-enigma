class Stadium:
    def __init__(self, name, year, country, city, capacity):
        self.__name = name
        self.__year = year
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def __repr__(self):
        return f"Name:{self.__name}, year:{self.__year}, country:{self.__country}, city:{self.__city}, capacity:{self.__capacity}"


stadium = Stadium('Wembley Stadium', 2003, 'Great Britain', 'Manchester', '90000')
print(stadium)
print(stadium.get_year())
stadium.set_year(year=2007)
print(stadium)
print(stadium.get_city())
stadium.set_city('London')
print(stadium)
