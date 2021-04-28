#!/usr/bin/env python3

import sys
from ngram import make_list
from ngram import line_test
from ngram import word_test
from ngram import Ngram
		
def main():
	n = 2
	probs1 = Ngram()
	probs2 = Ngram()
	command_list = []
	arguments = sys.argv[1:]

	# iterate through every command line argument (file)
	while arguments:
		argument = arguments.pop(0)
		command_list = make_list(command_list, argument)
	
	probs1.line_ngram(2, command_list)
	probs2.word_ngram(2, command_list)
#	probs1.display()
	probs2.display()

	line_test(n, probs1.prob_dict)
	word_test(n, probs2.prob_dict)

if __name__ ==  '__main__':
	main()

