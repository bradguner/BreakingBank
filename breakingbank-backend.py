"""
constraints
no negative balances
deleted account has zero balance, dpes it disappear?
created account should not have existing acc num,, 2 create same number
nam egiven for delete myst have a mathcing name

constraint fails and the fatal error stop
"""
def transaction(masterAccts,trans):
	#take trans, split by _ into list
	transCopy = trans.split('_') #[CC, AAAAAA, BBBBBB, MMMMMMMM, NNNNNNNNNNNNNNN]
	master = []
	for i in range(len(masterAccts)):
		master.append(masterAccts[i])
	for i in range(len(master)):
		master[i] = master[i].split('_')
		
	#deposit
	if (transCopy[0] == '01'):
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

	elif (transCopy[0] == '02'):	#same as deposit, just subtract from the account
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

	elif (transCopy[0] == '03'):
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
		#create neeeds check on account num, everything else should be working
		temp = 0
		acctNum = int(trans[1])
		newStr = format(trans[1], trans[3], trans[4])
		for acct in range(master):
			first = int(master[acct][0])
			if (acct + 1 <= range(master)):
				second = int(master[acct + 1][0])
			else:
				second = 'None'
			if (accNum < first):
				masterAccts.insert(acct - 1, newStr)
			elif (accNum > first and accNum < second):
				masterAccts.insert(acct, newStr)
			elif (accNum > first and second == 'None'):
				masterAccts.insert(acct, newStr)
		return masterAccts
	elif (transCopy[0] == '05'):
		#delete

		return 0
	elif (transCopy[0] == '00'):
		#end of session, skip
		return 0

def format(num, balance, name):
	string = "111111_1_NNNNNNNNNNNNNNN"
	return string

def writeNewMasterAccounts(list):
	f = open('./masteraccounts.txt','w')
	for i in list:
		f.write(i + "\n")
	f.close()
	return 0

def writeNewValidAccounts(list):
	f = open('./validaccounts.txt','w')
	for i in list:
		#wrong doesnt write it correctly
		f.write(i + "\n")
	f.close()
	return 0

def throwError():
	print "Fatal Error"
	return 0

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
	f = open('./mergedtransactions.txt')
	mergedtrans = f.readlines()
	for x in range(len(mergedtrans)):
		mergedtrans[x] = mergedtrans[x].strip()
	f.close()
	#for all transactions update the master accounts file
	for i in mergedtrans:
		masteraccts = transaction(masteraccts,i)
	#writes output files
	writeNewValidAccounts(masteraccts)
	writeNewMasterAccounts(masteraccts)
	return 0

main_program()