#The player should roll dice
#Number of rolls till they get 1 is counted
#If they stopped the game before getting 1 then the number of rolls is added to their score
#if player gets 1 then that game's score is 0

import time
import random
dice_list=[1,2,3,4,5,6]    

#the dice will be 1-6
def dice():
    dice_list=[1,2,3,4,5,6]    
    #for i in range(len(dice_list)):
    j=random.randint(0,len(dice_list)-1) #j chooses a random value from 1-6
    #    dice_list[i],dice_list[j]=dice_list[j],dice_list[i]
    return dice_list[j]

def players():
    num_players=int(input('Enter the number of players:'))
    player_list=[]
    for i in range(num_players):
        name_players=input('Enter the names of the players:')
        player_list.append(name_players)
    #to convert players list to dictationary
    player_dict={}
    for i in range(0,len(player_list)):
        player_dict[player_list[i]]=0
    return player_dict,player_list

#game
def game():
    for i in range(len(player_list)):
        print('Player',player_list[i],'will start the game')
        time.sleep(3)
        while True:
            
            a=dice()

            player_dict[list(player_dict.keys())[i]]+=a 

            print(a)
            query=input('Do you want to continue?(Press q to quit or Enter to continue)')
            if query=="q":
                print(player_dict)
                break
            time.sleep(1)
            if a==1:
                print('Player',player_list[i],'has lost')
                player_dict[list(player_dict.keys())[i]]=0
                print(player_dict)
                time.sleep(3)
                break  


player_dict,player_list=players()
def main():
    
    
    print('The current standings',player_dict)
    game()
    # roll=dice(dice_list)
    # print('The roll',roll)
main()


