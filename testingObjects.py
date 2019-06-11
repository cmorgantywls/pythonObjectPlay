# Define the class
class Product:
  # Define the __init__ method
  def __init__(self, theName, thePrice):
    self.name = theName
    self.price = thePrice
    self.stock = 0
    print(theName + " created successfully!")
  
  def receive(self, quantity):
    self.stock+=quantity
    #no return necessary bc it's updating in the class/object

# Initialize the first product
product1 = Product("Pillow Pal", 24.99)
product2 = Product("Pokeball", 80)
product1.name = "Bloop"
print(product1.name,product1.stock)
product1.receive(100)
print(product1.stock)

