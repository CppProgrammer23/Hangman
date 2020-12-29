import pygame
import random

### BackEnd Program ###
words=[]
with open('words.txt','r') as f:
    words=f.readlines()


cur_word=random.choice(words)[:-1]
print(cur_word)
### GUI ###
#init
pygame.init()
pygame.font.init()
#constant
BLACK=(10,10,10)
WHITE=(250,250,250)
DARK_BLUE=(0,0,255)
SIZE_WIN=(480,360)
FPS=30
RADUIS=13
GAP=10
LETTER = pygame.font.SysFont('arial',15)
#load the images
images=[]
for i in range(7):
    img=pygame.image.load('hangman'+str(i)+'.png')
    images.append(img)

LETTERS=[]
startx=round((SIZE_WIN[0] - (RADUIS*2+GAP)*13)/2)
starty=270
for i in range(26):
    x=startx+GAP*2+((RADUIS*2+GAP)*(i%13))
    y=starty+((i//13)*(GAP+RADUIS*2))
    LETTERS.append([x,y,chr(65+i),True])


#init the display
error=0
win=pygame.display.set_mode(SIZE_WIN)
pygame.display.set_caption('Hangman')
win.fill(WHITE)
#draw
win.blit(images[error],(4,4))
#update the display
pygame.display.update()
#loop game
done=False
clk=pygame.time.Clock()
score=60

#functions
def draw_btn():
    for l in LETTERS:
        *pos,ch,vis=l
        pygame.draw.circle(win,BLACK,tuple(pos),RADUIS,3)
        t=LETTER.render(ch,1,BLACK)
        win.blit(t,(pos[0]-6,pos[1]-8))
    for i in range(len(cur_word)):
        pygame.draw.line(win,BLACK,(200+i*30,140),(200+20+2*i*15,140),2) # 210 y=140
    pygame.display.update()
draw_btn()

while not done:

    #refresh the screen
    clk.tick(FPS)
    #init the display
    
    #look for an event
    for evt in pygame.event.get():
        if evt.type==pygame.QUIT:
            done=True
            print('Your score: ',score)
        if evt.type==pygame.KEYDOWN:
            if evt.key==pygame.K_ESCAPE:
                done=True
                print('Your score: ',score)
        if evt.type==pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print(position)

    #update the score and tries
    if error==6:
        done=True
        print('Your score: ',score)
    
    

#quit
pygame.quit()