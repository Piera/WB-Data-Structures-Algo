# Find the index of the target item in a list using binary search

def binary_search(array, target_item):
	lst_length = len(array)
	index = lst_length // 2
	pointer = array[index]
	if pointer == target_item:
		print index
		return index
	elif pointer > target_item:
		return binary_search(array[:index], target_item)
	elif pointer < target_item:
		return binary_search(array[index:], target_item)

lst = [1,2,3,4,5,6,7,8]
target = 7
start = lst[0]
end = lst[-1]

# binary_search(lst, target)
# Returns the index of the recursively shortened list. 

# Q: How to return the index of the original list?
# A: Don't split the list, instead just pass start and end.


def bsearch(lst, start, end, target):
	pointer = (end+start)/2
	if lst[pointer] == target:
		print pointer
		return pointer
	elif lst[pointer] > target:
		return bsearch(lst, 0, pointer, target)
	elif lst[pointer] < target:
		return bsearch(lst, pointer, end, target)

bsearch(lst, start, end, target)



