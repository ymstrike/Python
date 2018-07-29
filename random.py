import random

print("Do you want to roll? (Y)es or (N)o")
answer = input()
while answer.lower()[0] == "y":
    resultado = random.randint(1, 6)
    print("You roll number: ", resultado)
    print("Roll again? (Y)es or (N)o")
    answer = input()
