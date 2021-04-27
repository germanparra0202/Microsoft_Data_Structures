#!/usr/bin/env python3

import sys
import os
import subprocess

def main():
	
	# If the file exists, then we'll append any new history to it. If it does not exist, then we'll just create it and add all the history data to it	
	if(os.path.exists('history.txt')):
		# This chunk of code is finding the last line in history.txt so that we can continue to append to that file with new history data
		# process found at https://stackoverflow.com/questions/46258499/how-to-read-the-last-line-of-a-file-in-python	
		with open('history.txt', 'rb') as f:
			f.seek(-2, os.SEEK_END)
			while f.read(1) != b'\n':
				f.seek(-2,os.SEEK_CUR)
			last_line = f.readline().decode().strip()
		# this just provides proof that it's the last line
		print(last_line)
		# this is where the problem lies. The goal was to iterate through history until a date and time were found that were greater than the data and time of the last thing that was in history. Once that was found we could append the following lines in history to the history.txt file (or wherever you're storing your history), but os.popen does not correctly open history and read through the lines. I've tried multiple other things from online but can't find a way to get the history output we see in linux to open up in the python script 
		for line in os.popen('history'):
			print(line)
	else:
		f = open('history.txt', 'x')

if __name__ == '__main__':
	main()
