##############################################################################
#Computer Project #4
#   print game rules
#   prompt for bank balance
#   prompt for wager
#   roll dice
#   If 7 or 11, player is natural winner
#   If 2, 3, or 12, player loses (craps)
#   If 4,5,6,8,9, or 10 is rolled, point value is determined
#       second throw
#       if second throw matches point value, player wins
#       if second throw is 7, player loses
#       if second throw is neither, roll diced until win or lose
#   Update bank balace
#   Ask to play again
##############################################################################
#from random import randint  # the real Python random

from cse231_random import randint  # the cse231 test random for Mimir testing

def display_game_rules():
    """
    Prints the game rules
    """ 
    print('''A player rolls two dice. Each die has six faces. 
          These faces contain 1, 2, 3, 4, 5, and 6 spots. 
          After the dice have come to rest, 
          the sum of the spots on the two upward faces is calculated. 
          If the sum is 7 or 11 on the first throw, the player wins. 
          If the sum is 2, 3, or 12 on the first throw (called "craps"), 
          the player loses (i.e. the "house" wins). 
          If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
          then the sum becomes the player's "point." 
          To win, you must continue rolling the dice until you "make your point." 
          The player loses by rolling a 7 before making the point.''')

def get_bank_balance(): #function to prompt for initial bank balance
    """
    Prompts the player to give an initial bank balance.
    Returns: bank balance that was enetered (int)
    """
    get_bank_balance = int(input("Enter an initial bank balance (dollars): "))#prompt for bank balance
    balance = get_bank_balance #set balance equal to value entered
    return balance #returns the balance
    
def add_to_bank_balance(balance): #function to add to bank balance
    """
    Asks player how many dollars they want to add to their balance.
    Adds money enetered to already existing balance.
    Returns: new balance amount (int)
    """
    money_added = int(input("Enter how many dollars to add to your balance: ")) #prompts player to add money to balance
    balance  += money_added #add money to balance
    return balance #returns new balance

def get_wager_amount(): #function for receiving wager
    """
    Prompts player to enter wager amount
    wager: wager amount entered (int)
    Returns: wager amount(int)
    """
    get_wager_amount = int(input("Enter a wager (dollars): ")) #prompts player to enter a wager
    wager = get_wager_amount #sets wager to wager amount entered
    return wager #returns wager

def is_valid_wager_amount(wager, balance): #function to check if wager is valid
    """
    Checks to make sure the wager is a valid amount
    Return: True if wager is less than or equal to balance
    Return: False if wager is greater than balance
    """
    if wager <= balance:
        return True #wager is valid
    if wager > balance:
        return False #wager is not valid

def roll_die(): #function to create die value
    """
    Creates a random integer given in cse231_random
    Assigns value to a die
    Returns value from 1 to 6 (int)
    """
    die_value = randint(1,6) #create random integer from cse231_random
    return die_value #returns die value created
    
def calculate_sum_dice(die1_value, die2_value): #function to add two die values
    """
    Adds two die values together
    Returns sum of the two die (int)
    """
    sum_dice = die1_value + die2_value #add two die values together
    return sum_dice #return sum of two die values

def first_roll_result(sum_dice): #function to determine state of game after first roll
    """
    Assigns values for different sums of first roll
    When the sum is 7 or 11, returns 'win'(str) (player wins)
    When the sum is 2, 3 or 12, returns 'loss'(str) (player loses)
    When the sum is 4,5,6,8,9 or 10, returns 'point' (str) (second roll is required)
    """
    if sum_dice == 7 or sum_dice == 11:#7 or 11 rolled
        return "win" #natural win
    elif sum_dice == 2 or sum_dice == 3 or sum_dice ==12: #2,3 or 12 is rolled
        return "loss" #craps
    else: #4,5,6,8,9,or 10 is rolled
        return "point" #point value is created
    
def subsequent_roll_result(sum_dice, point_value): #function to determine state of game after second roll
    """
    Calles when a second roll is requred
    Uses sum of second roll and point value of first roll
    If the sum is equal to the point value, returns 'point'(str)(player wins)
    If the sum is equal to 7, returns 'loss' (str) (player loses)
    IF the sum is not equal to the point value or 7, returns 'neither' (str) (continues to roll)
    """
    if sum_dice == point_value: #second roll and point value match
        return "point" #player wins
    if sum_dice == 7: #7 is rolled
        return "loss" #player loses
    else: #point value or 7 is not rolled
        return "neither" #neither a win or loss

def main(): #function to play the game
    display_game_rules() #call for game rules function
    balance = get_bank_balance() #call for get balance function
    play_str = 'yes' #player initially plays
    
    while play_str == 'yes': #player wants to play
        
        wager = get_wager_amount()#checks for valid wager
        while is_valid_wager_amount(wager, balance) == False: #wager is false
            print("Error: wager > balance. Try again.")#prints error
            wager = get_wager_amount()#rechecks for valid wager
        
        while True:
            bank_balance = balance
            risk_wager = wager
            die_1_value = roll_die() #die 1 is given random int
            die_2_value = roll_die() #die 2 is given random int
            print("Die 1:",die_1_value)
            print("Die 2:", die_2_value)
            sum_dice = calculate_sum_dice(die_1_value, die_2_value) #sum of two dice is calculated
            print("Dice sum:", sum_dice)
            point_value = first_roll_result(sum_dice) #point value is assigned
            if point_value == "win": #natural win
                print("Natural winner.")
                print("You WIN!")
                balance = bank_balance + risk_wager #wager is added to balance
                print("Balance:", balance)
                break
            elif point_value == "loss": #craps (loss)
                print("Craps.")
                print("You lose.")
                balance = bank_balance - risk_wager #wager is subtracted from balance
                print("Balance:", balance)   
                break
            elif point_value == "point": #second roll is required
                point_value = sum_dice
                print("*** Point:", sum_dice) #first roll redult is printed
                
                point_sum_dice = "neither" 
                while point_sum_dice == "neither":
                    new_die_1 = roll_die() #second die 1 is given random int
                    new_die_2 = roll_die() #second die 2 is given random int
                    second_sum_dice = calculate_sum_dice(new_die_1, new_die_2) #new sum
                    print("Die 1:", new_die_1)
                    print("Die 2:", new_die_2)
                    print("Dice sum:", second_sum_dice)
                    point_sum_dice = subsequent_roll_result(second_sum_dice, point_value) #call for second roll function
                    
                    if point_sum_dice == "loss": #secodn roll is 7
                        print("You lose.")
                        balance = bank_balance - risk_wager #wager is subtracted from balance
                        print("Balance:", balance)
                    if point_sum_dice == "point": #point is matched
                        print("You matched your Point.")
                        print("You WIN!") #winner
                        balance = bank_balance + risk_wager #wager is added to balance
                        print("Balance:", balance)
                break #game is complete
                
        play_str = input("Do you want to continue? ") #ask to play again
        if play_str == 'yes': 
            add_to_balance = input("Do you want to add to your balance? ") #ask to add to balance
            if add_to_balance == 'yes':
                    balance = add_to_bank_balance(balance) #add to balance function is called
                    print("Balance:", balance) #new balance is printed
            if add_to_balance == 'no' and balance == 0: #player doesn't want to add money and they have no money in balance
                print("You don't have sufficient balance to continue.")
                play_str = 'no' #game is over
                continue
    print("Game is over.") #game is over
if __name__ == "__main__": #call for main function
    main() #game is played
