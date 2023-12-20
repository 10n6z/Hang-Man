import pygame
import math
import random


pygame.init()

#SET UP
WIDTH, HEIGHT = 1000 , 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("hangman")

#COLOR
WHITE = (255,255,255)
BLACK = (0,0,0)
SILVER = (192,192,192)

#IMAGEs
images = []
for i in range(7):
    image = pygame.image.load("hangman"+str(i)+".png")
    images.append(image)
hangman_status = 0

#FONT
Letter_font = pygame.font.SysFont("comicsans",40)
Word_font = pygame.font.SysFont("comicsans",70)
Titled_font = pygame.font.SysFont("comicsans",80)
Mess_font = pygame.font.SysFont("comicsans",100)

#VARIABLEs
words = ["ACCOUNT","AUNT","ABANDONED","AVERAGE","ABROAD","ATTEND","ATTEMPT","ADMIN","ADVERTISEMENT","APPLE","ADJECTIVE","APRICOT","AUTUMN","ASSITS","ATTACK","AGENCY","APPLY","ARCHITECT","ALLY","ARROW","ARCHER","AREA","ANXIETY","ANSWER","ATTRACTIVE","ADVANTAGE","ADVENTURE","AFFORDABLE","ARRANGE","AUTHORITY","ABOUT","AMONG","ADVISE","ACADEMY","ALLOW","ALLERGIC","AFFECT","ALPHA","ASTOUNDING","ASTONISHED","ABUNDANT","ACTIVITY","ACTION","ABDOMINAL","ABSOLUTELY","ABSTRACT","ACCIDENT","ASCENT","ACCEPT","AGGRESSIVE","ADDICT"]
word = random.choice(words)
guessed = []
hangman_status = 0
GAP = 21
RADIUS = 23
start_x = round((WIDTH-(GAP + RADIUS * 2)*13)/2)
start_y = 500
A = 65
letters = []
for i in range(26):
    x = start_x + GAP *2 + ((GAP + RADIUS * 2) * (i % 13))
    y = start_y + ((i//13) * (GAP + RADIUS * 2))
    letters.append([x, y,chr(A + i),True])

#DRAWINGS
def draw():
    global x,y,ltr,visible
    screen.fill(SILVER)
    #TITLE
    title = Titled_font.render("HANGMAN PYTHON",10,BLACK)
    screen.blit(title,(WIDTH/2-title.get_width()/2,20))
    #WORD
    displayword = ""
    for letter in word:

        if letter in guessed :
            displayword += letter + ""
        else:
            displayword += " _ "
    word_text = Word_font.render(displayword,5,BLACK)
    screen.blit(word_text,(400,300))
    #BUTTONS
    for letter in letters:
        x,y,ltr,visible = letter
        if visible:
            pygame.draw.circle(screen,BLACK,(x,y),RADIUS,3)
            text = Letter_font.render(ltr,1,BLACK)
            screen.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
    screen.blit(images[hangman_status],(150,100))
    pygame.display.update()

#SIGNALs
def message(in4):
    pygame.time.delay(700)
    screen.fill(WHITE)
    mess = Mess_font.render(in4,5,BLACK)
    screen.blit(mess,(WIDTH/2-mess.get_width()/2,HEIGHT/2-mess.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2500)

def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x , m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x,y,ltr,visible = letter
                    if visible:
                        distance = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                        if distance < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            message("YOU WON!")
            break
        if hangman_status == 6:
            message("YOU LOST!")
            break
while True:

    main()
    pygame.quit()