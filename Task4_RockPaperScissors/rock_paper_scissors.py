import random

# rock paper scissors game
choices = ['rock', 'paper', 'scissors']

print("Welcome to Rock Paper Scissors!")

# loop
play = True
while play == True:
    
    # get what the user wants to play
    User = input("Choose rock, paper, or scissors (or 'q' to quit): ")
    User = User.lower() # lowercase
    
    if User == 'q':
        print("Thanks for playing!")
        play = False
    
    elif User != "rock" and User != "paper" and User != "scissors":
        print("That is not a valid choice. Try again.")
        
    else:
        # computer choice
        num = random.randint(0,2)
        comp = choices[num]
        print("Computer chose: " + comp)
        
        # tie game
        if User == comp:
            print("It's a tie!")
        
        # if user wins
        if User == "rock" and comp == "scissors":
            print("You win!")
        if User == "paper" and comp == "rock":
            print("You win!")
        if User == "scissors" and comp == "paper":
            print("You win!")
            
        # if computer wins
        if User == "rock" and comp == "paper":
            print("You lose!")
        if User == "paper" and comp == "scissors":
            print("You lose!")
        if User == "scissors" and comp == "rock":
            print("You lose!")
            
    print()
