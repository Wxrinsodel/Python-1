# Random dice appearance
import random


# Aventurine Prologue (WELCOME)
def greeting() -> None :
    input("'Dare to embrace the thrill of uncertainty and seize the day.'")
    input("Ladies and gentlemen, welcome to the table.\n"
          "I'm Aventurine, your host for this incredible night.\n"
          "As a seasoned strategist and gambler, I'm here"
          " to guide you through the thrill of the unknown.\n")
    
    # Explain rules
    input("Before we start the show, let me break down the rules for you.")
    input("You have 6 precious opportunities with 1200 coins"
          " to roll the dice and test your luck.\n"
           "Here's how it works:")
    input("Roll 1 dice : This will cost you 100 coins."
          " Guess a number between 1 and 6 and"
          "have a chance to win '300' coins!")
    input("Roll 2 die : For 200 coins, you can roll 2 die. "
          " Guess the number between 1 and 12"
          " And have a chance to win '500' coins!\n"
          "The higher the stakes, the greater the reward.")
    input("Roll 3 die : For the truly daring, 250 coins."
          " Guess a number between 1 and 18.\n"
          "And have a chance to win '1000' coins!"
          " This is where the real fortunes are made.")


    input("So, you think it's simple, do you?\n"
          "Well, let's see if your luck matches your confidence.\n"
          "Remember, the game is always a gamble.\n")

    print("Are you ready to roll the dice and dare to win?")

        # Asking the agreement
    while True:
        user_input = input("(Yes/No): ")

        if user_input.lower() == "yes": 
            """ all input will result in lowercase letters """
            print("Your fate is now in your hands.\n"
                  "May the odds be ever in your favor... or against you.\n")
            input("Go ahead, use me as you wish, even stab me in"
                  " the back if you see fit.")
            input("Exploitation and treachery are simply tools of the trade.\n"
                  "But remember, I don't make deals that don't pay off..."
                  " So, I hope you don't disappoint me.")
            break

        elif user_input.lower() == "no":
            print("It's never too late to fold.\n"
                  "But remember, the greatest fortunes are often won"
                  " by daring to double down.")
            input("One more chance. The dice hold the key to your future."
                  " Are you ready to roll and see what unfolds?")
        else:
            print("Your silence speaks volumes. Perhaps you're not as daring"
                  " as I thought..\n"
                  "One more chance. The dice hold the key to your future."
                  " Are you ready to roll and see what unfolds?")


# Dice art for each face of a dice
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}


def roll_dice(num_of_dice: int) -> list[int]:
    """ the function returns a list of integers. 
        """
    
    return [random.randint(1, 6) for _ in range(num_of_dice)]


# Print horizontal dice
def display_dice(dice: int):
    for line in range(5):  
        """ 5 lines per dice face """
        for roll in dice:
            print(dice_art.get(roll)[line], end=" ") 
        print()


# Calculate total dice result
def calculate_total(dice: int):
    return sum(dice)


# Game loop
def play_game():
    starting_budget = 1200
    budget = starting_budget
    win_count = 0

    """ Using dictionaries for costs, guess ranges, and rewards
        """
    
    dice_mapping = {1: (100, 6), 2: (200, 12), 3: (250, 18)}
    reward_mapping = {1: 300, 2: 500, 3: 1000}

    for chance in range(1, 7):
        print(f"\n--- Round {chance} ---")
        print(f"Current budget: {budget} coins")

        try:
            num_of_dice = int(input("How many dice do you want to roll?"
                                    " (1/2/3): "))
            if num_of_dice not in dice_mapping:
                print("I said, choose between 1, 2, or 3 dice."
                      " Don't make me repeat myself.")
                continue
        except ValueError: # if the input can't be converted to an integer, this will solve it
            print("I said, choose between 1, 2, or 3 dice."
                  " Don't make me repeat myself.")
            continue

        cost, guess_range = dice_mapping[num_of_dice] 
            """ instead of using if/else, I use dictionary.
               """
        if budget < cost:
            print("It seems your luck is as limited as your funds. \n"
                  "Perhaps it's time for you to find a sugar daddy or "
                  " sugar mommy to fund your gambling habit."
                  " Just remember, there's no such thing as a free lunch.")
            break

        try:
            guess = int(input(f"Guess a number between 1 and {guess_range}: "))
            if guess < 1 or guess > guess_range:
                print(f"I said, choose between 1 and {guess_range}."
                       " Don't make me repeat myself.")
                print("You lose this round due to an invalid guess. Adiot...")
                continue
        except ValueError:
            print(f"I said, chooose a number between 1 and {guess_range}."
                   " Perhaps you should consider your words")
            continue

        budget -= cost
        dice = roll_dice(num_of_dice)

        print("Rolling the dice...")
        display_dice(dice)
        total = calculate_total(dice)
        print(f"The total of the dice is: {total}")

        # Check if the guess matches the dice total
        if guess == total:
            reward = reward_mapping.get(num_of_dice, 0)
            print(f"Congratulations! You've managed to outwit the odds.\n")
            print(f"Now you own {reward} coins. But remember,"
                   " fortune favors the bold.\n"
                   " Will you dare to risk it all and play again?!")
            budget += reward
            win_count += 1
        else:
            print(f"Well, well. It's {total}. It seems fortune wasn't"
                   " on your side this time.\n"
                   "But remember, the thrill of the game lies"
                   " in the uncertainty. Perhaps next time the dice"
                   " will roll in your favor.")

    print(f"\nThe curtain falls on another thrilling game of chance.\n")
    
    if budget < starting_budget:
        print(f"Your final budget: {budget} coins")
        input("Never mind. Thank you for playing. Your presence has been"
              " a... tolerable experience.\n"
              "Until next time, may your luck be as limited as"
              " your intelligence.")
    else:
        print(f"Your final budget: {budget} coins")
        input("Another victory? Impressive. Your luck is truly astounding.\n"
              "Perhaps you've stumbled upon a hidden talent for this.\n"
              "Congratulations!")

greeting()
play_game()
