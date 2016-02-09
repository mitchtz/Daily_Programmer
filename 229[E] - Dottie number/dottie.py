import math

num = float(input("Input number to calculate: "))

num_prev = 0
i = 0
while (num != num_prev):
	num_prev = num
	num = math.cos(num)
	i+=1
print("Dottie number =", num)
print("Took", i, "iterations")
