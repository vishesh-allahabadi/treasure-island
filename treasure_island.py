print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

while True:
    # Your code goes here
    # ...
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    # https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

    # Write your code below this line 👇

    print('This is your first crossroad')
    step_1 = input(
        "Do you want to go left or right? \nType 'L' for Left and 'R' for Right \n")

    if step_1 == 'l' or step_1 == 'L':
        print('You have arrived on the next hurdle. Do you want to Swim or Wait?')
        step_2 = input(
            "Do you want to go swim or wait? \nType 'S' for Swim and 'W' for Wait \n")
        if step_2 == 'w' or step_2 == 'W':
            print('You managed to go to next step. Now you have 3 doors in front of you. One of these doors has a treasure.')
            door = input(
                "Which Door do you want to go in- Red, Blue or Yellow? Type 'R' for Red, 'B' for Blue and 'Y' for Yellow \n")
            if door == 'b' or door == 'B':
                print('You are eaten by beasts. You Die. GAME OVER!')
            elif door == 'r' or door == 'R':
                print('there\'s a Dragon. You are burned by fire. You Die. GAME OVER!')
            elif door == 'y' or door == 'Y':
                print('Rejoice! You found the Treasure. You WIN!!!')
            else:
                print("GAME OVER")
        else:
            print('You were attacked by a Trout. You Die. GAME OVER!')
    else:
        print('You fell into a hole. You Die. GAME OVER!')

    # Ask the user if they want to restart
    restart = input("Would you like to restart? (y/n) ")

    # Check if the user wants to restart
    if restart.lower() != "y":
        break  # Exit the loop if the user doesn't want to restart
