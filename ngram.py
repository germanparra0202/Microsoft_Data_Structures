#!/usr/bin/env python3
# Uses unigram to find probabilites of commands. Assumes format of file is the format of the history file with date and time (this can easily be changed). Takes as many files as you want, just list them all as command line arguments 

import sys

def make_list(command_list, data):
	temp = [(line.strip()).split()[3:] for line in open(data)]
	command_list.extend(temp)

	return command_list

def ngram(n, data):
	numer_count = {}
	denom_count = {}
	numer_prob = {}
	denom_prob = {}
	final = {}
	numer_total = len(data) - n
	denom_total = len(data) - (n-1)

	for i in range(0,len(data)-n):
		wcommand = ':'.join(map(str, data[i:i+n+1]))
		previous = ':'.join(map(str, data[i:i+n]))
		numer_count[wcommand] = numer_count.get(wcommand, 0) + 1
		numer_prob[wcommand] = numer_count[wcommand]/numer_total
		denom_count[previous] = denom_count.get(previous, 0) + 1
		denom_prob[previous] = denom_count[previous]/denom_total
		final[wcommand] = numer_prob[wcommand]/denom_prob[previous]
		if final[wcommand] > 1:
			final[wcommand] = 1

	return final

def test(n, probabilities):
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
	#for command, count in sorted(probabilities.items(), key=lambda k: k[1], reverse = True):
		#print('{:7} {}'.format(command, count))
	
	#for command, count in probabilities.items():
 		#print('{:7} {}'.format(command, count)) 

if __name__ ==  '__main__':
	main()


	
		
