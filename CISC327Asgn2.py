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
	def withdraw(self):
		return 0
	def deposit(self):
		return 0 
	def transfer(self):
		return 0 
	def runRetailDay(self):
		running = True
		while (running):
			transaction = raw_input('Perform a transaction: ')
			transaction.lower()
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
	def withdraw(self):
		return 0 
	def deposit(self):
		return 0 
	def transfer(self):
		return 0 
	def create(self):
		return 0 
	def delete(self):
		return 0 
	def runAgentDay(self):
		running = True
		while (running):
			transaction = raw_input('Perform a transaction: ')
			transaction.lower()
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
		firstInput.lower()
		if (firstInput == "login"):
			pickDay = True
			while (pickDay):
				dayType = raw_input('agent or retail: ')
				dayType.lower()
				if (dayType == "retail"):
					pickDay = False
					retailDay = retail(dayType)
					loggedIn = retailDay.runRetailDay()
				elif (dayType == "agent"):
					pickDay = False	
					agentDay = agent(dayType)
					loggedIn = agentDay.runAgentDay()
				else: 
					print "Please enter a valid input.\n"
		else:
			print "Please enter a valid input.\n"
	#FILE SHOULD WRITE NOW BEFORE WE OFFICIALLY END DAY		
	return openBankingSystem()			

######	 MAIN PROGRAM 	  ######
openBankingSystem()

#ERROR AND TODO LOG
#needs file writing
#wont accept any whitespace on string
#methods in each agent and retail
