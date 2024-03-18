'''
3. Loop Condition Logic
Objective:
The aim of this assignment is to explore the importance of the loop condition in while loops.
You will create loops with different conditions to see how they influence the behavior of the loop.

Task 1: Loop Condition Exploration
Write a while loop with a condition that will never be true (an infinite loop). Inside the loop, print a statement.
Then, use a break statement to exit the loop after 5 iterations.

Task 2: Conditional Exit
Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement.
The loop should terminate naturally once the condition is met.

'''
# Task one.

time_of_day = list(range(24))

days = 0


while True:
  for hour in time_of_day:
    print(f"It is {hour} hundred hours.")
    if hour == 23:
      days += 1
      print(f"It has been {days} days!")
  if days == 5:
    
    print(f"It has been five iterations.")
    break

# Task two.
time_of_day = list(range(24))
days = 0
iterations = 0
while days < 5:
  for hour in time_of_day:
    print(f"It is {hour} hundred hours.")
    if hour == 23:
      days += 1
      print(f"It has been {days} days!")
     
     

  
      