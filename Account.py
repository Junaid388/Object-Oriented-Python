import datetime
import pytz


class  Account(object):
	"""Simple account class with balance"""

	@staticmethod
	def _current_time():
		utc_time = datetime.datetime.now()
		return pytz.utc.localize(utc_time)

	def __init__(self, name, balance):
		self._name = name
		self.__balance = balance #Name mangling
		self._transaction_list = [(Account._current_time(), balance)]
		print('Account created for '+ self._name)
		self.showbalance()

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			self.showbalance()
			self._transaction_list.append((Account._current_time(), amount))

	def withdraw(self, amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			self._transaction_list.append((Account._current_time(), -amount)) # static method should be called with class for faster access
		else:
			print('Amount must be greater than zero and no more than your account balance')
		self.showbalance()

	def showbalance(self):
		print('Balance is {}'.format(self.__balance))

	def show_transaction(self):
		for date, amount in self._transaction_list:
			if amount > 0:
				tran_type = "deposited"
			else:
				tran_type = "withdrawn"
				amount *= -1
			print('{:6} {} on {} (local time was {}) '.format(amount, tran_type, date, date.astimezone()))
	

if __name__ == '__main__':
	tim = Account('Tim',0)
	tim.showbalance()

	tim.deposit(1000)
	#tim.showbalance()
	tim.withdraw(500)
	#tim.showbalance()

	tim.withdraw(2000)

	tim.show_transaction()

	steph = Account('Steph', 800)
	steph.__balance = 200
	steph.deposit(100)
	steph.withdraw(200)
	steph.show_transaction()
	steph.showbalance()
	print(steph.__dict__)
	steph._Account__balance = 40
	steph.showbalance()
