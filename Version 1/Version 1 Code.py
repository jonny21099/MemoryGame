# This is Memory Version 1
# In this version
from uagame import Window
import pygame, time, random
from pygame.locals import *

# User-defined functions

def main():

   window = Window('Memory', 700, 550)
   window.set_auto_update(False)
   game = Game(window)
   game.play()
   window.close()

# User-defined classes

class Game:
   # An object in this class represents a complete game.
 
   def __init__(self, window):
      # Initialize a Game.
      # - self is the Game to initialize
      # - window is the uagame window object
      
      self.window = window
      self.pause_time = 0.0004 # smaller is faster game
      self.close_clicked = False
      self.continue_game = True
      Tile.set_window(window)
      Tile.load_images()
      
      #init score
      #self.score = 0
      #self.score_color = 'white'
      #self.score_font = 75      
      
      # init board
      self.board = []
      self.create_board()
      self.default_counter = 16
    
   def create_board(self):
      # create a 4x4 board by creating and adding one row at a time
      # -self is the Game object
      for row_index in range(4):
         # create row
         row = self.create_row(row_index)
         # Add row to board
         self.board.append(row)
         
   def create_row(self, row_index):
      # creates one row of 4 Tile objects and returns it
      # -self is the Game object
      # -row_index is the row number to be created
      row = []
      width = self.window.get_width()//5
      height = self.window.get_height()//4
      for col_index in range(4):
         x = width * col_index
         y = height * row_index
         # Create Tile object
         tile = Tile(x, y, width, height)
         # Add tile to row
         row.append(tile)
         Tile.delete_images()
      return row

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not
      while not self.close_clicked:  # until player clicks close box
          # play frame
         self.handle_event()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
         time.sleep(self.pause_time) # set game velocity by pausing

   def handle_event(self):
      # Handle each user event by changing the game state
      # appropriately.
      # - self is the Game whose events will be handled
      
      event = pygame.event.poll()
      if event.type == QUIT:
         self.close_clicked = True
      
      if event.type == MOUSEBUTTONUP and self.continue_game:
         self.handle_mouse_up(event)
         
   def handle_mouse_up(self, event):
      # handles mouse up event
      # - event is pygame.event.Event object
      for row in self.board:
         for tile in row:
            if tile.select(event.pos) == True:
               self.default_counter -= 1
      
         
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.window.clear()
      for row in self.board:
         for tile in row:
            tile.draw()
      
      #self.window.set_font_size(self.score_font)
      #self.window.set_font_color(self.score_color)
      #x = self.window.get_width() - self.window.get_string_width(str(self.score))
      y = 0
      #self.window.draw_string(str(self.score), x, y)
   
      # if not self.continue_game:
        # pass
      self.window.update()

   def update(self):
      # Update the game objects.
      # - self is the Game to update
      pass
      #self.score = pygame.time.get_ticks()//1000
   
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      pass
      #if self.default_counter == 0:
      #   self.continue_game = False

   
class Tile:
   # An object of this class represents a Tile
   # Class Attributes
   window = None
   #font_size = 133
   border_size = 2
   border_color = pygame.Color('black')
   #images = None
   #default = pygame.image.load('image0.bmp')
   
   # Class Method
   @classmethod
   def set_window(cls, window):
      cls.window = window
   
   #Instance Methods
   def __init__(self, x, y, width, height):
      # initializes the Tile object
      # - self is the Tile
      # - x,y are top left corner int coordinates of Tile object
      # - width, height are int dimensions of Tile object

      self.content = Tile.images[0]
      self.rect = pygame.Rect(x, y, width, height)
      self.exposed = True
      
   def draw(self):
      # draws the Tile based on its flashing attributes
      # - self is the Tile object to draw

      if self.exposed:
         image = self.content # When exposed = True, image = image 1-9.bmp
         
      else:
         image = Tile.default # When exposed = False, image = default image0.bmp
         
      surface = Tile.window.get_surface()
      pygame.draw.rect(surface, Tile.border_color, self.rect, Tile.border_size)
      width = self.rect[2] - Tile.border_size * 2  
      height = self.rect[3] - Tile.border_size * 2  
      x =  self.rect[0] + Tile.border_size 
      y =  self.rect[1] + Tile.border_size 
      image = pygame.transform.scale(image,(width, height)) # Scale image size
      surface.blit(image,(x,y)) # Put image surface onto tile surface
      
   
   @classmethod
   def delete_images(cls):
      # Deletes image so it doesn't get repeated
      del cls.images[0]
   
   @classmethod
   def load_images(cls):
      # load the images into a dictionary for later use
      cls.images = []
      for i in range(1,9):
         images = pygame.image.load('image' + str(i) + '.bmp')
         cls.images.append(images)
      cls.images += cls.images # Makes a duplicate of image list
      random.shuffle(cls.images)
      
   def select(self, position):
      pass
      # When tile is clicked, expose = True
      #if self.rect.collidepoint(position) and not self.exposed:
         #self.exposed = True 
         #return True
   
   
main()

