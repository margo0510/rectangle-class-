import pygame 

#initialize game 
pygame.init()

#set diamension of screen 
screen = pygame.display.set_mode((600,600))

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#filling the screen with color 
screen.fill(white)

#creating rectangle class 
class Rect():
    #creating constructor function
    def __init__(self,color,dimension):
        self.rect_surf = screen
        self.rect_color = color 
        self.rect_dimensions = dimension

    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)
    

#creating objects for rectangle class 
#object name = class name(parameters to give)
green_rectangle = Rect(green,(50,20,100,100))

#calling draw function of the class 
green_rectangle.draw()


blue_rectangle = Rect(blue,(150,200,150,150))
blue_rectangle.draw()


red_rectangle = Rect(red,(300,400,200,200))
red_rectangle.draw()

pygame.display.update()


        
        



        
    