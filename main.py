# Mai Klooster, Maya Sposito, Jessica Yoder ------------------------------------------------------
#        Name: Mai Klooster, Maya Sposito, Jessica Yoder
#       Peers: N/A
#  References: https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
#https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python
#https://www.youtube.com/watch?v=CuIV2-ivg0U
# ------------------------------------------------------

from graphics import *
import random
import time
from replit import audio


class Note:
  def __init__(self, win, position):
    """constructs black note centered at `position`, a line for the tail"""
    self.note = None
    self.tail = None

    self.construct(position)


  def construct(self, position):
    # draw note
    self.note = Circle(position, 5)
    self.note.setFill("black") #color note fully black

    # draw note tail
    p1 = Point(position.getX()+5, position.getY())
    p2 = Point(position.getX()+5, position.getY()-30)
    self.tail = Line(p1, p2)


  def draw(self, win):
    """draw the note to the window"""
    self.note.draw(win)
    self.tail.draw(win)


def main():
  # build a window
  width = 806
  height = 222
  win = GraphWin("Music", width, height)
  sheetMusic = Image(Point(403,501), "sheet_music_background.gif")  #image is 806 x 1003 pixels
  sheetMusic.draw(win)

  i = 0 # intialize while loop to iteration 0
  song_notes = [] # intialize song_notes as an empty list
  run = True # intialize run loop variable as true
  draw_note = False #initalize draw_note to false, so that only a valid entry will draw a note
  
  note_dict = {  #create dictonary of note scale degrees and their corresponding frequencies 
  1 : 261.62555,
  2 : 293.66475, 
  3 : 329.62755,
  4 : 345.22825,
  5 : 391.99545,
  6 : 440.0,
  7 : 493.885,
  } 


  while (run == True) and (i <= 15): #create a new note, repeating for the length of song_length
    
    try:
      note_type = input('\nWhat note would you like? \n 1-7: choose scale degree \n R: get randomized note \n Q: quit and play full melody \n').upper()

      if note_type == 'Q':
        run = False # stop loop
        draw_note = False #set draw_note to false so incorrect note is not drawn

      elif note_type == 'R':
        user_pitch = random.randint(1,7) # set user_pitch to a random note, 1 though 7
        draw_note = True # set draw_note to true to draw note


      elif (type(int(note_type)) == int):
        user_pitch = int(note_type)  #get user input
        draw_note = True #set draw_note to true to draw note

        if (user_pitch < 1) or (user_pitch > 7): # check if user entered a valid input
          print('Error: scale degree not in range 1-7') #print error message
          draw_note = False #set draw_note to false so incorrect note is not drawn
          i -= 1 #reset this loop iteration


    except ValueError:
      print('\nError: please enter Y or Q or scale degree not in range 1-7') #print error message
      i -= 1 #reset this loop iteration
      draw_note = False #set draw_note to false so incorrect note is not drawn


    if draw_note == True: #draw note, when supposed to draw note
      song_notes.append(user_pitch) #update song_notes with next note of song

      staff_x_placement = 120 + (i)*85 #assign user_note's x position to 120 pixels forward, added to the current number of the note loop multiplied by 85 pixels
      pitch_y_placement = 95 - user_pitch*5 #assign user_note's y position to 60 pixels down, minus the user_pitch scale degree multiplied by 5 pixels


      if (i) / 16 >= 0.5: #if this is the 9th-16th note, go to the second staff
        staff_x_placement -= 680 #subtract 680 pixels from the x position
        pitch_y_placement += 111 #add 111 pixels to the y position

      user_note = Note(win, Point(staff_x_placement, pitch_y_placement)) #assign user_note as an iteration of Note class located at given Point
    
      user_note.draw(win)

      #play user_pitch 
      note_tone = note_dict[user_pitch] #assign tone to be played as the frequency from note_dictionary that matches the user_pitch
      source = audio.play_tone(1, note_tone, 1)
      time.sleep(1.2) #play single tone audio for 1 second at volume 1
      
    #print(i, song_notes)
    i += 1 #update loop to next iteration
    

  #replit plays a series of notes for the user based on the sheet music they just created. 


  for note in song_notes:  #loop over song_notes list, playing each note
    note_tone = note_dict[note]
    source = audio.play_tone(1, note_tone, 1)
    time.sleep(1.2)
    
    #the sound parameters are: play_tone(duration, frequency, volume)


  print("Thanks for playing")
  

  
if __name__ == "__main__":
  main()
