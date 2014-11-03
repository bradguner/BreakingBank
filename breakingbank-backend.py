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
	master = masterAccts.split('_')

	if (transCopy[0] == '01'):
		#add amount from trans[3] to trans[1]
		for acct in range(len(master)):
			if (master[acct][0] == transCopy[1]):
				acctBalance = int(master[acct][1])
				depAmount = int(transCopy[3])
				acctBalance += depAmount
				acct[1] = str(acctBalance)
				newStr = master[acct][0] + '_' + master[acct][1] + '_' + master[acct][2]
				masterAccts[acct] = newStr
				return masterAccts

	elif (transCopy[0] == '02'):
		#subtract amount from trans[3] from trans[1]
	elif (transCopy[0] == '03'):
		#transfer
	elif (transCopy[0] == '04'):
		#create
	elif (transCopy[0] == '05'):
		#delete
	elif (transCopy[0] == '00'):
		#end of session, skip
	
	
	#edit the list in each case
	return list

def writeNewMasterAccounts(list):
	f = open('./masteraccounts.txt','w')
	for i in list:
		f.write(i + "\n")
	f.close()
	return 0

def writeNewValidAccounts(list):
	f = open('./validaccounts.txt','w')
	for i in list:
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