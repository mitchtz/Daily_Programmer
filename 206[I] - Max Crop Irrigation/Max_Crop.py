#Find optimal position for a sprinkler in a field with randomly places crops.Takes in h,w,r, where h is height, w is width, r is the sprinker radius
#http://www.reddit.com/r/dailyprogrammer/comments/2zezvf/20150318_challenge_206_intermediate_maximizing/

import random
import math

#Creates field with random crop placements
def create_field(height, width):
	#Choices for what can be in field. "." for nothing, "x" for crop
	option = [".", "x"]
	#List of lists for field
	field = []
	#Iterate through dimensions and create field
	#Iterate through height
	for i in range(height):
		#Create new row for field
		field.append([])
		#Iterate through width
		for j in range(width):
			field[i].append(random.choice(option))
	return field

#Finds best place for sprinkler, takes in field, height, width, and radius of sprinkler
def place_sprinkler(field, height, width, radius):
	#If field is big enough, start seaching for best placement radius/2 awway from the edge (So corner is not )
	if (width < radius) and (height < radius):
		start = int(radius/2)
	else:
		start = 0
	#Store best height and width
	best_h = 0
	best_w = 0
	#Store best coverage
	best_coverage = 0
	#Check through height
	for i in range(start, height):
		#Then check through width
		for j in range(start, width):
			#Check if coverage is better
			cover = coverage_count(field, i, j, radius, height, width)
			if cover > best_coverage:
				best_h = i
				best_w = j
				best_coverage = cover

	return [best_h, best_w, best_coverage]

#Return count of crops that are in the radius of the sprinkler
def coverage_count(field, sprinkler_h, sprinkler_w, radius, height, width):
	#Check if radius will go outside of map
	#Check top of field
	if (sprinkler_h - radius) < 0:
		start_h = 0
	else:
		start_h = sprinkler_h - radius
	#Check bottom of field
	if (sprinkler_h + radius) >= height:
		end_h = height-1
	else:
		end_h = sprinkler_h + radius
	#Check left side of field
	if (sprinkler_w - radius) < 0:
		start_w = 0
	else:
		start_w = sprinkler_w - radius
	#Check right side of field
	if (sprinkler_w + radius) >= width:
		end_w = width-1
	else:
		end_w = sprinkler_w + radius

	#Store number of crops covered
	crop = 0
	#Search sqaure that covers sprinkler area
	#Check through height
	for i in range(start_h, end_h+1):
		#Check width
		for j in range(start_w, end_w+1):
			#Check if square is in radius by getting hypotenuse
			if math.sqrt((sprinkler_h-i)**2 + (sprinkler_w-j)**2) <= radius:
				#Check if this square is the sprinkler location, if so, then don't count crop, as it would be destroyed placing sprinkler
				if (i == sprinkler_h) and (j == sprinkler_w):
					continue
				else:
					#If square is a crop, increment crops covered
					if field[i][j] == "x":
						crop = crop + 1


	return crop

def print_field(field):
	for i in field:
		row = ""
		for j in i:
			row = row + j + " "
		print(row)

h = int(input("Input field height: "))
w = int(input("Input field width: "))
r = int(input("Input sprinkler radius: "))
field = create_field(h, w)
print_field(field)
print(place_sprinkler(field, h, w, r), "-- Sprinkler Coordinates [height, width, crops covered]. Coordinates are 0 indexed")

'''
#Prints last item in first row
print(field[0][w-1])
'''