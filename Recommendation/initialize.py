#!/usr/bin/env python3

import sys 
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
	login_dirs = []

	while len(login_dirs) != 3:
		hold_dir = 




	# ngram Data Initialization
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

	

