import random

def play():
    options = ["rock", "paper", "scissors"]
    wins = losses = ties = 0

    while True:
        user = input("Choose rock, paper or scissors: ").lower()
        if user not in options:
            print("Invalid choice, please try again.")
            continue

        computer = random.choice(options)
        print(f"You chose {user}. Computer chose {computer}.")

        if user == computer:
            print("It's a tie!")
            ties += 1
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1

        print(f"Score: Wins: {wins}, Losses: {losses}, Ties: {ties}")
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

play()
