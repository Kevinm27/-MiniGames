#Test File
#Revision 7/4
# - Changed function numbers to a whole different algorithm
# - It is faster and a little easier to read
# - changed width and heigh to columns and rows respectfully

#For now we can have redundant code, once we finish, we can optimize and write sub functions

from calendar import c
from contextlib import nullcontext
import random

"""def numbers(array, width, height):
	#test push
	for i in range(width):
		left = i - 1
		right = i + 1
		for j in range(height):
			top = j + 1
			bottom = j - 1
			if array[i][j] == -1 and left >=0 and right <= (width - 1):
				if array[left][j] != -1:
					array[left][j] +=1
				if array[right][j] != -1:
					array[right][j] +=1

				if top >=0 and bottom <= (height - 1):
					if array[i][top] != -1:	
						array[i][top] +=1
					if array[i][bottom] != -1:
						array[i][bottom] +=1

					if array[left][top] != -1:
						array[left][top] +=1
					if array[right][bottom] != -1:
						array[right][bottom] +=1
					if array[right][top] != -1:
						array[right][top] +=1
					if array[left][bottom] != -1:
						array[left][bottom] +=1

	
	return array
"""			

#The helper functions are so we reduce the chances of mistakinly writing wrong code and improve readability
def incrementTopLeft(array, row, col):
	if array[row - 1][col - 1] != -1:
		array[row - 1][col - 1] += 1
	return array
def incrementTopMid(array, row, col):
	if(array[row - 1][col] != -1):
		array[row - 1][col] += 1
	return array
def incrementTopRight(array, row, col):
	if (array[row - 1][col + 1] != -1):
		array[row - 1][col + 1] += 1
	return array
def incrementMidLeft(array, row, col):
	if(col - 1 >= 0 and array[row][col - 1] != -1):
		array[row][col - 1] += 1
	return array
def incrementMidRight(array, row, col):
	if(col + 1 <= col - 1 and array[row][col + 1] != -1):
		array[row][col + 1] += 1
	return array
def incrementBotLeft(array, row, col):
	if(col - 1 > 0 and array[row + 1][col - 1] != -1):
		array[row + 1][col - 1] += 1
	return array
def incrementBotMid(array, row, col):
	if(array[row + 1][col] != -1):
		array[row + 1][col] += 1
	return array
def incrementBotRight(array, row, col):
	if(col + 1 <= col - 1 and array[row + 1][col + 1] != -1):
		array[row + 1][col + 1] += 1
	return array
#If you noticed, the code has redundancy, we can make the if statements even more efficient by changing the order
	# for example, some if statements will increment a box either way, im lazy so we can do it later

# Trying to shorten it, adding conditionals to helper functions
	"""

def incrementSurrounding(array, rows, cols, bomb_Locations, bomb_amount):
	for i in range(bomb_amount):
		row = bomb_Locations[i][0]
		col = bomb_Locations[i][1]
		array = incrementTopLeft(array, row ,col)

		array = incrementTopRight(array, row, col)

		array = incrementTopMid(array, row, col)

		array = incrementBotLeft(array, row, col)

		array = incrementBotRight(array, row, col)
	
		array = incrementBotMid(array, row, col)
		
		array = incrementMidLeft(array, row, col)

		array = incrementMidRight(array, row, col)
	print("Hello")
	return array
	"""

def incrementSurrounding(array, rows, cols, bomb_Locations, bomb_amount):
	for i in range(bomb_amount):
		row = bomb_Locations[i][0]
		col = bomb_Locations[i][1]

		#Check to not increment bombs on accident
		#Try to increment all around, if it cant then it wont go thru if

		#Check if we can increment above at all, if we can check corner and side
		if(row - 1 >= 0):
			if(col - 1 >= 0 and array[row - 1][col - 1] != -1):
				array = incrementTopLeft(array, row ,col)

			if(col + 1 <= cols - 1 and array[row - 1][col + 1] != -1):
				array = incrementTopRight(array, row, col)

			if(array[row - 1][col] != -1):
				array = incrementTopMid(array, row, col)
	
		#We checked the top, now lets check underneath
		if(row + 1 <= rows - 1):
			if(col - 1 > 0 and array[row + 1][col - 1] != -1):
				array = incrementBotLeft(array, row, col)

			if(col + 1 <= cols - 1 and array[row + 1][col + 1] != -1):
				array = incrementBotRight(array, row, col)
			
			if(array[row + 1][col] != -1):
				array = incrementBotMid(array, row, col)

		#Now we check the left and right
		if(col - 1 >= 0 and array[row][col - 1] != -1):
			array = incrementMidLeft(array, row, col)

		if(col + 1 <= col - 1 and array[row][col + 1] != -1):
			array = incrementMidRight(array, row, col)

	return array



			

def main():
	#Making seed actually random
	fileRead = open("seed.txt", "r")
	num = int(fileRead.read())
	SEED = num
	fileRead.close


	name = input("Welcome to Mine Sweeper!\nWhat is your name? ")
	rows = inputDimension("rows")
	cols = inputDimension("columns")
	print("Creating a", rows, " x ", cols, "board! ")

	grid = initialize_Array(rows, cols)

	bomb_amount = int((rows * cols) / 8) + 1
	#Made a list of pairs which holds the coordinates of the bombs
	grid, bomb_Locations = add_bombs(bomb_amount, grid, rows, cols, SEED)

	#grid = numbers(grid, width, height)
	grid = incrementSurrounding(grid, rows, cols, bomb_Locations, bomb_amount)
	print_board(grid, rows, cols)

	print(bomb_Locations)


	fileOverwrite = open("seed.txt", "w")
	fileOverwrite.write(str(num + 1))
	fileOverwrite.close



def inputDimension(measurement):
	returnMeasurement = input(f"What would you like the {measurement} of the board to be? ")
	while(returnMeasurement.isnumeric() == False or int(returnMeasurement) <= 3):
		returnMeasurement = input(f"ERROR, ENTER A VALID INT!(> 3)\nWhat would you like the {measurement} of the board to be? ")

	return int(returnMeasurement)

def initialize_Array(row, col):
	array = [[0 for x in range(row)] for y in range(col)]
	return array

def add_bombs(bombs, array, rows, cols, SEED):
	bomb_Locations = []
	while(bombs > 0):
		random.seed(bombs + SEED)
		row = random.randrange(rows - 1)
		random.seed(bombs + SEED + 1)
		col = random.randrange(cols - 1)
		if (array[row][col] != -1):
			bomb_Locations.append((row, col))
			array[row][col] = -1
			bombs -=1
	return array, bomb_Locations
		
	
def print_board(arr, row, col):
	for row in arr:
		print("".join(["{:<{mx}}".format(ele, mx = col) for ele in row]))

	
main()