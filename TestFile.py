#Test File

import random
def JefIsGay():
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

def initialize_Array(w, h):
	arr = [[0 for x in range(w)] for y in range(h)]
	return arr

def add_bombs(bombs, arr, h, w):
	while(bombs > 0):
		random.seed(bombs)
		a = random.randrange(h - 1)
		b = random.randrange(w - 1)
		if ((arr[a][b] != -1) ):
			arr[a][b] = -1
			bombs -=1
	return arr
		
	
def print_board(arr, height, width):
	for height in arr:
		print("".join(["{:<{mx}}".format(ele, mx = width) for ele in height]))

	
main()