class Car(object):
    condition = "new"
    
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    
    def display_car(self):
        return "This is %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
    def driving_car(self):
        self.condition = "used"

# Fix: Correct the class definition for ElectricCar
class ElectricCar(Car):  # ElectricCar should inherit from Car
    def __init__(self, model, color, mpg, battery_type):
        # Call the constructor of the parent class (Car) using super()
        super(ElectricCar, self).__init__(model, color, mpg)
        self.battery_type = battery_type

# Create an instance of ElectricCar
my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

# Test display_car method
print(my_car.display_car())

# Define the Square class
class Square(object):
    def __init__(self, side):
        self.side = side
    
    def perimeter(self):
        return self.side * 4

# Example usage of Square class
my_square = Square(5)
print("Perimeter of the square:", my_square.perimeter())

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
    
my_point = Point3D(x = 1, y = 2, z = 3)
print(my_point)




