def quit_game():
    print("thank you for playing")
    
def input_values():
    number=int(input("guess a number between 1 and 100: "))
    winning_number=int(input("let other player type the winning number:"))
    guess=1
    game_over=False

def play():
    while game_over==False:
        if number==winning_number:
            print(f"you win, and you guessed this number in {guess}th time")
            game_over=True
        else:
            if number<winning_number:
                print("guessed number is too low")
                play_quit=input("Type 'guess' to guess again or Type 'play' to play a new game or Type 'quit' to quit the game:")
                if play_quit=='guess':
                    number=int(input("enter number to guess again:"))
                    game_over==False
                elif play_quit=='play':
                    input_values()
                    play()
                elif play_quit=='quit':
                    quit_game()
            else:
                print("guessed number is too high")
                play_quit=input("Type 'guess' to guess again or Type 'play' to play a new game or Type 'quit' to quit the game:")
                if play_quit=='guess':
                    number=int(input("enter number to guess again:"))
                    game_over==False
                elif play_quit=='play':
                    input_values()
                    play()
                elif play_quit=='quit':
                    quit_game()
    guess +=1

game=input("type 'start' to start the game:")
if game=='start':
    input_values()
    play()
elif game=='':
    print("you have entered wrong input value")
    game=input("please type 'start' to start the game:")
    if game=='start':
        input_values()
        play()
    else:
        print("sorry you have input wrong field again , please come back again after some time")
        

        
if game_over==True:
    play_quit=input("type 'play' to play a new game else type 'quit':")
    if play_quit=='play':
        input_values()
        play()
    elif play_quit=='quit':
        quit_game()
                
    
