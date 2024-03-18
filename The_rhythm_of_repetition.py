'''
5. Looping Lists - The Rhythm of Repetition
Objective:
Dive into the heart of Python loops with a musical twist. Your task is to explore different ways of looping through lists, 
each with its unique style and purpose. By the end of this assignment, you will be able to control your loops 
like a DJ controls the tracks, ensuring each element gets its time to shine.

Task 1: The for Loop DJ Set
Using the provided genres list, write a for loop that prints out each genre with a custom message. 
Extend this task by adding a counter that displays the number of the track before the genre.

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
Task 2: The Remix Artist with while
Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a 
condition to stop the loop if a certain genre is played for instance Hip-hop.

Task 3: Light Show Technician Loop
Using the range() function, loop through the genres list by index. For each genre, print out the track number 
and a message that the light show is ready. Modify the loop to skip a genre if it's not suitable for the light show, 
for instance Classical genre.

'''

# Task one.


genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track_counter1 = 0 
track_counter2 = 0 
track_counter3 = 0 
track_counter4 = 0 
total_counter = 0

for count, song in enumerate(genres, start = 1):
  if song == "Jazz":
    track_counter1 += 1
    print(f"#{count}. {song}: Time to set back and relax. {track_counter1} plays.")
    
  elif song == "Rock":
    track_counter2 +=1
    print(f"#{count}. {song}: Time get to party! {track_counter2} plays.")
    
  elif song == "Hip-hop":
    track_counter3 += 1 
    print(f"#{count}. {song}: Now we are talking. {track_counter3} plays.")
    
  elif song == "Classical":
    track_counter4 += 1
    print(f"#{count}. {song}: Getting the brain working its maximum. {track_counter4} plays.")
    
else:
  total_counter +=1
  print(f"We have played this playlist {total_counter} times.")

# Could also do this for one single message just different name and count.
for count, genre in enumerate(genres, start = 1):
  print(f"#{count}. {genre}: We will be on this genre for a while.")

# Task two


genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track_counter1 = 0 
track_counter2 = 0 
track_counter3 = 0 
track_counter4 = 0 
total_counter = 0

while total_counter < 5:
  for count, song in enumerate(genres, start = 1):
    if song == "Jazz":
      track_counter1 += 1
      print(f"#{count}. {song}: Time to set back and relax. {track_counter1} plays.")
      
    elif song == "Rock":
      track_counter2 +=1
      print(f"#{count}. {song}: Time get to party! {track_counter2} plays.")
    
    elif song == "Hip-hop":
      track_counter3 += 1 
      print(f"#{count}. {song}: Now we are talking. {track_counter3} plays.")
     
    elif song == "Classical":
      track_counter4 += 1
      print(f"#{count}. {song}: Getting the brain working its maximum. {track_counter4} plays.")
     
  else:
    total_counter +=1
    print(f"We have played this playlist {total_counter} times.")    
else:
  print(f"Reset the counter if you want to shuffle back through the playlist.")


# Task Three




genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
light_show1 = input("Is the light show suitable for Jazz? (yes or no) ")
light_show2 = input("Is the light show suitable for Rock? (yes or no) ")
light_show3 = input("Is the light show suitable for Hip-hop? (yes or no) ")
light_show4 = input("Is the light show suitable for Classical? (yes or no) ")
  
for i in range(len(genres)):
  song = genres[i]
  count = genres.index(song) +1

  if song == "Jazz" and light_show1.lower() == "yes":
      print(f"#{count}. {song}: The light show is ready.")
      
  elif song == "Rock" and light_show2.lower() == "yes":
      print(f"#{count}. {song}: The light show is ready.")
      
  elif song == "Hip-hop" and light_show3.lower() == "yes":
    print(f"#{count}. {song}: The light show is ready.")
    
  elif song == "Classical" and light_show4.lower() == "yes":
    print(f"#{count}. {song}: The light show is ready.")

else:
   print("This will be a great show!")


# I could do this as well to just skip it.

for i in range(len(genres)):
  song = genres[i]
  count = genres.index(song) +1

  if song == "Jazz":
      print(f"#{count}. {song}: The light show is ready.")
      
  elif song == "Rock":
      print(f"#{count}. {song}: The light show is ready.")
      
  elif song == "Hip-hop":
    print(f"#{count}. {song}: The light show is ready.")
    
  elif song == "Classical":
    continue

else:
   print("That will be a great show!")
