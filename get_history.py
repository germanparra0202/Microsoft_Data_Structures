#!/usr/bin/env python3

import sys
import os
import subprocess
import datetime

def main():
	
	# This chunk of code is finding the last line in history.txt so that we can continue to append to that file with new history data
	# process found at https://stackoverflow.com/questions/46258499/how-to-read-the-last-line-of-a-file-in-python	
	with open('history.txt', 'rb') as f:
		f.seek(-2, os.SEEK_END)
		while f.read(1) != b'\n':
			f.seek(-2,os.SEEK_CUR)
		last = f.readline().decode().strip()
	
	beg_year = 20
	end_year = last[12:14]
	last_day = last[9:11]
	last_month = last[6:8]
	last_hour = last[15:17]
	last_min = last[18:20]
	last_sec = last[21:23]
	convert_epoch = int(datetime.datetime(int(f'{beg_year}{end_year}'), int(last_month), int(last_day), int(last_hour), int(last_min), int(last_sec)).timestamp())
	last_hist_num = int(last[0:4])
	
	# for loop to print all 
	i = 0;
	hist_file = open('history.txt', 'a')
	for line in os.popen('cat ~/.bash_history'):
		i+=1
		#print(line.strip())
		if( (i%2) == 1):
			epoch = int(line[1:])
			if (epoch > convert_epoch):
				epoch = datetime.datetime.fromtimestamp(int(epoch))
				epoch = str(epoch)
				month = epoch[5:7]
				day = epoch[8:10]
				year = epoch[2:4]
				time = epoch[11:]
				logic = True
				continue
			else:
				logic = False
				continue
		if( logic ):
			last_hist_num += 1
			#hist_file.write(f'{month}/{day}/{year} {time} {line.strip()}\n')
			hist_file.write(f' {last_hist_num:>4}  {month}/{day}/{year} {time} {line.strip()}\n')
			continue
		
if __name__ == '__main__':
	main()
