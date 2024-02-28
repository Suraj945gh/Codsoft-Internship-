import random
count = 0
print("            Rock ...... Paper ....... Scissors !!! ")
print("                       Let's Go........                  ")
for i in range(1,3):
    comp_selection = random.randint(0,2)
    print("\n\n\n #Trial ",i)
    print(" The computer has made its decision ....")
    print(" NOW YOU PLAY YOUR TURN.... ")
    user_selection = input(" Select any one \n 0 - Rock , 1 - Paper , 2 - Scissors: ")
    print(" GET READY ---->  Rock ... Paper ... Scissors...")
    if user_selection == 0 or user_selection == 1 or user_selection == 2:
        
        if user_selection == comp_selection:
            print(" It is a tie !!")

        elif comp_selection == 0:
            # Computer has selected Rock
            print("The computer selected Rock\n\n")
            if user_selection == 1:
                print(" Paper beats Rock")
                print(" YOU WON !!") 
                count = count + 1
            else:
                print(" Rock beats Scissors ")
                print(" Computer Wins !!")

        elif comp_selection == 1:
            print(" The computer selected Paper\n\n")
            if user_selection == 0:
                print(" Paper beats Rock")
                print(" Computer Wins !!")
                
            else:
                print(" Scissor cuts Paper ")
                print(" YOU WON !!") 
                count = count + 1

        else:
            print("The computer selected Scissors\n\n")
            if user_selection == 0:
                print(" Rock beats Scissors ")
                print(" YOU WON !!") 
                count = count + 1
            else:
                print(" Scissor cuts Paper ")
                print(" Computer Wins !!")
    else:
        print(" Invalid input entered. Please enter a number from 0/1/2")

print(f"You won {count} out of 3 times against computer")
