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

result=dice(dice_list)
print(result)