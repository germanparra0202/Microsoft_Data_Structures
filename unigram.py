#!/usr/bin/env python3
# Uses unigram to find probabilites of commands. Assumes format of file is the format of the history file with date and time (this can easily be changed). Takes as many files as you want, just list them all as command line arguments 

import sys

# creates and return a dictionary with the count of each command
def unigram(d, data):
	for line in open(data):
		command = ' '.join(line.split()[3:])
		d[command] = d.get(command, 0) + 1

	return d
		
def main():
	probabilities = {}
	arguments = sys.argv[1:]

	# iterate through every command line argument (file)
	while arguments:
		argument = arguments.pop(0)
		probabilities = unigram(probabilities, argument)

	# convert counts in dictionary to probabilities 
	total = sum(probabilities.values())
	for command, count in probabilities.items():
		count = count/total
		print('{:7} {}'.format(command, count)) # just so you can see what the output is, obviuously the real program wont print all of this 

if __name__ ==  '__main__':
	main()


	
		
