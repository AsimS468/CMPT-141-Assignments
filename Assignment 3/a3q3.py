#rock:                           paper:                             scissors:
#   beats scissors                  beats rock                         beats paper
#   beats lizard                    beats spock                        beats lizard

#   gets beaten by paper            gets beaten by lizard              gets beaten by rock
#   gets beaten by spock            gets beaten by scissors            gets beaten by spock

#   ties with rock                  ties with paper                    ties with scissors

#lizard:                           spock:
#   beats paper                       beats rock 
#   beats spock                       beats scissors 

#   gets beaten by rock               gets beaten by lizard  
#   gets beaten by scissors           gets beaten by paper  
 
#   ties with lizard                  ties with spock

import sys

rock = "rock"
paper = "paper"
scissors = "scissors"
lizard = "lizard"
spock = "spock"

def RPSLS(player1, player2):
    
    if player1==rock:
        if player2==scissors or player2==lizard:
            return 1
        elif player2==paper or player2==spock:
            return 2
        elif player2==rock:
            return 0
        
    elif player1==paper:
        if player2==rock or player2==spock:
            return 1
        elif player2==lizard or player2==scissors:
            return 2
        elif player2==paper:
            return 0
        
    elif player1==scissors:
        if player2==paper or player2==lizard:
            return 1
        elif player2==rock or player2==spock:
            return 2
        elif player2==scissors:
            return 0
        
    elif player1==lizard:
        if player2==paper or player2==spock:
            return 1
        elif player2==rock or player2==scissors:
            return 2
        elif player2==lizard:
            return 0
        
    elif player1==spock:
        if player2==scissors or player2==rock:
            return 1
        elif player2==paper or player2==lizard:
            return 2
        elif player2==spock:
            return 0
        

print('Enter move for player 1:')
p1Move = input()

if (p1Move!=rock)and(p1Move!=paper)and(p1Move!=scissors)and(p1Move!=lizard)and(p1Move!=spock):
    print('Invalid move!')
    sys.exit()

print('Enter move for player 2:')
p2Move = input()

if (p2Move!=rock)and(p2Move!=paper)and(p2Move!=scissors)and(p2Move!=lizard)and(p2Move!=spock):
    print('Invalid move!')
    sys.exit()

game = RPSLS(p1Move, p2Move)

if game==1:
    print('Player 1 wins!')
elif game==2:
    print('Player 2 wins!')
elif game==0:
    print('It was a tie!')
