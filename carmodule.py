import pygame

class car():
    x_pos = 0
    y_pos = 0
    car_image = ""
    game_display = None
    left_key = None
    right_key = None
    EPSILON = 10
    def __init__(self, car_image, init_x = 0, init_y = 0, left_key = pygame.K_LEFT, right_key = pygame.K_RIGHT):
        self.car_image = car_image
        self.x_pos = init_x
        self.y_pos = init_y
        self.left_key = left_key
        self.right_key = right_key
    
    def draw_car(self, game_display):
        game_display.blit(self.car_image, (self.x_pos, self.y_pos))

    def move_car(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.left_key:
                self.x_pos -= self.EPSILON
            elif event.key == self.right_key:
                self.x_pos += self.EPSILON
