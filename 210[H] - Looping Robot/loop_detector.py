#Takes input string of commands to move robot. Commands can be S (move one forward), R (Turn right) or L (Turn left)
#http://www.reddit.com/r/dailyprogrammer/comments/32vlg8/20150417_challenge_210_hard_loopy_robots/
#Takes in command string. return True if loops, with number of loops. Else returns False
#Loops the commands up to 4 times (max for these possible commands to produce loop)
def find_loop(commands):
	#Possible commands for robot, first number of pair is steps to take forward, second number is direction to turn
	poss_commands = {"S":[1,0], "R":[0,1], "L":[0,-1]}
	#Direction robot is facing. 0 is North, 1 is East, etc.
	direction = 0
	#X, y coordinates
	coord = [0,0]
	#Loop through commands up to 4 times
	for i in range(0, 4):
		#loop through command string
		for j in commands:
			move = poss_commands[j.upper()]
			#Check if we are stepping, if so, change x or y according to direction we are facing
			if move[0] == 1:
				#North
				if direction%4 == 0:
					coord[1] = coord[1] + 1
				#East
				if direction%4 == 1:
					coord[0] = coord[0] + 1
				#South
				if direction%4 == 2:
					coord[1] = coord[1] - 1
				#West
				if direction%4 == 3:
					coord[0] = coord[0] - 1
			#Else we are turning. Apply turn to direction
			else:
				direction = direction + move[1]

		#Print current location
		print(coord, direction%4)
		#Check if we are facing North again. If so, check for completion
		if direction%4 == 0:
			if coord == [0,0]:
				return [True, i+1]

	#Return solution
	return [False, 0]
commands_in = input("Input command string: ")
'''
Challenges
SRLLRLRLSSS - True, 4 loops
SRLLRLRLSSSSSSRRRLRLR - True, 2 loops
SRLLRLRLSSSSSSRRRLRLRSSLSLS - False
LSRS - False

commands_in = "LSRS"
'''
solution = find_loop(commands_in)
print("Command string loops =", solution[0])
if solution[0]:
	print("Takes", solution[1], "loops to return to start")