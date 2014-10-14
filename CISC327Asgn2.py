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

############################################	RETAIL 	  #################################################
class retail(object):
	def __init__(self, type,dailylimit):
		self.type = type
		self.dailylimit = dailylimit
		
	def withdraw(self):
		accNumInput = True
		while (accNumInput):
			accNum = raw_input('Account Number: ')
			#CHECK TO SEE IF VALID ACCOUNT NUMBER
			if (1 == 1): #if account num is valid
				amt = True
				accNumInput = False
				while (amt):
					amount = int(input('Withdrawal Amount: '))
					amount = amount*100
					if (amount > 100000):
						print "Please enter a valid amount."
					elif (amount < 0):
						print "Please enter a valid amount."	
					elif (self.dailylimit + amount > 100000):
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
	
	def deposit(self):
		accNumInput = True
		while (accNumInput):
			accNum = raw_input('Account Number: ')
			#CHECK TO SEE IF VALID ACCOUNT NUMBER
			if (1 == 1): #if account num is valid
				amt = True
				accNumInput = False
				while (amt):
					amount = int(input('Deposit Amount: '))
					amount = amount*100
					if (amount > 100000):
						print "Please enter a valid amount."
					elif (amount < 0):
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
		
	def transfer(self):
		accNumInput = True
		accNumInput2 = True
		while(accNumInput):
			accNumTo = raw_input('To Account Number: ')
			#CHECK to SEE IF FIRST ACCOUNT NUMBER IS VALID
			if (1 == 1):
				while (accNumInput2):
					accNumFrom = raw_input('From Account Number: ')
					#CHECK TO SEE IF SECOND ACCOUNT NUMBER IS VALID
					if (1 == 1):
						accNumTo = False
						accNumFrom = False
						amt = True
						while (amt):
							amount = int(input('Transfer Amount: '))
							amount = amount*100
							if (amount > 100000):
								print "Please enter a valid transfer amount."
							elif (amount < 0):
								print "Please enter a valid transfer amount."	
							else:
								amt = False
								#create string for write file
								accNumTo = str(accNumTo)
								accNumFrom = str(accNumFrom)
								amount = str(amount)
								transactionInfo = '03_' + accNumTo + '_' + accNumFrom + '_' + amount
					else:
						print "Please enter a valid account number."		
			else:
				print "Please enter a valid account number."
		return transactionInfo	
	
	#METHOD WHICH RUNS ANY TRANSACTIONS FOR A RETAIL DAY
	#WILL WRITE ANY TRANSACTIONS TO FILE
	#LOGOUT IS ACCEPTED AT THIS STAGE
	def runRetailDay(self):
		running = True
		#CREATES TRANSACTION SUMMARY FILE
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		save_path = './TransactionSummaryFiles/'
		file = 'Transaction_Summary_File__' + st + '.txt'
		filename = file.replace(":", "_")
		completeName = os.path.join(save_path, filename) 
		f = open(completeName,'w')
		while (running):
			#STARTS ACCEPTING RETAIL TRANSACTIONS
			transaction = raw_input('Perform a transaction: ')
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
###########################################################################################################		
		
