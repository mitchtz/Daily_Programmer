#Make numbers palindromic by taking a number and adding it to its reverse until its palindromic
#http://www.reddit.com/r/dailyprogrammer/comments/38yy9s/20150608_challenge_218_easy_making_numbers/
#Takes in number to make palindromic, outputs number of steps, palindromic number
def make_palindromic(num):
	#Max number of iterations to run for a number
	iter_max = 10000
	for i in range(0, (iter_max+1)):
		num_str = str(num)
		#Check if number is palindromic
		if num_str == num_str[::-1]:
			return [i,num]
		else:
			num = num + int(num_str[::-1])
	return [iter_max, 0]
'''
#Lychrel numbers don't converge in under 10000 steps
lychrel = []
for i in range(1,1001):
	print(i)
	palin_check = make_palindromic(i)
	if palin_check[1] == 0:
		lychrel.append(i)

print(lychrel)
'''
'''
num_to_check = [123, 286, 196196871]
for i in num_to_check:
	palindromic_out = make_palindromic(i)
	print(i, "Gets palindromic after", palindromic_out[0], "steps:", palindromic_out[1])
'''