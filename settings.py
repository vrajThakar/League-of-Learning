import pygame

#Initalizing Game
WIDTH = 1080
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
selected_rect = None



number_str = "" 



FONT_NAME = pygame.font.SysFont("algerian", 70)
FONT_TITLE = pygame.font.SysFont("algerian", 100)

font= pygame.font.SysFont("algerian", 45)
sfont= pygame.font.SysFont("algerian", 35)
bg = pygame.image.load("BG.png")
owl = pygame.image.load("owl.png")
dog = pygame.image.load("dog.png")
pig = pygame.image.load("pig.png")
chick = pygame.image.load("chick.png")
panda = pygame.image.load("panda.png")
grass = pygame.image.load("grass.png")
rabbit = pygame.image.load("rabbit.png")
plantcells = pygame.image.load("plantcell.png")
cellbg = pygame.image.load("Sky.png")
fox = pygame.image.load("fox.jpg")
lion = pygame.image.load("lion.jpg")
sciencebg = pygame.image.load("forest.png")
animalsbg = pygame.image.load("animalsbg.png")
ship1 = pygame.image.load("Ship_1_1_BTN.png")
ship1 = pygame.transform.scale(ship1, (110, 110))
ship1 = pygame.transform.rotate(ship1, -90)

ship2 = pygame.image.load("Ship_1_2_BTN.png")
ship2 = pygame.transform.scale(ship2, (110, 110))
ship2 = pygame.transform.rotate(ship2, -90)

ship3 = pygame.image.load("Ship_1_3_BTN.png")
ship3 = pygame.transform.scale(ship3, (110, 110))
ship3 = pygame.transform.rotate(ship3, -90)

ship4 = pygame.image.load("Ship_1_4_BTN.png")
ship4 = pygame.transform.scale(ship4, (110, 110))
ship4 = pygame.transform.rotate(ship4, -90)

ship5 = pygame.image.load("Ship_2_1_BTN.png")
ship5 = pygame.transform.scale(ship5, (110, 110))
ship5 = pygame.transform.rotate(ship5, -90)

ship6 = pygame.image.load("Ship_2_2_BTN.png")
ship6 = pygame.transform.scale(ship6, (110, 110))
ship6 = pygame.transform.rotate(ship6, -90)



menubtn = pygame.image.load("Menu_BTN.png")
menubtn = pygame.transform.scale(menubtn, (110, 110))

question = pygame.image.load("Stats_Bar.png")

check = pygame.image.load("Ok_BTN.png")
check = pygame.transform.scale(check, (110, 110))

replay = pygame.image.load("Replay_BTN.png")
replay = pygame.transform.scale(replay, (110, 110))

cont = pygame.image.load("Forward_BTN.png")
cont = pygame.transform.scale(cont, (110, 110))

back = pygame.image.load("Backward_BTN.png")
back = pygame.transform.scale(back, (110, 110))


score = pygame.image.load("Bonus_BTN_02.png")
score = pygame.transform.scale(score, (110, 110))



close = pygame.image.load("Close_BTN.png")
close = pygame.transform.scale(close, (110, 110))

play = pygame.image.load("Play_BTN.png")
play = pygame.transform.scale(play, (50, 50))

goldstar = pygame.image.load("Star_03.png")
nostar = pygame.image.load("Star_01.png")




mathb = pygame.image.load("Table.png")

welcome = pygame.image.load("Table_01.png")




instructions = pygame.image.load("Window.png")
win = pygame.transform.scale(instructions, (840, 980))

#Sound effects/Music

##effect = pygame.mixer.Sound('wrong.wav')
##gj = pygame.mixer.Sound('correct.wav')
selected_rect = None	
 

#Congruent/Similar 1
rect7 = pygame.Rect(100, 225, 160, 100)



rect8 = pygame.Rect(500, 225, 45, 60)






#Colours

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
