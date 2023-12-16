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

    15. @function.setter method allows you to change the value of the instance, even if it is set to read only.

    16. The four main principles of OOPS are, Encapsulation, Abstraction, Polymorphism and Inheritance.

	17. Encapsulation is just setting some restrictions on the attributes of a class we define, just like we did with self.name in Item class.

	18. Abstraction is the second principle of OOPS, it basically emphasizes on hiding the unecessary details. in java and some other languages, 
	this is done through private and public classes i think, in python we can use __ to private the method.

	19. Inheritance is the third principle of the OOPS, we have already seen inheritance by defining the Phone class, which inherits the attributes
	from the Item class. We can define as many child classes as we want to.

	20.Polymorphism is the last principle of the OOP, it basically refers to adaptability of a specific method defined. It changes according to the scenario.
	In our code, apply_discount method works on all the child classes. 


    """

from item import Item
from store import Store
store1 = Store('Duke Elec', 'Open', 'Ohio', 1000, 'Electronics')
item1 = Item('Phone', 1999, 12)



