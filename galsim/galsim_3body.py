from visual import *
import math

win = 500
rgal = 1e5
scene = display(title = "Galaxy Simulation", width = win, height = win, x = 0, y = 0, center = (.1*rgal/2, 0 , .1*rgal/2), range = (.2*rgal,.2*rgal, .2*rgal), autoscale = True)

#Constants
"""
G   = 6.674e-11

ly  = 9.4607e15                         #m
rgal = 1e5*ly                           #m scaling factor for equations
Msun = 1.99e30                          #kg
vgal = 301e3                            #velocity of Andromeda in m/s
rgalcore = 1.3e3*ly                     #galaxy core size
galmass = 1e10*Msun
"""
#Constants 2

G2 = 1.560e-13
ly = 9.4607e15 #m
rgal = 1e5
Msun = 1
vgal = 301e3 / ly * 3.1536e7
galmass = 1e10
rgalcore = 1.3e3
pi = math.pi

#Initial Conditions

dt = 1000                                #in years
simrate = 2000                          #Simulation Rate
dx = .1*rgal                             #separation in x direction
vgal1 = vgal
vgal2 = vgal
gal1_size = 1.0                         #scaling of galaxy core sizes
gal2_size = 1.0
gal1_speed = 0.1
gal2_speed = 0.1
gal1_mass = 1.0
gal2_mass = 1.0

#Galaxy Generation

gal1 = sphere(pos=(-1*dx, 0, 0), radius=rgalcore*gal1_size, color=color.blue, make_trail=True, interval=100, retain=2000)
gal2 = sphere(pos=(dx, 0, 0), radius=rgalcore*gal2_size, color = color.magenta, make_trail=True, interval=100, retain=2000)



gal1.v = vector(0, 0, -1*vgal*gal1_speed)
gal2.v = vector(0, 0, vgal*gal2_speed)

gal1.m = galmass*gal1_mass
gal2.m = galmass*gal2_mass

#Test Particle Generation

nParticles = 15
particleDistance = 5*rgalcore
testsize = rgalcore*0.10
testParticles = []
testParticlesv = []
testParticlesa = []
testParticlespos = []
for i in range(nParticles):
    theta = 2*pi/nParticles*i
    newParticleInitialSpeed = (G2*gal1.m/particleDistance)**.5
    newParticle = sphere(pos=gal1.pos+particleDistance*vector(math.cos(theta),0, math.sin(theta)), radius = testsize, color = color.red, make_trail=False, interval=100, retain=2000) 
    newParticleVelocity = gal1.v+newParticleInitialSpeed*vector(-1*math.sin(theta), 0, math.cos(theta))
    newParticlepos = gal1.pos+particleDistance*vector(math.cos(theta),0, math.sin(theta))
    testParticles.append(newParticle)
    testParticlesv.append(newParticleVelocity)
    testParticlespos.append(newParticlepos)
    r1 = gal1.pos - newParticlepos
    r2 = gal2.pos - newParticlepos
    testParticlesAcceleration = G2*(gal1.m*(r1/mag(r1)**3)+gal2.m*(r2/mag(r2)**3))
    testParticlesa.append(testParticlesAcceleration)

#Functions

def galaxyGeneration():
    return True

def galaxyPositionUpdate(gal1,gal2,testParticles, testParticlesv, testParticlespos, dt):
    r = gal1.pos - gal2.pos
    gal1.a = -1*G2*gal2.m*r/mag(r)**3
    gal2.a = G2*gal1.m*r/mag(r)**3

    gal1.v = gal1.v+gal1.a*dt
    gal2.v = gal2.v+gal2.a*dt

    for i in range(nParticles):
        r1 = gal1.pos - testParticlespos[i]
        r2 = gal2.pos - testParticlespos[i]
        testParticlesa[i] = G2*(gal1.m*(r1/mag(r1)**3) + gal2.m*(r2/mag(r2)**3))
        testParticlesv[i] = testParticlesv[i]+testParticlesa[i]*dt
        testParticlespos[i] = testParticlespos[i]+testParticlesv[i]*dt
        testParticles[i].pos = testParticlespos[i]
        
    gal1.pos = gal1.pos + gal1.v*dt
    gal2.pos = gal2.pos + gal2.v*dt
    
    return gal1.pos,gal2.pos, testParticlesv, testParticlespos


#Run Program

while True:
    rate(simrate)

    gal1.pos,gal2.pos,testParticlesv,testParticlespos = galaxyPositionUpdate(gal1,gal2,testParticles, testParticlesv, testParticlespos,dt)
    
    
        








