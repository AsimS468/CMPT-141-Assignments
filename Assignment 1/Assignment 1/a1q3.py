print("Enter the total value of wheat , barley and other grains plundered in dollars:")
booty = float(input())

print("Enter the number of crew:")
numCrewMembers = int(input())

captainsBooty = (booty/100)*30
crewsBooty = (booty/100)*70
crewMemberBooty = (crewsBooty/numCrewMembers)
donatedBooty = (captainsBooty/100)*15

print("Tractor Jack's 30 percent share of the booty is worth: " + str(captainsBooty))
print("Crew's 70 percent share of the booty is worth: " + str(crewsBooty))
print("Each crew member takes home: " + str(crewMemberBooty))
print("Jack donates $" + str(donatedBooty) + " to the Saskatoon Food Bank.")