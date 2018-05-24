import pygame
import random
import math
from vec2d import Vec2d
from pygame.locals import *

background_colour = (255,255,255)
(width, height) = (800, 800)

#Main Constants
Msun = 1
G2 = 1.560*10**(-13)
ly = 9.607*10**15 #m
vgal = 301*10**3 / ly * 3.1536*10**7
galm = 1*10**10
galr = 10**5
rgalcore = 1.3*10**3
pi = math.pi

#Parameters
galxsep = 2*galr
galysep = 1*galr
galattackangle = 0*pi/2

dt = 1000



class Galaxy():
    def __init__(self, (x, y), size, color, galattackangle):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.thickness = 3
        self.galattackangle = galattackangle

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += self.speed
        self.y -= self.speed
        self.speed *= drag

class Star():
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Galaxy Simulation')

number_of_particles = 1
my_particles = []

for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)

    particle = Particle((x, y), size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi*2)

    my_particles.append(particle)

selected_particle = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = findParticle(my_particles, mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - selected_particle.x
        dy = mouseY - selected_particle.y
        selected_particle.angle = 0.5*math.pi + math.atan2(dy, dx)
        selected_particle.speed = math.hypot(dx, dy) * 0.1

    screen.fill(background_colour)

    for particle in my_particles:
        particle.move()
        particle.bounce()
        particle.display()

    pygame.display.flip()
