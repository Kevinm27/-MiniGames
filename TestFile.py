#Test File



def main():
	name = input("Welcome to Mine Sweeper!\nWhat is your name? ")
	height = inputDimension("height")
	width = inputDimension("width")
	print("Creating a", str(height), " x ", str(width), "board! ")

def inputDimension(measurement):

	returnMeasurement = input("What would you like the " + measurement + " of the board to be? ")

	while(returnMeasurement.isnumeric() == False):
		returnMeasurement = input("ERROR, ENTER A VALID POSITIVE INT!\nWhat would you like the " + measurement + " of the board to be? ")
	return returnMeasurement
	
main()