class Store:
	all_stores = []
	def __init__(self, name, status, location, size, store_type):
		self.name = name
		self.status = status
		self.location = location
		self.size = size
		self.store_type = store_type
		Store.all_stores.append(self)

	def __repr__(self):
		return f'{self.name}({self.store_type}, {self.status}, {self.location})'