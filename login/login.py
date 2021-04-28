#!/usr/bin/env python3

# allows user to change directly to desired directory by typing 1, 2, or 3
# any other key will do nothing
#  - run once at login, add to ~/.profile file

import sys
import os
import json

##################################
# open example data- remove later#
##################################

#TODO fill in path to directory containing this file
cwd = '/escnfs/home/cgillila/Classes/DSProject/Microsoft-Data-Structures-Project'
f = open(f'{cwd}/example_data.txt')
example_data = json.load(f)
f.close()


#################################
#         keep this next part   #
#################################
# Available Directories
directories = [key for key in example_data.keys()]

# Text colors
RED   = '\033[1;31m'  
BLUE  = '\033[1;34m'
GREEN = '\033[0;32m'
RESET = '\033[0;0m'
BOLD  = '\033[;1m'

# Display with ~colors~
print()
sys.stdout.write(BOLD)
print('Directories')
sys.stdout.write(BLUE)
print(f'1) {directories[0]}')
sys.stdout.write(RED)
print(f'2) {directories[1]}')
sys.stdout.write(GREEN)
print(f'3) {directories[2]}')
sys.stdout.write(BOLD)
print('Option: ')

# User Input
for line in sys.stdin:
	line = line.rstrip()
	if line == '1' or line == '2' or line == '3':
		line = int(line) - 1
		os.chdir(f'{example_data[directories[line]]}')
		os.system('/bin/bash')
		break
	else:
		break	




# Text colors taken from:
# https://stackoverflow.com/questions/37340049/how-do-i-print-colored-output-to-the-terminal-in-python/37340245#:~:text=Perhaphs%20you%20can%20add%20optional,functions%20to%20color%20the%20text.&text=%23%20print%20%22%5C033%5B1,will%20be%20red%20...%22

