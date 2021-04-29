import os

HOME = os.getenv('HOME')
USER = os.getenv('USER')


def find_dir_abspath(search_dir):
	''' Searches for absolute path to directory
	
	search_dir is the name of the directory you are looking for. HOME is the 'HOME' 
	environmental variable. It does	does not work on hard or soft links. Returns the
	absolute pathname if found or an empty string if not found
	'''
	match = ''
	
	for dir_path, dir_names, file_names in os.walk(HOME):
		for dir_name in dir_names:
			if dir_name == search_dir:
				match = dir_path + '/' + dir_name

	return match




class Dir_Count:
	''' Dictionary of {key : [count, abs_path]}

	Use to count the number of times a directory is called in the user history
	'''

	def __init__(self):
		self.tracking_dirs = {}
		self.top3_dirs = {}


	def insert(self, key):
		''' Adds the key to the Tracking Directories

		Tries to find the abolute path to the key. If one is not found, then it sets the count
		to -1. If it is found, then it sets the count to 1.
		'''
		abspath = find_dir_abspath(key)
		count = 1
		if not abspath:
			count = -1
		self.tracking_dirs[key] = [count, abspath]

	def remove(self, key):
		''' Removes a key from the Tracking Directories

		If the removed directory is in the top 3, it linearly searches through the entirety
		of the tracking directories for the next largest value
		'''
		if key in self.tracking_dirs:
			del self.tracking_dirs[key]
		
		if key in self.top3_dirs:
			holder_val = 0
			holder_str = ''
			del self.top3_dirs[key]
			for check_key, check_value in self.tracking_dirs.items():
				if self.tracking_dirs[check_key][0] > holder_val and check_key not in self.top3_dirs:
					if holder_str:
						del self.top3_dirs[holder_str]
					holder_val = self.tracking_dirs[check_key][0]
					holder_str = check_key
					self.top3_dirs[check_key] = self.tracking_dirs.get(check_key)

	def update(self, key):
		''' Updates the count to a key in the list
		
		Adds 1 to the key's value and then checks if it is greater than any of the values in
		the top 3 directories. Replaces the directory if it is greater. Any directories where
		finding the absolute path failed are ignored
		'''
		if key in self.tracking_dirs and self.tracking_dirs[key][0] > 0:
			self.tracking_dirs[key][0] += 1
		else:
			return

		if key in self.top3_dirs:
			return
		else: 
			for top3_key, top3_value in self.top3_dirs.items():
				if self.tracking_dirs[key][0] > top3_value[0]:
					del self.top3_dirs[top3_key]
					self.top3_dirs[key] = self.tracking_dirs.get(key)
					return
		
	

