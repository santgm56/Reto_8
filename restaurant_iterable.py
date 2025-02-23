class MenuItem:
    """
    Clase base que representa un artículo del menú en el restaurante.
    Tiene atributos para el nombre, precio y descuento.
    """
    def __init__(self, name: str, price: float, discount: float = 0.0):
        if not isinstance(name, str): 
            raise TypeError("EL nombre debe ser un string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("El precio debe ser un número positivo.")    
        if not (0 <= discount <= 1):
            raise ValueError("El descuento debe estar entre 0 y 1.")
        
        self.name = name
        self.price = price
        self.discount = discount

    def calculate(self) -> float:
        return self.price * (1 - self.discount)

    def __str__(self):
        discount_price = self.calculate()
        if self.discount > 0:
            return f"{self.name}: ${self.price:.2f} (Descuento: ${discount_price:.2f})"
        return f"{self.name}: ${self.price:.2f}"

"""
Este módulo contiene clases que heredan de MenuItem y representan 
diferentes categorías de productos en el sistema.
"""
class Beverage(MenuItem):
    pass

class Appetizers(MenuItem):
    pass

class SideDishes(MenuItem):
    pass

class MainCourses(MenuItem):
    pass

class Desserts(MenuItem):
    pass

class Order:
    def __init__(self):
        self.items = []
        self._index = 0

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def bill_amount(self) -> float:
        """Calculates the total amount after individual discounts."""
        return sum(item.calculate() for item in self.items)

    def discount(self, global_discount: float) -> float:
        if not (0 <= global_discount <= 1):
            raise ValueError("El descuento debe estar entre 0 y 1.")
        return self.bill_amount() * (1 - global_discount)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.items):
            raise StopIteration
        item = self.items[self._index]
        self._index += 1
        return item

menu = [
    Beverage("Coca Cola", 2.5),
    Beverage("Sprite", 1.5),
    Beverage("Water", 1.0),
    Appetizers("Fries", 3.0),
    Appetizers("Egg Rolls", 3.0),
    Appetizers("Crab Chips", 3.0),
    SideDishes("Tacos", 4.0),
    SideDishes("Soup", 3.0),
    SideDishes("Salad", 2.0),
    SideDishes("Charred Sweetcorn Salsa", 6.0),
    MainCourses("Burger", 5.0),
    MainCourses("Chicken Fried Steak", 6.0),
    MainCourses("Pizza", 8.0),
    Desserts("Cake", 3.5),
    Desserts("Ice Cream", 4.0)
]

order = Order()
order.add_item(Beverage("Coca Cola", 2.5, 0.2))   
order.add_item(Appetizers("Fries", 3.0, 0.05))
order.add_item(SideDishes("Tacos", 4.0, 0.05))
order.add_item(MainCourses("Burger", 5.0, 0.1))
order.add_item(Desserts("Cake", 3.5))

print("Bienvenido a mi restaurante... :)")
print("Esta es tu orden:")
for item in order:
    print(item)

print(f"Este es el monto de tu cuenta: {order.bill_amount()} pesos")
print(f"Tu descuento es de: {order.discount(0.05):.3f} pesos")
