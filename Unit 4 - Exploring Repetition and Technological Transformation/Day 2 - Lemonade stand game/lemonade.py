import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def calculate_customers(weather):
    if weather == "sunny":
        return random.randint(30, 50)
    elif weather == "cloudy":
        return random.randint(10, 30)
    elif weather == "rainy":
        return random.randint(5, 15)
    else:
        return random.randint(20, 40)

def main():
    money = 20
    day = 1
    while True:
        cls()
        print(f"Day {day}")
        weather = random.choice(["sunny", "cloudy", "rainy"])
        print(f"Weather: {weather}")
        customers = calculate_customers(weather)
   

        price = float(input("Set the price per glass: $"))
        sold = int(input("How many glasses of lemonade will you sell today? "))

        if price > 50:
            print("stop scamming you lost")
        
        if sold > customers:
            print("You can't sell more glasses than potential customers!")
            sold = customers

        revenue = sold * price
        money += revenue
        print(f"Revenue for the day: ${revenue:.2f}")
        print(f"Total money earned so far: ${money:.2f}\n")

        response = input("Do you want to continue to the next day? (yes/no): ")
        if response.lower() != "yes":
            break

        day += 1

    print(f"Total money earned over {day} days: ${money:.2f}")

if __name__ == "__main__":
    main()
