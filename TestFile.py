#Test File

import random
def numbers(array, height):
	lis = {}
	for height in array:
		lis

			

	#Making the function to increment the values around the bomb
	#dont duplicate code
	#heeheeeeeeeereeee

def main():
	name = input("Welcome to Mine Sweeper!\nWhat is your name? ")
	height = inputDimension("height")
	width = inputDimension("width")
	print("Creating a", height, " x ", width, "board! ")

	grid = initialize_Array(width, height)

	bomb_amount = (width * height) / 8

	grid = add_bombs(bomb_amount, grid, height, width)

	print_board(grid, height, width)


def inputDimension(measurement):
	returnMeasurement = input(f"What would you like the {measurement} of the board to be? ")
	while(returnMeasurement.isnumeric() == False):
		returnMeasurement = input(f"ERROR, ENTER A VALID POSITIVE INT!\nWhat would you like the {measurement} of the board to be? ")

	return int(returnMeasurement)

def initialize_Array(width, height):
	array = [[0 for x in range(width)] for y in range(height)]
	return array

def add_bombs(bombs, array, height, width):
	while(bombs > 0):
		random.seed(bombs)
		a = random.randrange(height - 1)
		b = random.randrange(width - 1)
		if ((array[a][b] != -1) ):
			array[a][b] = -1
			bombs -=1
	return array
		
	
def print_board(arr, height, width):
	for height in arr:
		print("".join(["{:<{mx}}".format(ele, mx = width) for ele in height]))

	
main()