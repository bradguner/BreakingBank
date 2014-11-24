import sys

def transaction(masterAccts,trans):
	#take trans, split by _ into list
	transCopy = trans.split('_') #[CC, AAAAAA, BBBBBB, MMMMMMMM, NNNNNNNNNNNNNNN]
	master = []
	for i in range(len(masterAccts)):
		master.append(masterAccts[i])
	for i in range(len(master)):
		master[i] = master[i].split('_')
	
	print transCopy[0]	
	if (transCopy[0] == '01'):	#deposit
		for acct in range(len(masterAccts)):
			if (master[acct][0] == transCopy[1]):
				acctBalance = int(master[acct][1])
				depAmount = int(transCopy[3])
				acctBalance += depAmount
				master[acct][1] = str(master[acct][1])
				master[acct][1] = str(acctBalance)
				newStr = format(master[acct][0], master[acct][1], master[acct][2])
				masterAccts[acct] = newStr
		return masterAccts

	#withdraw
	elif (transCopy[0] == '02'):	
		for acct in range(len(masterAccts)):
			if (master[acct][0] == transCopy[1]):
				acctBalance = int(master[acct][1])
				depAmount = int(transCopy[3])
				acctBalance -= depAmount
				master[acct][1] = str(master[acct][1])
				master[acct][1] = str(acctBalance)
				newStr = format(master[acct][0], master[acct][1], master[acct][2])
				masterAccts[acct] = newStr
		return masterAccts

	elif (transCopy[0] == '03'):	#transfer
		for acct in range(len(masterAccts)):
			if (master[acct][0] == transCopy[1]):
				for anotherAcct in range(len(masterAccts)):
					if (master[anotherAcct][0] == transCopy[2]):
						recAcctBalance = int(master[acct][1])
						transAcctBalance = int(master[anotherAcct][1])
						transAmt = int(transCopy[3])
						recAcctBalance += transAmt
						transAcctBalance -= transAmt
						master[acct][1] = str(master[acct][1])
						master[anotherAcct][1] = str(master[acct][1])
						newStrFirstAcct = format(master[acct][0], master[acct][1], master[acct][2])
						masterAccts[acct] = newStr
						newStr = format(master[anotherAcct][0], master[anotherAcct][1], master[anotherAcct][2])
						masterAccts[anotherAcct] = newStr
		return masterAccts

	elif (transCopy[0] == '04'):
		acctNum = int(transCopy[1])
		newStr = format(transCopy[1], transCopy[3], transCopy[4])
		for acct in range(len(master)): 
				if (master[acct][0] == acctNum):
					throwError()
				else:
					current = int(master[acct][0])
					if (acctNum < current):
						masterAccts.insert(acct, newStr)
						return masterAccts
		masterAccts.append(newStr)
		return masterAccts

	elif (transCopy[0] == '05'):	#delete _ do decision testing, need a test case it evaluate every if both ways
		acctNum = str(transCopy[1])
		transAcctName = str(transCopy[4])
		for acct in range(len(master)): 
			if (acctNum == master[acct][0]):
				acctBalance = master[acct][1]
				if (acctBalance == '00000000'):
					acctName = str(master[acct][2])
					if (transAcctName == acctName):
						masterAccts = masterAccts.remove(masterAccts[acct])
					else:
						throwError()
				else:
					throwError()
		return masterAccts

	elif (transCopy[0] == '00'):
		return masterAccts

def format(num, balance, name):
	string = str(num) + "_" + str(balance) + "_" + str(name)
	return string

def writeNewMasterAccounts(list):
	f = open('./masteraccounts.txt','w')
	for i in list:							
		f.write(i + "\n")					
	f.close()
	return 0

def writeNewValidAccounts(list):	# needs to be split and only the account numbes		
	f = open('./validaccounts.txt','w')		
	for i in list:							
		f.write(i + "\n")	
	f.write("000000\n")					
	f.close()								
	return 0

def throwError():
	sys.exit('Fatal Error')

def main_program():
	#open master accounts
	masteraccts = []
	f = open('./masteraccounts.txt')
	masteraccts = f.readlines()
	for x in range(len(masteraccts)):
		masteraccts[x] = masteraccts[x].strip()
	f.close()

	#open merged transaction file
	mergedtrans= []
	f = open('./mergedtransactions.txt', 'r')
	mergedtrans = f.readlines()
	for x in range(len(mergedtrans)):
		mergedtrans[x] = mergedtrans[x].strip()
	f.close()

	print mergedtrans
	#for all transactions update the master accounts file
	for i in mergedtrans:
		if (i == "00"):
			print masteraccts
			writeNewValidAccounts(masteraccts)
			writeNewMasterAccounts(masteraccts)
		else:
			masteraccts = transaction(masteraccts,i)

	#writes output files
	#print masteraccts
	#writeNewValidAccounts(masteraccts)
	#writeNewMasterAccounts(masteraccts)
	return 0

main_program()
