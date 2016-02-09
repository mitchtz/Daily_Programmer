input = "challenge_4"
#Size of grid in storage
grid_storage = 0
#Number of logs to place
to_place = 0
#Already existing logs in storage
storage = []
with open(input) as data_in:
	#Store how large the storage grid is as an int
	grid_storage = int(data_in.readline().replace("\\n", ""))
	#Store how many logs to place as an int
	to_place = int(data_in.readline().replace("\\n", ""))
	#Read rest of lines, store list of lists with each line
	log_grid = data_in.readlines()
	#Parse through list of lists
	for i in log_grid:
		i.replace("\\n", "")
		#Convert list of strings to list of ints with list comprehension
		'''EG. [int(j) for j in i.split()] splits i into a list of strings, then runs though it converting to int and returns the list of ints'''
		storage = storage + [int(j) for j in i.split()]
	#Convert number of logs in each pile from string to int
	
#Run though logs to store until out of logs to store
while to_place > 0:
	#Find smallest pile, and find its index
	small_index = storage.index(min(storage))
	#Place log in smallest stack in storage by finding min stack, and indexing to it
	storage[small_index] = storage[small_index] + 1
	to_place = to_place - 1
#print(grid_storage, to_place, storage)
#Store where we are printing from
curr_index = 0
#Print new storage facility using input size
for i in range(0,grid_storage):
	print(storage[curr_index:curr_index+grid_storage])
	curr_index = curr_index + grid_storage