'''
Objective:
The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. 
You will correct a code snippet, simulate moods for different days, and create a countdown timer.

Task 1: Your Mood Today
Write a program that simulates different moods for each day of the week. 
Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, 
loop through the days of the week and for each day, randomly select a mood from the list and print it. 
Ensure that your program includes the use of the random module to select the mood.
'''
import random as r 
moods = ["Happy", "Sad", "Energetic", "Calm"]
days_week = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(len(days_week)):
  mood = r.choice(moods)
  day = days_week[i]
  print(f"My mood {day} was {mood}!")


'''
# Take the day of the week (for day in days_week:) than randomize the moods (random_mood = r.choice(moods)) that will give me the output
# that I am looking for in this problem but its not using the range function. 
for day in days_week:
  random_mood = r.choice(moods)
  print(f"My mood {day} was {random_mood}!")
'''