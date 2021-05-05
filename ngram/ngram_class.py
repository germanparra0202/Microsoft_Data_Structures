
def make_list(command_list, data):
	''' Appends each line of data to command_list

	Takes in a text file and a list, appends each line of the file as an element of
	the list. Returns the list 
	'''

	data_file = open(data)
	temp = [(line.strip()).split()[3:] for line in data_file]
	data_file.close()
	command_list.extend(temp)

	return command_list

def line_test(n, probabilities):
	'''Tests the ngram program
		
	Takes in the probabilities dictionary and n. Each command that is hardcoded 
	represents the previous commands. The command that has the highest probability 
	of following these commands is printed along with the probabilitiy. If the 
	probability of the previous commands is 0, nothing is printed. NEED MUCH DATA 
	TO MAKE THIS GOOD
	'''

	#feel free to play around with/change things
	command1 = "make -n"
	command2 = "make clean"
	lcommand1 = command1.split()
	lcommand2 = command2.split()
	target = str(lcommand1) + ":" + str(lcommand2) + ":"
	for key, value in sorted(probabilities.items(), key=lambda k: k[1], reverse = True):
		if target in key:
			command = ''.join((key.split(":"))[n])
			command = command.replace("[", "")
			command = command.replace("]", "")
			command = command.replace("'", "", 100)
			command = command.replace(",", "", 100)
			print(command, value)
			break

def word_test(n, commands, probabilities):
	'''Tests the ngram program

	Takes in the probabilities dictionary and n. Each command that is hardcoded 
	represents the previous commands. The first word of the command that has the 
	highest probability of following the first words of these commands is 
	printed along with the probability. If the probability of the previous 
	commands is 0, nothing is printed. NEED MUCH DATA TO MAKE THIS GOOD
	'''
	target = ""
	for command in commands:
		target += str(command.split()[0]) + " "
	for key, value in sorted(probabilities.items(), key=lambda k: k[1], reverse = True):
		if target in key:
			command = ''.join((key.split())[n])
			return command
			#print(command, value)
			break

class Ngram:
	''' Uses ngrams to find probabilites of commands

	Assumes format of file is the format of the history file with date and time (this can 
	easily be changed). Takes as many files as you want, just list them all as command 
	line arguments. Creates a dictionary with each sequence of commands as the key and 
	the probabilties as the value. Calls test function which given previous commands, 
	prints the following command with the highest probability, along with its probability  
	'''
	
	def __init__(self):
		self.prob_dict = {}

	def line_ngram(self, n, data):
		''' Calculates ngram probability for command line

		Takes in n (number of ngrams) and a list of data. Uses the conditional probability 
		formula to create a dictionary that calculates the probability of each command in 
		the list given the n previous commands. Keys are a string containing the n 
		previous commands and the current command (each command separated by a ":") and 
		values are the probabilities. Returns the dictionary
		'''

		if len(self.prob_dict) > 0:
			return

		numer_count = {}
		denom_count = {}
		numer_prob = {}
		denom_prob = {}
		numer_total = len(data) - n
		denom_total = len(data) - (n-1)

		for i in range(0,len(data)-n):
			wcommand = ':'.join(map(str, data[i:i+n+1]))
			previous = ':'.join(map(str, data[i:i+n]))
			numer_count[wcommand] = numer_count.get(wcommand, 0) + 1
			numer_prob[wcommand] = numer_count[wcommand]/numer_total
			denom_count[previous] = denom_count.get(previous, 0) + 1
			denom_prob[previous] = denom_count[previous]/denom_total
			# P(current command | previous commands) = P(current command and previous commands)
			#	/P(previous commands)
			self.prob_dict[wcommand] = numer_prob[wcommand]/denom_prob[previous]
			if self.prob_dict[wcommand] > 1:
				self.prob_dict[wcommand] = 1

	def word_ngram(self, n, data):
		''' Calculates ngram probability for first word of command line

		Takes in n (number of ngrams) and a list of data. Uses the conditional 
		probability formula to create a dictionary that calculates the probability of 
		each command in the list given the first word of each of the n previous 
		commands. Keys are a string containing these first words and the first word 
		of the current command (each word is separated by a space) and values are the 
		probabilities. Returns the dictionary
		'''

		if len(self.prob_dict) > 0:
			return

		numer_count = {}
		denom_count = {}
		numer_prob = {}
		denom_prob = {}
		numer_total = len(data) - n
		denom_total = len(data) - (n-1)

		for i in range(0,len(data)-n):
			wcommand = ""
			previous = ""
			for j in range(0, n+1):
				wcommand = wcommand + " " + str(data[i:i+n+1][j][0])
			for j in range(0, n):
				previous = previous + " " + str(data[i:i+n][j][0])
			numer_count[wcommand] = numer_count.get(wcommand, 0) + 1
			numer_prob[wcommand] = numer_count[wcommand]/numer_total
			denom_count[previous] = denom_count.get(previous, 0) + 1
			denom_prob[previous] = denom_count[previous]/denom_total
			self.prob_dict[wcommand] = numer_prob[wcommand]/denom_prob[previous]
			if self.prob_dict[wcommand] > 1:
				self.prob_dict[wcommand] = 1

	def display(self):
		for command, count in sorted(self.prob_dict.items(), key=lambda k: k[1], reverse = True):
			print('{:7} {}'.format(command, count))
	
