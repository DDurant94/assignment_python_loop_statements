'''
4. Python's Random Game Night
Objective:
The aim of this assignment is to explore the random package in Python and understand 
how it can be used with loops to introduce randomness into your programs.

Task 1: Random Choice Game
Create a game where a player has a list of items. They have to guess which item in the list was selected. 
Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.
'''
import random as r
item_list = ["rock", "paper", "scissors"]
users_name = input("Enter in your name. ")
computer_name = "Computer"
user_points = 0
computer_points = 0
total_points = 0
while total_points <= 5:
    for i in item_list:
      item = r.choice(item_list)
      user_input = input("Guess one of the items in the list: (rock, paper, scissors) ")
      if user_input.lower() == item:
        user_points += 1
       
        print(f"You guessed right! The computer picked {item}. You get a point. You have {user_points} points.")
      elif user_input.lower() != item:
        computer_points += 1 
      
        print(f"The computer picked {item}. The computer has {computer_points} points.")
    if user_points or computer_points == 5:
       print(F"{users_name} has {user_points} points and {computer_name} has {computer_points} points.")
       break 

  

if user_points > computer_points:
    print(f"Game Over! {users_name} wins this round.")
elif computer_points > user_points:
    print(f"Game Over! {computer_name} wins this round.")
else:
   print("Game Over! It was a tie.")

# I don't fully understand why the program wont stop at a certen point threshold. The program is going off one or the other for points rather
# than the total points.
