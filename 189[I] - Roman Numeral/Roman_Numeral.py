##Converts Roman Numerals to Base 10 and vice versa
##http://www.reddit.com/r/dailyprogrammer/comments/2ms946/20141119_challenge_189_intermediate_roman_numeral/



def roman_to_base10(romanNum):
	key = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	transform = 0
	
	
	if len(romanNum) < 2:
		return key[romanNum[0]]
	#Add first numeral to allow for comparisons in loop
	transform = key[romanNum[0]]
	for i in range(1,len(romanNum)):
		#If the next number is bigger, subtract
		if (key[romanNum[i-1]] < key[romanNum[i]]):
			transform = transform - (2*key[romanNum[i-1]])
			transform = transform + key[romanNum[i]]
		else:
			transform = transform + key[romanNum[i]]
	
	return transform
	

def base10_to_roman(baseNum):
	#make paired list to filter baseNum through
	key = zip([1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1], ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"])
	baseNum = int(baseNum)
	transform = ''
	#Try to fit largest piece first, and then fit as many as possible, adding associated roman numeral each iteration
	for b, r in key:
		while baseNum >= b:
			transform = transform + r
			baseNum = baseNum - b
	return transform

def main():
	num = input("Input base 10 number or roman numerals: ")
	roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
	base = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	#Check for numbers first
	input_base = True
	for i in num:
		if i not in base:
			input_base = False
			
	if (input_base == True and int(input_base) < 5000):
		print("Base10 input")
		print("Roman output:", base10_to_roman(num))
		
	else:
		#Change input to upper case
		num = num.upper()
		input_roman = True
		for i in num:
			if i not in roman:
				input_roman = False
				
		if input_roman == True:
			print("Roman input")
			print("Base 10 output:", roman_to_base10(num))
		else:
			print("Invalid input")
		
main()

