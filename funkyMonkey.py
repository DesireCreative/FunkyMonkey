import pygame
import time

pygame.init()

W_W = 1920
W_H = 1080

x = 100
y = 100
velocity = 3

screen = pygame.display.set_mode((W_W, W_H))
pygame.display.set_caption('Funky Monkey')

backgroundImage = pygame.image.load("images/BGBEACH.png").convert()
backgroundImage = pygame.transform.scale(backgroundImage, (W_W, W_H))

sidekickX = x - 50
sidekickY = y - 50

zone1Cutscene = "cutscenes/testCustscene.png"

zoneMusic = ["music/greenhill.mp3"]

"""funkyMonkeyImages = ["PNGSEQUENCES/idle0001.png", "idle0002.png", "idle0003.png", "idle0004.png", "idle0005.png", "idle0006.png", "idle0007.png", "idle0008.png", "idle0009.png", "idle0010.png"]
funkeyMonkey1 = pygame.image.load(funkyMonkeyImages[0]).convert_alpha()
funkeyMonkey1 = pygame.transform.scale(funkeyMonkey1, (352.25, 264.2))"""

monkey = pygame.image.load("images/funkyMonkey.png").convert_alpha()
monkey = pygame.transform.scale(monkey, (352, 264))
sidekick = pygame.image.load("images/penguien.png").convert_alpha()
sidekick = pygame.transform.scale(sidekick, (165, 123))

zone1Checkpoint = pygame.image.load("images/checkPointMarker.png").convert_alpha()
zone1Checkpoint = pygame.transform.scale(zone1Checkpoint, (464, 348))

def movementSystem(keys, x, y):
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    """if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity"""
    return x, y

def musicPlayer():
    zone1 = pygame.mixer.music.load(zoneMusic[0])
    pygame.mixer.music.play(-1)

musicPlayer()

#def checkPoint():
    

def cutSceneAdder():
    zone1Cutscene = pygame.image.load("cutscenes/testCustscene.png").convert_alpha()
    if abs(x - 1497.1) < 5:
        screen.blit(zone1Cutscene, (0, 0))
        zone1Cutscene = pygame.transform.scale(sidekick, (W_W, W_H))
        print("test")
      

def playerHitbox(self, rect):
    if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
        if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False
        
def itemDrawer():
    pass
    
def linInter(current, target, speed):
    return current + (target - current) * speed
    
def enemyDrawer():
    pass

status = True
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    keys = pygame.key.get_pressed()

    x, y = movementSystem(keys, x, y)

    sidekickX = linInter(sidekickX, x, 0.01)
    sidekickY = linInter(sidekickY, y, 0.01)
    
    cutSceneAdder()
    #checkPoint()
    screen.blit(backgroundImage, (0, 0))
    screen.blit(monkey, (x, y))
    #screen.blit(funkeyMonkey1, (x, y))
    screen.blit(sidekick, (sidekickX, sidekickY))
    screen.blit(zone1Checkpoint, (1598, 655))
    
    pygame.display.update()

pygame.quit()
