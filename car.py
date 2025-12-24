# Car class
class Car:
    def __init__(self, car_id, brand, model, price):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price = price

    def display_car(self):
        print(f"ID: {self.car_id} | {self.brand} {self.model} | ₹{self.price}")


# Dealership class
class Dealership:
    def __init__(self, name):
        self.name = name
        self.inventory = []   # list to store Car objects

    # Add car to inventory
    def add_car(self, car):
        self.inventory.append(car)
        print("Car added to inventory.")

    # Remove car by ID
    def remove_car(self, car_id):
        for car in self.inventory:
            if car.car_id == car_id:
                self.inventory.remove(car)
                print("Car removed from inventory.")
                return
        print("Car not found.")

    # Display all cars
    def show_inventory(self):
        print(f"\n--- {self.name} Inventory ---")
        if not self.inventory:
            print("No cars available.")
        for car in self.inventory:
            car.display_car()


# Using the classes
car1 = Car(101, "Toyota", "Inova Crysta", 3500000)
car2 = Car(102, "Honda", "City", 1500000)
car3 = Car(103, "Hyundai", "Creta", 1800000)

dealer = Dealership("Elite Cars")

dealer.add_car(car1)
dealer.add_car(car2)
dealer.add_car(car3)

dealer.show_inventory()

dealer.remove_car(102)
dealer.show_inventory()
