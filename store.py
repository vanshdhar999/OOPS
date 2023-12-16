class Store:
	all_stores = []
	def __init__(self, name, status, location, size, store_type):
		self.__name = name
		self.status = status
		self.location = location
		self.size = size
		self.store_type = store_type
		Store.all_stores.append(self)

	def __repr__(self):
		return f'{self.name}({self.store_type}, {self.status}, {self.location})'
	@property
	def name(self):
		print('You tried to get the store name !')
		return self.__name

	@name.setter
	def name(self, value):
		print('You tried to change the name value !')
		self.__name = value

