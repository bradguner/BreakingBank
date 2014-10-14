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
			accNum = input('Account Number: ')
			#CHECK TO SEE IF VALID ACCOUNT NUMBER
			if (1 == 1): #if account num is valid
				amt = True
				accNumInput = False
				while (amt):
					amount = int(input('Withdrawal Amount: '))
					if (amount > 1000 || amount < 0):
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
					if (amount > 1000 || amount < 0):
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
			accNumTo = input('To Account Number: ')
			#CHECK to SEE IF FIRST ACCOUNT NUMBER IS VALID
			if (1 == 1):
				while (accNumInput2):
					accNumFrom = input('From Account Number: ')
					#CHECK TO SEE IF SECOND ACCOUNT NUMBER IS VALID
					if (1 == 1):
						accNumTo = False
						accNumFrom = False
						amt = True
						while (amt):
							amount = int(input('Transfer Amount: '))
							if (amount > 1000 || amount < 0):
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
###########################################################################################################		
		
############################################	AGENT 	  #################################################		
class agent(object):
	def __init__(self, type):
		self.type = type
		
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
					if (amount > 9999.99 || amount < 0):
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
			accNum = input('Account Number: ')
			#CHECK TO SEE IF VALID ACCOUNT NUMBER
			if (1 == 1): #if account num is valid
				amt = True
				accNumInput = False
				while (amt):
					amount = int(input('Deposit Amount: '))
					if (amount > 9999.99 || amount < 0):
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
			accNumTo = input('To Account Number: ')
			#CHECK to SEE IF FIRST ACCOUNT NUMBER IS VALID
			if (1 == 1):
				while (accNumInput2):
					accNumFrom = input('From Account Number: ')
					#CHECK TO SEE IF SECOND ACCOUNT NUMBER IS VALID
					if (1 == 1):
						accNumTo = False
						accNumFrom = False
						amt = True
						while (amt):
							amount = int(input('Transfer Amount: '))
							if (amount > 9999.99 || amount < 0):
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
		return 0
	def delete(self):
		return 0		
	
	#METHOD WHICH RUNS ANY TRANSACTIONS FOR A RETAIL DAY
	#WILL WRITE ANY TRANSACTIONS TO FILE
	#LOGOUT IS ACCEPTED AT THIS STAGE
	def runAgentDay(self):
		running = True
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
