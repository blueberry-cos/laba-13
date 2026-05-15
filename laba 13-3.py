class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} открыт! Добро пожаловать!")
    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлён до {self.rating}")
my_restaurant = Restaurant("Династия", "Корейская кухня", 4.3)
my_restaurant.describe_restaurant()
my_restaurant.update_rating(4.8)
my_restaurant.describe_restaurant()