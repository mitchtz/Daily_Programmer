#Mitch Zinser
#Can read natural operator sequence (NOS) and cnovert to decimal, and can find the shortest representation of a number in NOS
#NOS numbers are defined by inserting operators into a sequence of decimals such that 0_1_2_3_4
#0 = + | 1 = - | 2 = * (Read left to right, no operator precedence)
#0022 = 0+1+2*3*4 = 36
#10020 = 21
import itertools, math, time
#Convert from NOS forat to deciaml format
def nos2dec(num_in):
	tot = 0
	for num,i in enumerate(num_in):
		if i == "0":
			tot += num+1
		elif i == "1":
			tot -= num+1
		else:
			tot *= num+1
	return tot

def find_shortest(goal_num):
	#Max decimal value for a NOS sequence of length n is (n!)*1.5  (Since it is almost a fact sequence, just the first two nums are added)
	#Find minimum length the NOS sequence must be
	nos_len = 1
	while True:
		if math.factorial(nos_len)*1.5 >= goal_num:
			break
		else:
			nos_len += 1

	
	#Start at min length required and build up until solution is found. First found solution of a length fill be used
	while True:
		#Create list of possible sequences using cartesian product
		nos_list = itertools.product("012", repeat=nos_len)
		#Check each combination
		for comb in nos_list:
			#Concat list into one string and check if it is correct
			if nos2dec("".join(comb)) == goal_num:
				return "".join(comb)
		#Increase length of NOS to try
		nos_len += 1

start = time.time()
for num_to_find in range(500+1):
	print(num_to_find, find_shortest(num_to_find))
print("Time elapsed", time.time()-start)

