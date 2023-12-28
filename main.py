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

#Write your code below this line 👇
import random
you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
rival = random.randint(0,2)
images = [rock, paper, scissors]
print(images[you])
print("Computer chose:")
print(images[rival])

if you == rival:
  print("It's a draw")
elif (you == 0 and rival == 1) or (you == 1 and rival == 2) or (you == 2 and rival == 0):
  print("You lose")
else:
  print("You win")