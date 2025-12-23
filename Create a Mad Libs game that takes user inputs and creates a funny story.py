# Mad Libs Game 

print("Welcome to the Mad Libs Game!")
print("Please enter the following words:\n")

name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb (ending with -ing): ")
food = input("Enter a food item: ")

# Create the story
story = f"""
One day, {name} went to {place}.
and dog has barking to other prople
There, they saw a very {adjective} {animal}.
The {animal} was {verb} near a {food} stall!
Everyone around started laughing, and {name} will never forget that day.
"""

# Display the story
print("\n Here is your Mad Libs story:")
print(story)
