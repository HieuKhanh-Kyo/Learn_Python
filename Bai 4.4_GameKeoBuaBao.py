# quy uoc: 1-Keo  2-Bua  3-Bao

import random

robot= random.randint(1,3)
user = input("Ban chon gi (Keo, Bua, Bao): ")

print("Robot chon so: ", robot)

if user == "Keo":
    user = 1
elif user == "Bua":
    user = 2
else:
    user = 3

if user == 1:
    if robot == 2:
        print("Robot win, User lose")
    elif robot == 3:
        print("Robot lose, User win")
    else:
        print("Draw!")
elif user == 2:
    if robot == 1:
        print("Robot lose, User win")
    elif robot == 3:
        print("Robot win, User lose")
    else:
        print("Draw!")
else:
    if robot == 1:
        print("Robot win, User lose")
    elif robot == 2:
        print("Robot lose, User win")
    else:
        print("Draw!")