'''
graph["A"].append("T")
print(graph)
graph["A"].remove("T")
print(graph)
graph["Z"] = ["H", "J"]
'''
#Read in graph data from text file, takes in name of data file, returns dict with street names and info
def read_create_list(map_file):
	with open(map_file) as in_file:
		map = {}
		for line in in_file.readlines():
			#Holds the input line
			temp = line.split(" ")
			#Record street name
			street = ""
			#Record if the street name is being written
			write = False
			for i in temp:
				if "\"" in i:
					street = street + i
					#If the end of the street name is found
					if write == True:
						write = False
					#Otherwise start writing
					else:
						write = True
				elif write == True:
					street = street + i
			#print(temp)
			length = len(temp)
			#print(length)
			last = int(str(temp[length-1]).replace("\n", ""))
			map[(temp[0]+temp[1])] = [street.replace("\"", ""), int(temp[length-4]), int(temp[length-3]), int(temp[length-2]), last]
		'''
		print("------------------------------------------")
		for address in map:
			print(address, map[address])
		'''
	return map
	
#Create graph using passed in list of intersections and info. Pass in the list of 
def create_graph(list_in):
	graph = {}
	for key in list_in:
		#If first intersection is in graph already
		if key[0] in graph:
			#If the intersection to be added is not already connected to the first intersection
			if key[1] not in graph[key[0]]:
				graph[key[0]].append(key[1])
		#If first intersection is not in graph
		else:
			graph[key[0]] = [key[1]]
		#Repeat for opposite order of intersections
		#If second intersection is in graph already
		if key[1] in graph:
			#If the intersection to be added is not already connected to the first intersection
			if key[0] not in graph[key[1]]:
				graph[key[1]].append(key[0])
		#If first intersection is not in graph
		else:
			graph[key[1]] = [key[0]]
		
	return graph
		
	
#Find fastest route from input start intersection to input end intersection
#Takes in start point, end point, map graph, map list, and start time (as numbers 0 through 3, each as one time zone)
#Returns path to finish
def find_fastest(map_start, map_end, map_graph, map_list, map_timezone):
	pass
	
	
def main():
	file_in = "map_data.txt"
	#Get input about start point, end point, and start time
	map_start = input("Input starting intersection: ")
	map_end = input("Input ending intersection: ")
	map_time = int(input("Input time delivery starts at (in military time, such as 1400 for 2:00 PM)\n"))
	#Create map list (Has intersections, street names, and times for travelling streets)
	map_list = read_create_list(file_in)
	#Create graph from list that has all connections and no vertex repeats
	map_graph = create_graph(map_list)
	#Determine which time one the delivery starts in, map_timezone is from 0-3 indicating which time zone selivery starts in
	#If input time is after 6 am
	if map_time <= 600:
		#If input time is after 10 am
		if map_time <= 1000:
			#If iput time is after 3 pm
			if map_time <= 1500:
				#If input time is after 7 pm and before midnight
				if map_time <= 1900:
					map_timezone = 3
				#If input time is between 3 pm and 7 pm
				else:
					map_timezone = 2
			#If input time is between 10 am and 3 pm
			else:
				map_timezone = 1
		#If input time is between 6 am and 10 am
		else:
			map_timezone = 0
	#If time is between midnight and 6 am
	else:
		map_timezone = 3
		
	
	#Find fastest path
	find_fastest(map_start, map_end, map_graph, map_list, map_timezone)
	
	
	for line in map_graph:
		print(line, map_graph[line])
	
main()
	