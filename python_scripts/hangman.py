import random

print("Hello handman")

word = ["hacker","bounty","random"]

randword = random.choice(word)

letter = input("Enter a letter you have guessed: ").lower()

print(letter)

for i in word:
    if i == letter:
        print('right')
    else:
        print("wrong")
