class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.__storage = storage          # Encapsulated attribute (private)
        self.battery_life = battery_life

    def make_call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def browse_internet(self, website):
        return f"Browsing {website} on {self.brand} {self.model}"

    def get_storage(self):  # Encapsulation (getter)
        return f"Storage: {self.__storage}GB"

    def set_storage(self, storage):  # Encapsulation (setter)
        if storage > 0:
            self.__storage = storage
        else:
            print("Invalid storage size.")

# Inherited class with polymorphism
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu

    def play_game(self, game):
        return f"Playing {game} with {self.gpu} GPU on {self.brand} {self.model}!"

    # Polymorphism: overriding method
    def browse_internet(self, website):
        return f"Browsing {website} at ultra speed with gaming mode ON!"


# Testing
phone1 = Smartphone("Samsung", "Galaxy S22", 128, "12hrs")
print(phone1.make_call("0712345678"))
print(phone1.browse_internet("YouTube"))
print(phone1.get_storage())

gaming_phone = GamingPhone("Asus", "ROG 6", 512, "15hrs", "Adreno 730")
print(gaming_phone.play_game("PUBG"))
print(gaming_phone.browse_internet("Twitch"))
