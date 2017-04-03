import pygame
import random

class Block:
		current_x = None
		current_y = None
		width = None
		height = None
		speed = None
		game_display = None
		color = None
		def __init__(self, X,Y, width, height, speed, color,game_display):
			self.current_x = X 
			self.current_y = Y
			self.width = width
			self.height = height
			self.speed = speed
			self.game_display = game_display
			self.color = color
			self.draw(self.current_y)



		#Draw the block with a particular Y
		def draw(self,Y):
			pygame.draw.rect(self.game_display, self.color, 
				[self.current_x, self.current_y, self.width, self.height])
