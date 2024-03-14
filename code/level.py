import pygame 
from settings import *
from player import Player

class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = pygame.sprite.Group()

		# setup the level
		self.setup()

	def setup(self):
		# create a player
		player = Player((SCREEN_WIDTH//2,SCREEN_HEIGHT//2), self.all_sprites)

	def run(self,dt):
		self.display_surface.fill('black')
		self.all_sprites.draw(self.display_surface)
		self.all_sprites.update(dt)