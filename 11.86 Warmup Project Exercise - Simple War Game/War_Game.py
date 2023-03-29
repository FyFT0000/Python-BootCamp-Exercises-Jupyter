
""" Simple War Game, card game. """
import os
import random

class Game():
    """ Game calls that is used to ineritance to the classes Players and Cards """
    def __init__(self, player,turn):
        self.player = player
        self.turn = turn

        pass

class Card(Game):
    """  """
    def __init__(self, player, turn,rank,suits,color):
        self.player = player
        self.turn = turn
        self.turn = turn
        self.rank = rank
        self.suits = suits
        self.color = color

        pass

class Player(Game):
    """  """
    def __init__(self, player, turn,quantity):
        self.player = player
        self.turn = turn
        self.quantity = quantity

        pass

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def create_players():
    """  """
    select = "NO"
    while True:
        player1_name = input("Please enter de Player 1 name: ")
        player2_name = input("Please enter de Player 2 name: ")
        select = input(f"is the name {player1_name} and {player2_name} correct for Player 1 and Player 2?. YES / NO : ").upper()
        cls()
        if select.startswith("Y"):
            break
        else:
            print("Enter de desired name for the Player. Or YES if it is correct")
            #raise ValueError("Enter de desired name or YES if it is correct")
    return player1_name, player2_name

def deal_cards():



print(create_players())
    


        