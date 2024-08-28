import random
import math
import sys #to exit the program if the random number is not a perfect cube

min = 1
max = 10000

randNum = random.randint(min, max)

print('Your random number is: ' + str(randNum))

if math.pow(randNum, 1/3) == int(math.pow(randNum, 1/3)):
    print("Amazing! "+ str(randNum) +" is a perfect cube!")
else:
    sys.exit() #to exit the program if the random number is not a perfect cube