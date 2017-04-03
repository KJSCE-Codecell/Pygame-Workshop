import pygame
import carmodule
import random
from block import Block

def main():
	'''
		Main function
		Run this using $python3 main.py
	'''
    pygame.init()   #Initialize Pygame

	#Initializing display resolution variables
    display_width = 800
    display_height = 600

	#Initializing color tuples in format (r, g, b)
    black = (0, 0, 0)
    white = (255, 255, 255)

	#Game display is the main game screen
	#The set_mode function returns a display object with specified configuration
    game_display = pygame.display.set_mode((display_width, display_height))   #Initialize Main screen size
    pygame.display.set_caption('Codecell Wars')   #Game's Name (Comes in title bar)
    clock = pygame.time.Clock() #Time with respect to game, used for FPS

    '''
        Pygame works in a loop
        The exit_game variable is a boolean flag to indicate if the loop needs
        to be exited.
    '''

    exit_game = False 

    car_image = pygame.image.load('racecar.png')    #Load car sprite
    car_dimensions = car_image.get_rect().size    #Get car dimensions in form of a tuple
    mycar = carmodule.Car(car_image, (display_width*0.45), (display_height*0.8),
		boundary_left = 100, boundary_right = 700 - car_dimensions[0])    #Create object for first car with default key_bindings
    '''
        Add two player functionality
    '''
    #random obstacles
    block_startx = random.randrange(100, 600 - car_dimensions[0])	#Set block's starting x
    block_starty = -600	#Set block's starting y
    block_speed = 7	#Set block's speed
    block_width = 100	#Set block's width
    block_height = 100	#Set block's height 
    isDodged = True	#Set to true if the block is dodged, else False

    while not exit_game:
		#Start new Frame loop
		#Read all Events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:	#User wants to quit
                exit_game = True
        mycar.move_car(event)	#Send the last event to car
        game_display.fill(white)	#Make Background white
        mycar.draw_car(game_display)	#Draw Car on given pygame display

        #__init__(self, X,Y, width, height, speed, color,game_display):
        block = Block(block_startx, block_starty, block_width,
         block_height, block_speed, black, game_display)	#Create new block at new position
       
        block_starty += block_speed		#Increase Block's Y coordinate

        if(mycar.get_x()>display_width-car_dimensions[0] or mycar.get_x()<0):	#If car moves out of frame
            isDodged = False
        if(block_starty>display_height):	#Block is below screen
            block_starty = 0 - block_height	#Take block to top
            block_startx = random.randrange(100, 600 - car_dimensions[0])	#keep block's X coordinate random
            isDodged = True	#Block has been dodged
            mycar.increase_score(isDodged)	#Increase score since it's dodged
            #block_speed +=0.5 increase speed

        if mycar.get_y()<block_starty+block_height:	#Block and Car are crashing
            if mycar.get_x()>block_startx and mycar.get_x()<block_startx+block_width
				or mycar.get_x()+car_dimensions[0]>block_startx and mycar.get_x()+car_dimensions[0]<block_startx+block_width:
                isDodged = False 
        
        pygame.display.update() #Update the screen
                                #If parameter is mentioned, update only that part
        if not isDodged: mycar.crash()	#If car has crashed
        block.draw(block_starty)	#Draw block
        clock.tick(60)  #Frames per second

    pygame.quit() #Exit pygame
    quit() #Exit program overall

if __name__ == "__main__":
    main()
