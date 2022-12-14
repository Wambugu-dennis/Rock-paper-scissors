import random


def rock_paper_scissors():
    print("Hi, Welcome to the famous rock-paper-scissors game!\n")
    print("Rules of the game are:\n \t#1. rock beats scissors\n \t#2. paper beats rock\n \t#3. Scissor beats paper\n")

    r = "rock"
    p = "paper"
    s = "scissors"
    valid_choices = (r, s, p)

    player_choice = input(f"[+]Please enter your preferred choice({r}, {p}, {s}): ")
    if player_choice not in valid_choices:
        print("[-]Invalid choice! please try again\n")
        return

    comps_choice = random.choice(valid_choices)
    print(f"[+]Your choice is {player_choice}, against {comps_choice}.")

    # compute syntax
    # 1. rock beats scissors
    # 2. paper beats rock
    # 3. Scissor beats paper
    if player_choice == comps_choice:
        print("[+]you Tied\n")
    elif (
            (player_choice == r and comps_choice == s) or
            (player_choice == p and comps_choice == r) or
            (player_choice == s and comps_choice == p)
    ):
        print("[+]You won!\n")
    else:
        print("[-]You lost!\n")


rock_paper_scissors()
