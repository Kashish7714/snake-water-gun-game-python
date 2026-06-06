import random

# Game symbols mapped to numbers for easy comparison
# Snake = 1, Water = -1, Gun = 0
CHOICES = {"s": 1, "w": -1, "g": 0}
NAMES = {1: "Snake", -1: "Water", 0: "Gun"}

# Game rules:
# Snake drinks Water   → Snake wins
# Water drowns Gun     → Water wins
# Gun kills Snake      → Gun wins


def get_computer_choice():
    """Returns a random choice for the computer."""
    return random.choice([1, -1, 0])


def get_player_choice():
    """Asks the player for input and returns the corresponding number.
    Keeps asking until a valid input is given."""
    while True:
        user_input = input("Enter your choice (s = Snake, w = Water, g = Gun): ").lower().strip()
        if user_input in CHOICES:
            return CHOICES[user_input]
        print("Invalid input! Please enter 's', 'w', or 'g'.")


def find_winner(player, computer):
    """Compares player and computer choices and returns the result."""
    if player == computer:
        return "draw"

    # All winning conditions for the player
    winning_combinations = [
        (1, -1),   # Snake beats Water
        (-1, 0),   # Water beats Gun
        (0, 1),    # Gun beats Snake
    ]

    if (player, computer) in winning_combinations:
        return "player"
    else:
        return "computer"


def play_game():
    """Main function that runs one round of the game."""
    print("\n--- Snake Water Gun ---")
    print("Rules: Snake beats Water | Water beats Gun | Gun beats Snake\n")

    computer_choice = get_computer_choice()
    player_choice = get_player_choice()

    print(f"\nYou chose:      {NAMES[player_choice]}")
    print(f"Computer chose: {NAMES[computer_choice]}")

    result = find_winner(player_choice, computer_choice)

    if result == "draw":
        print("\nIt's a Draw!")
    elif result == "player":
        print("\nYou Win! 🎉")
    else:
        print("\nComputer Wins! Better luck next time.")


def main():
    """Entry point — lets the player play multiple rounds."""
    print("Welcome to Snake Water Gun!")

    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("\nThanks for playing! Goodbye 👋")
            break


if __name__ == "__main__":
    main()
