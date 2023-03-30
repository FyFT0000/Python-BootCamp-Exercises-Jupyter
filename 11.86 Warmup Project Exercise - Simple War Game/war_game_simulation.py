
""" Simple War Game, card game. """

import os
import random
import time
import statistics

class Game():
    """ Game() calls that is used to ineritance to the classes Players and Cards """
    def __init__(self, player,turn):
        self.player = player
        self.turn = turn


class Card(Game):
    """ Card(Game) """
    def __init__(self, player, turn,rank,suits,color):
        self.player = player
        self.turn = turn
        self.rank = rank
        self.suits = suits
        self.color = color

    def __str__(self):
        print_card = self.rank
        if self.rank == 11: print_card = 'J'
        elif self.rank == 12: print_card = 'Q'
        elif self.rank == 13: print_card = 'K'
        elif self.rank == 14: print_card = 'A'
        return f'{self.player},{print_card}.{self.suits}'


class Player(Game):
    """ Player(Game) """
    def __init__(self, player, turn, packet):
        self.player = player
        self.turn = turn
        self.packet = packet

    def __str__(self):
        print_player = f'{self.player}:\n'
        for n in self.packet:
            print_player += f'{n} _ '
        print_player += f'\n{len(self.packet)}'
        return print_player


def cls():
    """ cls() """
    os.system('cls' if os.name=='nt' else 'clear')


def create_players():
    """ create_players() """
    select = "NO"
    while True:
        player1_name = input("Please enter de Player 1 name: ")
        player2_name = input("Please enter de Player 2 name: ")
        select = input(f"is the name {player1_name} and {player2_name}correct for Player 1 and Player 2?. YES / NO : ").upper()
        cls()
        if select.startswith("Y"):
            break
        else:
            print("Enter de desired name for the Player. Or YES if it is correct")
    return player1_name, player2_name


def random_cards():
    """ random_cards() """
    rank = (14,13,12,11,10,9,8,7,6,5,4,3,2)
    suits = ('Heart','Diamond','Clover','Pikes')
    color = ('Red','Black')
    packet = []

    for r in rank:
        for s in suits:
            if s in ('Heart','Diamond'):
                packet.append([r,s,'Red'])
            else:
                packet.append([r,s,'Black'])
    random.shuffle(packet)
    random.shuffle(packet)
    random.shuffle(packet)
    return packet


def deal_cards(packet,player1Name,player2Name):
    """ deal_cards(packet,player1Name,player2Name) """
    count = 0
    player1 = []
    player2 = []
    for p in packet:
        count += 1
        if count < (len(packet)+1)/2:
            player1.append(Card(player1Name,'Pile',p[0],p[1],p[2]))
        else:
            player2.append(Card(player2Name,'Pile',p[0],p[1],p[2]))
    p1 = Player(player1Name,'Pile',player1)
    p2 = Player(player2Name,'Pile',player2)
    return p1,p2


def game_win(p1,p2,i):
    """ game_win(p1,p2,i) """
    if len(p1.packet) > i and len(p2.packet) > i:
        return True
    else:
        #if len(p1.packet) > len(p2.packet):
            #print(f'Player {p1.player} Wins!!')
        #else:
            #print(f'Player {p2.player} Wins!!')
        return False


def game_battle(p1,p2,i):
    """ game_battle(p1,p2,i) """
    #time.sleep(0.01)
    #print(f'{len(p1.packet):2} . {p1.packet[i].rank:2}  -  {p2.packet[i].rank:2} . {len(p2.packet):2}     {i:2}',flush=True)
    if p1.packet[i].rank > p2.packet[i].rank:
        n = 0
        while n <= i:
            p1.packet.append(p2.packet[0])
            p1.packet.append(p1.packet[0])
            p1.packet.pop(0)
            p2.packet.pop(0)
            n += 1
        return 'Battle'
    elif p1.packet[i].rank < p2.packet[i].rank:
        n = 0
        while n <= i:
            p2.packet.append(p1.packet[0])
            p2.packet.append(p2.packet[0])
            p2.packet.pop(0)
            p1.packet.pop(0)
            n += 1
        return 'Battle'
    else:
        return 'War'


