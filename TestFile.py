#Test File



def main():
	name = input("Welcome to Mine Sweeper! What is your name? ")
	height = inputDimension("height")
	width = inputDimension("width")

<<<<<<< Updated upstream



=======
	print("Creating a", str(height), " x ", str(width), "board!")

def inputDimension(measurement):
	print("What would you like the", measurement, "of the board to be?")
	returnMeasurement = input()

	try:
		returnMeasurement = int(returnMeasurement)
		return returnMeasurement
	except:
		print("Please enter a number!")
		inputDimension(measurement)
	
>>>>>>> Stashed changes
main()