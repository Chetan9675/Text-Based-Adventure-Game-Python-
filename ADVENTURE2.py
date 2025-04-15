import time
import random

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You wake up in a dark forest.", 2)
    print_pause("The trees loom tall, and the air is thick with mist.", 2)
    print_pause("You see two paths ahead:", 2)
    print_pause("1. A narrow, winding trail leading deeper into the woods.", 2)
    print_pause("2. A faintly lit clearing with a small cottage.", 2)

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
    print_pause("\nYou follow the winding trail...", 2)
    print_pause("The trees grow thicker, and the air grows colder.", 2)
    print_pause("Suddenly, a wolf jumps out in front of you!", 2)
    
    while True:
        action = input("What will you do? (1. Fight / 2. Run / 3. Try to tame it): ").strip()
        if action == "1":
            print_pause("\nYou bravely fight the wolf...", 2)
            if random.choice([True, False]):
                print_pause("After a fierce struggle, you defeat it!", 2)
                print_pause("You find a hidden treasure chest behind a tree.", 2)
                print_pause("🏆 **You win!** 🏆", 2)
            else:
                print_pause("The wolf overpowers you...", 2)
                print_pause("💀 **Game Over.** 💀", 2)
            break
        elif action == "2":
            print_pause("\nYou sprint away, but the wolf chases you.", 2)
            print_pause("You trip on a root and fall...", 2)
            print_pause("💀 **Game Over.** 💀", 2)
            break
        elif action == "3":
            print_pause("\nYou slowly extend your hand, speaking softly.", 2)
            if random.choice([True, False]):
                print_pause("The wolf sniffs your hand and calms down.", 2)
                print_pause("It leads you to a hidden glade with a magical spring.", 2)
                print_pause("Drinking from it, you feel invigorated!", 2)
                print_pause("🌿 **You win!** 🌿", 2)
            else:
                print_pause("The wolf growls and attacks!", 2)
                print_pause("💀 **Game Over.** 💀", 2)
            break
        else:
            print_pause("Invalid choice. Try again.")

def path_cottage():
    print_pause("\nYou approach the cottage...", 2)
    print_pause("The door creaks open, revealing an old woman inside.", 2)
    print_pause("She offers you a warm drink.", 2)
    
    while True:
        action = input("Do you accept? (1. Yes / 2. No / 3. Ask for help): ").strip()
        if action == "1":
            print_pause("\nThe drink was enchanted!", 2)
            if random.choice([True, False]):
                print_pause("You fall into a deep sleep...", 2)
                print_pause("When you wake up, you're home safely.", 2)
                print_pause("🏡 **You win!** 🏡", 2)
            else:
                print_pause("You fall into a deep sleep...", 2)
                print_pause("You wake up in a dungeon!", 2)
                print_pause("💀 **Game Over.** 💀", 2)
            break
        elif action == "2":
            print_pause("\nYou refuse and leave.", 2)
            print_pause("As you walk away, the cottage vanishes into thin air.", 2)
            print_pause("You're lost forever in the forest...", 2)
            print_pause("💀 **Game Over.** 💀", 2)
            break
        elif action == "3":
            print_pause("\nYou ask the woman for help.", 2)
            print_pause("She smiles and gives you a magical amulet.", 2)
            print_pause("It glows brightly, guiding you out of the forest.", 2)
            print_pause("🔮 **You win!** 🔮", 2)
            break
        else:
            print_pause("Invalid choice. Try again.")

def secret_path():
    print_pause("\nYou notice a hidden third path covered in vines.", 2)
    print_pause("Curious, you push through and find an ancient ruins.", 2)
    print_pause("Inside, a riddle is inscribed on a stone tablet:", 2)
    print_pause("'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'", 2)
    
    answer = input("Your answer (one word): ").strip().lower()
    if answer == "echo":
        print_pause("\nThe ruins tremble, revealing a chest of gold!", 2)
        print_pause("💰 **You win!** 💰", 2)
    else:
        print_pause("\nThe ground shakes, and the ruins collapse!", 2)
        print_pause("💀 **Game Over.** 💀", 2)

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
    print_pause("🌟 **Welcome to the Text Adventure!** 🌟", 2)
    while True:
        intro()
        if random.random() < 0.2:  # 20% chance to find the secret path
            secret_path()
        else:
            choose_path()
        if not play_again():
            print_pause("\nThanks for playing! Goodbye. 👋", 2)
            break

if __name__ == "__main__":
    main()
