#higher lower game:
import art
from Data import data
import random
from replit import clear

def get_random_account():
  return random.choice(data)

def format_data(account):
  name= account["name"]
  description= account["description"]
  country= account["country"]
  return f"{name} a {description} from {country}"


def check_answer(guess,a_follower_count,b_follower_count):
  if a_follower_count>b_follower_count:
    return guess=="a"

  else:
    return guess=="b"


def game():
  print(art.logo)
  score=0
  game_should_continue= True
  a_account=get_random_account()
  b_account=get_random_account()

  while game_should_continue:

   a_account = b_account
   b_account = get_random_account()
   while a_account == b_account:
     b_account= get_random_account()
   print(f"Compare A {format_data(a_account)}")
   print(art.vs)
   print(f"Against B {format_data(b_account)}")
   guess= input("Who has the most follower Type A or B :  ").lower()
   a_follower_count = a_account["follower_count"]
   b_follower_count = b_account["follower_count"]
   is_correct = check_answer(guess, a_follower_count, b_follower_count)
   clear()
   print(art.logo)
   if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
   else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")

game()

  
