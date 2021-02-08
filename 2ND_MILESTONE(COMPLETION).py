# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:11:58 2020

@author: jonat
"""
import colorama
from colorama import Fore
import random
from random import choice
3#   ***********RULES OF THE GAME**********
'''
When all the players have placed their bets, the dealer gives one card face up 
to each player in rotation clockwise, and then one card face up to themselves. 
Another round of cards is then dealt face up to each player, but the dealer takes
 the second card face down. Thus, each player except the dealer receives two cards 
face up, and the dealer receives one card face up and one card face down.
If a player's first two cards are an ace and a "ten-card" (a picture card or 10),
 giving a count of 21 in two cards, this is a natural or "blackjack." If any player 
 has a natural and the dealer does not, the dealer immediately pays that player one 
 and a half times the amount of their bet. If the dealer has a natural, they immediately 
 collect the bets of all players who do not have naturals, (but no additional amount).
 If the dealer and another player both have naturals, the bet of that player is a 
 stand-off (a tie), and the player takes back his chips.
If the dealer's face-up card is a ten-card or an ace, they look at their face-down 
card to see if the two cards make a natural. If the face-up card is not a ten-card or 
an ace, they do not look at the face-down card until it is the dealer's turn to play.
'''




           
class Blackjack():
    
    '''
    clubs=['ace',2,3,4,5,6,7,8,9,10,'face card']
    diamonds=['ace',2,3,4,5,6,7,8,9,10,'face card']
    hearts=['ace',2,3,4,5,6,7,8,9,10,'face card']
    spades=['ace',2,3,4,5,6,7,8,9,10,'face card']
    deck= clubs+diamonds+spades+hearts
    '''
    def __init__ (self,dealers_sum,dealers_hand=[],minimum_bet=10,maximum_bet=200,end_game=False):
        
        Blackjack.dealers_hand=dealers_hand
        Blackjack.dealers_sum=dealers_sum
        Blackjack.minimum_bet=minimum_bet
        Blackjack.maximum_bet=maximum_bet
        Blackjack.end_game=end_game
    '''
    def return_deck(self):
        
        deck=[5,5,5,5,5,5]
        #print(type(deck))
        #print(deck)
        return deck
    '''
        
    def return_deck(self):
        clubs=['ace',2,3,4,5,6,7,8,9,10,'face card']
        diamonds=['ace',2,3,4,5,6,7,8,9,10,'face card']
        hearts=['ace',2,3,4,5,6,7,8,9,10,'face card']
        spades=['ace',2,3,4,5,6,7,8,9,10,'face card']
        deck= clubs+diamonds+spades+hearts
        #print(type(deck))
        #print(deck)
        return deck
    
    
    def firstbet(self):
        pass
    
    def win_loss(self):
    #FUNCTION THAT CALCULATES IF THERE IS A VICTORY    
        if Blackjack.dealers_sum==21:#CHECKING 21 FOR THE THE DEALER ON THE START
            print(f'dealer has got blackjack! the house won')
            Player.player_money-=Player.player_bet
            print(f'Mr jack you lost and your mnoney is now {Player.player_money}$$$ ')
            myblackjack.end_game=True
            Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
            Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
            Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
        
        if Blackjack.dealers_sum>21:#IF DEALER PASSED 21
            print(f'Mr dealer your sum is {Blackjack.dealers_sum} and your busted!')
            Player.player_money+=Player.player_bet
            print(f'Mr jack has won and his money is now {Player.player_money}')
            myblackjack.end_game=True
            Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
            Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
            Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
            
        if Player.card_sum>21:#IF PLAYER PASSED 21
            print(f'Mr jack your sum is {Player.card_sum} and your busted!')
            print(f'your loss is {Player.player_bet}$$$ ')
            Player.player_money-=Player.player_bet
            print(f'players money is now {Player.player_money}!')
            Blackjack.end_game=True
            Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
            Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
            Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
                

        if Player.card_sum==21:#IF PLAYER GOT 21 
            print(f'Mr jack has got blackjack! collect your winnings')
            print(f'your win is {Player.player_bet}$$$ ')
            Player.player_money+=Player.player_bet
            print(f'players money is now {Player.player_money}!')
            myblackjack.end_game=True
            Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
            Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
            Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
    
    
    
    def lets_start(self):
        print('welcome Mr. jack to casino florentins blackjack! ')
        print('where the women are always hot and the joints are a plenty!')
        print(Fore.RED + 'minimum and maximum bets are: 10$ , 200$')#PUT COCLORANA HERE!
        print(Fore.RESET)#RESSETING THE COLOR OF TEXT
        print('Mr. jack place your bet!')
        jack_player.firstbet()#CALLING FIRST BET FOR PLAYER
        print('ok now 2 cards for you and 2 for the dealer')
    
    def dealer_cards(self):
        
        first_dealers_sum=0
        i=0
        
        while i<2:#GETTING THE 2 FIRST CARDS FROM THE DEALER!
                
            Blackjack.dealers_hand.append(random.choice(deck))#INSERTING A RANDOM CARD FROM THE DECK
            if Blackjack.dealers_hand[-1]=='face card'or Blackjack.dealers_hand[-1]=='ace':#IF ITS A FACE CARD THE PLAYER GETS 10

                if Blackjack.dealers_hand[-1]=='ace':#GO TO INPUT CONSOLE TO ASK THE PLAYER DOES HE WANT 1 OR 11
                    ace_dilema=input(f'Mr dealer your sum is {Blackjack.dealers_sum} do you want your ace to be one or eleven?  ')          
                    if ace_dilema.lower()=='one':
                        if i==0:#THE SUM OF THE ONLY FIRST CARD OF THE DEALER
                            first_dealers_sum+=1
                            Blackjack.dealers_sum+=1
                        else:
                            Blackjack.dealers_sum+=1
                    else:
                        if i==0:#THE SUM OF THE ONLY FIRST CARD OF THE DEALER
                            first_dealers_sum+=11
                            Blackjack.dealers_sum+=11
                        else:
                            Blackjack.dealers_sum+=11
                        
                        
                else:#FACE CARD
                    try:
                        #print('LETS TRY ADDING FACE FOR THE DEALER')
                        if i==0:
                            first_dealers_sum+=10
                            Blackjack.dealers_sum+=10
                        else:
                            Blackjack.dealers_sum+=10
                            
                    except:
                        Blackjack.dealers_hand[-1]=type(int)
                        print(f'in EXCEPTION type is {(type(Blackjack.dealers_hand[-1]))}')
                    
                        
                        
            else:#NOT FACE CARD OR ACE
                #print('LETS TRY ADDING REGULAR FOR THE DEALER')
                if i==0:
                    first_dealers_sum+=Blackjack.dealers_hand[-1]
                    Blackjack.dealers_sum+=Blackjack.dealers_hand[-1]
                else:
                    Blackjack.dealers_sum+=Blackjack.dealers_hand[-1]
                
                   
                    
            i+=1
        print(f'dealers one card is {Blackjack.dealers_hand[0]} and first sum is {first_dealers_sum} ')
        print(f'dealers cards are  {Blackjack.dealers_hand}')
        
    def dealers_move(self):#DEALERS TIME TO REVEAL HIS 2ND CARD AND TRYING TO BEAT THE PLAYER
        print(f'dealers move is now!')
        print(f'dealers cards are  {Blackjack.dealers_hand}')
        myblackjack.win_loss()
        
        if Blackjack.dealers_sum<21:#CONTINUE PLAYING!
            print(f'dealers sum is {Blackjack.dealers_sum} ')
            
            dealer_answer=input('Mr. dealer you wanna hit or stand?  ')
            
            while dealer_answer.lower()=='hit':
                
    
                Blackjack.dealers_hand.append(random.choice(deck))#INSERTING A RANDOM CARD FROM THE DECK
                if Blackjack.dealers_hand[-1]=='face card'or Blackjack.dealers_hand[-1]=='ace':#IF ITS A FACE CARD THE PLAYER GETS 10
    
                    if Blackjack.dealers_hand[-1]=='ace':#GO TO INPUT CONSOLE TO ASK THE PLAYER DOES HE WANT 1 OR 11
                        ace_dilema=input(f'Mr dealer your sum is {Blackjack.dealers_sum} do you want your ace to be one or eleven?  ')          
                        if ace_dilema.lower()=='one' :
                                Blackjack.dealers_sum+=1
                            
                        else:
                                Blackjack.dealers_sum+=11
                           
                            
                            
                    else:#FACE CARD
                        try:
                            #print('LETS TRY ADDING FACE FOR THE DEALER')
                            Blackjack.dealers_sum+=10
                            
                                
                        except:
                            Blackjack.dealers_hand[-1]=type(int)
                            print(f'in EXCEPTION type is {(type(Blackjack.dealers_hand[-1]))}')
                        
                            
                            
                else:#NOT FACE CARD OR ACE
                    #print('LETS TRY ADDING REGULAR FOR THE DEALER')
                    Blackjack.dealers_sum+=Blackjack.dealers_hand[-1]
                    
                myblackjack.win_loss()
                
                if myblackjack.end_game==True:
                    break
                
                print(f'now dealers sum is currently {Blackjack.dealers_sum}') 
                dealer_answer=input('Mr. dealer you wanna hit or stand?  ')
            
            if myblackjack.end_game==False:#DECIDE WINNER WHEN THEY BOTH STAND
                
                if Blackjack.dealers_sum!=Player.card_sum:#THEY BOTH STAND AND NOW WERE SEEING WHOS SUM IS BIGGER
                    if Blackjack.dealers_sum>Player.card_sum:
                        print(f'the dealer sum is bigger than Mr jack the house wins!')
                        Player.player_money-=Player.player_bet
                        print(f'Mr jack you lost and your mnoney is now {Player.player_money}$$$ ')
                        myblackjack.end_game=True
                        Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
                        Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
                        Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
                        
                    else:
                        print(f'Mr jack sum is bigger than the dealer Mr jack wins!')
                        Player.player_money+=Player.player_bet
                        print(f'Mr jack has won and his money is now {Player.player_money}')
                        myblackjack.end_game=True
                        Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
                        Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
                        Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
                
                else:#IN CASE OF A TIE
                    print('there has been a tie Mr jack will receive his bet back')
                    print(f'Mr jack your back to {Player.player_money}')
                    myblackjack.end_game=True
                    Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
                    Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
                    Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
            
            
            
            else:#GAME IS DONE
                pass
                    
                
            if myblackjack.end_game==False:#GAME DIDNT END YET
                myblackjack.dealers_move()#DEALERS TIME TO REVEAL HIS 2ND CARD AND TRYING TO BEAT THE PLAYER
            else:
                print('bye bye')
            
myblackjack=Blackjack(dealers_sum=0)#INITIALIZING THE BLACKJACK CLASS

class Player(Blackjack):
    global deck
    deck=myblackjack.return_deck()
    
    
    def __init__ (self,player_money,card_sum=0,player_cards=[],player_bet=0):
        Player.player_money=player_money
        Player.card_sum=card_sum
        Player.player_cards=player_cards
        Player.player_bet=player_bet
    


        
    def firstcards(self):
        i=0
        while i<2:#GETTING THE 2 FIRST CARDS FROM THE DEALER!
            '''    
            Player.player_cards.append(random.choice(deck))#INSERTING A RANDOM CARD FROM THE DECK
            if Player.player_cards[-1]=='face card':#IF ITS A FACE CARD THE PLAYER GETS 10
                Player.card_sum+=10
            if Player.player_cards[-1]=='ace':#NEEDS TWIKING FOR THE LOGIC 
                                                 #RATHER TO TAKE 1 OR 11 WITH THE ACE!!!
                Player.card_sum+=1
            else:#OR ELSE THE PLAYER GETS THE SUM OF THE CARD
                Player.card_sum+=Player.player_cards[-1]
                    
            i+=1
            '''
            Player.player_cards.append(random.choice(deck))#INSERTING A RANDOM CARD FROM THE DECK
            if Player.player_cards[-1]=='face card'or Player.player_cards[-1]=='ace':#IF ITS A FACE CARD THE PLAYER GETS 10

                if Player.player_cards[-1]=='ace':#GO TO INPUT CONSOLE TO ASK THE PLAYER DOES HE WANT 1 OR 11
                    ace_dilema=input(f'Mr jack your sum is {Player.card_sum} do you want your ace to be one or eleven?  ')          
                    if ace_dilema.lower()=='one':
                        Player.card_sum=Player.card_sum+1
                    else:
                        Player.card_sum+=11
                        
                        
                else:#FACE CARD
                    try:
                        #print('LETS TRY ADDING FACE TO PLAYER')
                        Player.card_sum+=10
                    except:
                        Player.player_cards[-1]=type(int)
                        print(f'in EXCEPTION type is {(type(Player.player_cards[-1]))}')
                    
                        
                        
            else:#NOT FACE CARD OR ACE
                #print('LETS TRY ADDING REGULAR TO PLAYER')
                Player.card_sum+=Player.player_cards[-1]
                
                    
             
            myblackjack.win_loss()
            
            if myblackjack.end_game==True:
                break
            i+=1
        if myblackjack.end_game==False:
            print(f'players sum is currently {Player.card_sum}')
            print(f'players cards are currently {Player.player_cards}')       
            jack_player.hit_stand()
            
        else:
            pass

            
            
                
        #print(f'players sum is currently {Player.card_sum}')
        #print(f'players cards are currently {Player.player_cards}')
        
    def hit_stand(self):
        #deck=cards.return_deck()
        player_answer=input('Mr. jack you wanna hit or stand?  ')
        
        while player_answer.lower()=='hit' :
            
            Player.player_cards.append(random.choice(deck))#INSERTING A RANDOM CARD FROM THE DECK
            if Player.player_cards[-1]=='face card'or Player.player_cards[-1]=='ace':#IF ITS A FACE CARD THE PLAYER GETS 10
        
                if Player.player_cards[-1]=='ace':#GO TO INPUT CONSOLE TO ASK THE PLAYER DOES HE WANT 1 OR 11
                    ace_dilema=input(f'Mr jack your sum is {Player.card_sum} do you want your ace to be one or eleven?  ')          
                    if ace_dilema.lower()=='one':
                        Player.card_sum=Player.card_sum+1
                    else:
                        Player.card_sum+=11
                                
                                
                else:#FACE CARD
                    try:
                        #print('LETS TRY ADDING FACE TO PLAYER')
                        Player.card_sum+=10
                    except:
                        Player.player_cards[-1]=type(int)
                        print(f'in EXCEPTION type is {(type(Player.player_cards[-1]))}')
                            
                                
                                
            else:#NOT FACE CARD OR ACE
                #print('LETS TRY ADDING REGULAR TO PLAYER')
                Player.card_sum+=Player.player_cards[-1]
            
            myblackjack.win_loss()
            
            if myblackjack.end_game==True:
                break
            
            print(f'now players sum is currently {Player.card_sum}') 
            player_answer=input('Mr. jack you wanna hit or stand?  ')
            
        if myblackjack.end_game==True:#GAME DIDNT END YET
            print('bye bye')
        else:
            myblackjack.dealers_move()#DEALERS TIME TO REVEAL HIS 2ND CARD AND TRYING TO BEAT THE PLAYER

            
        
        
    def firstbet(self):
        Player.player_bet=int(input('Mr jack how much you want to bet?  '))
        if Player.player_bet>Blackjack.maximum_bet or Player.player_bet<Blackjack.minimum_bet:
            while True:
                print('Mr jack please bet again in the aggreed upon bets for the game') 
                Player.player_bet=int(input('place yor bet again  '))
                if Player.player_bet<=Blackjack.maximum_bet and Player.player_bet>=Blackjack.minimum_bet: 
                    print(f'Mr jacks bet is {Player.player_bet}') 
                    return Player.player_bet 
                    break
                else:
                    pass#CONTINUE THE WHILE LOOP
        else:
            print(f'Mr jacks bet is {Player.player_bet}') 
        return Player.player_bet   
            
                
            
        
   
jack_player=Player(1000,0)   
while True:
      
    myblackjack.lets_start()
    myblackjack.dealer_cards()
    jack_player.firstcards()  
    #jack_player.hit_stand()
    myblackjack.end_game=False
    playagain=input('Mr jack you wanna play again?  ')
    if playagain.lower()=='yes':#CHECKING IF THE PLAYER WANTS TO PLAY AGAIN!
        pass
    else:
        break
    jack_player=Player(Player.player_money,0,[])
    myblackjack=Blackjack(dealers_sum=0)#MAKING SURE THE DEALER SUM IS RESETED EVERY NEW ITERATION

    
'''#1ST ONE
        if Blackjack.dealers_sum==21:#CHECKING 21 FOR THE THE DEALER ON THE START
            print(f'dealer has got blackjack! the house won')
            Player.player_money-=Player.player_bet
            print(f'Mr jack you lost and your mnoney is now {Player.player_money}$$$ ')
            myblackjack.end_game=True
            Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
            Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
            Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
        
        if Blackjack.dealers_sum>21:#IF DEALER PASSED 21
            print(f'Mr dealer your sum is {Blackjack.dealers_sum} and your busted!')
            Player.player_money+=Player.player_bet
            print(f'Mr jack has won and his money is now {Player.player_money}')
            myblackjack.end_game=True
            Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
            Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
            Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
            
        '''       

'''#2ND ONE
                if Blackjack.dealers_sum>21:#IF DEALER PASSED 21
                    print(f'Mr dealer your sum is {Blackjack.dealers_sum} and your busted!')
                    Player.player_money+=Player.player_bet
                    print(f'Mr jack has won and his money is now {Player.player_money}')
                    myblackjack.end_game=True
                    Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
                    Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
                    Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
                    break
                
                if Blackjack.dealers_sum==21:#IF DEALER GOT 21 
                    print(f'dealer has got blackjack! the house won')
                    Player.player_money-=Player.player_bet
                    print(f'Mr jack you lost and your mnoney is now {Player.player_money}$$$ ')
                    myblackjack.end_game=True
                    Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
                    Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
                    Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
                    break
                
                '''
'''#3RD ONE
            if Player.card_sum>21:#IF PLAYER PASSED 21
                print(f'Mr jack your sum is {Player.card_sum} and your busted!')
                print(f'your loss is {Player.player_bet}$$$ ')
                Player.player_money-=Player.player_bet
                print(f'players money is now {Player.player_money}!')
                Blackjack.end_game=True
                Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
                Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
                Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
                break

            
            if Player.card_sum==21:#IF PLAYER GOT 21 
                print(f'Mr jack has got blackjack! collect your winnings')
                print(f'your win is {Player.player_bet}$$$ ')
                Player.player_money+=Player.player_bet
                print(f'players money is now {Player.player_money}!')
                myblackjack.end_game=True
                Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
                Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
                Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
                break
            '''
'''#4TH ONE
            
            if Player.card_sum>21:#IF PLAYER PASSED 21
                print(f'Mr jack your sum is {Player.card_sum} and your busted!')
                print(f'your loss is {Player.player_bet}$$$ ')
                Player.player_money-=Player.player_bet
                print(f'players money is now {Player.player_money}!')
                Blackjack.end_game=True
                Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
                Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
                Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
                break

            
            if Player.card_sum==21:#IF PLAYER GOT 21 
                print(f'Mr jack has got blackjack! collect your winnings')
                print(f'your win is {Player.player_bet}$$$ ')
                Player.player_money+=Player.player_bet
                print(f'players money is now {Player.player_money}!')
                myblackjack.end_game=True
                Player.player_cards=Player.player_cards.clear()#CLEARING BOTH HANDS!
                Blackjack.dealers_hand=Blackjack.dealers_hand.clear()
                Blackjack.dealers_hand=[]#TRYING TO FIX THE TYPE ERROR
                break
            '''
#print(cards.return_deck())
#jack_player.hit_stand()

