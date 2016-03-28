#Mitch Zinser
#Genetic Algorithm that evolves a desired string from a randomly created pool of candidate strings

import random, string, time, sys 
#String for list of letters, time for timing operation
letter_pool = string.ascii_letters + string.punctuation + " "


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
'''TODO
Make variable mutation rate *(decrease as generation increases)
MEMORY MANAGEMENT:
(?)Only keep current and next generation in full, and keep the max 5 of previous generations
'''
def genetic(goal, pop_size, cross_rate, mutate_rate, gen_max):
	#Get length of goal string
	goal_len = len(goal)
	#Get goal fitness for solution
	goal_fit = fitness(goal, goal)
	#Get indexes of the 1/4 point
	parent_cutoff = int(pop_size/4)
	#Get index of where to split string of parent in crossover
	cross_index = int(goal_len*cross_rate)

	#Each generation is list of citiens (each citizen is a list of [fitness func value, string])
	cur_gen = []
	next_gen = []
	#list of best fit for each generation. This allows basic archiving without wasting as much memory
	generations = []
	#Create starting population
	cur_gen = pop_gen(pop_size, goal_len, goal)

	####generations.append(pop_gen(pop_size, goal_len, goal))
	#Start main generation loop. Each iteration creates a new generation and evaluates the current one. Run until solution found or generation limit reached
	for i in range(gen_max):
		#Record best candidate in this generation
		generations.append(max(cur_gen))

		#Check if any of the generation are a perfect fit. Break if they are
		if max(cur_gen)[0] == goal_fit:
			break
			print("Break with", max(cur_gen))
		#Make pool of best fitness citizens and some not great fits for diversity. Do this by iterating through current generation and sorting. Take the top half and then
		#Fill pool with top 3/4 of this generations citizens
		parent_pool = sorted(cur_gen)[parent_cutoff:]

		#Create empty list for next generation
		####generations.append([])
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
				child.extend(list(parent1[1][:cross_index]))
				child.extend(list(parent2[1][cross_index:]))
				#Apply mutation rate to child
				for let in range(goal_len):
					#Get random number, if it is below mutation rate, change letter to random letter
					if random.random() < mutate_rate:
						child[let] = random.choice(letter_pool)
				child = "".join(child)
				#Get fitness value of child and add to next generation
				next_gen.append([fitness(goal, child), child])
				

				#Create second child
				child = []
				#Run crossover with first part from parent2
				child.extend(list(parent2[1][:cross_index]))
				child.extend(list(parent1[1][cross_index:]))
				#Apply mutation rate to child
				for let in range(goal_len):
					#Get random number, if it is below mutation rate, change letter to random letter
					if random.random() < mutate_rate:
						child[let] = random.choice(letter_pool)
				child = "".join(child)
				#Get fitness value of child and add to next generation
				next_gen.append([fitness(goal, child), child])
				##print(child)
				#Increment next gen size
				next_gen_len += 2

		#Copy next generation into current generation and reset next generation
		cur_gen = next_gen
		next_gen = []
		#Print progress
		if i%100 == 0:
			print("On generation:", i)


	return generations

'''Observations
Population:
Higher populations (eg 1000+) take longer to run, but require fewer generations.
Around 100-200 runs fastest for shorter strings, but require many more generations.
Nearly linear (Time to run and generations required) from observations, not quite, but enough for estimation.

Crossover Rate:
Not much studied. Around 0.5 seems to work well, not sure how relevant is is for this algorithm since two children are created from two parents

Mutation rate:
0.1 seems to high for later calculations, 0 is too low to converge. Could make it variable and decreases each generation
0.01 Tests very well so far

Generation Max:
Not much to be said. Would be a problem for lower populations. Would need to be increased when running low pop. for speed.
For "What a time, to be alive.", witha pop. of around 100, solutions could be found around generation 800

Seeding:
Random number engine seeding does work for this algorithm, as expected.
'''

if __name__ == "__main__":
	if len(sys.argv) > 1:
		#String that will try to be evolved to
		goal_string = sys.argv[1]
	else:
		goal_string = "Long string, aaahhAAAHHaaahh, fighter of the short string."
	#Population size
	pop = 5000
	#Crossover rate, percent chance that letter will come from 1st parent
	cross = 0.5
	#Mutation rate, percent chance of each letter to be mutated
	mut = 0.01
	#Max amount of generations to create
	gen = 2000
	#Get fitness of goal string
	goal_fitness = fitness(goal_string, goal_string)
	print("Looking for:" + goal_string + " with max fitness of " + str(fitness(goal_string, goal_string)))

	'''Can seed random number generator and get consistent and identical results for seed'''
	#random.seed(0.1)
	#Start timer
	start = time.time()

	#Start genetic algorithm
	generation_done = genetic(goal_string, pop, cross, mut, gen)
	end = time.time()
	##Status
	print("Done in", end-start, "Writing to file")

	#Create file name
	filename = goal_string[:5] + "pop" + str(pop) + "-cross0," + str(cross)[2:] + "-mutate0," + str(mut)[2:] + "-genmax" + str(gen) + ".txt"
	#Check if solution was ever found
	if generation_done[len(generation_done)-1][0] == goal_fitness:
		print("Solution found on generation: " + str(len(generation_done)))
	else:
		print("No solution found, only approximation")
	print("Best fit found: " + str(generation_done[len(generation_done)-1]))
	print("Data saved to",filename)
	#Write to file
	with open(filename, 'w') as out_file:
		#Write header
		out_file.write("Looking for: " + goal_string + " with max fitness of " + str(fitness(goal_string, goal_string)) + "\n")
		out_file.write("Population size: " + str(pop) + "\n")
		out_file.write("Crossover rate: " + str(cross) + "\n")
		out_file.write("Mutation rate: " + str(mut) + "\n")
		out_file.write("Max number of generations: " + str(gen) + "\n")
		out_file.write("Time to run: " + str(end-start) + "\n")
		#Check if solution was ever found
		if generation_done[len(generation_done)-1][0] == goal_fitness:
			out_file.write("Solution found on generation: " + str(len(generation_done)) + "\n")
		#Otherwise say it could only find best fit
		else:
			out_file.write("No solution found, only best fit" + "\n")
		#Print the best fit from the last generation
		out_file.write("Best fit found: " + str(generation_done[len(generation_done)-1]) + "\n")
		#Print only the best fit from each generation
		for gen_num, i in enumerate(generation_done):
			out_file.write("Generation " + str(gen_num) + "\n")
			#Print each citizen of each generation
			out_file.write(str(i) + "\n")