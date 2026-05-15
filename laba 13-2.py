class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} открыт! Добро пожаловать!")
restaurant1 = Restaurant("Пышечная", "Французская кухня")
restaurant2 = Restaurant("ДЕД ХО", "Японская кухня")
restaurant3 = Restaurant("Пицца-Хаус", "Итальянская кухня")
restaurant1.describe_restaurant()
print("---")
restaurant2.describe_restaurant()
print("---")
restaurant3.describe_restaurant()