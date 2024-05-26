import random
from art import logo

print(logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")

number = random.randint(1, 100)
#print(number)
difficulty = input("Choose a difficulty.Type 'easy' or 'hard' : ")

if difficulty == "hard":
    attempts = 5
elif difficulty == "easy":
    attempts = 10
else:
    print("Wrong entry")

print(f"You have {attempts} attempts remaining to guess the number.")
guess = int(input("Make a Guess: "))

while (attempts != 1):
  attempts -= 1
  if guess == number:
      print(f"You got it.The answer was {number}.")
      break

  elif guess > number:
      print("Too high")
      print("Guess again")

  elif guess < number:
      print("Too low")
      print("Guess again")

  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a Guess: "))
  if attempts == 1  and  guess != number:
      print("You've run out of guesses, you lose.")
