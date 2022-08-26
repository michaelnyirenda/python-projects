# from game_data import data
# # # print higher lower logo
# #   from art import logo
# #   print(logo)
# #    print("\n")

# # def compare(foll_A, foll_B):
# #   if choice == 'a':
# #     choice = foll_A
# #     follows = foll_B
# #   elif choice == 'b':
# #     choice = foll_B
# #     follows = foll_A

# x = 0
# y = 1

# choice = input("who has more followers? type 'a' or 'b': ")

# if choice ==  "a":
#   choice = foll_A
#   follows = foll_B
# elif choice == "b":
#   choice = foll_B
#   follows = foll_A

#  # x =+ 1
#  #  y =+ 1
  
#  #  # assignment for option A
#  #  dict_A = data[x]
#  #  name_A = dict_A['name']
#  #  desc_A = dict_A['description']
#  #  country_A = dict_A['country']
#  #  foll_A = int(dict_A['follower_count'])

#  #  # assignment for option B
#  #  dict_B = data[y]
#  #  name_B = dict_B['name']
#  #  desc_B = dict_B['description']
#  #  country_B = dict_B['country']
#  #  foll_B = int(dict_B['follower_count'])



# while choice > follows:

#   # def option_A()
#   print(f"compare a: {name_A}, a {desc_A}, from {country_A}\n")

#   # print VS logo
#   from art import vs
#   print(vs)

#   # def option_B()
#   print(f"\ncompare b: {name_B}, a {desc_B}, from {country_B}")
  
 
#   if choice < follows:
#     print(f"sorry, thats wrong. current score: {x}")
#   else:
#     print(f"youre right! current score: {x}")


# # # print VS logo
# #   from art import vs
# #   print(vs)

#######################################################################
from game_data import data
from art import logo, vs
import random
from replit import clear

game_end = False
x = 0
account_b = random.choice(data)

# loop the game
while game_end == False:
  
  # format the account data into printable format
  def format_data(account):
    """take the account data and returns printable format"""
    name = account['name']
    desc = account['description']
    country = account['country']
    return f"{name}, a {desc}, from {country}\n"
  
  # compare the answer
  def compare(choice, foll_a, foll_b):
    """take the user choice and follower count and returns if they got it right"""
    
    if choice ==  "a":
      choice = foll_a
      follows = foll_b
    elif choice == "b":
      choice = foll_b
      follows = foll_a
  
    if choice > follows:
      return True
    else:
      
      return False
  
  # print logo
  print(logo)
  
  
  # generate random account from game data
  # make option B into option A
  
  account_a = account_b
  account_b = random.choice(data)
  
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"compare a: {format_data(account_a)}")
  
  # print vs
  print(vs)
  
  print(f"compare b: {format_data(account_b)}")
  
  # ask for a choice
  choice = input("who has more followers? type 'a' or 'b': ").lower()
  
  # check if user is correct
  ## get each follower count
  follow_a = account_a["follower_count"]
  follow_b = account_b["follower_count"]
  
  is_correct = compare(choice, follow_a, follow_b)

  # clear the screen after answer
  clear()

  # score keeping
  if is_correct:
    x += 1
    print(f"you are right! current score: {x}")
  else:
    game_end = True
    print(f"thats wrong. final score: {x}")
  
  
  


