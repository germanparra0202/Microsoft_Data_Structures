#!/usr/bin/env python3

from dir_funcs import Dir_Count

def main():
	''' 
	Test the Dir_count class
	'''
	dir1 = 'Classes'
	dir2 = 'doodoo'
	dir3 = 'dstest'
	dir4 = 'test'
	dir5 = 'Microsoft-Data-Structures-Project'

	# test init
	a = Dir_Count()

	# hard code top 3 (will be done with initialization method)
	a.top3_dirs['holder1'] = [1, 'holder_path']
	a.top3_dirs['holder2'] = [1, 'holder_path']
	a.top3_dirs['holder3'] = [1, 'holder_path']

	# test insert
	print('Test insert')
	a.insert(dir1)
	a.insert(dir2)
	a.insert(dir3)
	a.insert(dir4)
	a.insert(dir5)
	print(a.tracking_dirs)
	print()

	# test update
	print('Test update')
	print('Top 3')
	print(a.top3_dirs)
	print('Tracking')
	print(a.tracking_dirs)
	a.update(dir1)
	a.update(dir1)
	a.update(dir1)
	a.update(dir1)
	a.update(dir1)
	print('Top 3')
	print(a.top3_dirs)
	a.update('fake_dir')
	a.update(dir3)
	a.update(dir3)
	a.update(dir3)
	a.update(dir3)
	a.update(dir2)
	print('Top 3')
	print(a.top3_dirs)
	a.update(dir5)
	a.update(dir5)
	a.update(dir5)
	print('Top 3')
	print(a.top3_dirs)
	print('Tracking')
	print(a.tracking_dirs)
	print()

	# test remove
	print('Test remove')
	a.remove('Classes')
	print('Classes removed')
	print(a.tracking_dirs)
	a.remove('failure')
	print('Top 3')
	print(a.top3_dirs)
	print()

if __name__ == '__main__':
	main()
	
