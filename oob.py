class Kettle(object):

	power_source = 'Electricity'

	def __init__(self,make, price):
		self.make = make
		self.price = price
		self.on = False

	def switch_on(self):
		self.on = True

Kenwood = Kettle("Kenwood", 8.99)
print(Kenwood.make)
print(Kenwood.price)

Kenwood.price = 12.75
print(Kenwood.price)

Hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(Kenwood.make, Kenwood.price, Hamilton.make, Hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(Kenwood, Hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: A function defined in a class.
Attribute: A variable bound to instance of a class.
self: reference to instance of a class.
Constructor: Is a special method that is exectuted when the instance of a class is created/constructed.
"""

print(Hamilton.on)
Hamilton.switch_on()
print(Hamilton.on)

Kettle.switch_on(Kenwood)
print(Kenwood.on)
Kenwood.switch_on()

Kenwood.power = 1.5
print(Kenwood.power)
#print(Hamilton.power)

print('Switch to atomic power')
Kettle.power_source = 'atomic'
print(Kettle.power_source)
print('Switch kenwood to Gas')
Kenwood.power_source = 'Gas'
print(Kenwood.power_source)
print(Hamilton.power_source)

print(Kettle.__dict__)
print(Kenwood.__dict__)
print(Hamilton.__dict__)