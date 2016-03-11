import random, string, time
#String for list of letters, time for timing operation
letter_pool = string.ascii_letters
#Fitness function. Takes in goal string and string to eval. Returns number for fitness (0 <= fitness <= len(goal_str))
def fitness(goal, str_in):
	fit = 0
	for i in range(len(goal)):
		if goal[i] == str_in[i]:
			fit += 1
	return fit


#Function that populates the starting generation. Takes in number of citizens, length of each citizens string, and goal string, returns list that is a list of citizens
def pop_gen(pop_num, str_len, goal_str):
	#List this is the generation being created. Each entry is a citizen list of [fitness func value, string]
	gen = []
	for i in range(pop_num):
		#Choose str_len number of random letters (upper and lower)
		citizen = ""
		for j in range(str_len):
			citizen += random.choice(letter_pool)
		#Start with fitness function being 0
		gen.append([fitness(goal_str, citizen), citizen])
	return gen

#Genetic algorithm loop. Takes in goal word, population size, crossover rate, mutation rate, and max generations. Returns list of all generations
def genetic(goal, pop_size, cross_rate, mutate_rate, gen_max):
	#Get length of goal string
	goal_len = len(goal)
	#Get indexes of the 1/4 point
	parent_cutoff = int(pop_size/4)
	#Get index of where to split string of parent in crossover
	cross_index = int(goal_len*cross_rate)
	#list of all generations. Each generation is list of citiens (each citizen is a list of [fitness func value, string])
	generations = []
	#Create starting population
	generations.append(pop_gen(pop_size, goal_len, goal))
	#Start main generation loop. Each iteration creates a new generation and evaluates the current one. Run until solution found or generation limit reached
	for i in range(gen_max):
		#Check if any of the generation are a perfect fit. Break if they are
		if max(generations[i])[0] == goal_len:
			break
		#Make pool of best fitness citizens and some not great fits for diversity. Do this by iterating through current generation and sorting. Take the top half and then
		#Fill pool with top 3/4 of this generations citizens
		parent_pool = sorted(generations[i])[parent_cutoff:]

		#Create empty list for next generation
		generations.append([])
		#Population size of next generation
		next_gen_len = 0
		#Create children until the next generation is long enough
		while (next_gen_len < pop_size):
			#Choose two parents
			parent1 = random.choice(parent_pool)
			parent2 = random.choice(parent_pool)
			#If they aren't the same, create two children for the next generation
			if parent1 != parent2:
				'''Using one point crossover
				at crossover percent of parent. eg. crossover rate = 0.4, take 0.4 of first parent and 0.6 of second, then vice versa'''
				#Create two children from parent
				#Store children strings as list 
				#Create first child
				child = []
				#Run crossover with first part from parent1
				child.append(list(parent1[1][:cross_index]))
				child.append(list(parent2[1][cross_index:]))
				#Apply mutation rate to child
				for let in range(goal_len):
					#Get random number, if it is below mutation rate, change letter to random letter
					if random.random() < mutate_rate:
						child[let] = random.choice(letter_pool)
				child = str(child)
				#Get fitness value of child and add to next generation
				generations[i+1].append([fitness(goal, child), child])

				#Create second child
				child = ""
				#Run crossover with first part from parent2
				child = parent2[1][:cross_index] + parent1[1][cross_index:]
				#Apply mutation rate to child
				for let in range(goal_len):
					#Get random number, if it is below mutation rate, change letter to random letter
					if random.random() < mutate_rate:
						child[let] += random.choice(letter_pool)
				#Get fitness value of child and add to next generation
				generations[i+1].append([fitness(goal, child), child])

				#Increment next gen size
				next_gen_len += 2


	return generations


if __name__ == "__main__":
	#String that will try to be evolved to
	goal_string = "Hello world"
	#Population size
	pop = 10
	#Crossover rate, percent chance that letter will come from 1st parent
	cross = 0.5
	#Mutation rate, percent chance of each letter to be mutated
	mut = 0.3
	#Max amount of generations to create
	gen = 15
	#Start timer
	start = time.time()
	#Start genetic algorithm
	generation_done = genetic(goal_string, pop, cross, mut, gen)
	end = time.time()
	#Write to file
	with open("Hello World GA", 'w') as out_file:
		#Write header
		out_file.write("Looking for: " + goal_string)
		out_file.write("Population size: " + str(pop))
		out_file.write("Crossover rate: " + str(cross))
		out_file.write("Mutation rate: " + str(mut))
		out_file.write("Max number of generations: " + str(gen))
		out_file.write("Time to run: " + str(end-start))
		#Check if solution was ever found
		if max(generation_done[len(generation_done)-1])[0] == len(goal_string):
			out_file.write("Solution found on generation: " + str(len(generation_done)))
		#Start printing generations
		for gen_num, i in enumerate(generation_done):
			out_file.write("Generation " + str(gen_num))
			for cit in i:
				out_file.write(str(cit))