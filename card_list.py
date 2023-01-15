#!/usr/bin/python3
cards = {
        'star': [1,2,4,5,7,8],
         'circle': [1,2,3,4,5,7,8,10,11,12,13,14],
         'triangle': [1,2,3,4,5,7,8,10,11,12,13,14],
         'cross': [1,2,3,5,7,10,11,13,14],
         'square': [1,2,3,5,7,10,11,13,14],
         'whot': ['20a','20b','20c','20d'],
         }
import random
total_shapes = len(cards)
#print(cards)

park = []
for shapes, number in cards.items():
    for numbers in number:
        
        #listall = random.choice(list(shapes))
        #listnum = random.choice(list(cards[listall]))
        #indexofcard = cards[listall].index(listnum)
        card_list = f"{numbers} {shapes}"
        #fullcard = f'{listall}  {listnum}'
        park.append(card_list)
        #del cards[listall][indexofcard]

allcards = park
newlist = []
for mix in range(len(allcards)):
    hell = random.choice(allcards)
    if hell in newlist:
        pass
    else:
        newlist.append(hell)
newlist_total = len(newlist)

for final in range(1000):
    hell = random.choice(allcards)
    if hell in newlist:
       pass
    else:
        newlist.append(hell)

#def complete():
    #hell = random.choice(allcards)
    #if hell in newlist:
        #pass
    #else:
        #newlist.append(hell)
    #if newlist_total != 50:
        #complete()
#complete()

newlist_total = len(newlist)
#print(newlist_total)





player1_cards = []
for shapes in range(6):
    collect = random.choice(newlist)
    if collect in player1_cards:
       pass
    else:
        player1_cards.append(collect)

player1_cards = player1_cards[0:5]
print(f"PLAYER 1 :{player1_cards} \n\n")

set1 = set(newlist)
set2 = set(player1_cards)
newlist = list(set1 - set2)


player2_cards = []
for shapes in range(6):
    collect2 = random.choice(newlist)
    if collect2 in player2_cards:
       pass
    else:
        player2_cards.append(collect2)

player2_cards = player2_cards[0:5]
print(f"PLAYER 2: {player2_cards}\n\n")
set3 = set(newlist)
set4 = set(player2_cards)
newlist = list(set3 - set4)



set5 = set(newlist)
set6 = set(newlist[0:1])
newlist = list(set5 - set6)

play_spot = list(set6)


print(f"SPORT: {play_spot}\n")
#print(f"SPORT: {play_spot[-1][-3:]}\n")
print(f"MARKET: {newlist}")

all_the_cards = int(len(newlist)) + int(len(player2_cards)) + int(len(player1_cards)) 


print(all_the_cards)

#user_input_type = input("type 'p' to play or 'm' for market: ")
#user_input = input("type name of card: ")

class Whot:
    def __init__(self, spot, player1, player2,market):
        #self.card = card
        #self.types = types
        self.spot = spot
        self.player1 = player1
        self.player2 = player2
        self.market = market

    def play(self):
        user_input_type = input("type 'p' to play or 'm' for market: ") 
        if user_input_type == "p":
            user_input = input("type name of card: ")
            if user_input[:2] == play_spot[-1][:2] and user_input in player1_cards:
                
                print("good")
                self.spot =  play_spot
                self.spot.append(user_input)
                print(f"GAME SPOT #### {self.spot}\n")
                index = self.player1.index(self.spot[-1])
                del self.player1[index]
                print(f"YOUR CARDS ####{self.player1}\n")
                Whot.has_been_called = True
                Whot.computer(self)
            elif user_input[-4:] == play_spot[-1][-4:] and user_input in player1_cards:
                print("good")
                self.spot =  play_spot
                self.spot.append(user_input)
                print(f"GAME SPOT #### {self.spot}\n")
                index = self.player1.index(self.spot[-1])
                del self.player1[index]
                print(f"YOUR CARDS ####{self.player1}\n")
                Whot.has_been_called = True
                Whot.computer(self)
            elif user_input[-4:] =="whot" :
                print("good")
                self.spot =  play_spot
                self.spot.append(user_input)
                print(f"GAME SPOT #### {self.spot}\n")
                index = self.player1.index(self.spot[-1])
                del self.player1[index]
                print(f"YOUR CARDS ####{self.player1}\n")
                Whot.has_been_called = True
                Whot.whot(self)
                Whot.computer(self)
            else:
         
                print("bad play again")
                Whot.play(self)
        elif user_input_type == "m":
            market = self.market[-1]
            print(f"YOU PICKED {market}")
            self.player1.append(market)
            index2 = self.market.index(market)
            del self.market[index2]
            Whot.has_been_called = True
            Whot.computer(self)


    def whot(self):
        ask_whot = input("What shape do you want? ")

    def computer(self):
        if Whot.has_been_called:
            print("Computer's turn")
            #if self.spot[-1][:2] in self.player2[:2]:
            
            y = []
            y1 = []
            y2 = []
            for x in self.player2:
                if x:
                    y.append(x[:2])
                    y1.append(x)
                    y2.append(x[-4:])
            if self.spot[-1][:2] in y:
                index2 = y.index(self.spot[-1][:2])
                self.player2 = y1 
                card = self.player2[index2]
                print(f"THE COMPUTER PLAYS #### {card}")
                self.spot.append(card)
                del self.player2[index2]
                print(f"SPOT #####{self.spot}\n\n")
                print(f"COMPUTER GAMES #####{self.player2}\n\n")
                Whot.play(self)
                Whot.has_been_called = False
            elif self.spot[-1][-4:] in y2:
                index2 = y2.index(self.spot[-1][-4:])
                self.player2 = y1
                card = self.spot[index2]
                print(f"THE COMPUTER PLAYS #### {card}")
                self.spot.append(card)
                del self.player2[index2]
                print(f"SPOT #####{self.spot}\n\n")
                print(f"COMPUTER GAMES #####{self.player2}\n\n")
                Whot.play(self)
                Whot.action.has_been_called = False
            else:
                print("Computer no get card to play so he go market to get!")

                market = self.market[-1]
                self.player2.append(market)
                index2 = self.market.index(market)
                del self.market[index2]
                Whot.play(self)
                Whot.action.has_been_called = False






my_whot = Whot( play_spot, player1_cards, player2_cards,newlist)
my_whot.play()

