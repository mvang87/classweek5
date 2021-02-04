import random

seven = [7, 7, 7]

credits = 100
bet = 10
spin = input("Do you want to spin the wheel? Yes or No: ")


x = 7
y = 2
z = 7

while spin == "yes":
    slot = [x, y, z]
    break

while spin == str("yes"):
    print(slot)
    if slot != seven:
        spin = input("Do you want to spin again? Yes or No: ")
        continue
    if seven == slot:
        break
if seven == slot:
    print("You hit the jack pot!")
if spin == str("no"):
    print("Have a great day!")
