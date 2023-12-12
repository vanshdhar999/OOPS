# This application is a basic introduction to OOPS.

# please follow through the code and see the comments alongside.

# we will be re creating a store management application. 

class Item:
	"""
	This docstring contains the global keywords or references to common methods:
	1. __ function refer to the magic methods eg. __init__ method

	2. assert function is a testing function.

	3. instance attributes vs class attributes. """
	pay_rate = 0.8 # rate after applying discount
					# this is a class attribute
	store_status = False # True if store is open, false is closed
	def __init__(self, name: str , price: float, quantity = 0): # functions starting with __ are called magic methods, these get run automatically when the class is called
				
				# running validations
				assert price >= 0, f"Invalid price"
				assert quantity >=0 , f"Invalid quantity"


				# assigning to self object 
				self.name = name					# init is also called constructor method sometimes
				self.price = price
				self.quantity = quantity
	def calculate_total_price(self):  # self keyword is a common convention used in oops

		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * self.pay_rate

	def store_open_closed(self):
		if not self.store_status:
			return f'Store is closed !'




item1 = Item("Pencil", 100, 4)
item2 = Item("Laptop", 100, 4) # Instantiating instance attributes

print(item1.store_open_closed())











