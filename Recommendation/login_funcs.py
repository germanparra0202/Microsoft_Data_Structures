#!/usr/bin/env python3

# Globals
##########
import os

HOME = os.getenv('HOME')
USER = os.getenv('USER')

# Text colors
class Colors:
	RED   = '\033[1;31m'  
	BLUE  = '\033[1;34m'
	GREEN = '\033[0;32m'
	RESET = '\033[0;0m'
	BOLD  = '\033[;1m'

# Functions
############

def find_dir_abspath(search_dir):
	''' Searches for absolute path to directory
	
	search_dir is the name of the directory you are looking for. It does	does not work 
	on hard or soft links. Returns the absolute pathname if found or an empty string
	if not found
	'''
	match = ''
	
	for dir_path, dir_names, file_names in os.walk(HOME):
		for dir_name in dir_names:
			if dir_name == search_dir:
				match = dir_path + '/' + dir_name

	return match


# Text colors taken from:
# https://stackoverflow.com/questions/37340049/how-do-i-print-colored-output-to-the-terminal
# -in-python/37340245#:~:text=Perhaphs%20you%20can%20add%20optional,functions%20to%20color%2
# 0the%20text.&text=%23%20print%20%22%5C033%5B1,will%20be%20red%20...%22
