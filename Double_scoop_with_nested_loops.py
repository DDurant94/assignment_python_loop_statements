'''
2. Double Scoop with Nested Loops
Objective:
The aim of this assignment is to practice using nested loops in Python. You will correct a nested loop code snippet, 
simulate a mood tracker, and generate a multiplication table.

Task 1: Your Mood Tracker
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) 
for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, 
and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.

'''
import random as r 

moods = ["Happy", "Sad", "Energetic", "Calm"]
time_of_day = ["morning", "afternoon", "evening"]
day_of_week = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in day_of_week:
  for time in time_of_day:
    mood = r.choice(moods)
    print(f"My mood was {mood} in the {time} on {day}.")
