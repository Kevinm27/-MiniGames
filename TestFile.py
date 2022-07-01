#Test File

import random
#seed(1)
def main():
	name = input("Welcome to Mine Sweeper!\nWhat is your name? ")
	height = inputDimension("height")
	width = inputDimension("width")
	print("Creating a", height, " x ", width, "board! ")

	grid = main_array(width, height)
	#At this point array0 contains all 0s
	#---------------------------------------
	bomb_amount = width * height / 8 - 10
	print("Hi")
	add_bombs(bomb_amount, grid, height, width)

	#print_board(array0, height)


def inputDimension(measurement):

	returnMeasurement = input(f"What would you like the {measurement} of the board to be? ")

	while(returnMeasurement.isnumeric() == False):
		returnMeasurement = input(f"ERROR, ENTER A VALID POSITIVE INT!\nWhat would you like the {measurement} of the board to be? ")

	return int(returnMeasurement)

def main_array(w, h):
	#arr = [[0] * int(w)] * int(h)
	arr = [[0 for x in range(w)] for y in range(h)]
	return arr

def add_bombs(bombs, arr, h, w):
	print("While")
	while(bombs != 0):
		print("Random")
		a = random.randint(0, h - 1)
		print("A: ", a)
		b = random.randint(0, w - 1)
		print("B: ", b)
		if ((arr[a][b] != -1) ):
			arr[a][b] = -1
		bombs -=1
	#return arr
		
	

def print_board(arr, height):
	print(arr[0])

	
main()