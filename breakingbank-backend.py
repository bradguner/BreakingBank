"""
reads in merged trans file
ends in 00
for each line perform said transaciton on master accounts

constraints
no negative balances
deleted account has zero balance, dpes it disappear?
created account should not have existing acc num,, 2 create same number
nam egiven for delete myst have a mathcing name

constraint fails and the fatal error stop
"""
def transaction(trans):
	return 0

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
	#for all tranasactions update the master accounts file
	for i in mergedtrans:
		transaction(i)
	#writes output files
	writeNewValidAccounts(masteraccts)
	writeNewMasterAccounts(masteraccts)


	return 0

main_program()