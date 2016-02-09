#Mitch Zinser
from PIL import Image
import math, sys, time, os
#Uses Sobel edge detection to output an image of detected lines. File input can be command line (without.jpg)
def sobel(img_in):
	#Convert to grayscale and get pixels
	jpg_pixels = img_in.convert('L').load()
	#Create new image in grayscale
	jpg_sobel = Image.new( 'L', (img_in.size[0],img_in.size[1]), "black")
	jpg_sobel_pixels = jpg_sobel.load()
	'''Sobel Algorithm'''
	#Iterate over x axis (not edges)
	for x in range(1,img_in.size[0]-1):
		#Iterate over y axis (not edges)
		for y in range(1,img_in.size[1]-1):
			#Calculate horizontal edge
			edge_h = (jpg_pixels[x+1,y-1] + 2*jpg_pixels[x+1,y] + jpg_pixels[x+1,y+1]) - (jpg_pixels[x-1,y-1] + 2*jpg_pixels[x-1,y] + jpg_pixels[x-1,y+1])
			#Calculate vertical edge
			edge_v = (jpg_pixels[x-1,y+1] + 2*jpg_pixels[x,y+1] + jpg_pixels[x+1,y+1]) - (jpg_pixels[x-1,y-1] + 2*jpg_pixels[x,y-1] + jpg_pixels[x+1,y-1])
			#Calculate gradient
			grad = math.sqrt((edge_h * edge_h) + (edge_v * edge_v))
			#Less detection, less affected by noise?
			##grad = abs(edge_h + edge_v)
			#Write pixel
			jpg_sobel_pixels[x,y] = int(grad)

	return jpg_sobel

if __name__ == "__main__":
	if len(sys.argv) > 1:
		name_in = sys.argv[1]
	else:
		name_in = "potatoes"
	jpg_in = Image.open(name_in + ".jpg")
	#print("X:", jpg.size[0], "Y:", jpg.size[1])
	#Set edge detection mode to use
	edge_mode = "sobel"
	#Use sobel edge detection
	if (edge_mode == "sobel"):
		start = time.time()
		sobel_img = sobel(jpg_in)
		sobel_img.show()
		print(time.time()-start, "seconds to process", jpg_in.size[0]*jpg_in.size[1], "pixels")

		#Save image to folder
		dl_path = os.getcwd() + "\\sobel"
		#Test to see if directory exists already, if not, create one
		if not os.path.exists(dl_path):
			os.makedirs(dl_path)
		#Change working directory to one on customers computer
		os.chdir(dl_path)
		sobel_img.save("sobel_" + name_in + ".jpg")

	#jpg.show()