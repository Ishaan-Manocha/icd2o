import random
 
def choose_superhero():
    name = input("What is your name?: ")
    print("Choose your Marvel superhero:")
    heroes = {"1": "Iron Man",
              "2": "Spider-Man",
              "3": "Captain America"}
    print(heroes)
    choice = None
    while choice not in heroes:
        choice = input("Enter the number of your chosen superhero: ")
        if choice not in heroes:
            print("Please enter a valid number (1, 2, or 3).")
    return choice, name, heroes[choice]
 
initial_health = random.randint(50, 100)
print(f"Starting health: {initial_health}")
 
choice, name, superhero = choose_superhero()
print(f"Welcome, {name}! You have chosen {superhero}.")
print("The world is in danger, and your mission is to save it!")
 
def make_decision():
    choice = None
    while choice not in ['1', '2']:
        print("A supervillain is causing trouble.")
        print("1. Confront the villain")
        print("2. Seek assistance from another hero")
        choice = input("What do you want to do? Enter 1 or 2: ")
        if choice not in ['1', '2']:
            print("Invalid choice! Try again.")
    return choice
 
def superhero_mission(action, player_superhero):
    if action == "1":
        print(f"You, as {player_superhero}, be brave and confront the supervillain!")
        damage_taken = 0 or 100
    elif action == "2":
        print(f"{player_superhero} seeks help from another superhero")
        damage_taken = (60, 90)
    else:
        print("Invalid choice! Try again.")
        damage_taken = 0
    return damage_taken
 
def award_bonus_points(condition):
    bonus_points = 0
    if condition:
        bonus_points += 10
    return bonus_points
 
decision = make_decision()
damage_taken = superhero_mission(decision, superhero)
 
remaining_health = initial_health - damage_taken
if remaining_health <= 0:
    print("Your superhero's health has dropped below 0. Game over!")
else:
    print(f"Remaining health: {remaining_health}")
    bonus = award_bonus_points(True)
    final_score = remaining_health + bonus
    print(f"Your final score: {final_score}")
    print("YOU WON!")