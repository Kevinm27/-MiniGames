#Test File

import random

def numbers(array, width, height):
	
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