"""
CISC 327
Breaking Bank
Assignment #2
Scott Wallace 10051890
Brad Guner 10059112
"""

class retail(object):
	def __init__(self, type):
		self.type = type
	def withdraw():
		return 0 
	def deposit():
		return 0 
	def transfer():
		return 0 
	def runRetailDay():
		running = True
		while (running):
			transaction = raw_input('Perform a transaction: ')
			transaction.lowercase
			if (transaction == "withdraw"):
				self.withdraw()
			elif (transaction == "deposit"):
				self.deposit()	
			elif (transaction == "transfer"):
				self.transfer()		
			elif (transaction == "logout"):
				running = False
			else:
				print "Please enter a valid transaction type."	
		return False	
		

class agent(object):
	def __init__(self, type):
		self.type = type
	def withdraw():
		return 0 
	def deposit():
		return 0 
	def transfer():
		return 0 
	def create():
		return 0 
	def delete():
		return 0 
	def runAgentDay():
		running = True
		while (running):
			transaction = raw_input('Perform a transaction: ')
			transaction.lowercase
			if (transaction == "withdraw"):
				self.withdraw()
			elif (transaction == "deposit"):
				self.deposit()	
			elif (transaction == "transfer"):
				self.transfer()	
			elif (transaction == "create"):
				self.create()	
			elif (transaction == "delete"):
				self.delete()	
			elif (transaction == "logout"):
				running = False
			else:
				print "Please enter a valid transaction type."	
		return False				


def openBankingSystem():
	loggedIn = True
	while (loggedIn):
		firstInput = raw_input('Type "login" to login: ')
		firstInput.lowercase
		if (firstInput == "login"):
			pickDay = True
			while (pickDay):
				dayType = raw_input('agent or retail: ')
				dayType.lowercase
				if (dayType == "retail"):
					pickDay = False
					retailDay = retail(dayType)
					loggedIn = retailDay.runRetailDay()
				elif (dayType == "agent"):
					pickDay = False	
					agentDay = agent(dayType)
					loggedIn = agentObject.runAgentDay()
				else: 
					print "Please enter a valid input.\n"
		else:
			print "Please enter a valid input.\n"
	return openBankingSystem()			

######	 MAIN PROGRAM 	######
openBankingSystem()
#needs file writing