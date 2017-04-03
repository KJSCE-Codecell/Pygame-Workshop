import pygame

class car():
    x_pos, y_pos= 0, 0
    car_image = ""
    EPSILON = 10
    left_key, right_key, boundary_left, boundary_right = None, None, None, None

    def __init__(self, car_image, init_x = 0, init_y = 0, left_key = pygame.K_LEFT, right_key = pygame.K_RIGHT, boundary_left = 0, boundary_y = 600):
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
        if event.key == self.left_key:
            self.x_pos -= self.EPSILON
            self.x_pos = min(self.x_pos, self.boundary_left)
        elif event.key == self.right_key:
            self.x_pos += self.EPSILON
            self.x_pos = max(self.x_pos, self.boundary_right)
