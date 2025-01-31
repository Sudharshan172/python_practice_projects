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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
l = [rock,paper,scissor]
print("Welcome to the Rock, Paper and Scissor Game.\nLet's Begin!!!")
print("Type '0' for rock, '1' for paper, '2' for scissor.")
user_choice = int(input())
if user_choice == 0:
    print(f"You'r choise\n{l[user_choice]}  Rock\n")
elif user_choice == 1:
    print(f"You'r choise\n{l[user_choice]}  Paper\n")
else:
    print(f"You'r choise\n{l[2]}  Scissor\n")
import random
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(f"Computer choosen\n{l[computer_choice]}  Rock\n")
elif computer_choice == 1:
    print(f"Computer choosen\n{l[computer_choice]}  Paper\n")
else:
    print(f"Computer choosen\n{l[2]}  Scissor\n")
if user_choice == 0:
    if computer_choice == 0:
        print("Game Tie")
    elif computer_choice == 1:
        print("You Lose")
    else:
        print("You Win")
elif user_choice == 1:
    if computer_choice == 0:
        print("You Win")
    elif computer_choice == 1:
        print("Game Tie")
    else:
        print("You Lose")
if user_choice == 2:
    if computer_choice == 0:
        print("You Lose")
    elif computer_choice == 1:
        print("You Win")
    else:
        print("Game Tie")