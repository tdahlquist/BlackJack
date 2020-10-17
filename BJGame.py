# This is a game that will play Blackjack
import random
import sys

####### Variables
deck = {'A - hearts': 1,'2 - hearts': 2,'3 - hearts': 3,'4 - hearts': 4,'5 - hearts': 5,'6 - hearts': 6,'7 - hearts': 7 ,'8 - hearts': 8,'9 - hearts': 9,'10 - hearts': 10,'J - hearts': 10,'Q - hearts': 10,'K - hearts': 10,
        'A - Clubs': 1,'2 - Clubs': 2,'3 - Clubs': 3,'4 - Clubs': 4,'5 - Clubs': 5,'6 - Clubs': 6,'7 - Clubs': 7 ,'8 - Clubs': 8,'9 - Clubs': 9,'10 - Clubs': 10,'J - Clubs': 10,'Q - Clubs': 10,'K - Clubs': 10,
        'A - Spades': 1,'2 - Spades': 2,'3 - Spades': 3,'4 - Spades': 4,'5 - Spades': 5,'6 - Spades': 6,'7 - Spades': 7 ,'8 - Spades': 8,'9 - Spades': 9,'10 - Spades': 10,'J - Spades': 10,'Q - Spades': 10,'K - Spades': 10,
        'A - Diamonds': 1,'2 - Diamonds': 2,'3 - Diamonds': 3,'4 - Diamonds': 4,'5 - Diamonds': 5,'6 - Diamonds': 6,'7 - Diamonds': 7 ,'8 - Diamonds': 8,'9 - Diamonds': 9,'10 - Diamonds': 10,'J - Diamonds': 10,'Q - Diamonds': 10,'K - Diamonds': 10,
}

chipCount, minBet, maxBet = 100, 5, 100
cardAndValue = list(deck.items())

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
    card, cValue = random.choice(cardAndValue)    
    dealerHand.setdefault(card,cValue)
    newDeck.pop(card)
    print('Dealer flips second card and is showing ' + str(dealerHand.keys()) + ' for a total of: ' + str(sum(dealerHand.values())) + '\n')
    while True:
        dh = sum(dealerHand.values())
        if dh > 16:
            return dh
        else:
            card, cValue = random.choice(cardAndValue)    
            dealerHand.setdefault(card,cValue)
            newDeck.pop(card)
            print('Dealer hits and now has a total of: ' + str(sum(dealerHand.values())) + '\n')

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
    newDeck = deck # Set's the new deck - each game uses a freshly shuffled deck.
    
    print('You currently have $' + str(chipCount))

    # Place and check if bet is legal
    bet = placeBet()

    # flop initial cards into a list called flop
    playerHand = {}
    dealerHand = {}
    for i in range(3):
        card, cValue = random.choice(cardAndValue)
        if (i+2) % 2 == 0:
            playerHand.setdefault(card,cValue)
            newDeck.pop(card)
        else:
            dealerHand.setdefault(card,cValue)
            newDeck.pop(card) 
    print('You are showing the two cards ' + str(playerHand.keys()))
    print('The dealer is showing a ' + str(dealerHand.keys()) + '\n')

    # Ask P1 what they would like to do first do if stay
    hitStay = ask(input('What would you like to do? Hit or Stay? (Type H or S): '))
    print('You decided to - ' + hitStay)
    if hitStay == 'Stay':       
        dh = dealerHitCheck() # Dealer needs to hit if necessary
        gameStatus = whoWon(sum(playerHand.values()),dh)
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
