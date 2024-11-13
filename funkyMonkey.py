import pygame
import time

W_W = 1920
W_H = 1080


x = W_W // 2 - 352 // 2
y = W_H // 2 - -200 // 2
velocity = 3
screen = pygame.display.set_mode((W_W, W_H))
pygame.display.set_caption('Funky Monkey')
backgroundImage = pygame.image.load("images/BGBEACH.png").convert()
backgroundImage = pygame.transform.scale(backgroundImage, (W_W, W_H))
sidekickX = x - 50
sidekickY = y - 50
zone1Cutscene = pygame.image.load("cutscenes/testCustscene.png").convert_alpha()
zone1Cutscene = pygame.transform.scale(zone1Cutscene, (W_W, W_H))
zoneMusic = ["music/greenhill.mp3"]
monkey = pygame.image.load("images/funkyMonkey.png").convert_alpha()
monkey = pygame.transform.scale(monkey, (352, 264))
sidekick = pygame.image.load("images/penguien.png").convert_alpha()
sidekick = pygame.transform.scale(sidekick, (165, 123))
zone1Checkpoint = pygame.image.load("images/checkPointMarker.png").convert_alpha()
zone1Checkpoint = pygame.transform.scale(zone1Checkpoint, (464, 348))
bbGun = pygame.image.load("images/bbgun20.png").convert_alpha()
crabEnemy = pygame.image.load("images/crab.png").convert_alpha()
crabEnemy = pygame.transform.scale(crabEnemy, (199, 149))
crabX = x - 50
crabY = y - 50
levelTilesNames = ["images/sandyTIle.png"]
tileCount = 19
beachTileInit = pygame.image.load(levelTilesNames[0]).convert_alpha()
beachTileInit = pygame.transform.scale(beachTileInit, (199, 149))
rectWidth = 200
rectHeight = 50
yOffset = 132
showHitbox = True # Turn this to False if you dont want a hitbox to show
hitboxColor = (255, 0, 0)
movement = True
checpointReached = False
playMusic = False
pygame.init()

def movementSystem(keys, x, y):
    if movement:
        if keys[pygame.K_LEFT]:
            x -= velocity
        if keys[pygame.K_RIGHT]:
            x += velocity
    return x, y

def musicPlayer():
    if(playMusic == True):
        pygame.mixer.init()
        pygame.mixer.music.load(zoneMusic[0])
        pygame.mixer.music.play(-1)

musicPlayer()

def cutSceneAdder():
    if abs(x - 1497.1) < 5:
        screen.blit(zone1Cutscene, (0, 0))

def linInter(current, target, speed):
    return current + (target - current) * speed

def drawTiles():
    for i in range(100):
        y = i * (rectHeight + yOffset) + 100
        screen.blit(beachTileInit, (y, 870))

def showHitboxes():
    if showHitbox:
        pygame.draw.rect(screen, hitboxColor, pygame.Rect(x, y, 352, 264), 2)

status = True
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    
    keys = pygame.key.get_pressed()
    x, y = movementSystem(keys, x, y)
    #screen.blit(backgroundImage, (0, 0))
    drawTiles()
    screen.blit(zone1Checkpoint, (1598, 655))
    #screen.blit(sidekick, (sidekickX, sidekickY))
    #screen.blit(crabEnemy, (crabX, crabY))
    sidekickX = linInter(sidekickX, x, 0.01)
    sidekickY = linInter(sidekickY, y, 0.01)
    crabX = linInter(crabX, x, 0.01)
    crabY = linInter(crabY, y, 0.01)
    showHitboxes()
    cutSceneAdder()
    screen.blit(monkey, (x, y))
    pygame.display.update()

pygame.quit()
