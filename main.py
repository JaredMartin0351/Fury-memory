des_Loc = ['Park','Zoo','Beach','Nature Trail']
nom_Item = ['Pizza Place','Burger Joint','Taco Truck','Sushi Bar']
zoom_How_To = ['Bus','Uber','Bike','Walk']
fun_Times = ['Hike','Swim','Playing Pool','Karaoke']

import random

# Function selects randomly from the lists.
def random_Ch(CH1):  
    random.choice(CH1)
    ran1 = random.choice(CH1)
    result = ran1
    return result

# Function will promt user for an answer and return the answer.
def user_Input():
    in1 = (input('Do you like the choices I picked for you?\nPlease answer Yes or No: '))
    result = in1
    return in1

# Determines if the user input returned answer is true or false for the while loop below.
def booL_dec():
    if user_Input() == ('no'):
        ans1 = False
        result = ans1
        return ans1
    else:
        ans1 = True
        result = ans1
    return ans1


# This function will run the random choice for each list.
def ran_Op(po1,po2,po3,po4):
    random_Ch(op1)
    random_Ch(op2)
    random_Ch(op3)
    random_Ch(op4)
    return po1

# Will assign the randomly selected item from the lists to this variable for use.
op1 = random_Ch(des_Loc)
op2 = random_Ch(nom_Item)
op3 = random_Ch(zoom_How_To)
op4 = random_Ch(fun_Times)

print (f' {op1}\n {op2}\n {op3}\n {op4}\n')
boo1 = booL_dec()

while boo1 == False:
    ran_Op(op1,op2,op3,op4)
    print (f' {random_Ch(des_Loc)}\n {random_Ch(nom_Item)}\n {random_Ch(zoom_How_To)}\n {random_Ch(fun_Times)}\n')
    boo1 = booL_dec()
else:
    print(f' {op1}\n {op2}\n {op3}\n {op4}\n')
    print('Please enjoy the trip I have planned for you!')

