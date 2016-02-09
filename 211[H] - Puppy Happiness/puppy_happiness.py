import itertools
import time

#Evaluates a combination of treats, returns happiness of combo
def eval_combo(combo):
	happiness = 0
	for i in range(len(combo)):
		#Single case for start
		if i == 0:
			#if dog to right has better treat
			if combo[1] > combo[0]:
				happiness = happiness - 1
			#If dog to right has worse treat
			elif combo[1] < combo[0]:
				happiness = happiness + 1
		#Single case for end
		elif i == len(combo)-1:
			#if dog to left has better treat
			if combo[i-1] > combo[i]:
				happiness = happiness - 1
			#If dog to left has worse treat
			elif combo[i-1] < combo[i]:
				happiness = happiness + 1

		#For all middle dogs
		else:
			#If neighbors have bigger treats
			if (combo[i-1] > combo[i]) and (combo[i+1] > combo[i]):
				happiness = happiness - 1
			#If neighbors have smaller treats
			if (combo[i-1] < combo[i]) and (combo[i+1] < combo[i]):
				happiness = happiness + 1
	return happiness


#Takes in a list of treats, in order, returns [happiness, best combo]
def find_happiest(treats_in):
	num_treats = len(treats_in)
	happiness = []
	#Create all combos for treats_in
	treat_combos = itertools.permutations(treats_in, num_treats)
	total_combos = 0
	#Brute force through all combinations
	best_combo = []
	best_happiness = 0
	for i in treat_combos:
		#Evaluate happiness of combo
		combo_happy = eval_combo(i)
		#If this combo is better than previous best, record new best
		if combo_happy > best_happiness:
			best_happiness = combo_happy
			best_combo = i
		total_combos = total_combos + 1
	print("Number of combos:", total_combos)
	return [best_happiness, best_combo]


bought_treat = input("Treats: ")
bought_treat = bought_treat.replace(" ", "")
#Turn into list
treats = []
for i in bought_treat:
	treats.append(int(i))

#treats = [1,2,2,3,3,3,4]
start = time.time()
best = find_happiest(treats)
compute_time = time.time() - start
print("Happiness of best combo:", best[0])
print("Best combo:", best[1])
print("Time to find:", compute_time, "seconds")