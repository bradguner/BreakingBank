class retail():
	#initialize class
	function runRetailDay():
		#so in the funcition it will basically run a loop, gets 
		#inputs and does a test based on inputs and selects a function to run
		#each method within the retail class would get called
		#each methond has its own input checking 
	function withdraw
	function deposit
	function tranfer

class agent():
	#initialize class
	function runAgentDay():
	function withdraw
	function deposit
	function tranfer
	function create
	function delete	


function openBankingSystem():
	loggedIn = true
	while (loggedIn):
		#get input
		if (input = "login"):
			#get second input
			pickDay = true
			while (pickDay)
				if (input = "retail"):
					pickDay = false
					#new retail object
					loggedIn = retailObject.runRetailDay()
				else if (input = "agent"):
					pickDay = false	
					#new agent object
					loggedIn = agentObject.runAgentDay()
				else: #get new second input and start loop over	
		else:
			print INVALID INPUT		
	#end while
	return openBankingSystem()				

#MAIN PROGRAM
openBankingSystem()	

