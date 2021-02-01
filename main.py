"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):

	while left <= right:
		middle = (left+right)//2
		if mylist[middle] == key:
			return middle
		elif mylist[middle] > key:
			return _binary_search(mylist,key,left,middle-1)
		elif mylist[middle] < key:
			return _binary_search(mylist,key,middle+1,right)
	return -1

def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	### TODO: add two more tests here.
	###
	assert binary_search([1,2], 5) == -1
	assert binary_search([], 2) == -1

def time_search(search_fn, arr, key):
	start_time1 = time.time()
	search_fn(arr, key,)
	end_time1 = time.time()

	final_time1 = (end_time1 - start_time1)*1000

	return final_time1
	
	### TODO
	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	key = -1
	results = []
	for i in sizes:
		line = time_search(linear_search, sizes, -1)
		binary = time_search(binary_search, sizes, -1)
		results += (i, line, binary)
	return results

	### TODO
	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))


def test_compare_search():
	res = compare_search(sizes=list(range(10, 100)))
	print(res)

	assert res[0] == 10
	#assert res[1][0] == 100
	#assert res[0][1] < 1
	#assert res[1][1] < 1py

