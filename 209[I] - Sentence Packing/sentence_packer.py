sent = "IT IS RAINING CATS AND DOGS OUT THERE"
sent = sent.replace(" ", "")

#Finds squarest rectangle for given input. Prefers exact fill
#Returns [x, y] of rectangle
def find_rect(length):
	#If rectangle is full perfectly
	full = False
	#Best width of box
	x = 2
	for i in range(2, int(length/2)+1):
		#If the test width fits all letters perfectly
		if length%i == 0:
			#Test if test width and height is closer than best height and width
			if (abs(i - int(length/i)) < abs(x - int(length/x))):
				#Change best width to current test width
				x = i
				#Change full to reflect that a perfect fill has been found
				full = True
	#If perfect fit can't be found, then try to find best fit where leftover is highest
	if not full:
		for i in range(2, int(length/2)+1):
			#Chcek if the test width produces a closer to perfect fit
			if (length%i > length%x):
				#Change best width to current test width
				x = i
		#Then add one to the smaller side of the box, as we need one more column or row for the overflow
		#If x is bigger, add to y
		if (x > length/x):
			return [x, int(length/x)+1]
		else:
			return [x+1, int(length/x)]

	return [x, int(length/x)]

'''
for i in range(1, 31):
	print(i, find_rect(i))
'''
#Get rectangle
x, y = find_rect(len(sent))
#Print starting position
print("start: 1,1")
pos = 0
#Print out string
for i in range(0, y+1):
	if pos%2 == 0:
		print(sent[pos:pos+x])
	else:
		print(sent[pos:pos+x][::-1])
	pos = pos + x 
