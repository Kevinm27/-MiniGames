#Test File

import random
import sys

def numbers(array, width, height):
	rows  = height
	col = width
		# for loop looks into the value of the array
		# we might be able to transform it into a dictionary instead 
		#I think they're the same speed
		
	for i, rows in enumerate(array):
		
		for j, value in enumerate(rows):
			# Need to check what the error is to throw an exception
			if (value == -1):
				array[i + 1][j + 1] = array[i + 1][j + 1] + 1
				array[i + 1][j] = array[i + 1][j] + 1
				array[i][j + 1] = array[i][j + 1] + 1

				array[i - 1][j - 1] = array[i - 1][j - 1] + 1
				array[i ][j - 1] = array[i ][j - 1] + 1
				array[i - 1][j ] = array[i - 1][j ] + 1

				array[i - 1][j + 1] = array[i - 1][j + 1] + 1
				array[i + 1][j - 1] = array[i + 1][j - 1] + 1

	
	return array
			
#Instead of the numbers function above, we could probably make it a lil better
#Im thinking of storing the random bombs into an array with their coordinates
	# - In these coordinates, we add one to the numbers around it
'''def incrementSurrounding(array, rows, cols, bomb_Locations, num_Bombs):
	for i in range(num_Bombs):
		#Check all use cases, including the sides and corners
'''		


def main():
	#Making seed actually random
	fileRead = open("seed.txt", "r")
	num = int(fileRead.read())
	SEED = num
	fileRead.close

	fileOverwrite = open("seed.txt", "w")
	fileOverwrite.write(str(num + 1))
	fileOverwrite.close

	name = input("Welcome to Mine Sweeper!\nWhat is your name? ")
	height = inputDimension("height")
	width = inputDimension("width")
	print("Creating a", height, " x ", width, "board! ")

	grid = initialize_Array(width, height)

	bomb_amount = (width * height) / 8

	grid, bomb_Locations = add_bombs(bomb_amount, grid, height, width, SEED)

	grid = numbers(grid, width, height)

	print_board(grid, height, width)

	print(bomb_Locations)


def inputDimension(measurement):
	returnMeasurement = input(f"What would you like the {measurement} of the board to be? ")
	while(returnMeasurement.isnumeric() == False or int(returnMeasurement) <= 3):
		returnMeasurement = input(f"ERROR, ENTER A VALID INT!(> 3)\nWhat would you like the {measurement} of the board to be? ")

	return int(returnMeasurement)

def initialize_Array(width, height):
	array = [[0 for x in range(width)] for y in range(height)]
	return array

def add_bombs(bombs, array, height, width, SEED):
	bomb_Locations = []
	while(bombs > 0):
		random.seed(bombs + SEED)
		a = random.randrange(height - 1)
		random.seed(bombs + SEED + 1)
		b = random.randrange(width - 1)
		if ((array[a][b] != -1) ):
			bomb_Locations.append((a, b))
			array[a][b] = -1
			bombs -=1
	return array, bomb_Locations
		
	
def print_board(arr, height, width):
	for height in arr:
		print("".join(["{:<{mx}}".format(ele, mx = width) for ele in height]))

	
main()