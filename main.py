#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art
import random

HARD_LIVES = 10
EASY_LIVES = 5

def difficulty(level):
  if level == "easy":
    lives = HARD_LIVES
    print(f"You have {HARD_LIVES} attempts remaining to guess the number.")
  elif level == "hard":
    lives = EASY_LIVES
    print(f"You have {EASY_LIVES} attempts remaining to guess the number.")
  return lives  

def compare(g_num, m_num, lives):
  if g_num > m_num:
    lives -= 1
    print(f"Too high! You have {lives} lives remaining")
    return lives
  elif g_num < m_num:
    lives -= 1
    print(f"Too low! You have {lives} lives remaining")
    return lives
  else:
    print(f"You guessed it. The answer was {m_num}.")
    return lives  


mystery_number = random.randint(1,100)
lives = 0

print(art.logo)
print("I'm thinking of a number between 1 and 100.")
print(f"The number is {mystery_number}")

level = input("Choose a level, easy or hard: ")
lives = difficulty(level)

guess = 0
while guess != mystery_number:
  guess = int(input("Make a guess: "))
  lives = compare(guess, mystery_number, lives)
  if lives == 0:
    print("Game Over!")
    guess = mystery_number
  elif guess != mystery_number:  
    print("Guess again.")

if guess == mystery_number and lives > 0:
  print("You win!")       