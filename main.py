import random

print("Welcome to Python Slots")
symbols = ['A', 'B', 'C', 'D', 'E']
turn = 0
balance = 100
random_letters = []

print("Symbols: A, B, C, D, E \n")
print("Current balance: $100")


while True:
    betamount = int(input("Place your bet amount:"))
    turn += 1
    print("Spinning...")
    random_symbols = random.choices(symbols, k=3)
    random_letters.append(random_symbols)
    print(random_symbols)

    if betamount > balance:
        print("Sorry you do not have that much money")
        betamount = int(input("Place your bet amount:"))

    if random_letters[turn-1][0] == random_letters[turn-1][1] == random_letters[turn-1][2]:
        balance = balance - betamount
        balance += 10
        print(f"You won $10. Your current balance is {balance}")
    else:
        balance = balance - betamount
        print(f"You lost. Your current balance is {balance}")


    if balance == 0:
        print("You ran out of money.")
        break

    continue_playing = input("Would you like to continue playing y/n").lower()

    if continue_playing == "n":
        print("Thanks for playing.")
        break
