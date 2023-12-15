from item import Item

class Phone(Item):
	def __init__(self, name: str, price: float, quantity=0, broken_phones = 0):

		super().__init__(name, price, quantity) # super function copies the arguments from the parent class, so that we dont have to hard code them again
		assert broken_phones >=0, f'Broken phones Invalid!'
		self.broken_phones = broken_phones