import random
import pygame

map = [[random.randrange(0,2)]*80 for i in range(80)]
print(map)


pygame.init()
pygame.display.set_caption("game of life")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    event = pygame.event.get()
   
   
    for event in pygame.event.get():
        break
   
   
   
    pygame.time.wait(200)
    for i in range (80):
        for j in range(80):
            counter = 0
            if i<79 and map[i+1][j] == 1:
                counter+=1
            if i<79 and map[i-1][j] == 1:
                counter+=1  
            if j<79 and map[i][j+1] == 1:
                counter+=1
            if j<79 and map[i][j-1] == 1:
                counter+=1
               
            if i<79 and j<79 and map[i+1][j+1] == 1:
                counter+=1
            if i<79 and j<79 and map[i-1][j+1] == 1:
                counter+=1
            if i<79 and j<79 and map[i-1][j-1] == 1:
                counter+=1
            if i<79 and j<79 and map[i+1][j-1] == 1:
                counter+=1
               
               
            if map[i][j]==1 and counter <=1:
                map[i][j]=0
                print("I died from lonliness")
            if map[i][j]==1 and counter >=4:
                map[i][j]=0
                print("I died from overpopulation")
            if map[i][j]==0 and counter ==3:
                map[i][j]=1
                print("I born")
           
           
   
   
    screen.fill((0,0,0))
    for i in range (80):
        for j in range(80):
            if map[i][j]==0:
                pygame.draw.rect(screen,(0,0,0), (j*10, i*10, 10,10))
                pygame.draw.rect(screen,(255,255,255), (j*10, i*10, 10, 10), 1)
            if map[i][j]==1:
                pygame.draw.rect(screen,(0,200,200), (j*10, i*10, 10, 10))
               
   
    pygame.display.flip()
   
   
pygame.quit()