def game_play():
    """ game_play() """
    turn = "Pile"
    simulation = 0
    sim_index = 0
    war_0 = [0]
    war_1 = [0]
    war_2 = [0]
    war_3 = [0]
    war_4 = [0]
    war_5 = [0]
    war_6 = [0]
    war_7 = [0]
    war_8 = [0]
    war_9 = [0]
    war_10 = [0]

    war_max_0 = [0]
    war_max_1 = [0]
    war_max_2 = [0]
    war_max_3 = [0]
    war_max_4 = [0]
    war_max_5 = [0]
    war_max_6 = [0]
    war_max_7 = [0]
    war_max_8 = [0]
    war_max_9 = [0]
    war_max_10 = [0]

    #player1_name, player2_name = create_players()
    player1_name, player2_name = ('P1','P2')
    while True:
        try:
            simulation = int(input('Please enter the number of simulation to execute: '))
        except:
            print('Please provide a valid number')
        else:
            break
    st = time.time()

    while sim_index < simulation:

        p1,p2 = deal_cards(random_cards(),player1_name,player2_name)
        #print(p1)
        #print(p2)
        #cls()
        i = 0
        indice_battle = 0
        indice_war = 0
        indice_max_war = 0
        

        while game_win(p1,p2,i):
            turn = game_battle(p1,p2,i)
            if turn == "Battle":
                i = 0
                indice_battle += 1
            elif turn == 'War':
                i += 2
                indice_war += 1
                if i > indice_max_war:
                    indice_max_war = i
                #print('------- War -------',flush=True)
        
        #print(f'Turns: {(indice_war + indice_battle):4}, Battles: {indice_battle:4}, War: {indice_war:3}, Long War: {int(indice_max_war/2):2}')

        if indice_war == 0:
            war_0.append((indice_war + indice_battle))
        if indice_war == 1:
            war_1.append((indice_war + indice_battle))
        if indice_war == 2:
            war_2.append((indice_war + indice_battle))
        if indice_war == 3:
            war_3.append((indice_war + indice_battle))
        if indice_war == 4:
            war_4.append((indice_war + indice_battle))
        if indice_war == 5:
            war_5.append((indice_war + indice_battle))
        if indice_war == 6:
            war_6.append((indice_war + indice_battle))
        if indice_war == 7:
            war_7.append((indice_war + indice_battle))
        if indice_war == 8:
            war_8.append((indice_war + indice_battle))
        if indice_war == 9:
            war_9.append((indice_war + indice_battle))
        if indice_war >= 10:
            war_10.append((indice_war + indice_battle))
        
        if int(indice_max_war/2) == 0:
            war_max_0.append((indice_war + indice_battle))
        if int(indice_max_war/2) == 1:
            war_max_1.append((indice_war + indice_battle))
        if int(indice_max_war/2) == 2:
            war_max_2.append((indice_war + indice_battle))
        if int(indice_max_war/2) == 3:
            war_max_3.append((indice_war + indice_battle))
        if int(indice_max_war/2) == 4:
            war_max_4.append((indice_war + indice_battle))
        if int(indice_max_war/2) == 5:
            war_max_5.append((indice_war + indice_battle))
        if int(indice_max_war/2) == 6:
            war_max_6.append((indice_war + indice_battle))
        if int(indice_max_war/2) == 7:
            war_max_7.append((indice_war + indice_battle))
        if int(indice_max_war/2) == 8:
            war_max_8.append((indice_war + indice_battle))
        if int(indice_max_war/2) == 9:
            war_max_9.append((indice_war + indice_battle))
        if int(indice_max_war/2) >= 10:
            war_max_10.append((indice_war + indice_battle))



        sim_index += 1

    et = time.time()
    print('\n\n\nSimulations: ',sim_index,' Time: ',f'{((et-st)*1000):.4f}',' miliseconds.\n')

    print('\nFor the number of Wars, count how many battled repeats and the Mean, Median and Maximum of the list for each data')
    print(' Number, Count, Mean, Median, Max')

    print(f'   0:  {len(war_0)-1:4} , {int(statistics.mean(war_0)):4} , {int(statistics.median(war_0)):4} , {max(war_0):4}')
    
    print(f'   1:  {len(war_1)-1:4} , {int(statistics.mean(war_1)):4} , {int(statistics.median(war_1)):4} , {max(war_1):4}')

    print(f'   2:  {len(war_2)-1:4} , {int(statistics.mean(war_2)):4} , {int(statistics.median(war_2)):4} , {max(war_2):4}')

    print(f'   3:  {len(war_3)-1:4} , {int(statistics.mean(war_3)):4} , {int(statistics.median(war_3)):4} , {max(war_3):4}')

    print(f'   4:  {len(war_4)-1:4} , {int(statistics.mean(war_4)):4} , {int(statistics.median(war_4)):4} , {max(war_4):4}')

    print(f'   5:  {len(war_5)-1:4} , {int(statistics.mean(war_5)):4} , {int(statistics.median(war_5)):4} , {max(war_5):4}')

    print(f'   6:  {len(war_6)-1:4} , {int(statistics.mean(war_6)):4} , {int(statistics.median(war_6)):4} , {max(war_6):4}')

    print(f'   7:  {len(war_7)-1:4} , {int(statistics.mean(war_7)):4} , {int(statistics.median(war_7)):4} , {max(war_7):4}')

    print(f'   8:  {len(war_8)-1:4} , {int(statistics.mean(war_8)):4} , {int(statistics.median(war_8)):4} , {max(war_8):4}')

    print(f'   9:  {len(war_9)-1:4} , {int(statistics.mean(war_9)):4} , {int(statistics.median(war_9)):4} , {max(war_9):4}')

    print(f'>=10:  {len(war_10)-1:4} , {int(statistics.mean(war_10)):4} , {int(statistics.median(war_10)):4} , {max(war_10):4}')


    print('For the number of Wars Size, count how many battled repeats and the Mean, Median and Maximum of the list for each data')
    print(' Number, Count, Mean, Median, Max')

    print(f'   0:  {len(war_max_0)-1:4} , {int(statistics.mean(war_max_0)):4} , {int(statistics.median(war_max_0)):4} , {max(war_max_0):4}')
    
    print(f'   1:  {len(war_max_1)-1:4} , {int(statistics.mean(war_max_1)):4} , {int(statistics.median(war_max_1)):4} , {max(war_max_1):4}')

    print(f'   2:  {len(war_max_2)-1:4} , {int(statistics.mean(war_max_2)):4} , {int(statistics.median(war_max_2)):4} , {max(war_max_2):4}')

    print(f'   3:  {len(war_max_3)-1:4} , {int(statistics.mean(war_max_3)):4} , {int(statistics.median(war_max_3)):4} , {max(war_max_3):4}')

    print(f'   4:  {len(war_max_4)-1:4} , {int(statistics.mean(war_max_4)):4} , {int(statistics.median(war_max_4)):4} , {max(war_max_4):4}')

    print(f'   5:  {len(war_max_5)-1:4} , {int(statistics.mean(war_max_5)):4} , {int(statistics.median(war_max_5)):4} , {max(war_max_5):4}')

    print(f'   6:  {len(war_max_6)-1:4} , {int(statistics.mean(war_max_6)):4} , {int(statistics.median(war_max_6)):4} , {max(war_max_6):4}')

    print(f'   7:  {len(war_max_7)-1:4} , {int(statistics.mean(war_max_7)):4} , {int(statistics.median(war_max_7)):4} , {max(war_max_7):4}')

    print(f'   8:  {len(war_max_8)-1:4} , {int(statistics.mean(war_max_8)):4} , {int(statistics.median(war_max_8)):4} , {max(war_max_8):4}')

    print(f'   9:  {len(war_max_9)-1:4} , {int(statistics.mean(war_max_9)):4} , {int(statistics.median(war_max_9)):4} , {max(war_max_9):4}')

    print(f'>=10:  {len(war_max_10)-1:4} , {int(statistics.mean(war_max_10)):4} , {int(statistics.median(war_max_10)):4} , {max(war_max_10):4}')
    



game_play()
