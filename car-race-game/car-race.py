from random import randint
import pygame
pygame.init()
b_colour=(64,64,64)
screen=pygame.display.set_mode((1500,685))
top=pygame.display.set_caption('CAR RACE')
car=pygame.image.load('car1.png')
car2=pygame.image.load('car2.png')
black=pygame.image.load('car1.png')
x=50
y=640
s=1
run=True
i=0
b=0
d=0
f=0
h=0
j=0
a=randint(240,490)
c=randint(50,130)
e=randint(140,230)
g=randint(240,490)
i=randint(240,490)
k=randint(240,490)
z=600
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x>=29:
            x=x-5
        if keys[pygame.K_RIGHT] and x<=436:
            x=x+5
        if keys[pygame.K_UP]:
            y=y-5
        if keys[pygame.K_DOWN] <= 636:
            y=y+5
        if z<=600:
            k=randint(40,100)
            l=0
            z=0
        if z==400:
            a=randint(105,160)
            b=0
        if z==500:
            c=randint(165,220)
            d=0
        if z==200:
            e=randint(225,280)
            f=0
        if z==300:
            g=randint(285,340)
            h=0
        if z==100:
            i=randint(345,401)
            j=0
        if b-25<y<b+25 or d-25<y<d+25 or f-25<y<f+25 or h-25<y<h+25 or j-25<y<j+25 or l-25<y<l+25:
            if a-25<x<a+25 or c-25<x<c+25 or e-25<x<e+25 or g-25<x<g+25 or k-25<x<k+25:
                print(a,b,c,d,e,f,g,h,i,j,k,l,x,y)
                run=False
        if y<=30:
            run=False
        screen.fill(b_colour)
        screen.blit(black,(0,0))
        pygame.draw.line(screen(230,1840),(15,1000),(15,0),30)
        pygame.draw.line(screen(230,1840),(485,685),(485,0),30)
        pygame.draw.line(screen(255,255,256),(245,685),(245,0),20)
        screen.blit(car(x,y))
        screen.blit(car2(a,b))
        screen.blit(car2(c,d))
        screen.blit(car2(e,f))
        screen.blit(car2(g,h))
        screen.blit(car2(i,j))
        screen.blit(car2(k,l))
        l=l+1;b+=1;d+=1;f+=1;h+=1;j+=1;z+=1
        pygame.display.update()    
