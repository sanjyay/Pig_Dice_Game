#The player should roll dice
#Number of rolls till they get 1 is counted
#If they stopped the game before getting 1 then the number of rolls is added to their score
#if player gets 1 then that game's score is 0

import random
#the dice will be 1-6
dice_list=[1,2,3,4,5,6]
def dice(dice_list):
    
    for i in range(len(dice_list)):
        j=random.randint(0,len(dice_list)-1) #j chooses a random value from 1-6
        dice_list[i],dice_list[j]=dice_list[j],dice_list[i]
    
    return dice_list[j]

def players():
    num_players=int(input('Enter the number of players:'))
    player_list=[]
    for i in range(num_players):
        name_players=input('Enter the names of the players:')
        player_list.append(name_players)
    return player_list

#to convert players list to dictationary
def convert(list):
    player_dict={}
    for i in range(0,len(list)):
        player_dict[list[i]]=0
    return player_dict

def main():
    pl_list=players()
    pl_dict=convert(pl_list)
    print('The current standings',pl_dict)
    # roll=dice(dice_list)
    # print('The roll',roll)
main()