############################################	AGENT 	  #################################################		
class agent(object):
	def __init__(self, type):
		self.type = type
		
	def withdraw(self):
		accNumInput = True
		while (accNumInput):
			accNum = raw_input('Account Number: ')
			#CHECK TO SEE IF VALID ACCOUNT NUMBER
			if (1 == 1): #if account num is valid
				amt = True
				accNumInput = False
				while (amt):
					amount = int(input('Withdrawal Amount: '))
					amount = amount*100
					if (amount > 999999):
						print "Please enter a valid amount."
					elif (amount < 0):
						print "Please enter a valid amount."
					else: 
						amt = False
						#CREATE STRING TO WRITE TO FILE
						accNum = str(accNum)
						amount = str(amount)
						transactionInfo = '02_' + accNum + '_' + amount #NEEDS PROPER FORMATTING STILL
			else:
				print "Please enter a valid account number."
		return transactionInfo		
	
	def deposit(self):
		accNumInput = True
		while (accNumInput):
			accNum = raw_input('Account Number: ')
			#CHECK TO SEE IF VALID ACCOUNT NUMBER
			if (1 == 1): #if account num is valid
				amt = True
				accNumInput = False
				while (amt):
					amount = int(input('Deposit Amount: '))
					amount = amount*100
					if (amount > 999999):
						print "Please enter a valid amount."
					elif (amount < 0):
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
		
	def transfer(self):
		accNumInput = True
		accNumInput2 = True
		while(accNumInput):
			accNumTo = raw_input('To Account Number: ')
			#CHECK to SEE IF FIRST ACCOUNT NUMBER IS VALID
			if (1 == 1):
				while (accNumInput2):
					accNumFrom = raw_input('From Account Number: ')
					#CHECK TO SEE IF SECOND ACCOUNT NUMBER IS VALID
					if (1 == 1):
						accNumInput = False
						accNumInput2 = False
						amt = True
						while (amt):
							amount = int(raw_input('Transfer Amount: '))
							amount = amount*100
							if (amount > 999999):
								print "Please enter a valid transfer amount."
							elif (amount > 999999):
								print "Please enter a valid transfer amount."	
							else:
								amt = False
								#create string for write file
								accNumTo = str(accNumTo)
								accNumFrom = str(accNumFrom)
								amount = str(amount)
								transactionInfo = '03_' + accNumTo + '_' + accNumFrom + '_' + amount
					else:
						print "Please enter a valid account number."		
			else:
				print "Please enter a valid account number."
		return transactionInfo	

	def create(self):
		accNumInput = True
		accNameInput = True
		while (accNumInput):
			accNum = int(input('Enter your desired account number: '))
			#if (accNum < 1000000 && accNum >= 0):	#Account Number must be 6 digits. Maximum of 999999, so if < 1000000, account number is 6 digits long
			#	#CHECK TO SEE IF INPUT ACCOUNT NUMBER DOES NOT EXIST
				if (1 == 1):
					accNumInput = False
					while (accNameInput): 
						accName = str(input('Enter your desired account name: '))
						if (accName.Length > 15 || accName.Length == 0):
							print "Please enter a valid account name."
						else:
							accNameInput = False
							#create string for write file
							accNum = str(accNum)
							accName = str(accName)
							transactionInfo = '04_' + accNum + "_" + accName #proper formatting on end of string is needed
				else:
					print "Please enter a valid account number."
			#else:
			#	print "Please anter a valid account number."
		return transactionInfo

	def delete(self):
		accNumInput = True
		accNameInput = True
		while (accNumInput):
			accNum = int(input('Enter your account number: '))
			#CHECK TO SEE IF INPUT ACCOUNT NUMBER EXISTS
			if (1 == 1):
				accNumInput = False
				while (accNameInput):
					accName = str(input('Enter your desired account name: '))
					#CHECK TO SEE IF INPUT ACCOUNT NAME MATCHES ACCOUNT NUMBER
					if (1 == 0):
						print "Please enter the proper account name for this account."
					else:
						accNameInput = False
						#create string for write file
						accNum = str(accNum)
						accName = str(accName)
						transactionInfo = '05_' + accNum + '_' + accName #proper formatting on end of string is needed
			else:
				print "Please enter a valid account number."
		return transactionInfo
	
	#METHOD WHICH RUNS ANY TRANSACTIONS FOR A RETAIL DAY
	#WILL WRITE ANY TRANSACTIONS TO FILE
	#LOGOUT IS ACCEPTED AT THIS STAGE
	def runAgentDay(self):
		running = True
		#CREATES TRANSACTION SUMMARY FILE
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		save_path = './TransactionSummaryFiles/'
		file = 'Transaction_Summary_File__' + st + '.txt'
		filename = file.replace(":", "_")
		completeName = os.path.join(save_path, filename) 
		f = open(completeName,'w')
		while (running):
			#STARTS ACCEPTING RETAIL TRANSACTIONS
			transaction = raw_input('Perform a transaction: ')
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
			elif (transaction == "create"):
				newTrans = self.create()
				f.write(newTrans + '\n')
			elif (transaction == "delete"):
				newTrans = self.delete()
				f.write(newTrans + '\n')		
			elif (transaction == "logout"):
				f.close()
				running = False
			else:
				print "Please enter a valid transaction type."	
		return False
					
###########################################################################################################	

def openBankingSystem():
	loggedIn = True
	while (loggedIn):
		#GETS LOGIN TO START, STAGE 0
		firstInput = raw_input('Type "login" to login: ')
		firstInput.lower()
		if (firstInput == "login"):
			pickDay = True
			while (pickDay):
				#ACCEPTS INPUT FOR AGENT OR RETAIL, STAGE 1
				dayType = raw_input('agent or retail: ')
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
