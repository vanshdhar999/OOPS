# This application is a basic introduction to OOPS.

# Please follow through the multiple files to see which class is being used.

# We will be re creating a store management application. 
"""
	This docstring contains the global keywords, main features of the OOPS and some common but useful methods:
	1. __ function refer to the magic methods eg. __init__, __repr__ method

	2. assert function is a testing function.

	3. instance attributes vs class attributes.

	4. __dict__ method gives the details of the class instantitated, in the form of a dictionary.

	5. __repr__ magic method helps us represent our instances of class in the way we want. 

	6. We do not want to hardcode the instances of the class, therefore we define a method for it, take the data from a csv file

	7. class methods are useful when we want to instantiate the instances with the help of a method defined in the class
	
	8. static methods are used to define normal functions, more on this later. @staticmethod is used as a decorator.
	
	9. See in static method, we use a normal argument as used in normal functions.
	
	10. class inheritance is used when we want a specific class for something, but has common features as it's super class.
	
	11. self.__class__.__name__ takes in the class instance, useful in repr method.
    
    12. As our code gets lengthier we, split our classes into multiple files and import the required classes.
    
    13. getters and setters, we can set any attribute to be read only, using the @property decorator.

    14. @property decorator, raises an exception we try to change the value of the attribute specified.
    """

from item import Item
from store import Store
store1 = Store('Duke Elec', 'Open', 'Ohio', 1000, 'electronics')
item1 = Item('Phone', 1999, 12)
print(item1.calculate_total_price())





