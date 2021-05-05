#!/usr/bin/env python3

import sys
import os
import json
from login_funcs import find_dir_abspath
from ngram_class import make_list
from ngram_class import Ngram

def main():
	'''
	Program meant to be run once when the user decides to use the Recommendation System

	This program takes in files from the user and uses ngrams to create a dictionary
	to be used when recommending commands. It also finds the absolute path to the directories
	chosen by the user. If the absolute path is not found, then it requests that the user
	choose a different directory.	
	'''

	# Login Data Initialization
	############################
	
	#initialize variables
	login_dirs = {}

	# Checks to see if data already exists (in case ngram initialization has an issue)
	# to avoid extra unneccesary work
	if not os.path.exists('directory_data.txt'):
		while len(login_dirs) != 3:
			hold_dir = input('Choose a directory: ')
			dir_path = find_dir_abspath(hold_dir)
			if not dir_path:
				print('Absolute path not found, please select a different directory')
				continue
			login_dirs[hold_dir] = dir_path

		# export directory data to json file
		data_json = json.dumps(login_dirs)
		with open('directory_data.txt', 'w') as f:
			f.write(data_json)


	
	# ngram Data Initialization - Danielle
	############################
	n = 2; # the n in ngram
	probabilities = Ngram() # ngram dictionary
	data = [] # all data from the input files 
	arguments = sys.argv[1:]

	# Parse command line arguments
	while arguments:
		argument = arguments.pop(0)
		data = make_list(data, argument)

	# Check to make sure data is not empty
	if not data:
		print('No valid files provided')
		exit(1)

	# Create probabilities dictionary based on data from history files inputted in the 
	# command line
	probabilities.word_ngram(n, data)
	
	# export ngram data to json file
	data_json = json.dumps(probabilities.prob_dict)
	with open('ngram_data.txt', 'w') as f:
		f.write(data_json)
	

if __name__ ==  '__main__':
	main()

