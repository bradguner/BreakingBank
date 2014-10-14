"""
CISC 327
Breaking Bank
Assignment #2
Scott Wallace 10051890
Brad Guner 10059112
"""
import datetime
import time
import os.path

class retail(object):
	def __init__(self, type,dailylimit):
		self.type = type
		self.dailylimit = dailylimit
		
	def withdraw(self):
		accNumInput = True
		while (accNumInput):
			accNum = input('Account Number: ')
			#CHECK TO SEE IF VALID ACCOUNT NUMBER
			if (1 == 1): #if account num is valid
				amt = True
				accNumInput = False
				while (amt):
					amount = int(input('Withdrawal Amount: '))
					if (amount > 1000):
						print "Please enter a valid amount."
					elif (self.dailylimit + amount > 1000):
						print "This amount exceeds your daily limit."
					else: 
						self.dailylimit += amount
						amt = False
						#CREATE STRING TO WRITE TO FILE
						accNum = str(accNum)
						amount = str(amount)
						transactionInfo = '02_' + accNum + '_' + amount #NEEDS PROPER FORMATTING STILL
			else:
				print "Please enter a valid account number."
		return transactionInfo	
		#return transactionInfo		
	
	def deposit(self):
		accNumInput = True
		while (accNumInput):
			accNum = input('Account Number: ')
			#CHECK TO SEE IF VALID ACCOUNT NUMBER
			if (1 == 1): #if account num is valid
				amt = True
				accNumInput = False
				while (amt):
					amount = int(input('Deposit Amount: '))
					if (amount > 1000):
						print "Please enter a valid amount."
					else: 
						amt = False
						#CREATE STRING TO WRITE TO FILE
						accNum = str(accNum)
						amount = str(amount)
						transactionInfo = '01_' + accNum + '_' + amount #NEEDS PROPER FORMATTING STILL
			else:
				print "Please enter a valid account number."
		return transactionInfo	
		#return transactionInfo
		
	def transfer(self):
		return 0
		
	#METHOD WHICH RUNS ANY TRANSACTIONS FOR A RETAIL DAY
	#WILL WRITE ANY TRANSACTIONS TO FILE
	#LOGOUT IS ACCEPTED AT THIS STAGE
	def runRetailDay(self):
		running = True
		#READ IN CURRENT ACCOUNTS FILE GOES HERE
		#CREATES TRANSACTION SUMMARY FILE
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		save_path = 'C:/TransactionSummaryFiles/'
		file = 'Transaction_Summary_File__' + st + '.txt'
		filename = file.replace(":", "_")
		completeName = os.path.join(save_path, filename) 
		f = open(completeName,'w')
		while (running):
			#STARTS ACCEPTING RETAIL TRANSACTIONS
			transaction = str(input('Perform a transaction: '))
			transaction.lower()
			#TESTS INPUT FOR WHICH TRANSACTION TYPE TO PERFORM
			if (transaction == "withdraw"):
				newTrans = self.withdraw()
				f.write(newTrans + '\n')
			elif (transaction == "deposit"):
				newTrans = self.deposit()
				f.write(newTrans + '\n')
			elif (transaction == "transfer"):
				newTrans = self.transfer()
				f.write(newTrans + '\n')
			elif (transaction == "logout"):
				f.close()
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
			transaction = str(input('Perform a transaction: '))
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
		#GETS LOGIN TO START, STAGE 0
		firstInput = str(input('Type "login" to login: '))
		firstInput.lower()
		if (firstInput == "login"):
			pickDay = True
			while (pickDay):
				#ACCEPTS INPUT FOR AGENT OR RETAIL, STAGE 1
				dayType = str(input('agent or retail: '))
				dayType.lower()
				if (dayType == "retail"):
					pickDay = False
					retailDay = retail(dayType,0)
					loggedIn = retailDay.runRetailDay()
				elif (dayType == "agent"):
					pickDay = False	
					agentDay = agent(dayType)
					loggedIn = agentDay.runAgentDay()
				else: 
					print "Please enter a valid input.\n"
		else:
			print "Please enter a valid input.\n"
	#STARTS OVER AGAIN AFTER LOGOUT AT STAGE 0
	return openBankingSystem()			

######	 MAIN PROGRAM 	  ######
#open current accounts file
openBankingSystem()
#close curren accounts file

#ERROR AND TODO LOG
#wont accept any whitespace on string
#methods in each agent and retail
#code needs comments and variable names may need work
