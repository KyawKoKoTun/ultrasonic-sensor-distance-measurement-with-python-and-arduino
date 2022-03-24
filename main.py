import serial
import pygame

pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

X = 1000
Y = 700

display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Serial')
font = pygame.font.Font('freesansbold.ttf', 32)

ser = serial.Serial('COM3')
ser.flushInput()

run = True

while run:
    ser_bytes = ser.readline()
    data = ''
    for i in str(ser_bytes):
        if i.isnumeric()==True:
            data=data+i
    data = int(data)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    display_surface.fill(black)
    pygame.draw.rect(display_surface, blue,
                     [130+(20*data),50, 40, 600], 0)
    pygame.draw.rect(display_surface, red, [10,200, 100,300], 0)
    pygame.draw.rect(display_surface, green, [110, 200, 30, 100], 0)
    pygame.draw.rect(display_surface, green, [110, 400, 30, 100], 0)
    text = font.render(str(data)+' cm', True, green, blue)
    display_surface.blit(text, (20, 20))
    pygame.display.update()
