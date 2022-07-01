#Test File



def main():
	name = input("Welcome to Mine Sweeper!\nWhat is your name? ")
	height = inputDimension("height")
	width = inputDimension("width")
	print("Creating a", str(height), " x ", str(width), "board! ")

	array0 = main_array(width, height)


def inputDimension(measurement):

	returnMeasurement = input(f" What would you like the {measurement} of the board to be? ")

	while(returnMeasurement.isnumeric() == False):
		returnMeasurement = input(f" ERROR, ENTER A VALID POSITIVE INT!\nWhat would you like the {measurement} of the board to be? ")
	return returnMeasurement

def main_array(w, h):
	arr = [[0] * w] * h
	return arr
	
main()