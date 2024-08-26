def tripCostCalculator(airFarePerPerson, roomCostPerNight, numberOfTravellers, numberOfNights):
    
    #calculate the total flight cost
    flightCost = (airFarePerPerson * numberOfTravellers)

    #calculate the total hotel cost
    #If the number of travellers is odd, one extra room will be booked
    if (numberOfTravellers % 2) == 0:
        hotelCost = (numberOfTravellers/2)*roomCostPerNight*numberOfNights
    elif (numberOfTravellers % 2) == 1:
        hotelCost = (((numberOfTravellers-1)/2)+1)*roomCostPerNight*numberOfNights

    #Calculate the total cost
    totalCost = (flightCost + hotelCost)

    #Return the total cost
    return totalCost


print("Calculate Trip Cost")
print("Enter cost of flight per person ($): ")
ticketPrice = float(input())

print("Enter cost of a double room per night: ")
nightlyPrice = float(input())

print("Enter the number of people: ")
totalTravelers = float(input())

print("Enter the number of nights: ")
numOfNights = float(input())

#Call the function with the necessary parameters and give it a variable name so it can be printed to the output terminal
tripCost = tripCostCalculator(ticketPrice, nightlyPrice, totalTravelers, numOfNights)
print("The total cost of the trip for the group is $" + str(tripCost) + ".")


    