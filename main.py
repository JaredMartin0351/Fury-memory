des_Loc = ['Park','Zoo','Beach','Nature Trail']
nom_Item = ['Pizza Place','Burger Joint','Taco Truck','Sushi Bar']
zoom_How_To = ['Bus','Uber','Bike','Walk']
fun_Times = ['Hike','Swim','Playing Pool','Karaoke']

import random
user1=True
# Function selects randomly from the lists.
def random_Choise(CH1):  
    random.choice(CH1)
    ran1 = random.choice(CH1)
    return ran1

# Function will promt user for an answer. 
def user_Input(in1):
    in1 = (input('Do you like the choices I picked for you?\nPlease answer Yes or No: '))
    result = in1
    return result

# Will run function and asign outcome to variables.
op1 = random_Choise(des_Loc)
op2 = random_Choise(nom_Item)
op3 = random_Choise(zoom_How_To)
op4 = random_Choise(fun_Times)

print (op1,op2,op3,op4)
user_Input(user1)

def booL_dec():
    if user_Input(user1) == 'No':
        ans1 = False
    else:
        ans1 = True
    result = ans1
    return result



while booL_dec() == False:
    user_Input(user1)
    print (op1,op2,op3,op4)
    #user_Input(user1)
    booL_dec()
else:
    print('Please enjoy the trip')




















    
    
    

