import random

def generate_random_number(min: int, max: int) -> int:
    """ Generate random number in specified range """
    return random.randrange(min, max + 1, 1)

def get_response(game_number: int, player_number: int) -> str:
    """ Get feedback on player's guess """
    if (player_number > game_number):
        return "The number is LOWER than your written."
    elif (player_number < game_number):
        return "The number is HIGHER than you think."
    else:
        return ">>> Congratulation! You guessed the number."

def play_game() -> None:
    """"Play guessing game"""
    secret_number = generate_random_number(0,100)
    attemps_count = int(0)

    print("******************************")
    print("Welcome to the GUESS GAME.")
    print("Try to find out number between 0 and 100.")
    print("******************************")
    
    while True:
        # Entered value handling
        while True:
            player_input = input("Write number: ")
            try:
                player_number = int(player_input)
                break
            except ValueError:
                print("[!] Invalid input. Write number between 0 and 100")    

        response = get_response(secret_number, player_number)

        # Break the cycle
        if player_number == secret_number:
            break

        print(response)
        attemps_count += 1
    # End of cycle    
    # Winning message
    print(response, "Number of attemps:", attemps_count)    

if __name__ == "__main__":
    play_game()