from PIL import Image
import numpy as np
class circle:
    def __init__(self, diam, perim, fill):
        self.diameter = diam
        self.perimeter = perim
        self.filled = fill
#Function that takes first pixel of circle, then fills in the circle
#Returns a list of the perimeter points, a list of every pixel in the circle and the diameter of the circle
def fill_circle(image, pix_y, pix_x):
	diameter = 1
	#Current pixel coordinates
	curr_y = pix_y
	#Find diameter by going straight up circle
	while image.getpixel((curr_y, pix_x)) == (0, 0, 0):
		if curr_y+1 == im_height:
			break
		curr_y += 1
		diameter += 1
	#List of perimeter coordinates
	perimeter = [(pix_x, pix_y)]
	#List of every pixel in circle
	circle_fill = [(pix_x, pix_y)]
	#Current pixel coordinates
	curr_x, curr_y = pix_x, pix_y
	#Try to find perimeter by looking rotating counter clockwise around circle
	done = False
	while not done:

		#Check if the pixel is at the start and loop isn't the first
		if (len(perimeter) > 1) and ((curr_x == pix_x) and (curr_y == pix_y)):
			#Check if his is first run, if so, change state
				done = True
		#Check if the pixel to the right is black, then upper diagonal, then up
		elif (curr_x+1 < im_width) and (image.getpixel((curr_y, curr_x + 1)) == (0, 0, 0)):
			#Adjust current coordinates and add pixel to perimeter and circle_filled
			curr_x+=1
			perimeter+=((curr_x, curr_y))
			circle_fill+=((curr_x, curr_y))
		#Check if pixel to the upper right is black
		elif ((curr_y+1 < im_height) and (curr_x+1 < im_width)) and (image.getpixel((curr_y+1, curr_x+1)) == (0, 0, 0)):
			#Adjust current coordinates and add pixel to perimeter and circle_filled
			curr_x+=1
			curr_y+=1
			perimeter+=((curr_x, curr_y))
			circle_fill+=((curr_x, curr_y))
		#Check if pixel to the up is black
		elif (curr_y+1 < im_height) and (image.getpixel((curr_y+1, curr_x)) == (0, 0, 0)):
			#Adjust current coordinates and add pixel to perimeter and circle_filled
			curr_y+=1
			perimeter+=((curr_x, curr_y))
			circle_fill+=((curr_x, curr_y))
		#Check if pixel to the upper left is black
		elif ((curr_y+1 < im_height) and (curr_x-1 > -1)) and (image.getpixel((curr_y+1, curr_x-1)) == (0, 0, 0)):
			#Adjust current coordinates and add pixel to perimeter and circle_filled
			curr_x-=1
			curr_y+=1
			perimeter+=((curr_x, curr_y))
			circle_fill+=((curr_x, curr_y))
		#Check if the pixel to the left is black
		elif (curr_x-1 > -1) and (image.getpixel((curr_y, curr_x - 1)) == (0, 0, 0)):
			#Adjust current coordinates and add pixel to perimeter and circle_filled
			curr_x-=1
			perimeter+=((curr_x, curr_y))
			circle_fill+=((curr_x, curr_y))
		#Check if the pixel to the bottom left is black
		elif ((curr_y-1 > -1) and (curr_x-1 > -1)) and (image.getpixel((curr_y-1, curr_x-1)) == (0, 0, 0)):
			#Adjust current coordinates and add pixel to perimeter and circle_filled
			curr_x-=1
			curr_y-=1
			perimeter+=((curr_x, curr_y))
			circle_fill+=((curr_x, curr_y))
		#Check if the pixel down is black
		elif (curr_y-1 > -1) and (image.getpixel((curr_y-1, curr_x)) == (0, 0, 0)):
			#Adjust current coordinates and add pixel to perimeter and circle_filled
			curr_y-=1
			perimeter+=((curr_x, curr_y))
			circle_fill+=((curr_x, curr_y))
		#Check if the pixel to the bottom right is black
		elif ((curr_y-1 > -1) and (curr_x+1 < im_width)) and (image.getpixel((curr_y-1, curr_x+1)) == (0, 0, 0)):
			#Adjust current coordinates and add pixel to perimeter and circle_filled
			curr_x+=1
			curr_y-=1
			perimeter+=((curr_x, curr_y))
			circle_fill+=((curr_x, curr_y))
		#Else circle is a point
		else:
			done = True

	return perimeter, circle_fill, diameter

#Function to find circles, looks for the first black pixel then calls fill to get info
#Takes in the image to look at, retturns list of circle objects
def find_circles(image):
	'''Image is iterated through starting at bottom right. image[y, x]'''
	#Keep track of pixels that do not need to be scanned
	filled = []
	#List of circle objects
	circles = []
	#Iterate through picture row by row
	#Start at row 0
	for i in range(im_height):
		#Iterate through row starting at 0, stopping at width
		for j in range(im_width):
			if image[i,j] == "[0 0 0]":
				print("----Found Circle----")
				print("i: ", i)
				print("j: ", j)
				per, fill, diam = fill_circle(image, i, j)
				filled.append(fill)
				circles.append(circle(diam, per, fill))
				print("--------------------")
				return circles

if __name__ == "__main__":
	try:
		#input_im = Image.open(input("Image name(with extension): "))
		pass
	except:
		print("Couldn't open image")
	input_im = Image.open("input1.png")
	#Convert image to rgb
	im = input_im.convert("RGB")
	#Convert rgb to array
	im_arr = np.array(im)
	im_width, im_height = im.size
	print("Width: ", im_width)
	print("Height: ", im_height)
	print("--------Finding Circles--------")
	#print(type(im_arr[1,1]))
	print(list(im.getdata()))
	#Find circles
	found_circles = find_circles(im_arr)
	circle_number = 0
	for i in found_circles:
		print("Circle: ", circle_number)
		print("Diameter: ", i.diameter)
		print("Perimeter: ", i.perimeter)
		print("Filled: ", i.filled)
		circle_number+=1