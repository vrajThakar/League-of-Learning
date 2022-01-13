import pygame
from settings import *
user = input("What is your name")

tries = 0
count = 0

# - Button Click Class -
class Button(object):

    def __init__(self, position, size, color, text):

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0,0), size)

        font = pygame.font.SysFont("Algerian", 32)
        text = font.render(text, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)


#- Home Screen -
def menu(screen):
    global user
    button1 = Button((361, 503), (340, 84), (255,255,204), "")
    button2 = Button((361, 653), (340, 84), (0,255,0), "")
    button3 = Button((361, 803), (340, 84), (0,255,0), "")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if button1.is_clicked(event):   
                # go to stage2
                math(screen)
            if button2.is_clicked(event):
                # go to stage 3
                science(screen)

            if button3.is_clicked(event):
                # go to stage 3
                pygame.quit()
                exit()

        # - draws -
        
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        screen.blit(bg, (0,0) )
        screen.blit(welcome,(326, 270))
        screen.blit(mathb, (350,500) )
        screen.blit(mathb, (350,650) )
        screen.blit(mathb, (350,800) )
        
        
        
        ctext = FONT_NAME.render("Welcome", False, WHITE)
        screen.blit(ctext, (367, 280))

        usertext = FONT_NAME.render(str(user) + "!", False, WHITE)
        screen.blit(usertext,(430, 345))
        mathtext = "Math"
        mtext = FONT_NAME.render(mathtext, False, WHITE)
        screen.blit(mtext, (432, 507))
        sciencetext = "Science"
        stext = FONT_NAME.render(sciencetext, False, WHITE)
        screen.blit(stext, (400, 657))
        exittext = "Exit"
        etext = FONT_NAME.render(exittext, False, WHITE)
        screen.blit(etext, (460, 807))
        title1 = FONT_TITLE.render("League of", False, WHITE)
        title2 = FONT_TITLE.render("Learning", False, WHITE)
        screen.blit(title1, (300, 25))
        screen.blit(title2, (320, 130))
        
        
        
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)

def math(screen):

    button1 = Button((361, 303), (340, 84), (255,0,0), "")
    button2 = Button((361, 703), (340, 84), (255,0,0), "")
    button3 = Button((482, 501), (108, 108), (255,0,0), "")
    

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                addition_instructions(screen)
                
            if button2.is_clicked(event):
                similar_congruent_instructions(screen)

            if button3.is_clicked(event):
                menu(screen)

        # - draws -
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        screen.blit(bg, (0,0) )
        screen.blit(mathb, (350,300) )
        screen.blit(mathb, (350,700) )
        screen.blit(menubtn, (480,500) )
        addtext = "Speed Racer"
        atext = font.render(addtext, False, WHITE)
        screen.blit(atext, (380, 317))
        sciencetext = "SAME?"
        stext = font.render(sciencetext, False, WHITE)
        screen.blit(stext, (465, 717))
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)


def addition_instructions(screen):

    button1 = Button((84,896 ), (108, 108), (255,0,0), "")
    button2 = Button((877,896 ), (108, 108), (255,0,0), "")
    
    

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    
            if button1.is_clicked(event):
                # go to stage2
                math(screen)
            if button2.is_clicked(event):
                # go to stage2
                addition(screen)
            
            

            

        # - draws -
        button1.draw(screen)
        button2.draw(screen)
        screen.blit(bg,(0,0))
        screen.blit(instructions,(65,0))
        screen.blit(check, (875,895))
        screen.blit(close, (82, 895))
        text = "Welcome to Speed Math!"
        addinstructions = FONT_NAME.render(text, 000, WHITE)
        screen.blit(addinstructions, (100, 38))

        instructionsc= font.render("Click the correct answer as fast as ", False, WHITE)
        screen.blit(instructionsc, (90, 450))

        instructionsc1= font.render("you can! ", False, WHITE)
        screen.blit(instructionsc1, (450, 500))
        
        
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)

def fail_add_subtract(screen):
    global tries
    button1 = Button((834, 837), (100, 100), (0,255,0), "")
    button2 = Button((134, 837), (100, 100), (0,255,0), "")
    
    
    

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button2.is_clicked(event):
                
                addition_instructions(screen)

            if button1.is_clicked(event):
                menu(screen)
           
            
            

            

        # - draws -
        
        congratstext = ("You Lose!" )
        button1.draw(screen)
        button2.draw(screen)
        screen.blit(bg,(0,0))
        screen.blit(win,(115,0))
        screen.blit(score, (650, 630))
        trytext = (str(tries))
        ttext = font.render(trytext, False, WHITE)
        screen.blit(ttext, (690, 663))
        atext = font.render("Attempts", False, WHITE)
        screen.blit(atext, (400, 663))
        screen.blit(replay, (130, 836))
        screen.blit(menubtn, (830, 836))
        screen.blit(nostar, (140, 245))
        screen.blit(nostar, (380, 160))
        screen.blit(nostar, (620, 245))
        ctext = FONT_NAME.render(congratstext, False, WHITE)
        screen.blit(ctext, (370, 25))
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)






        
def addition(screen):
    global tries
    rect1 = -75
    rect2 = -80
    rect3 = -65
    rect4 = -70
    rect5 = -54
    rect6 = -63
    
    
    
    
    
 
    # - mainloop -

    clock = pygame.time.Clock()
    count = 0
    tries = 0
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            # - If right answer is clicked, new screen, and attemps += 1 -
            if button3.is_clicked(event):
                
                tries += 1
                
                mathpass1(screen)
                
                
                
                
            # - If wrong selection, count and tries are increased by 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                tries += 1
                count += 1

        # - If count ==8: GAME OVER -      
        if count == 8:
            fail_add_subtract(screen)
            
        # - draws -
        
        button1 = Button((rect1, 95 ), (108, 108), (0, 100, 250), str(31))
        button2 = Button((rect2, 260 ), (108, 108), (0, 100, 250), str(13))
        button3 = Button((rect3, 450 ), (108, 108), (0, 100, 250), str(23))
        button4 = Button((rect4, 581 ), (108, 108), (0, 100, 250), str(33))
        button5 = Button((rect5, 751 ), (108, 108), (0, 100, 250), str(21))
        button6 = Button((rect6, 891 ), (108, 108), (0, 100, 250), str(19)) 
        
        
        button7 = Button((225, 0), (150, 40), (255,0,0), "What is 12+11")
               
        # - MOVING THE RECTANGLE -   
        rect1 += 6
        if rect1 > WIDTH:
            rect1 = -70
            
            
        rect2 += 8
        if rect2 > WIDTH:
            rect2 = -70
            count += 1
            
        rect3 += 6.5
        if rect3 > WIDTH:
            rect3 = -70

        rect4 += 5
        if rect4 > WIDTH:
            rect4 = -70

        rect5 += 6
        if rect5> WIDTH:
            rect5 = -70

        rect6 += 7
        if rect6 > WIDTH:
            rect6 = -70
            
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button4.draw(screen)
        button5.draw(screen)
        button6.draw(screen)
        screen.blit(bg, (0,0))

        # - OVERLAYING THE RECTANGLE WITH IMAGES -
        screen.blit(question, (0,10))
        screen.blit(ship1, (rect1 -7,94))
        screen.blit(ship2, (rect2 -7,259))
        screen.blit(ship3, (rect3 -7,449))
        screen.blit(ship4, (rect4 -7,580))
        screen.blit(ship5, (rect5 -7,750))
        screen.blit(ship6, (rect6 -7,890))
        counttext = ("Counter: " + str(count))
        ctext = font.render(counttext, False, WHITE)
        screen.blit(ctext, (70, 26))
        
        rect1text = str(31)
        r1text = font.render(rect1text, False, WHITE)
        screen.blit(r1text, (rect1+108, 84))

        rect2text = str(13)
        r2text = font.render(rect2text, False, WHITE)
        screen.blit(r2text, (rect2+108, 290))

        rect3text = str(23)
        r3text = font.render(rect3text, False, WHITE)
        screen.blit(r3text, (rect3+108, 480))

        rect4text = str(33)
        r4text = font.render(rect4text, False, WHITE)
        screen.blit(r4text, (rect4+108, 611))

        rect5text = str(21)
        r5text = font.render(rect5text, False, WHITE)
        screen.blit(r5text, (rect5+108, 781))

        rect6text = str(33)
        r6text = font.render(rect6text, False, WHITE)
        screen.blit(r6text, (rect6+108, 921))
        
        trytext = ("Attempts " + str(tries))
        ttext = font.render(trytext, False, WHITE)
        screen.blit(ttext, (760, 27))
        

        questiontext = ("What is 12+11")
        qtext = font.render(questiontext, False, WHITE)
        screen.blit(qtext, (380, 27))
        pygame.display.flip()
        
        # - FPS -

        clock.tick(FPS)

