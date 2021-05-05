#!/usr/bin/env python3

# Globals
##########
HOME = os.getenv('HOME')
USER = os.getenv('USER')

# Text colors
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


