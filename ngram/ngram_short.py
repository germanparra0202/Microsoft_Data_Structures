#!/usr/bin/env python3
# Uses ngrams to find probabilites of commands. Assumes format of file is the format of the history file with date and time (this can easily be changed). Takes as many files as you want, just list them all as command line arguments. Creates a dictionary with the FIRST WORD of each command as the key and the probabilities as the value. Calls test function which given previous commands, prints the FIRST WORD of the following command with the highest probability, along with its probability 

import sys

def make_list(command_list, data):
	'''Takes in a text file and a list, appends each line of the file as an element of the list. Returns the list'''
	temp = [(line.strip()).split()[3:] for line in open(data)]
	command_list.extend(temp)

	return command_list

def ngram(n, data):
	'''Takes in n (number of ngrams) and a list of data. Uses the conditional probability formula to create a dictionary that calculates the probability of each command in the list given the first word of each of the n previous commands.Keys are a string containing these first words and the first word of the current command (each word is separated by a space) and values are the probabilities. Returns the dictionary'''
	numer_count = {}
	denom_count = {}
	numer_prob = {}
	denom_prob = {}
	final = {}
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
		final[wcommand] = numer_prob[wcommand]/denom_prob[previous]
		if final[wcommand] > 1:
			final[wcommand] = 1

	return final

def test(n, probabilities):
	'''Tests the ngram program. Takes in the probabilities dictionary and n. Each command that is hardcoded represents the previous commands. The first word of the command that has the highest probability of following the first words of these commands is printed along with the probability. If the probability of the previous commands is 0, nothing is printed. NEED MUCH DATA TO MAKE THIS GOOD'''
	#feel free to play around with/change things 
	command1 = "ls"
	command2 = "make clean"
	lcommand1 = command1.split()[0]
	lcommand2 = command2.split()[0]
	target = str(lcommand1) + " " + str(lcommand2) + " " 
	for key, value in sorted(probabilities.items(), key=lambda k: k[1], reverse = True):
		if target in key:
			command = ''.join((key.split())[n])
			print(command, value)
			break
	
		
		
def main():
	n = 2
	probabilities = {}
	command_list = []
	arguments = sys.argv[1:]

	# iterate through every command line argument (file)
	while arguments:
		argument = arguments.pop(0)
		command_list = make_list(command_list, argument)

	probabilities = ngram(n, command_list)
	test(n, probabilities)
	#can uncomment the code below if you would like to see the full dictionary printed 
	#for command, count in sorted(probabilities.items(), key=lambda k: k[1], reverse = True):
		#print('{:7} {}'.format(command, count))
	

if __name__ ==  '__main__':
	main()


	
		
