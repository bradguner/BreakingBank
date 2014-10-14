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