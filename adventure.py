import time

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You wake up in a dark forest.")
    print_pause("The trees loom tall, and the air is thick with mist.")
    print_pause("You see two paths ahead:")
    print_pause("1. A narrow, winding trail leading deeper into the woods.")
    print_pause("2. A faintly lit clearing with a small cottage.")

def choose_path():
    while True:
        choice = input("Which path will you take? (1 or 2): ").strip()
        if choice == "1":
            return path_woods()
        elif choice == "2":
            return path_cottage()
        else:
            print_pause("Invalid choice. Try again.")

def path_woods():
    print_pause("\nYou follow the winding trail...")
    print_pause("The trees grow thicker, and the air grows colder.")
    print_pause("Suddenly, a wolf jumps out in front of you!")
    
    while True:
        action = input("What will you do? (1. Fight / 2. Run): ").strip()
        if action == "1":
            print_pause("\nYou bravely fight the wolf...")
            print_pause("After a fierce struggle, you defeat it!")
            print_pause("You find a hidden treasure chest behind a tree.")
            print_pause("🏆 **You win!** 🏆")
            break
        elif action == "2":
            print_pause("\nYou sprint away, but the wolf chases you.")
            print_pause("You trip on a root and fall...")
            print_pause("💀 **Game Over.** 💀")
            break
        else:
            print_pause("Invalid choice. Try again.")

def path_cottage():
    print_pause("\nYou approach the cottage...")
    print_pause("The door creaks open, revealing an old woman inside.")
    print_pause("She offers you a warm drink.")
    
    while True:
        action = input("Do you accept? (1. Yes / 2. No): ").strip()
        if action == "1":
            print_pause("\nThe drink was enchanted!")
            print_pause("You fall into a deep sleep...")
            print_pause("When you wake up, you're home safely.")
            print_pause("🏡 **You win!** 🏡")
            break
        elif action == "2":
            print_pause("\nYou refuse and leave.")
            print_pause("As you walk away, the cottage vanishes into thin air.")
            print_pause("You're lost forever in the forest...")
            print_pause("💀 **Game Over.** 💀")
            break
        else:
            print_pause("Invalid choice. Try again.")

def play_again():
    while True:
        choice = input("\nPlay again? (y/n): ").lower().strip()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print_pause("Invalid choice. Try again.")

def main():
    print_pause("🌟 **Welcome to the Text Adventure!** 🌟")
    while True:
        intro()
        choose_path()
        if not play_again():
            print_pause("\nThanks for playing! Goodbye. 👋")
            break

if __name__ == "__main__":
    main()
