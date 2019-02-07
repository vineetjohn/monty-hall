import sys
import random

def play_game():
    # define the initial set of doors
    all_doors = set(range(3))

    # randomly select the winning and losing doors
    win_door = random.randint(0, 2)
    lose_doors = all_doors - {win_door}

    # make a random choice on behalf of the user
    user_choice = random.randint(0, 3)
    not_user_choice = all_doors - {user_choice}

    # allow the host to open a losing door that wasn't chosen
    losing_doors_not_chosen = lose_doors & not_user_choice
    opened_door = random.choice(tuple(losing_doors_not_chosen))

    # allow user to switch their initial choice
    switch_choice = list(all_doors - {opened_door, user_choice})[0]

    # count if switching leads to victory
    return 1 if switch_choice == win_door else 0


num_exp = 1000000
wins = 0
for _ in range(num_exp):
    wins += play_game()
print(wins/num_exp)
