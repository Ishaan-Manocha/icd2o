
name = input("Enter your name: ")

opponents_name1 = "Brandon"
opponents_name2 = "Abraham"
opponents_name3 = "Alex"
opponents_name4 = "Joshua"
opponents_name5 = "Brandon"

game1 = int(input("Enter your game one points here: "))
game2 = int(input("Enter your game two points here: "))
game3 = int(input("Enter your game three points here: "))
game4 = int(input("Enter your game four points here: "))
game5 = int(input("Enter your game five points here: "))

opgame1 = int(input("Enter opponents game one points here: "))
opgame2 = int(input("Enter opponents game two points here: "))
opgame3 = int(input("Enter opponents game three points here: "))
opgame4 = int(input("Enter opponents game four points here: "))
opgame5 = int(input("Enter opponents game five points here: "))

bp = int(game1/36*100)
bp2 = int(game2/36*100)
bp3 = int(game3/36*100)
bp4 = int(game4/36*100)
bp5 = int(game5/36*100) 

print(" ")
print(" ")
print (f"{name}'s results: ")
print(" ")
print(" ")

print("Game #1: ")
print(f"Opponents Name: {opponents_name1}")
print(f"Your points: {game1} ")
print(f"Opponents Points: {opgame1} ")
print(f"Who won game 1: {name}")
print(" ")
print(" ")

print("Game #2: ")
print(f"Opponents Name: {opponents_name2}")
print(f"Your points: {game2} ")
print(f"Opponents Points: {opgame2} ")
print(f"Who won game 2: {name} ")

print(" ")
print(" ")

print("Game #3: ")
print(f"Opponents Name: {opponents_name3}")
print(f"Your points: {game3} ")
print(f"Opponents Points: {opgame3} ")
print(f"Who won game 2: {name} ")

print(" ")
print(" ")

print("Game #4: ")
print(f"Opponents Name: {opponents_name4}")
print(f"Your points: {game4} ")
print(f"Opponents Points: {opgame4} ")
print(f"Who won game 2: {opponents_name4} ")

print(" ")
print(" ")

print("Game #5: ")
print(f"Opponents Name: {opponents_name5}")
print(f"Your points: {game5} ")
print(f"Opponents Points: {opgame5} ")
print(f"Who won game 2: {name} ")

print("Dots and Boxes Table:")
print(" ")
print(f"Player Name: {name}")
 
print("Opponent         Your Points             Opponents Points              Box% ")
print("===============================================================================")
print(f"{opponents_name1} {game1:>15} {opgame1:>26} {bp:>23.2f}")
print(f"{opponents_name2} {game2:>15} {opgame2:>26} {bp2:>23.2f}")
print(f"{opponents_name3} {game3:>18} {opgame3:>26} {bp3:>23.2f}")
print(f"{opponents_name4} {game4:>16} {opgame4:>26} {bp4:>23.2f}")
print(f"{opponents_name5} {game5:>15} {opgame5:>26} {bp5:>23.2f}")
print("===============================================================================")

your_total = game1+game2+game3+game4+game5
opponents_total = opgame1+opgame2+opgame3+opgame4+opgame5
overall = your_total + opponents_total

print(" ")
print("Summary: ")
print(" ")
print(f"Your Total Points: {your_total}")
print(f"Total Opponent Points: {opponents_total}")
print(f"Total Points: {overall}")