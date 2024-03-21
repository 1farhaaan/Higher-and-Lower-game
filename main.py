from game_data import data
import random
from art import logo,vs
from replit import clear

def get_random_account():
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description =account["description"]
  country =account["country"]
  return f"{name} ,a {description},from {country}"

def check_answer(guess,a_followers,b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def compare():
  print(logo)
  answer =0
  is_game =True
  account_a = get_random_account()
  account_b = get_random_account()

  while is_game:
    account_a =account_b
    account_b = get_random_account()
    
    while account_a == account_b:
      account_b =get_random_account()
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    
    user =input("Who has more followers? Type 'A or 'B': ").lower()
    a_count = account_a["follower_count"]
    b_count = account_b["follower_count"]
    is_correct = check_answer(user,a_count, b_count)                 
    clear() 
    print(logo)
    if is_correct:
      answer +=1
      print(f"You are right! current score: {answer}")
    else:
      is_game =False
      print(f"You are wrong,your final score is:{answer}")
          
compare()