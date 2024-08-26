def areaOfWalls(width, height):
    totalWallArea = 4*width*height
    return totalWallArea

def areaOfRoof(width, slantHeight):
    totalRoofArea = 4*width*(slantHeight/2)
    return totalRoofArea

def totalCost(width, height, slantHeight, costPerSqrMeter):
    wallArea = areaOfWalls(width, height)
    roofArea = areaOfRoof(width, slantHeight)
    totalArea = wallArea+roofArea
    cost=costPerSqrMeter*totalArea
    return cost

print("House Paint Calculator")
print("Width of house walls:")
W = float(input())

print("Height of house walls:")
H = float(input())

print("Roof slant height:")
T = float(input())

print("Cost of paint for each square meter:")
C = float(input())

#Call the function with the necessary parameters and give it a variable name so it can be printed to the output terminal
totalPrice = totalCost(W, H, T, C)
print("Total cost for an all-blue house: $" + str(totalPrice))

