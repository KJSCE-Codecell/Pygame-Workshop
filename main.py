import pygame
import carmodule

def main():
    pygame.init()   #Initialize Pygame

#Initializing display resolution variables
    display_width = 800
    display_height = 600

#Initializing color tuples in format (r, g, b)
    black = (0, 0, 0)
    white = (255, 255, 255)

    game_display = pygame.display.set_mode((display_width, display_height))   #Initialize Main screen size
    pygame.display.set_caption('Codecell Wars')   #Game's Name (Comes in title bar)
    clock = pygame.time.Clock() #Time with respect to game

    '''
        Pygame works in a loop
        The crashed variable is a boolean flag to indicate if the loop needs\
                to be exited.
    '''
    exit_game = False 

    car_image = pygame.image.load('racecar.png')    #Load car sprite
    car_dimensions = car_image.get_rect().size    #Get car dimensions in form of a tuple
    mycar = carmodule.car(car_image, (display_width*0.45), (display_height*0.8))    #Create object for first car with default key_bindings
    mycar_two = carmodule.car(car_image, (display_width*0.45), (display_height*0.8), pygame.K_a, pygame.K_f)    #Create object for second car with ASDF key bindings

    while not exit_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            mycar.move_car(event)
            mycar_two.move_car(event)

        game_display.fill(white)
        mycar.draw_car(game_display)
        mycar_two.draw_car(game_display)
        
        pygame.display.update() #Update the screen
                                #If parameter is mentioned, update only that part

        clock.tick(60)  #Frames per second

    pygame.quit() #Exit pygame
    quit() #Exit program overall

if __name__ == "__main__":
    main()
