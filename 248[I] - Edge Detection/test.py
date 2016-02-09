from PIL import Image
import sys, math

if __name__ == "__main__":
	if len(sys.argv) > 1:
		name_in = sys.argv[1]
	else:
		name_in = "advice_dog"
	jpg_in = Image.open(name_in + ".jpg")

	#Convert to grayscale and get pixels
	jpg_pixels = jpg_in.load()
	#New Image
	jpg_sobel = Image.new( 'RGB', (jpg_in.size[0],jpg_in.size[1]), "black")
	jpg_sobel_pixels = jpg_sobel.load()
	##jpg_sobel_pixels[0,0] = 

	'''Sobel Algorithm
	#Iterate over x axis (not edges)
	for x in range(1,jpg_in.size[0]-1):
		#Iterate over y axis (not edges)
		for y in range(1,jpg_in.size[1]-1):
			#Calculate horizontal edge
			edge_h = (jpg_pixels[x+1,y-1] + 2*jpg_pixels[x+1,y] + jpg_pixels[x+1,y+1]) - (jpg_pixels[x-1,y-1] + 2*jpg_pixels[x-1,y] + jpg_pixels[x-1,y+1])
			#Calculate vertical edge
			edge_v = (jpg_pixels[x-1,y+1] + 2*jpg_pixels[x,y+1] + jpg_pixels[x+1,y+1]) - (jpg_pixels[x-1,y-1] + 2*jpg_pixels[x,y-1] + jpg_pixels[x+1,y-1])
			#Calculate gradient
			grad = math.sqrt((edge_h * edge_h) + (edge_v * edge_v))
			##if grad > 255: print(grad)
			#Less detection, less affected by noise?
			#grad = abs(edge_h + edge_v)
			#Write pixel
			jpg_sobel_pixels[x,y] = int(grad)
	'''




	#Color Attempt
	value = 0
	for i in range(jpg_in.size[0]):
		aR = 50
		aG = 50
		aB = 225  # RGB for our 1st color (blue in this case).
		bR = 255
		bG = 100
		bB = 50  # RGB for our 2nd color (red in this case).

		value = i*(1/jpg_in.size[0])

		red = int((bR - aR) * vaule + aR)      # Evaluated as -255*value + 255.
		green = int((bG - aG) * value + aG)     # Evaluates as 0.
		blue  = int((bB - aB) * value + aB)
		#for j in range(10+1):
		jpg_sobel_pixels[i, 40] = (red, green, blue)
		
		print(red, green, blue)

	print(jpg_sobel_pixels[20,40])
	print(value)
	jpg_sobel.show()