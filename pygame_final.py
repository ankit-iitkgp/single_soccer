import pygame
import random
import os

WIDTH=1920
HIGHT=1080
FPS=1

#initialising conditions
pygame.init()
#for sound
pygame.mixer.init()

screen=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("single_soccer")
#tells pygame to keep track of time.
clock=pygame.time.Clock
#define colors
white = (255,255,255)
black =(0,0,0)
green = (44, 176, 55)
blue = (0,0,255)
red = (255,0,0)

#set up asset(art)



# defining the class of player
class PLAYER(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.image.load("p1_jump.png").convert()#right here 
                #self.image.fill(black)
                self.image.set_colorkey(black)
                self.rect=self.image.get_rect()
                self.rect.centerx=WIDTH/2
                self.rect.bottom=HIGHT-10
                self.speedx=0
                self.speedy=0
# updating the player after every frame        
        def update(self):
                self.speedx=0
                self.speedy=0
                press=pygame.key.get_pressed()
                if press[pygame.K_LEFT]:
                        self.speedx=-3
                if press[pygame.K_RIGHT]:
                        self.speedx=3
                if press[pygame.K_UP]:
                        self.speedy=-3
                if press[pygame.K_DOWN]:
                        self.speedy=3
# modifying the position of ball by speed
		self.rect.x += self.speedx
		self.rect.y += self.speedy
#to be within arena
		if self.rect.y>HIGHT:
			self.rect.y=HIGHT
		if self.rect.y<0:
			self.rect.y=0
		if self.rect.x>WIDTH:
			self.rect.x=WIDTH
		if self.rect.x<0:
			self.rect.x=0

#defining kick
	def kick(self):
		Ball = BALL(self.rect.centerx,self.rect.top)
		all_sprites.add(Ball)
		ball.add(Ball)

                     
class OPPONENT(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.image.load("p3_duck.png").convert()
                self.image.set_colorkey(black)
                self.rect=self.image.get_rect()
                self.rect.x=random.randrange(WIDTH/2,WIDTH - self.rect.width)
                self.rect.y=random.randrange(20,HIGHT/2)
                self.speedx=random.randrange(-4,4)
                self.speedy=random.randrange(-4,4)

        def update(self):
                self.rect.x += self.speedx
                self.rect.y += self.speedy
                # condition so that opponent do not overshoot the frame
                if self.rect.x>WIDTH-10:
                        self.speedx = random.randrange(-4,0)
			self.speedy = random.randrange(-4,4)
		if self.rect.x<10:
			self.speedx = random.randrange(0,4)  
			self.speedy = random.randrange(-4,4) 			
                if self.rect.y>HIGHT-10:
                        self.speedy = random.randrange(-4,0)
			self.speedx = random.randrange(-4,4)
		if self.rect.y<10:
			self.speedy = random.randrange(0,4)
			self.speedx = random.randrange(-4,4)


class GOAL(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.Surface((330,7))
                self.image.fill((255,255,255))
                self.rect=self.image.get_rect()
                self.rect.centerx=WIDTH/2
                self.rect.top=4


class LINE1(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.Surface((WIDTH/3,3))
                self.image.fill((255,255,255))
                self.rect=self.image.get_rect()
                self.rect.centerx=WIDTH/2
                self.rect.centery=HIGHT/4

class LINE2(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.Surface((3,HIGHT/4))
                self.image.fill((255,255,255))
                self.rect=self.image.get_rect()
                self.rect.centerx=WIDTH/3
                self.rect.centery=HIGHT/8
class LINE3(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.Surface((WIDTH,3))
                self.image.fill((255,255,255))
                self.rect=self.image.get_rect()
                self.rect.centerx=WIDTH/2
                self.rect.centery=HIGHT/2

class LINE4(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.Surface((3,HIGHT/4))
                self.image.fill((255,255,255))
                self.rect=self.image.get_rect()
                self.rect.centerx=(WIDTH*2)/3
                self.rect.centery=HIGHT/8


class BALL(pygame.sprite.Sprite):
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.image.load("lollipopRed.png").convert()
                self.image.set_colorkey(black)
                self.rect=self.image.get_rect()
                #position of the ball should be with player
                self.rect.centery=y
                self.rect.centerx=x
                self.speedy=-4

#If the ball goes out of the arena, it should be removed and new ball should be provided
        def update(self):
		self.rect.y += self.speedy
                if self.rect.bottom<=0:
                        self.kill()
			
        
                             
all_sprites = pygame.sprite.Group()
#creating name for all other class than player
mob = pygame.sprite.Group()
goal=pygame.sprite.Group()
ball=pygame.sprite.Group()
Player=PLAYER()
Goal=GOAL()
Line1 = LINE1()
Line2 =LINE2()
all_sprites.add(Line1)
all_sprites.add(Player)
all_sprites.add(Goal)
all_sprites.add(Line2)
Line3 =LINE3()
all_sprites.add(Line3)
Line4 =LINE4()
all_sprites.add(Line4)


goal.add(Goal)
#initialising score
SCORE=0
for i in range(5):
        Opponent=OPPONENT()
        all_sprites.add(Opponent)
        mob.add(Opponent)

running=True
while running:
        #screen.fill((100,23,13))
        for event in pygame.event.get():
                #closing the window
                if event.type==pygame.QUIT:
                        running = False
                elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                                Player.kick()

# UPDATE
        all_sprites.update()

# Various conditions of the game
        scored=pygame.sprite.groupcollide(ball,goal,True,False)
        if scored:
                SCORE=SCORE+1
                Player.kill()
                Player=PLAYER()
            	all_sprites.add(Player)
            	for i in range(4):
            	        Opponent.kill()

                Opponent=OPPONENT()
                all_sprites.add(Opponent)
                mob.add(Opponent)


        defended=pygame.sprite.groupcollide(ball,mob,True,False)
        if defended:
		Player.kill()
                Player=PLAYER()
                all_sprites.add(Player)


        Lost=pygame.sprite.spritecollide(Player,mob,False)
        if Lost:
                running=False

        screen.fill(green)
        all_sprites.draw(screen)
        pygame.display.flip()

pygame.quit()
print "\t\t\t\tGAME OVER"
print "\t\t\t\tYour score is: "
print "\t\t\t\t      ",SCORE
#ADHIKANSH: Provide more and more graphics to make this game look realistic.

