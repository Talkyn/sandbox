#######################################################
#                                                     #
#     A simple number guessing game, written with     #
#     an emphasis on breaking bits into functions     #
#                                                     #
#######################################################

from random import randint

hl = "*" * 38
error_msg = "Sorry, please use a proper command."

def padding():
    print ("\r\n")
def hl():
    print ("*" * 38)

def welcome_msg():
    padding()
    hl()
    #padding()
    print (" Welcome to The Number-Guessing Game! ")
    #padding()
    hl()
    
def win_game():
    padding()
    hl()
    print ("         CONGRATULATIONS!!")
    hl()
    main_menu()

def lose_game():
    padding()
    hl()
    print ("               YOU SUCK!!")
    hl()
    main_menu()
    
def play_game():
    padding()
    print ("Great!  Here we go!")
    print ("Pick a number between 1 and 10.")
    guess = input("Your Guess: ")
    number = randint(1, 10)
    if guess == number:
        win_game()
    else:
        lose_game()

def eval_cmd(command):

    if command == "Y" or \
         command == "y" or \
         command == "yes":
        return True
    elif command == "N" or \
          command == "n" or \
          command == "no" :
        return False
    else:
        return error_msg
    
    
def main_menu():
    padding()
    print (" Would you like to play?")
    cmd = raw_input(" (Y/N) ")
    choice = eval_cmd(cmd)
    making_choice = True
    if choice == True:
        play_game()
    elif choice == False:
        quit()
    else: 
        print error_msg
        main_menu()
    

if __name__ == "__main__":
    try:
        welcome_msg()
        main_menu()
    except SystemExit, e:
        print(e)