#!/usr/bin/env python3

import sys
import json 
from ngram_class import word_test

def main():
	'''
	Program to similuate a mock shell and provide command predictions

	Program takes in at least one file in the command line that has history data formatted 
	with the date and time. Calls the Ngram class to build a dictionary of probabilities 
	based on this data. After inputting at least n (2) commands, runs until the user enters 
	q. Using the ngram probabilities, predicts the first word of the succeeding command 
	after every new command is entered. The user can enter n to delete the prediction or 
	continue typing the command to accept it.

	- Code written by Danielle, slightly modified by others 
	'''

	# Import data
	with open(f'ngram_data.txt', 'r') as f:
		probabilities = json.load(f)
	
	# Initialize Variables
	n = 2
	commands = []
	count = 0

	# Display options
	print('Enter two commands on separate lines to start recieving command predictions.')
	print('\tEnter n to delete prediction')
	print('\tEnter q to quit')

	# Create inital list of n commands to base first prediction off of 
	while count < n:
		line = input()
		if line.strip() == "q":
			exit()
		commands.append(line.rstrip().split()[0])
		count += 1

	#Use word test to get prediction
	prediction = word_test(n, commands, probabilities)

	# If there is no prediction, clear the line and have the next prediction be based on 
	# the next line inputted (I feel like this block could be a function since it repeats 
	# later but I couldn't figure out how)
	while prediction == None:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")
			line = input()
			if line.strip() == "q":
				exit()
			prediction = line.rstrip().split()[0]
			commands.append(prediction)
			commands.pop(0)
			prediction = word_test(n, commands, probabilities)
	#If there is a prediction, prompt the user with the prediction and allow them to type 
	# the rest of the command
	else:
		line = input(prediction)

	while 1:
		if line.strip() == "q":
			exit()
		# When the user enters n, clear the line and have the next prediction be based on the 
		# next line inputted 
		if line.strip() == "n":
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")
			line = input()
			if line.strip() == "q":
				exit()
			prediction = line.rstrip().split()[0]
		# Add most recent command to the list, and remove oldest command. Make a new 
		# prediction based on this new list of commands
		commands.append(prediction)
		commands.pop(0)
		prediction = word_test(n, commands, probabilities)
		while prediction == None:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")
			line = input()
			if line.strip() == "q":
				exit()
			prediction = line.rstrip().split()[0]
			commands.append(prediction)
			commands.pop(0)
			prediction = word_test(n, commands, probabilities)
		else:
			line = input(prediction)

if __name__ == '__main__':
	main()
		
		
		 
