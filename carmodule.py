import pygame

class Car():
    '''
    Car class
    -----------------------------
    Class Variables
    -----------------------------
    xpos, ypos - coordinates of car
    score - score
    EPSILON - change in x coordinate
    car_image - sprite for car
    left_key, right_key - key binding for moving left and right (Default is left and right arrow keys)
    boundary_left, boundary_right - boundary for car to left and / or right
    ------------------------------
    Class Functions
    ------------------------------
    __init__ - default constructor
    draw_car - function to draw car using blit in pygame
    move_car - move car to left and right
    get_x - getter for x_pos
    get_y - getter for y_pos
    get_score - getter for score
    increase_score - increment score if dodged parameter is True, else crash
    crash - Function to crash car and exit after printing score
    '''
    x_pos, y_pos, score = 0, 0, 0
    EPSILON = 10
    car_image, left_key, right_key, boundary_left, boundary_right = None, None, None, None, None

    def __init__(self, car_image, init_x = 0, init_y = 0, left_key = pygame.K_LEFT,
            right_key = pygame.K_RIGHT, boundary_left = 0, boundary_right = 600):
        self.car_image = car_image
        self.x_pos = init_x
        self.y_pos = init_y
        self.left_key = left_key
        self.right_key = right_key
        self.boundary_left = boundary_left
        self.boundary_right = boundary_right
    
    def draw_car(self, game_display):
        game_display.blit(self.car_image, (self.x_pos, self.y_pos))

    def move_car(self, event):
        if event.type is pygame.KEYDOWN:
            if event.key == self.left_key:
                self.x_pos -= self.EPSILON
                self.x_pos = max(self.x_pos, self.boundary_left)
            elif event.key == self.right_key:
                self.x_pos += self.EPSILON
                self.x_pos = min(self.x_pos, self.boundary_right)

    def get_x(self):
        return self.x_pos

    def get_y(self):
        return self.y_pos

    def get_score(self):
        return self.score

    def increase_score(self, dodged):
        if not dodged:
            self.crash()
        else:
            self.score += 1
    def crash(self):
        pygame.quit()
        print("You crashed!")
        print("Final score is ", self.score)
        quit()
