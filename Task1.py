class Automobile:
    def __init__(self, name, year, produced, engine_volume, color, price):
        self.__name = name
        self.__year = year
        self.__produced = produced
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def get_model(self):
        return self.__name

    def set_model(self, name):
        self.__name = name

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_produced(self):
        return self.__produced

    def set_produced(self, produced):
        self.__produced = produced

    def get_engine_volume(self):
        return self.__engine_volume

    def set_engine_volume(self, engine_volume):
        self.__engine_volume = engine_volume

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __repr__(self):
        return f"model:{self.__name}, year:{self.__year}, produced:{self.__produced}, engine_volume:{self.__engine_volume}, color:{self.__color}, price:{self.__price}"


automobile = Automobile('Hyundai Sonata ', 1985, 'Hyundai Motor Company', '2l', 'grey', '549533 UAH')
print(automobile)
print(automobile.get_year())
automobile.set_year(year=1987)
print(automobile)
