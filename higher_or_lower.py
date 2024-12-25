import random
import os
import art
from gamedata import data

def get_random(gamedata):
  random_index = random.randint(0, len(gamedata))
  return gamedata.pop(random_index)

def print_matchup(letter, list):
  celebrity = list[key[letter]]
  if letter == "A":
    command = "Compare"
  else:
    command = "Against"
  print(f"{command} {letter}: {celebrity["name"]}, a {celebrity["description"]}, from {celebrity["country"]}.")

def choice_handler(input_string):
  while True:
    response = input(input_string)
    if response.upper() == "A" or response.upper() == "B":
      return response.upper()
    print("I didn't catch that...")

current_score = 0
in_play = True
pairs = [get_random(data), get_random(data)]
key = { "A": 0, "B": 1 }

# print(pairs)
while True:
  os.system('cls' if os.name == 'nt' else 'clear')
  print(art.logo)
  if not in_play:
    print(f"Sorry, that's wrong. Final score: {current_score}")
    break
  if current_score:
    print(f"You're right! Current score: {current_score}")
  print_matchup("A", pairs)
  print(art.vs)
  print_matchup("B", pairs)
  choice = choice_handler("Who has more followers? Type 'A' or 'B': ")
  opponent_index = 1 - key[choice]
  if pairs[key[choice]]["follower_count"] > pairs[opponent_index]["follower_count"]:
    current_score += 1
    pairs = [pairs[1], get_random(data)]
  else:
    in_play = False
