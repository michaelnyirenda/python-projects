import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand = [rock, paper, scissors]
player = input("pick 0 for rock, 1 for paper or 2 for scissors: ")
if int(player) >= 3 or int(player) < 0:
  print("nigga, the fuck?")
else: 
  print("you chose: ")
  print(hand[int(player)])

  cpu = random.randint(0, 2)
  print("the cpu chose: ")
  print(hand[cpu]) 

  if int(player) == 2 and cpu == 0:
    print("take the L")
  elif int(player) == 0 and cpu == 2:
    print("thats a W")
  elif int(player) < cpu:
    print ("take the L")
  elif int(player) == cpu:
    print("yall the same fr")
  elif int(player) > cpu:
    print ("you win")


