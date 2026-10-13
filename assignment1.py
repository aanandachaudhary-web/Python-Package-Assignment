import pyjokes
import random

jokes = random.sample(pyjokes.get_jokes(), 3)

for joke in jokes:
    print("\nProgramming joke:", joke)

while True:
    answer = input("\nDo you want another joke? (yes/no): ").strip().lower()

    if answer == "yes":
        print("\nHere is another joke:")
        print(random.choice(pyjokes.get_jokes()))
    else:
        print("Thanks for using the joke generator!")
        break