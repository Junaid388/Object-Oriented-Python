import random
class Enemy(object):
	"""docstring for Enemy"""
	def __init__(self, name="Enemy", hit_points = 0, lives = 1): #Python doesn't have method overloading as java, In case for Java you would have created 3 different methods for passing diff the arguments
		self.name = name
		self.hit_points = hit_points
		self.lives = lives
		self.alive = True

	def take_damage(self, damage):
		remaining_points = self.hit_points - damage
		if remaining_points >= 0:
			self.hit_points = remaining_points
			print("I took {} points damage and have {} left".format(damage, self.hit_points))
		else:
			self.lives -= 1
			if self.lives > 0:
				print('{0.name} lost a life'.format(self))
			else:
				print('{0.name} is dead'.format(self))
				self.alive = False

	def __str__(self):
		return "Name: {0.name}, lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy):
	"""docstring for Troll"""
	def __init__(self, name):
		#Enemy.__init__(self, name = name, lives = 1, hit_points = 23)
		super(Troll, self).__init__(name = name, lives = 1, hit_points = 23) #Troll and self are optional

	def grunt(self):
		print("Me {0.name}. {0.name} stomp you".format(self))


class Vampyre(Enemy):
	"""docstring for Vampyre"""
	def __init__(self, name):
		super().__init__(name = name, lives = 3, hit_points = 12)

	def dodges(self):
		if random.randint(1, 3) == 3:
			print("***** {0.name} dodges *****".format(self))
			return True
		else:
			return False

	def take_damage(self, damage):
		if not self.dodges():
			super().take_damage(damage=damage)


class VampyreKing(Vampyre):
	"""docstring for VampyreKing"""
	def __init__(self, name):
		super().__init__(name)
		self.hit_points = 140

	def take_damage(self, damage):
		super().take_damage(damage // 4)
		
		