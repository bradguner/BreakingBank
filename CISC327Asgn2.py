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
		return 0	

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
		return 0	

def openBankingSystem():
	loggedIn = true
	while (loggedIn):
		firstInput = raw_input('Type "login" to login: ')
		firstInput.lowercase
		if (firstInput = "login"):
			pickDay = true
			while (pickDay)
				dayType = raw_input('agent or retail: ')
				dayType.lowercase
				if (dayType = "retail"):
					pickDay = false
					retailDay = retail(dayType)
					loggedIn = retailDay.runRetailDay()
				else if (dayType = "agent"):
					pickDay = false	
					agentDay = agent(dayType)
					loggedIn = agentObject.runAgentDay()
				else: 
					print "Please enter a valid input.\n"
		else:
			print "Please enter a valid input.\n"
	return openBankingSystem()			

######	 MAIN PROGRAM 	######
openBankingSystem()