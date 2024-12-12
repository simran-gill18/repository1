import pygame
import random
import math

pygame.init()

rule1 = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
rule2 = pygame.image.load("spaceship.png")
pygame.display.set_icon(rule2)

playerimg = pygame.image.load("spaceship2.png")
playerx = 370                                       # where we see it
playery = 480
playerx_change = 0

enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("spaceship3.png"))
    enemyx.append(random.randint(0, 736))
    enemyy.append(random.randint(0, 150))
    enemyx_change.append(0.3)
    enemyy_change.append(40)

bulletimg = pygame.image.load("bullet.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textx = 10
testy = 10

game_end = pygame.font.Font("freesansbold.ttf", 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    rule1.blit(score, (x, y))

def game_over_text():
    over_text = game_end.render("Game Over", True, (255, 255, 255))
    rule1.blit(over_text, (200, 250)) 
    
def player(x, y):
    rule1.blit(playerimg, (x, y))

def enemy(x, y, i):
    rule1.blit(enemyimg[i], (x, y))

def fire_bullet(x, y): 
    global bullet_state            
    bullet_state = "fire"
    rule1.blit(bulletimg, (x + 16, y + 10))

def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2))) 
    if distance < 27:
        return True
    else:
        return False

rule3 = True
while rule3:

    rule1.fill((128, 0, 0))
    for event in pygame.event.get():              # pygame.event.get is screen open's name 
        if event.type == pygame.QUIT:
            rule3 = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
            if event.key == pygame.K_SPACE:
                bulletx = playerx
                fire_bullet(bulletx, bullety)                         
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    for i in range(num_of_enemies):

        if enemyy[i] > 440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break
            
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.3
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -0.3
            enemyy[i] += enemyy_change[i]
        collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = 480
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint (0, 736)
            enemyy[i] = random.randint (50, 150)

        enemy(enemyx[i], enemyy[i], i)
    
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"

    if bullet_state == "fire":  
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

    player(playerx, playery)
    show_score(textx, testy)
    pygame.display.update()