def mathpass1(screen):
    
    global tries
    global count
    
    button1 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button2 = Button((134, 837), (100, 100), (0,255,0), "Back")
    button3 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button4 = Button((134, 837), (100, 100), (0,255,0), "Back")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                addition2(screen)
                
            if button2.is_clicked(event):
                addition(screen)

            if button4.is_clicked(event):
                
                addition_instructions(screen)

            if button3.is_clicked(event):
                menu(screen)

        # - If completed on first attempt with the count still being less then 8 -
        
        if tries ==1 and count <8:
            congratstext = ("Congrats!" )
            button2.draw(screen)
            button1.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))

            
            
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(goldstar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()   
            
        
        # - If completed on 2nd attempt with the count still being less then 8 -
        
        if tries ==2 and count <8:
            congratstext = ("Congrats!" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()

        # - If completed on 3rd attempt with the count still being less then 8 -
        
        if tries ==3 and count <8:
            congratstext = ("Congrats!" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()

        # - Game over -
        
        if tries>3:
            congratstext = ("You Lose!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(nostar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()
        # - FPS -

        clock.tick(FPS)


def addition2(screen):
    
    global tries

    rect1 = -75
    rect2 = -80
    rect3 = -65
    rect4 = -70
    rect5 = -54
    rect6 = -63
    
    
    
    
    
    
    
 

    # - mainloop -

    clock = pygame.time.Clock()
    count = 0
    tries = 0
    running = True
    
    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button5.is_clicked(event):
                tries += 1
                
                mathpass2(screen)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                count += 1
                tries += 1
                
        if count ==6:
            fail_add_subtract(screen)
    
        # - draws -
        

        screen.fill((128,128,128))
        
    
        
       
        rect1 += 8
        if rect1 > WIDTH:
            rect1 = -70
            
            
        rect2 += 10
        if rect2 > WIDTH:
            rect2 = -70
            
            
        rect3 += 8
        if rect3 > WIDTH:
            rect3 = -70

        rect4 += 9
        if rect4 > WIDTH:
            rect4 = -70

        rect5 += 11
        if rect5> WIDTH:
            rect5 = -70
            count += 1

        rect6 += 9.5
        if rect6 > WIDTH:
            rect6 = -70
            
        
        button1 = Button((rect1, 95 ), (108, 108), (0, 100, 250), str(31))
        button2 = Button((rect2, 260 ), (108, 108), (0, 100, 250), str(13))
        button3 = Button((rect3, 450 ), (108, 108), (0, 100, 250), str(23))
        button4 = Button((rect4, 581 ), (108, 108), (0, 100, 250), str(33))
        button5 = Button((rect5, 751 ), (108, 108), (0, 100, 250), str(21))
        button6 = Button((rect6, 891 ), (108, 108), (0, 100, 250), str(19))        
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button4.draw(screen)
        button5.draw(screen)
        button6.draw(screen)
        screen.blit(bg, (0,0))
        
        screen.blit(question, (0,10))
        screen.blit(ship1, (rect1 -7,94))
        screen.blit(ship2, (rect2 -7,259))
        screen.blit(ship3, (rect3 -7,449))
        screen.blit(ship4, (rect4 -7,580))
        screen.blit(ship5, (rect5 -7,750))
        screen.blit(ship6, (rect6 -7,890))
        
        counttext = ("Counter: " + str(count))
        ctext = font.render(counttext, False, WHITE)
        screen.blit(ctext, (70, 26))
        
        rect1text = str(75)
        r1text = font.render(rect1text, False, WHITE)
        screen.blit(r1text, (rect1+108, 125))

        rect2text = str(85)
        r2text = font.render(rect2text, False, WHITE)
        screen.blit(r2text, (rect2+108, 290))

        rect3text = str(100)
        r3text = font.render(rect3text, False, WHITE)
        screen.blit(r3text, (rect3+108, 480))

        rect4text = str(91)
        r4text = font.render(rect4text, False, WHITE)
        screen.blit(r4text, (rect4+108, 611))

        rect5text = str(101)
        r5text = font.render(rect5text, False, WHITE)
        screen.blit(r5text, (rect5+108, 781))

        rect6text = str(95)
        r6text = font.render(rect6text, False, WHITE)
        screen.blit(r6text, (rect6+108, 921))
        
        trytext = ("Attempts " + str(tries))
        ttext = font.render(trytext, False, WHITE)
        screen.blit(ttext, (760, 27))
        

        questiontext = ("What is 34+67")
        qtext = font.render(questiontext, False, WHITE)
        screen.blit(qtext, (380, 27))
        pygame.display.flip()
        
        # - FPS -

        clock.tick(FPS)

def mathpass2(screen):
    global tries
    global count
    
    button1 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button2 = Button((134, 837), (100, 100), (0,255,0), "Back")
    button3 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button4 = Button((134, 837), (100, 100), (0,255,0), "Back")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                addition3(screen)
                
            if button2.is_clicked(event):
                addition2(screen)

            if button4.is_clicked(event):
                # go to stage2
                addition_instructions(screen)

            if button3.is_clicked(event):
                menu(screen)

            
        if tries ==1 and count <8:
            congratstext = ("Congrats!" )
            button2.draw(screen)
            button1.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))

            
            
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(goldstar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()   
            
        

        if tries ==2 and count <8:
            congratstext = ("Congrats!" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()

        if tries ==3 and count <8:
            congratstext = ("Congrats!" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()
        
        if tries>3:
            congratstext = ("You Lose!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(nostar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()
        # - FPS -

        clock.tick(FPS)

def addition3(screen):
    global tries
    

    rect1 = -75
    rect2 = -80
    rect3 = -65
    rect4 = -70
    rect5 = -54
    rect6 = -63
    
    
    
    
 

    # - mainloop -

    clock = pygame.time.Clock()
    count = 0
    tries = 0
    running = True
    
    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                
                tries +=1
                mathpass3(screen)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                count += 1
                tries += 1

        if count ==4:
            fail_add_subtract(screen)
    
        # - draws -
        

        screen.fill((128,128,128))
        
    
        
       
        rect1 += 12.5
        if rect1 > WIDTH:
            rect1 = -70
            
            
        rect2 += 11
        if rect2 > WIDTH:
            rect2 = -70

        rect3 += 13
        if rect3 > WIDTH:
            rect3 = -70

        rect4 += 12
        if rect4 > WIDTH:
            rect4 = -70

        rect5 += 14
        if rect5 > WIDTH:
            rect5 = -70
            count += 1

        rect6 += 11.5
        if rect6 > WIDTH:
            rect6 = -70
            
        button7 = Button((225, 0), (150, 40), (255,0,0), "What is 96-79")
        button1 = Button((rect1, 95 ), (108, 108), (0, 100, 250), str(31))
        button2 = Button((rect2, 260 ), (108, 108), (0, 100, 250), str(13))
        button3 = Button((rect3, 450 ), (108, 108), (0, 100, 250), str(23))
        button4 = Button((rect4, 581 ), (108, 108), (0, 100, 250), str(33))
        button5 = Button((rect5, 751 ), (108, 108), (0, 100, 250), str(21))
        button6 = Button((rect6, 891 ), (108, 108), (0, 100, 250), str(19)) 
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button4.draw(screen)
        button5.draw(screen)
        button6.draw(screen)
        button7.draw(screen)
        screen.blit(bg, (0,0))
        
        screen.blit(question, (0,10))
        screen.blit(ship1, (rect1 -7,94))
        screen.blit(ship2, (rect2 -7,259))
        screen.blit(ship3, (rect3 -7,449))
        screen.blit(ship4, (rect4 -7,580))
        screen.blit(ship5, (rect5 -7,750))
        screen.blit(ship6, (rect6 -7,890))
        counttext = ("Counter: " + str(count))
        ctext = font.render(counttext, False, WHITE)
        screen.blit(ctext, (70, 26))
        
        rect1text = str(17)
        r1text = font.render(rect1text, False, WHITE)
        screen.blit(r1text, (rect1+108, 125))

        rect2text = str(15)
        r2text = font.render(rect2text, False, WHITE)
        screen.blit(r2text, (rect2+108, 290))

        rect3text = str(11)
        r3text = font.render(rect3text, False, WHITE)
        screen.blit(r3text, (rect3+108, 480))

        rect4text = str(13)
        r4text = font.render(rect4text, False, WHITE)
        screen.blit(r4text, (rect4+108, 611))

        rect5text = str(18)
        r5text = font.render(rect5text, False, WHITE)
        screen.blit(r5text, (rect5+108, 781))

        rect6text = str(12)
        r6text = font.render(rect6text, False, WHITE)
        screen.blit(r6text, (rect6+108, 921))
        
        trytext = ("Attempts " + str(tries))
        ttext = font.render(trytext, False, WHITE)
        screen.blit(ttext, (760, 27))
        

        questiontext = ("What is 96-79")
        qtext = font.render(questiontext, False, WHITE)
        screen.blit(qtext, (380, 27))
        pygame.display.flip()
        
        # - FPS -

        clock.tick(FPS)

def mathpass3(screen):
    global tries
    global count
    
    button1 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button2 = Button((134, 837), (100, 100), (0,255,0), "Back")
    button3 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button4 = Button((134, 837), (100, 100), (0,255,0), "Back")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                addition4(screen)
                
            if button2.is_clicked(event):
                addition3(screen)

            if button4.is_clicked(event):
                # go to stage2
                addition_instructions(screen)

            if button3.is_clicked(event):
                menu(screen)

            
        if tries ==1 and count <8:
            congratstext = ("Congrats:" )
            button2.draw(screen)
            button1.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            level2text = FONT_NAME.render("Level 2", False, WHITE)
            screen.blit(level2text, (600, 25))
            
            
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(goldstar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (150, 25))
            pygame.display.flip()   
            
        

        if tries ==2 and count <8:
            congratstext = ("Congrats!" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(nostar, (620, 245))
            level2text = FONT_NAME.render("Level 2", False, WHITE)
            screen.blit(level2text, (600, 25))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (150, 25))
            pygame.display.flip()

        if tries ==3 and count <8:
            congratstext = ("Congrats!" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            level2text = FONT_NAME.render("Level 2", False, WHITE)
            screen.blit(level2text, (600, 25))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (150, 25))
            pygame.display.flip()
        
        if tries>3:
            congratstext = ("You Lose!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(nostar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()
        # - FPS -

        clock.tick(FPS)


def addition4(screen):
    
    global tries

    rect1 = -75
    rect2 = -80
    rect3 = -65
    rect4 = -70
    rect5 = -54
    rect6 = -63
    
    
    # - mainloop -

    clock = pygame.time.Clock()
    count = 0
    tries = 0
    running = True
    
    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button6.is_clicked(event):
                #gj.play()
                tries += 1
                mathpass4(screen)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                count += 1
                tries += 1
        if count ==2:
            fail_add_subtract(screen)
    
        # - draws -
        

        screen.fill((128,128,128))
        
    
        
       
        rect1 += 17
        if rect1 > WIDTH:
            rect1 = -70
            count += 1
            
        rect2 += 15
        if rect2 > WIDTH:
            rect2 = -70

        rect3 += 16.5
        if rect3 > WIDTH:
            rect3 = -70

        rect4 += 14
        if rect4 > WIDTH:
            rect4 = -70

        rect5 += 16
        if rect5> WIDTH:
            rect5 = -70

        rect6 += 14
        if rect6 > WIDTH:
            rect6 = -70
            
        button7 = Button((225, 0), (250, 40), (255,0,0), "")
        button1 = Button((rect1, 95 ), (108, 108), (0, 100, 250), str(31))
        button2 = Button((rect2, 260 ), (108, 108), (0, 100, 250), str(13))
        button3 = Button((rect3, 450 ), (108, 108), (0, 100, 250), str(23))
        button4 = Button((rect4, 581 ), (108, 108), (0, 100, 250), str(33))
        button5 = Button((rect5, 751 ), (108, 108), (0, 100, 250), str(21))
        button6 = Button((rect6, 891 ), (108, 108), (0, 100, 250), str(19)) 
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button4.draw(screen)
        button5.draw(screen)
        button6.draw(screen)
        button7.draw(screen)
        screen.blit(bg, (0,0))
        
        screen.blit(question, (0,10))
        screen.blit(ship1, (rect1 -7,94))
        screen.blit(ship2, (rect2 -7,259))
        screen.blit(ship3, (rect3 -7,449))
        screen.blit(ship4, (rect4 -7,580))
        screen.blit(ship5, (rect5 -7,750))
        screen.blit(ship6, (rect6 -7,890))
        counttext = ("Counter: " + str(count))
        ctext = font.render(counttext, False, WHITE)
        screen.blit(ctext, (70, 26))
        
        rect1text = str(286)
        r1text = font.render(rect1text, False, WHITE)
        screen.blit(r1text, (rect1+108, 125))

        rect2text = str(390)
        r2text = font.render(rect2text, False, WHITE)
        screen.blit(r2text, (rect2+108, 290))

        rect3text = str(486)
        r3text = font.render(rect3text, False, WHITE)
        screen.blit(r3text, (rect3+108, 480))

        rect4text = str(396)
        r4text = font.render(rect4text, False, WHITE)
        screen.blit(r4text, (rect4+108, 611))

        rect5text = str(400)
        r5text = font.render(rect5text, False, WHITE)
        screen.blit(r5text, (rect5+108, 781))

        rect6text = str(369)
        r6text = font.render(rect6text, False, WHITE)
        screen.blit(r6text, (rect6+108, 921))
        
        trytext = ("Attempts " + str(tries))
        ttext = font.render(trytext, False, WHITE)
        screen.blit(ttext, (760, 27))
        

        questiontext = ("What is 123+246")
        qtext = sfont.render(questiontext, False, WHITE)
        screen.blit(qtext, (384, 27))
        pygame.display.flip()
        
        # - FPS -

        clock.tick(FPS)

def mathpass4(screen):
    
    global tries
    global count
    
    button1 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button2 = Button((134, 837), (100, 100), (0,255,0), "Back")
    button3 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button4 = Button((134, 837), (100, 100), (0,255,0), "Back")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                addition5(screen)
                
            if button2.is_clicked(event):
                addition4(screen)

            if button4.is_clicked(event):
                # go to stage2
                addition_instructions(screen)

            if button3.is_clicked(event):
                menu(screen)

            
        if tries ==1 and count <8:
            congratstext = ("Congrats!" )
            button2.draw(screen)
            button1.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))

            
            
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(goldstar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()   
            
        

        if tries ==2 and count <8:
            congratstext = ("Congrats!" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()

        if tries ==3 and count <8:
            congratstext = ("Congrats!" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()
        
        if tries>3:
            congratstext = ("You Lose!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(nostar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()
        # - FPS -

        clock.tick(FPS)

def addition5(screen):
    
    
    global tries
    rect1 = -75
    rect2 = -80
    rect3 = -65
    rect4 = -70
    rect5 = -54
    rect6 = -63
    
    
    # - mainloop -

    clock = pygame.time.Clock()
    count = 0
    tries = 0
    running = True
    
    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button4.is_clicked(event):
                #gj.play()
                tries +=1
                win_add_subtract(screen)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                count += 1
                tries += 1
        if count ==1:
            fail_add_subtract(screen)
    
        # - draws -
        

        screen.fill((128,128,128))
        
    
        
       
        rect1 += 17.5
        if rect1 > WIDTH:
            rect1 = -70
            count += 1
            
        rect2 += 19
        if rect2 > WIDTH:
            rect2 = -70

        rect3 += 18
        if rect3 > WIDTH:
            rect3 = -70

        rect4 += 20
        if rect4 > WIDTH:
            rect4 = -70

        rect5 += 17
        if rect5> WIDTH:
            rect5 = -70

        rect6 += 18.5
        if rect6 > WIDTH:
            rect6 = -70
            
        button7 = Button((225, 0), (200, 40), (255,0,0), "")
        button1 = Button((rect1, 95 ), (108, 108), (0, 100, 250), str(31))
        button2 = Button((rect2, 260 ), (108, 108), (0, 100, 250), str(13))
        button3 = Button((rect3, 450 ), (108, 108), (0, 100, 250), str(23))
        button4 = Button((rect4, 581 ), (108, 108), (0, 100, 250), str(33))
        button5 = Button((rect5, 751 ), (108, 108), (0, 100, 250), str(21))
        button6 = Button((rect6, 891 ), (108, 108), (0, 100, 250), str(19)) 
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button4.draw(screen)
        button5.draw(screen)
        button6.draw(screen)
        button7.draw(screen)
        screen.blit(bg, (0,0))
        
        screen.blit(question, (0,10))
        screen.blit(ship1, (rect1 -7,94))
        screen.blit(ship2, (rect2 -7,259))
        screen.blit(ship3, (rect3 -7,449))
        screen.blit(ship4, (rect4 -7,580))
        screen.blit(ship5, (rect5 -7,750))
        screen.blit(ship6, (rect6 -7,890))
        counttext = ("Counter: " + str(count))
        ctext = font.render(counttext, False, WHITE)
        screen.blit(ctext, (70, 26))
        
        rect1text = str(46)
        r1text = font.render(rect1text, False, WHITE)
        screen.blit(r1text, (rect1+108, 125))

        rect2text = str(69)
        r2text = font.render(rect2text, False, WHITE)
        screen.blit(r2text, (rect2+108, 290))

        rect3text = str(65)
        r3text = font.render(rect3text, False, WHITE)
        screen.blit(r3text, (rect3+108, 480))

        rect4text = str(59)
        r4text = font.render(rect4text, False, WHITE)
        screen.blit(r4text, (rect4+108, 611))

        rect5text = str(55)
        r5text = font.render(rect5text, False, WHITE)
        screen.blit(r5text, (rect5+108, 781))

        rect6text = str(49)
        r6text = font.render(rect6text, False, WHITE)
        screen.blit(r6text, (rect6+108, 921))
        
        trytext = ("Attempts " + str(tries))
        ttext = font.render(trytext, False, WHITE)
        screen.blit(ttext, (760, 27))
        
        
        questiontext = ("What is 453-394")
        qtext = sfont.render(questiontext, False, WHITE)
        screen.blit(qtext, (384, 27))
        pygame.display.flip()
        
        # - FPS -

        clock.tick(FPS)
        
def win_add_subtract(screen):
    
    global tries
    global count
    
    
    button3 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button4 = Button((134, 837), (100, 100), (0,255,0), "Back")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            

            if button4.is_clicked(event):
                
                addition_instructions(screen)

            if button3.is_clicked(event):
                menu(screen)

            
        if tries ==1 and count <8:
            congratstext = ("You Win!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))

            
            
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(goldstar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()   
            
        

        if tries ==2 and count <8:
            congratstext = ("You Win!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()

        if tries ==3 and count <8:
            congratstext = ("You Win!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()
        
        if tries>3:
            congratstext = ("You Lose!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(nostar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()
        # - FPS -

        clock.tick(FPS)
        


def similar_congruent_instructions(screen):

    button1 = Button((84,896 ), (108, 108), (255,0,0), "")
    button2 = Button((877,896 ), (108, 108), (255,0,0), "")
    
    

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    
            if button1.is_clicked(event):
                # go to stage2
                math(screen)
            if button2.is_clicked(event):
                # go to stage2
                similar_congruent(screen)
            
            

            

        # - draws -
        button1.draw(screen)
        button2.draw(screen)
        screen.blit(bg,(0,0))
        screen.blit(instructions,(65,0))
        screen.blit(check, (875,895))
        screen.blit(close, (82, 895))
        text = "Welcome to Same?"
        addinstructions = FONT_NAME.render(text, 000, WHITE)
        screen.blit(addinstructions, (170, 38))

        instructions1 = font.render("Using the right mouse button, scale", 000, WHITE)
        screen.blit(instructions1, (95, 400))

        instructionsc= font.render("the rectangles to make them either", False, WHITE)
        screen.blit(instructionsc, (95, 450))

        instructionsc2= font.render("similar or congruent", False, WHITE)
        screen.blit(instructionsc2, (250, 500))
        
        
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)
        
def similar_congruent(screen):
    
    
    global selected_rect
    global tries
    
    
    button1 = Button((142, 25), (48, 48), (255,0,0), "Done")
    
    rect7 = pygame.Rect(100, 300, 160, 100)
    
    rect8 = pygame.Rect(600, 300, 350, 500)
        
    # - mainloop -
    
    clock = pygame.time.Clock()
    tries = 0
    
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect in (rect7,):
                    if rect.collidepoint(event.pos):
                        selected_rect = rect  # Select the colliding rect.
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_rect = None  # De-select the rect.
                
            elif event.type == pygame.MOUSEMOTION:
                if selected_rect is not None:  # If a rect is selected.
                    if not event.buttons[0]:  # Right or middle mouse button.
                        # Scale the rect.
                        selected_rect.w += event.rel[0]
                        selected_rect.h += event.rel[1]
                        selected_rect.w = max(selected_rect.w, 10)
                        selected_rect.h = max(selected_rect.h, 10)
            
            # If correct, tries +=1 and new screen
            if button1.is_clicked(event):
                if rect7[2] == rect8[2] and rect7[3] == rect8[3]:
                    
                        tries +=1
                        
                        similar_congruentpass(screen)

                # If wrong, tries increased by 1
                if  not rect7[2] == rect8[2] and not rect7[3] == rect8[3]:
                    tries +=1
                    

        # If more than 3 tries, GAME OVER
        
        if tries>3:
            fail_congruency(screen)
            
        
        # - draws -
        
        screen.blit(bg, (0,0))
            
        button1.draw(screen)
        
        widthtext1 = str(rect7[2])
        wtext1 = sfont.render(widthtext1, False, WHITE)
        screen.blit(wtext1, ((rect7[0]+(rect7[2]/2)-15, 255)))

        heighttext1 = str(rect7[3])
        htext1 = sfont.render(heighttext1, False, WHITE)
        screen.blit(htext1, (32, (rect7[1]+(rect7[3]/2))))


        widthtext2 = str(rect8[2])
        wtext2 = sfont.render(widthtext2, False, WHITE)
        screen.blit(wtext2, (725, 255))

        heighttext2 = str(rect8[3])
        htext2 = sfont.render(heighttext2, False, WHITE)
        screen.blit(htext2, (530, (550)))

        
        
        screen.blit(question, (0,10))
        questiontext = ("Congruent")
        qtext = font.render(questiontext, False, WHITE)
        screen.blit(qtext, (420, 27))
        
        trytext = ("Attempts:" + str(tries))
        ttext = font.render(trytext, False, WHITE)
        screen.blit(ttext, (760, 27))

        screen.blit(play, (140,25))
        
        pygame.draw.rect(screen, (0, 200, 120), rect8)
        pygame.draw.rect(screen, (0, 51, 102), rect7)
        
        
        
        
        
        
        
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)
        
def fail_congruency(screen):

    button2 = Button((834, 837), (100, 100), (0,255,0), "mENU")
    button1 = Button((134, 837), (100, 100), (0,255,0), "M")
    
    

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                
                similar_congruent_instructions(screen)

            if button2.is_clicked(event):
                
                menu(screen)
           
            
            

            

        # - draws -
        
        if tries>3:
            congratstext = ("You LoseR!" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(nostar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()

        # - FPS -

        clock.tick(FPS)

def similar_congruentpass(screen):
    global tries
    
    
    button1 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button2 = Button((134, 837), (100, 100), (0,255,0), "Back")
    
    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                similar_congruent2(screen)
                
            if button2.is_clicked(event):
                similar_congruent(screen)

            

            
        if tries ==1 :
            congratstext = ("Congrats:" )
            button2.draw(screen)
            button1.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))

            
            
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(goldstar, (620, 245))
            level2text = FONT_NAME.render("Level 2", False, WHITE)
            screen.blit(level2text, (600, 25))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (150, 25))
            pygame.display.flip()   
            
        

        if tries ==2 :
            congratstext = ("Congrats:" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(nostar, (620, 245))
            level2text = FONT_NAME.render("Level 2", False, WHITE)
            screen.blit(level2text, (600, 25))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (150, 25))
            pygame.display.flip()

        if tries ==3:
            congratstext = ("Congrats:" )
            button1.draw(screen)
            button2.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            level2text = FONT_NAME.render("Level 2", False, WHITE)
            screen.blit(level2text, (600, 25))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (150, 25))
            pygame.display.flip()
        
        
        # - FPS -

    clock.tick(FPS)



def similar_congruent2(screen):
    
    
    global selected_rect
    global tries
    
    
    button1 = Button((142, 25), (48, 48), (255,0,0), "Done")
    
    rect7 = pygame.Rect(100, 300, 160, 100)
    
    rect8 = pygame.Rect(700, 300, 150, 210)
        
    # - mainloop -
    
    clock = pygame.time.Clock()
    tries = 0
    
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect in (rect7,):
                    if rect.collidepoint(event.pos):
                        selected_rect = rect  # Select the colliding rect.
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_rect = None  # De-select the rect.
                
            elif event.type == pygame.MOUSEMOTION:
                if selected_rect is not None:  # If a rect is selected.
                    if not event.buttons[0]:  # Right or middle mouse button.
                        # Scale the rect.
                        selected_rect.w += event.rel[0]
                        selected_rect.h += event.rel[1]
                        selected_rect.w = max(selected_rect.w, 10)
                        selected_rect.h = max(selected_rect.h, 10)
            
            
            if button1.is_clicked(event):
                # For rectangles to be similar width of rect1 divided by width of rect2 == rect1 height divded by rect 2 height
                if rect7[2] != rect8[2] and rect7[3] !=rect8[3]:
                    if (rect7[2]/rect8[2]) == (rect7[3]/rect8[3]):
                        tries +=1
                        
                        similar_congruentpass2(screen)


                if  not rect7[2] == rect8[2] and not rect7[3] == rect8[3]:
                    tries +=1
                    

            
        if tries>3:
            fail_congruency(screen)
            
        
        # - draws -
        
        screen.blit(bg, (0,0))
            
        button1.draw(screen)
        
        widthtext1 = str(rect7[2])
        wtext1 = sfont.render(widthtext1, False, WHITE)
        screen.blit(wtext1, ((rect7[0]+(rect7[2]/2)-15, 255)))

        heighttext1 = str(rect7[3])
        htext1 = sfont.render(heighttext1, False, WHITE)
        screen.blit(htext1, (32, (rect7[1]+(rect7[3]/2))))


        widthtext2 = str(rect8[2])
        wtext2 = sfont.render(widthtext2, False, WHITE)
        screen.blit(wtext2, ((rect8[0]+(rect8[2]/2)-25, 255)))

        heighttext2 = str(rect8[3])
        htext2 = sfont.render(heighttext2, False, WHITE)
        screen.blit(htext2, (637, (rect8[1]+(rect8[3]/2))))

        
        
        screen.blit(question, (0,10))
        questiontext = ("Similar")
        qtext = font.render(questiontext, False, WHITE)
        screen.blit(qtext, (450, 27))
        
        trytext = ("Attempts:" + str(tries))
        ttext = font.render(trytext, False, WHITE)
        screen.blit(ttext, (760, 27))

        screen.blit(play, (140,25))
        
        pygame.draw.rect(screen, (0, 200, 120), rect8)
        pygame.draw.rect(screen, (0, 51, 102), rect7)
        
        
        
        
        
        
        
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)
        
        
        
        
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)

def similar_congruentpass2(screen):
    
    button3 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button4 = Button((134, 837), (100, 100), (0,255,0), "Back")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            

            if button4.is_clicked(event):
                # go to stage2
                similar_congruent_instructions(screen)

            if button3.is_clicked(event):
                menu(screen)

            
        if tries ==1:
            congratstext = ("You Win!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.blit(bg, (0,0))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))

            
            
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(goldstar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()   
            
        

        if tries ==2 :
            congratstext = ("You Win!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()

        if tries ==3:
            congratstext = ("You Win!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.fill((128,128,128))
            screen.blit(win,(115,0))
            screen.blit(score, (650, 630))
            trytext = (str(tries))
            ttext = font.render(trytext, False, WHITE)
            screen.blit(ttext, (690, 663))
            atext = font.render("Attempts", False, WHITE)
            screen.blit(atext, (400, 663))
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(nostar, (380, 160))
            screen.blit(nostar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()
        
        
        # - FPS -

    clock.tick(FPS)
        
def science(screen):
    
    button1 = Button((361, 303), (340, 84), (255,0,0), "")
    button2 = Button((361, 703), (340, 84), (255,0,0), "")
    button3 = Button((482, 501), (108, 108), (255,0,0), "")
    

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                animals_instructions(screen)
                
            if button2.is_clicked(event):
                cells_instructions(screen)

            if button3.is_clicked(event):
                menu(screen)

        # - draws -
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        screen.blit(sciencebg, (0,0) )
        screen.blit(mathb, (350,300) )
        screen.blit(mathb, (350,700) )
        screen.blit(menubtn, (480,500) )
        addtext = "Animals"
        atext = font.render(addtext, False, WHITE)
        screen.blit(atext, (430, 317))
        sciencetext = "Cells"
        stext = font.render(sciencetext, False, WHITE)
        screen.blit(stext, (465, 717))
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)
        # - FPS -

        clock.tick(FPS)

def animals_instructions(screen):
    
    button1 = Button((84,896 ), (108, 108), (255,0,0), "")
    button2 = Button((877,896 ), (108, 108), (255,0,0), "")
    
    

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    
            if button1.is_clicked(event):
                
                science(screen)
            if button2.is_clicked(event):
            
                matching(screen)
            
            

            

        # - draws -
        button1.draw(screen)
        button2.draw(screen)
        screen.blit(animalsbg,(0,0))
        screen.blit(instructions,(65,0))
        screen.blit(check, (875,895))
        screen.blit(close, (82, 895))
        text = "Welcome to Animals!"
        addinstructions = FONT_NAME.render(text, 000, WHITE)
        screen.blit(addinstructions, (150, 38))


        level1 = font.render("Level 1:", 000, WHITE)
        screen.blit(level1, (415, 300))

        level_1_text = font.render("Match the animal to its corresponding", False, WHITE)
        screen.blit(level_1_text, (80, 350))
        level_1_textc = font.render("name", False, WHITE)
        screen.blit(level_1_textc, (425, 395))

        level2 = font.render("Level 2:", 000, WHITE)
        screen.blit(level2, (415, 500))

        level_2_text = font.render("Order the animals in terms of the", False, WHITE)
        screen.blit(level_2_text, (100, 550))
        level_2_textc = font.render("foodchain", False, WHITE)
        screen.blit(level_2_textc, (415, 595))
        
        
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)

def matching(screen):
    
    
    global selected_rect
    # - mainloop -
    button1 = Button((88,25 ), (115, 75), (34,139,34), "OWL")
    button2 = Button((188,325 ), (115, 75), (34,139,34), "DOG")
    button3 = Button((88,655 ), (115, 75), (34,139,34), "PIG")
    button4 = Button((368,575 ), (115, 75), (34,139,34), "CHICK")
    button5 = Button((488,125 ), (115, 75), (34,139,34), "PANDA")
    
    #Move
    rect12 = pygame.Rect(900, 100, 75, 75)
    rect10 = pygame.Rect(900, 200, 95, 100)
    rect14 = pygame.Rect(900, 300, 75, 75)
    rect16 = pygame.Rect(900, 400, 75, 75)
    rect18 = pygame.Rect(900, 500, 75, 75)
    
    #Not Move
    rect9 = pygame.Rect(100, 100, 75, 75)
    rect11 = pygame.Rect(200, 400, 75, 75)
    rect13 = pygame.Rect(100, 730, 75, 75)
    rect15 = pygame.Rect(380, 650, 75, 75)
    rect17 = pygame.Rect(500, 200, 75, 75)
    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect in (rect10, rect12, rect14, rect16, rect18 ):
                    if rect.collidepoint(event.pos):
                        selected_rect = rect  # Select the colliding rect.
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_rect = None  # De-select the rect.
            elif event.type == pygame.MOUSEMOTION:
                if selected_rect is not None:  # If a rect is selected.
                    if event.buttons[0]:  # Left mouse button is down.
                        # Move the rect.
                        selected_rect.x += event.rel[0]
                        
                        
                            
                        selected_rect.y += event.rel[1]
        
            if 100<rect10[0]<175  and 100<rect10[1]<175 :
                        rect10[0] = 100
                        rect10[1] = 100
                        if event.type == pygame.MOUSEMOTION:
                            selected_rect = None
     

            if 200<rect12[0]<275  and 400<rect12[1]<475:
                    rect12[0] = 200
                    rect12[1] = 400
                    if event.type == pygame.MOUSEMOTION:
                        selected_rect = None
                        

            if 100<rect14[0]<175  and 730<rect14[1]<805 :
                        rect14[0] = 100
                        rect14[1] = 730
                        if event.type == pygame.MOUSEMOTION:
                            selected_rect = None
                            
            if 380<rect16[0]<455  and 650<rect16[1]<725 :
                        rect16[0] = 380
                        rect16[1] = 650
                        if event.type == pygame.MOUSEMOTION:
                            selected_rect = None

            if 500<rect18[0]<575  and 200<rect18[1]<275 :
                        rect18[0] = 500
                        rect18[1] = 200
                        if event.type == pygame.MOUSEMOTION:
                            selected_rect = None
            

            # If all images are in correct positon, new screen
            if rect10[0] == 100 and rect10[1] == 100 and rect12[0] == 200 and rect12[1] == 400 and rect14[0] ==100 and rect14[1] == 730 and rect16[0] ==380 and rect16[1]==650 and rect18[0] ==500 and rect18[1]==200 :
                matchingpass(screen)
                

            screen.blit(animalsbg, (0,0))
            
            
            screen.blit(owl, (rect10[0], rect10[1]))
            screen.blit(dog, (rect12[0], rect12[1]))
            screen.blit(pig, (rect14[0], rect14[1]))
            screen.blit(chick, (rect16[0], rect16[1]))
            screen.blit(panda, (rect18[0], rect18[1]))
            
            
            
            
            
            
           
            button1.draw(screen)
            button2.draw(screen)
            button3.draw(screen)
            button4.draw(screen)
            button5.draw(screen)
            pygame.display.flip()


        # - FPS -

        clock.tick(FPS)


def matchingpass(screen):
    global tries
    
    
    button1 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button2 = Button((134, 837), (100, 100), (0,255,0), "Back")
    
    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                food_chain(screen)
                
            if button2.is_clicked(event):
                matching(screen)

            

            congratstext = ("Congrats:" )
            button2.draw(screen)
            button1.draw(screen)
            screen.blit(animalsbg, (0,0))
            screen.blit(win,(115,0))
           

            
            

            
        
            screen.blit(back, (130, 836))
            screen.blit(cont, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(goldstar, (620, 245))
            level2text = FONT_NAME.render("Level 2", False, WHITE)
            screen.blit(level2text, (600, 25))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (150, 25))
            pygame.display.flip()   
            
        

      
        
        
        # - FPS -

    clock.tick(FPS)

def food_chain(screen):
    
    
    global selected_rect
    # - mainloop -
    button1 = Button((0,325 ), (245, 75), (34,139,34), "Producer")
    button2 = Button((262,325 ), (250, 75), (34,139,34), "Primary")
    button3 = Button((530,325 ), (250, 75), (34,139,34), "Secondary")
    button4 = Button((800,325 ), (280, 75), (34,139,34), "Tertiary")
    
    
    #Move
    rect12 = pygame.Rect(700, 100, 154, 150)
    rect10 = pygame.Rect(100, 100, 160, 190)
    rect14 = pygame.Rect(300, 100, 154, 150)
    rect16 = pygame.Rect(500, 100, 163, 67)

    
    
    
    #Not Move
    
    
    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect in (rect10, rect12, rect14, rect16,):
                    if rect.collidepoint(event.pos):
                        selected_rect = rect  # Select the colliding rect.
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_rect = None  # De-select the rect.
            elif event.type == pygame.MOUSEMOTION:
                if selected_rect is not None:  # If a rect is selected.
                    if event.buttons[0]:  # Left mouse button is down.
                        # Move the rect.
                        selected_rect.x += event.rel[0]
                        
                        
                            
                        selected_rect.y += event.rel[1]
        
            if 810<rect10[0]<1080  and 400<rect10[1]<1000 :
                        rect10[0] = 850
                        rect10[1] = 630
                        
     

            if 540<rect12[0]<790  and 400<rect12[1]<1000:
                    rect12[0] = 580
                    rect12[1] = 630
                

            if 270<rect14[0]<520  and 400<rect14[1]<1000 :
                        rect14[0] = 310
                        rect14[1] = 630
                        
                        

            if 0<rect16[0]<250  and 400<rect16[1]<1000 :
                        rect16[0] = 40
                        rect16[1] = 650
                        
                            
            

            
            

            
            if rect10[0] == 850 and rect10[1] == 630 and rect12[0] == 580 and rect12[1] == 630 and rect14[0] ==310 and rect14[1] == 630 and rect16[0] ==40 and rect16[1]==650 :
                food_chainpass(screen)
                

            screen.blit(animalsbg, (0,0))
            
            
            
            
            
            
            pygame.draw.line(screen, (204, 229, 255), (250, 400), (250, 1000), 20)

            pygame.draw.line(screen, (204, 229, 255), (520, 400), (520, 1000), 20)

            pygame.draw.line(screen, (204, 229, 255), (790, 400), (790, 1000), 20)

            screen.blit(lion, (rect10[0], rect10[1]))
            
            screen.blit(fox, (rect12[0], rect12[1]))
            screen.blit(rabbit, (rect14[0], rect14[1]))
        
            
            screen.blit(grass, (rect16[0], rect16[1]))
            
            
            
           
            button1.draw(screen)
            button2.draw(screen)
            button3.draw(screen)
            button4.draw(screen)
           
            pygame.display.flip()


            # - FPS -

            clock.tick(FPS)


def food_chainpass(screen):
    global tries
    
    
    button3 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button4 = Button((134, 837), (100, 100), (0,255,0), "Back")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            

            if button4.is_clicked(event):
                # go to stage2
                animals_instructions(screen)

            if button3.is_clicked(event):
                menu(screen)

            

            congratstext = ("You Win!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.blit(animalsbg, (0,0))
            screen.blit(win,(115,0))
            
            
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(goldstar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()   
            
def cells_instructions(screen):
    
    button1 = Button((84,896 ), (108, 108), (255,0,0), "")
    button2 = Button((877,896 ), (108, 108), (255,0,0), "")
    
    

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    
            if button1.is_clicked(event):
                # go to stage2
                science(screen)
            if button2.is_clicked(event):
                # go to stage2
                plantcell(screen)
            
            

            

        # - draws -
        button1.draw(screen)
        button2.draw(screen)
        screen.blit(cellbg,(0,0))
        screen.blit(instructions,(65,0))
        screen.blit(check, (875,895))
        screen.blit(close, (82, 895))
        text = "Welcome to Cells!"
        cellinstructions = FONT_NAME.render(text, 000, WHITE)
        screen.blit(cellinstructions, (200, 38))
        cell = font.render("Place the correct plant cell", 000, WHITE)
        screen.blit(cell, (145, 500))
        cellc = font.render("organelle in its appropriate place", 000, WHITE)
        screen.blit(cellc, (100, 550))
        
        
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)
        # - FPS -

        clock.tick(FPS)
def plantcell(screen):

    global selected_rect
    
   
    
    

    # - mainloop -
    rect9 = pygame.Rect(20, 330, 180,75)
    rect10 = pygame.Rect(50, 100, 180, 75)
    rect11 = pygame.Rect(20, 410, 180,75)
    rect12 = pygame.Rect(250, 100, 75, 75)
    rect13 = pygame.Rect(900, 470, 180,75)
    rect14 = pygame.Rect(450, 100, 180,75)
    rect15 = pygame.Rect(20, 572, 210,75)
    rect16 = pygame.Rect(650, 100, 210,75)
    rect17 = pygame.Rect(20, 685, 210,75)
    rect18 = pygame.Rect(870, 100, 210,75)
    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect in (rect10, rect12, rect14, rect16, rect18 ):
                    if rect.collidepoint(event.pos):
                        selected_rect = rect  # Select the colliding rect.
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_rect = None  # De-select the rect.
            elif event.type == pygame.MOUSEMOTION:
                if selected_rect is not None:  # If a rect is selected.
                    if event.buttons[0]:  # Left mouse button is down.
                        # Move the rect.
                        selected_rect.x += event.rel[0]
                        
                        
                            
                        selected_rect.y += event.rel[1]
        
            if 20<rect10[0]<200  and 330<rect10[1]<405 :
                        rect10[0] = 20
                        rect10[1] = 330
                        if event.type == pygame.MOUSEMOTION:
                            selected_rect = None

        
                

            if 20<rect12[0]<200  and 410<rect12[1]<485:
                    rect12[0] = 20
                    rect12[1] = 410
                    
                    if event.type == pygame.MOUSEMOTION:
                        selected_rect = None

            if 900<rect14[0]<1080  and 470<rect14[1]<545:
                    rect14[0] = 900
                    rect14[1] = 470
                    
                    if event.type == pygame.MOUSEMOTION:
                        selected_rect = None

            if 20<rect16[0]<230  and 572<rect16[1]<647:
                    rect16[0] = 20
                    rect16[1] = 572
                    
                    if event.type == pygame.MOUSEMOTION:
                        selected_rect = None

            if 20<rect18[0]<230  and 685<rect18[1]<760:
                    rect18[0] = 20
                    rect18[1] = 685
                    
                    if event.type == pygame.MOUSEMOTION:
                        selected_rect = None

            
            if rect10[0] == 20 and rect10[1] == 330 and rect12[0] == 20 and rect12[1] == 410 and rect14[0] ==900 and rect14[1] == 470 and rect16[0] ==20 and rect16[1] == 572 and rect18[0]==20 and rect18[1] ==685:
                plantcell_pass(screen)

            
                    
                   

        # - draws -

        screen.blit(cellbg, (0,0))
        screen.blit(plantcells, (250,150))
        
       
        
        
        pygame.draw.line(screen, (204, 229, 255), (200, 365), (350, 365), 5)
        pygame.draw.line(screen, (204, 229, 255), (200, 445), (430, 445), 5)
        pygame.draw.line(screen, (204, 229, 255), (230, 607), (430, 607), 5)
        pygame.draw.line(screen, (204, 229, 255), (200, 720), (340, 720), 5)
        pygame.draw.line(screen, (204, 229, 255), (720, 500), (900, 500), 5)
        pygame.draw.rect(screen, WHITE, rect9)
        pygame.draw.rect(screen, WHITE, rect13)
        pygame.draw.rect(screen, WHITE, rect15)
        pygame.draw.rect(screen, WHITE, rect17)
        pygame.draw.rect(screen, WHITE, rect11)
        button1 = Button((rect10[0],rect10[1] ), (180, 75), (34,139,34), "Cytoplasm")
        button2 = Button((rect12[0],rect12[1] ), (180, 75), (34,139,34), "Nucleus")
        button3 = Button((rect14[0],rect14[1] ), (180, 75), (34,139,34), "Vacuole")
        button4 = Button((rect16[0],rect16[1] ), (210, 75), (34,139,34), "Mitochondria")
        button5 = Button((rect18[0],rect18[1] ), (210, 75), (34,139,34), "Chloroplast")
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button4.draw(screen)
        button5.draw(screen)
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)
def plantcell_pass(screen):

    
    
    button3 = Button((834, 837), (100, 100), (0,255,0), "Continue")
    button4 = Button((134, 837), (100, 100), (0,255,0), "Back")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            

            if button4.is_clicked(event):
                # go to stage2
                cells_instructions(screen)

            if button3.is_clicked(event):
                menu(screen)

            

            congratstext = ("You Win!" )
            button3.draw(screen)
            button4.draw(screen)
            screen.blit(animalsbg, (0,0))
            screen.blit(win,(115,0))
        
           
            

             
            screen.blit(replay, (130, 836))
            screen.blit(menubtn, (830, 836))
            screen.blit(goldstar, (140, 245))
            screen.blit(goldstar, (380, 160))
            screen.blit(goldstar, (620, 245))
            ctext = FONT_NAME.render(congratstext, False, WHITE)
            screen.blit(ctext, (370, 25))
            pygame.display.flip()   
            






# - start -

menu(screen)

# - end -

pygame.quit()
