import emoji

name = input("Enter your name: ")
activity = input("What is your favourite activity? ")

print(emoji.emojize(f"\nHello {name}! :smile:"))
print(f"You enjoy {activity}!")
print(emoji.emojize("Keep learning Python! :thumbs_up:"))
print(emoji.emojize("Have a wonderful day! :star:"))