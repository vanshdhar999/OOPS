import csv

class Item:
	pay_rate = 0.8 # rate after applying discount
					# this is a class attribute

	all_items = [] # this list stores all the items and number of stores
	def __init__(self, name: str , price: float, quantity = 0): # functions starting with __ are called magic methods, these get run automatically when the class is called
				
				# running validations
				assert price >= 0, f"Invalid price"
				assert quantity >=0 , f"Invalid quantity"


				# assigning to self object 
				self.__name = name	
				self.__price = price
				self.quantity = quantity

				Item.all_items.append(self)	# adds the items to the item list 
	
	@property # Property decorator--Read Only Attribute.
	def name(self):
		return self.__name
	

	@name.setter
	def name(self, value):
		self.__name = value


	@property
	def price(self):
		return self.__price

	def calculate_total_price(self):  # self keyword is a common convention used in oops

		return self.__price * self.quantity

	def apply_discount(self):
		self.__price = self.__price * self.pay_rate

	@price.setter
	def price(self, value):
		assert value>=0, f'Price is invalid !'
		self.__price = value

	def apply_increment(self, increment_value):
		assert increment_value >=0, f'Increment value is invalid !'

		self.__price = self.__price + self.__price * increment_value

	def __repr__(self):
		return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
	

	@classmethod # decorator defined in python to define a class method
	def instantiate_from_csv(cls):

		with open('./items.csv', 'r') as f:
			reader = csv.DictReader(f)
			items = list(reader)
			print(items)

		for item in items:
			Item(
				name = item.get('name'),
				price = item.get('price'),
				quantity = item.get('quantity'),
			)
	@staticmethod
	def is_integer(num):

		if isinstance(num, float):
			return num.is_integer() # this function counts x.0 as an integer, where x is a placeholder for some integer
		elif isinstance(num, int):
			return True
		else:
			return False


	def __connect(self ,smtp_server): # Double underscore is used to private the method, so that unnecessary details are hidden.
		pass

	def __prepare_body(self):
		return f'Some message !'

	def __send(self):
		pass

	def send_email(self):
		self.__connect("")
		self.__prepare_body()
		self.__send()

