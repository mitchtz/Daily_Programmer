#Mitch Zinser
from PIL import Image
import math, sys, time, os
#Uses Sobel edge detection to output an image of detected lines. File input is command line for directory of files
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
			jpg_sobel_pixels[x,y] = (grad)

	return jpg_sobel

if __name__ == "__main__":
	if len(sys.argv) > 1:
		directory_in = sys.argv[1]
	else:
		directory_in = ""

	#Set edge detection mode to use
	edge_mode = "sobel"
	#Change to other directory
	os.chdir(os.getcwd() + "\\" + directory_in)
	start_all = time.time()
	file_processed = 0
	#Iterate through all images with .jpg in directory
	for i in os.listdir(os.getcwd()):
		#If file is a jpg
		if i.endswith(".jpg"): 
			jpg_in = Image.open(i)
			
			#Use sobel edge detection
			if (edge_mode == "sobel"):
				file_processed += 1
				print("Processing", i)
				start = time.time()
				sobel_img = sobel(jpg_in)
				##sobel_img.show()
				print(time.time()-start, "seconds to process", jpg_in.size[0]*jpg_in.size[1], "pixels")
				#Save image
				sobel_img.save("sobel_" + i)
				print("<---------------->")
	print(time.time()-start_all, "seconds to process", file_processed, "files")
	#jpg.show()