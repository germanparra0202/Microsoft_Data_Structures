#!/usr/bin/env python3

###############################################
#                  libraries                  #
###############################################
import os
import json


##############################################
#            test space                      #
##############################################

def test_func():
	dir1 = f'cse-20289-sp21-assignments-{USER}'
	dir2 = 'Microsoft-Data-Structures-Project'
	dir3 = 'sp21-cse-20312.01'
	example_data = {}

	for dir_name in dir1, dir2, dir3:
		abspath = find_dir_abspath(dir_name)
		example_data[dir_name] = abspath

	data_json = json.dumps(example_data)
	f = open('example_data.txt', 'w')
	f.write(data_json)
	f.close()	



#################################################
# some functions that might be helpful later on #
#################################################

HOME = os.getenv('HOME')
USER = os.getenv('USER')


# similar to "find", searches through all the directories
# for match, returns absolute path name
	# search_dir is the name of the directory you are looking for
	# does not work on links
def find_dir_abspath(search_dir):
	for dir_path, dir_names, file_names in os.walk(HOME):
		for dir_name in dir_names:
			if dir_name == search_dir:
				match = dir_path + '/' + dir_name

	return match
	# directories with matching names?
	# hard and soft links?




test_func()
