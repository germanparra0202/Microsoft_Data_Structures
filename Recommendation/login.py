#!/usr/bin/env python3

import sys
import os
import json
from login_funcs import Colors

def main():
	'''
	Program that changes to selected directory

	This program will run when the user logins to give them the option of changing to a
	directory that they had previously picked. The user has to input a 1, 2, or 3 to change
	to the directory, or the user can skip this and just continue. To run this at login, 
	the path to this file need to be added to the ~/.profile file
	'''
	
	#TODO fill in path to directory containing this file
	cwd = '/escnfs/home/cgillila/Classes/DSProject/Microsoft-Data-Structures-Project/Recommendation'
	
	# Load in directory data 
	with open(f'{cwd}/directory_data.txt', 'r') as f:
		data = json.load(f)

	# Get directories from the data
	directories = [key for key in data.keys()]

	"""
	# Text colors
	RED   = '\033[1;31m'  
	BLUE  = '\033[1;34m'
	GREEN = '\033[0;32m'
	RESET = '\033[0;0m'
	BOLD  = '\033[;1m'
	"""


	# Display directories with colors
	print()
	sys.stdout.write(Colors.BOLD)
	print('Directories')
	sys.stdout.write(Colors.BLUE)
	print(f'1) {directories[0]}')
	sys.stdout.write(Colors.RED)
	print(f'2) {directories[1]}')
	sys.stdout.write(Colors.GREEN)
	print(f'3) {directories[2]}')
	sys.stdout.write(Colors.BOLD)
	choice = input('Option: ')

	# Response to user input
	if choice == '1' or choice == '2' or choice == '3':
		choice = int(choice) - 1
		os.chdir(f'{data[directories[choice]]}')
		os.system('/bin/bash')
	else:
		exit(0)
		

if __name__ ==  '__main__':
	main()

