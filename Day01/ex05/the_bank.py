# in the_bank.py
class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		if hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1
	def transfer(self, amount):
		self.value += amount

# in the_bank.py
class Bank(object):
	"""The bank"""
	def __init__(self):
		self.account = []
	def add(self, account):
		self.account.append(account)
	def transfer(self, origin, dest, amount):
		"""
			@origin: int(id) or str(name) of the first account
			@dest:    int(id) or str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return         True if success, False if an error occured
		"""
		

	def fix_account(self, account):
		"""
			fix the corrupted account
			@account: int(id) or str(name) of the account
			@return         True if success, False if an error occured
		"""
		
	
	def check_account(self, account):
		"""
		  It has an even number of attributes.
		• It has an attribute starting with b.
		• It has no attribute starting with zip or addr.
		• It has no attribute name, id and value.
		"""
		if not isinstance(account, Account):
			raise Exception("an account object was expected")


		