#Test File

import random



def main():
	name = input("Welcome to Mine Sweeper!\nWhat is your name? ")
	height = inputDimension("height")
	width = inputDimension("width")
	print("Creating a", str(height), " x ", str(width), "board! ")

	array0 = main_array(width, height)

	bomb_amount = int(width) * int(height)/8 -10

	array0 = add_bombs(bomb_amount, array0, height, width)

	print_board(array0, height)


def inputDimension(measurement):

	returnMeasurement = input(f" What would you like the {measurement} of the board to be? ")

	while(returnMeasurement.isnumeric() == False):
		returnMeasurement = input(f" ERROR, ENTER A VALID POSITIVE INT!\nWhat would you like the {measurement} of the board to be? ")
	return returnMeasurement

def main_array(w, h):
	arr = [[0] * int(w)] * int(h)
	return arr

def add_bombs(bombs, arr, h, w):
	while(bombs != 0):
		a = random.randrange(int(h) - 1)
		b = random.randrange(int(w) - 1)
		if ((arr[a][b] != -1) ):
			arr[a][b] = -1
			bombs -=1
	return arr
		
	

def print_board(arr, height):
	for height in arr:
		print(height)

	
main()