# This is a game that will play Blackjack
import random
import sys

####### Variables
deck = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 10, 10, 10]
chipCount, minBet, maxBet = 100, 5, 100


###### Functions

# Checks if bet is legal
def placeBet():
    okayToBet = True
    while okayToBet:
        try:
            bet = int(input('What is your bet? \n'))
            if bet < minBet:
                print('Is this your first time? The minimum bet is $5')
            elif bet > chipCount:
                print('You better count your chips again')
            elif bet > maxBet:
                print('Hold on now, the max is 100')
            else:
                return int(bet)
        except ValueError:
            print('Enter a number only for your bet.')

# Checking to make sure user entered the correct command for hitting or staying
def ask(userInput):
    while True:
        if userInput == 'H':
            return 'Hit'
        if userInput == 'S':
            return 'Stay'
        else:
            userInput = input('Dude - If you want to hit, type H, or if you want to stay, type S: ')

# Need to play out dealers hand as needed
def dealerHitCheck():
    print('Dealer flips second card and shows he has a ' + str(dealerHand[0]) + ' and a ' + str(dealerHand[1]) + ' for a total of: ' + str(sum(dealerHand)) + '\n')
    while True:
        dh = sum(dealerHand)
        if dh > 16:
            return dh
        else:
            dealerHand.append(random.choice(deck))
            print('Dealer hits and now has: ' + str(sum(dealerHand)) + '\n')

def playerHit():
    cardNum = 3
    while True:
        playerHand.append(random.choice(deck))
        print('You got a ' + str(playerHand[cardNum-1]) + ' for a total of: ' + str(sum(playerHand)) + '\n')
        ph = sum(playerHand)
        if ph > 21:
            return ph
        hitStay = ask(input('What would you like to do? Hit or Stay? (Type H or S): \n'))
        if hitStay == 'Stay':
            return sum(playerHand)
        else:
            cardNum += 1

# This gets 2 values p-hand and d-hand to see who wins and return value of win, lose, push
def whoWon(player1, dealer): # Checking who won the game
    if player1 > 21:
        print('You busted!')
        gameStatus = 'lost'
    elif dealer > 21:
        print('Dealer busts!')
        gameStatus = 'won'
    elif player1 > dealer:
        print('You won!')
        gameStatus = 'won'
    elif player1 < dealer:
        print('You Lost!')
        gameStatus = 'lost'
    else:
        print('You pushed!')
        gameStatus = 'push'
    return gameStatus



####### Main program starts here
# Greeting

print ("-" * 70)
print ("|" + " " * 68 + "|")
print ("|" + " " * 25 + "Welcome to BLACKJACK" + " " * 23 + "|")
print ("|" + " " * 68 + "|")
print ("-" * 70 + '\n')

name = input('Please enter your name: ')
print('Hi ' + name + ', have not seen you in a while, pull up a chair! We are playing Blackjack. \n')

# Game starts here
while True:
    print('You currently have $' + str(chipCount))

    # Place and check if bet is legal
    bet = placeBet()

    # flop initial cards into a list called flop
    playerHand = []
    dealerHand = []
    for cards in range(2):
        playerHand.append(random.choice(deck))
        dealerHand.append(random.choice(deck))
    print('You show a ' + str(playerHand[0]) + ' and a ' + str(playerHand[1]))
    print('The dealer is showing a ' + str(dealerHand[0]) + '\n')

    # Ask P1 what they would like to do first do if stay
    hitStay = ask(input('What would you like to do? Hit or Stay? (Type H or S): '))
    print('You decided to - ' + hitStay)
    if hitStay == 'Stay':
        dh = dealerHitCheck() # Dealer needs to hit if necessary
        gameStatus = whoWon(sum(playerHand),dh)
    else:
        ph = playerHit() # player hits
        dh = dealerHitCheck() # Dealer needs to hit if necessary
        gameStatus = whoWon(ph,dh)

    # Program if they hit what to do

    # Updating the chip count based on the hand's outcome
    if gameStatus == 'won': 
        chipCount += bet
    elif gameStatus == 'lost':
        chipCount -= bet
    else:
        chipCount == chipCount
    if chipCount == 0:
        print('You lost all of your money, come back when you get some more.')
        sys.exit()

# End of loop
