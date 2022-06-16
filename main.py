import numbers
from pygame import *
import pygame 
from random import randint
import time as my_time
import os,sys
a=False
def quest_with_numbers(c,question):
    global a
    pygame.init()
    name = ""
    font = pygame.font.Font(None, 50)
    while name !=c or a!=True :
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isdigit():
                    a=False 
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    a=False
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    if name==c:
                        a=True
                    else:
                        name=''
        window.fill((0, 0, 0))
        window.blit(question,(400,100))
        block = font.render("Введите число затем тыкните enter:   "+name, True, (255, 255, 255))
        window.blit((block), (100,500))
        pygame.display.flip()
def quest_with_letters(c,question):
    global a
    pygame.init()
    name = ""
    font = pygame.font.Font(None, 50)
    while name !=c or a!=True :
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    a=False 
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    a=False
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    if name==c:
                        a=True
                    else:
                        name=''
        window.fill((0, 0, 0))
        window.blit(question,(400,100))
        block = font.render("Введите ответ: "+name, True, (255, 255, 255))
        window.blit((block), (100,500))
        pygame.display.flip()  
def quest_with_yesno(d,c,question):
    pygame.init()
    name = ""
    font = pygame.font.Font(None, 50)
    while name !=c and name!=d :
        for evt in pygame.event.get():
            if evt.type == MOUSEBUTTONDOWN:
                x, y = mouse.get_pos()
                if x >= 348 and x <= 448 :
                    if y >= 478 and y <= 525:
                        name=d
                        return name
                elif x >= 467 and x <= 572 :
                    if y >= 478 and y <= 525:
                        name=c   
                        return name
        window.fill((0, 0, 0))
        window.blit(question,(400,100))
        window.blit(yesno,(300,450))
        pygame.display.flip()
    return name
def ok(text):
    pygame.init()
    name = ""
    font = pygame.font.Font(None, 50)
    while name !='ok':
        for evt in pygame.event.get():
            if evt.type == MOUSEBUTTONDOWN:
                x, y = mouse.get_pos()
                if x >= 400 and x <= 600 :
                    if y >= 450 and y <= 550:
                        name='ok'
        window.fill((0, 0, 0))
        window.blit(gk,(500,100))
        block = font.render(text, True, (255, 255, 255))
        window.blit(block,(300,300))
        window.blit(ok_a,(400,450))
        pygame.display.flip()                             

#----SETTING_GAME----
#player
player_speed = 7
player_hp=100

player_size_width, player_size_height = 50,70
FPS=80

#window
display.set_caption('Find the way out')
win_width, win_height = 1200 , 700
window = display.set_mode((win_width, win_height)) 

#COMMON
os.system('cls')
clock = time.Clock()


#----IMG----
text_question1 = "question.png"
ok_a =transform.scale(image.load("ok_a.png"), (200,100))
gk =transform.scale(image.load("gold_key.png"), (200,100))
#player-stop
img_player_stop=transform.scale(image.load("img_player_down_2.png"), (player_size_width, player_size_height))

#player-up
img_player_up_1=transform.scale(image.load("img_player_up_1.png"), (player_size_width, player_size_height))
img_player_up_2=transform.scale(image.load("img_player_up_2.png"), (player_size_width, player_size_height))
img_player_up_3=transform.scale(image.load("img_player_up_3.png"), (player_size_width, player_size_height))
img_list_player_up=[img_player_up_1,img_player_up_2,img_player_up_1,img_player_up_3]

#player-down
img_player_down_1=transform.scale(image.load("img_player_down_1.png"), (player_size_width, player_size_height))
img_player_down_2=transform.scale(image.load("img_player_down_2.png"), (player_size_width, player_size_height))
img_player_down_3=transform.scale(image.load("img_player_down_3.png"), (player_size_width, player_size_height))
img_list_player_down=[img_player_down_1,img_player_down_2,img_player_down_1,img_player_down_3]

#player-left
img_player_left_1=transform.scale(image.load("img_player_left_1.png"), (player_size_width, player_size_height))
img_player_left_2=transform.scale(image.load("img_player_left_2.png"), (player_size_width, player_size_height))
img_list_player_left=[img_player_left_1,img_player_left_2,img_player_left_1,img_player_left_2]

#player-right
img_player_right_1=transform.scale(image.load("img_player_right_1.png"), (player_size_width, player_size_height))
img_player_right_2=transform.scale(image.load("img_player_right_2.png"), (player_size_width, player_size_height))
img_list_player_right=[img_player_right_1,img_player_right_2,img_player_right_1,img_player_right_2]

#common
img_dark_background="img_dark_background.png" #dark_background/illusion of light
img_backgraund= "ground_normal.jpg"

#----SOUND----
#mixer.init()

#mixer.music.load('SOUNDS/sTest-sound.mp3')
#mixer.music.set_volume(0.5)
#mixer.music.play()

#----CLASS----
class Player(sprite.Sprite):#class Player and dark_background/illusion of light
    def __init__(self, player_x, player_y):
        sprite.Sprite.__init__(self)

        #player
        self.img_player_now=img_player_stop

        self.player_speed = player_speed

        self.rect = img_player_stop.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.img_number=0
        #dark_background/illusion of light
        self.img_dark_background=transform.scale(image.load(img_dark_background), (win_width*2, win_height*2))

        self.rect_d_b = self.img_dark_background.get_rect()


    def update(self):    
        global values_up, values_down, values_right, values_left
        
        if keys[K_s] and self.rect.y < win_height - player_size_height and values_down == True or keys[K_DOWN] and self.rect.y < win_height -player_size_height:
            self.rect.y += player_speed
            self.img_player_now=img_list_player_down[self.img_number]
            self.img_number+=1

        if self.img_number>3:
            self.img_number=0   

        if keys[K_w] and self.rect.y > 5 and values_up == True or keys[K_UP] and self.rect.y > 5:
            self.rect.y -= player_speed
            self.img_player_now=img_list_player_up[self.img_number]
            self.img_number+=1

        if self.img_number>3:
            self.img_number=0

        if keys[K_a] and self.rect.x > 5 and values_left == True or keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= player_speed
            self.img_player_now=img_list_player_right[self.img_number]
            self.img_number+=1

        if self.img_number>3:
            self.img_number=0

        if keys[K_d] and self.rect.x < win_width - player_size_width and values_right == True or keys[K_RIGHT] and self.rect.x < win_width - player_size_width:
            self.rect.x += player_speed
            self.img_player_now=img_list_player_left[self.img_number]
            self.img_number+=1

        if self.img_number>3:
            self.img_number=0

        if keys[K_d]==keys[K_a]==keys[K_w]==keys[K_s]:
            self.img_player_now=img_player_stop

    def reset(self):
        window.blit(self.img_player_now, (self.rect.x, self.rect.y))
        window.blit(self.img_dark_background, (self.rect.x-win_width+(player_size_width/2), self.rect.y-win_height+(player_size_height/2)))

class Wall(sprite.Sprite):
    def __init__(self, wall_x,wall_y,wall_size_width,wall_size_height):
        sprite.Sprite.__init__(self)

        self.wall_size_width=wall_size_width
        self.wall_size_height=wall_size_height

        self.image=Surface((self.wall_size_width,self.wall_size_height))
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def update(self):
        window.blit(self.image, (50,50))


class Enemy(sprite.Sprite):
    def __init__(self, plaer_hp, gun):
        print('classEnemy')

class Hud(sprite.Sprite):
    def __init__(self, plaer_hp, gun):
        print('classHud')
    #hp
    #guns
    #Inventory / Quick access

class Button(sprite.Sprite):
    def __init__(self,button_img,button_x, button_y, button_size_height,button_size_width,action):
        self.button_x=button_x
        self.button_y=button_y
        self.button_size_height=button_size_height
        self.button_size_width=button_size_width
        self.action=action

class Door():
    def __init__(self, door_x, door_y, door_size_width, door_size_height,tp_x,tp_y,tp_location):
        sprite.Sprite.__init__(self)
        self.door_x=door_x
        self.door_y=door_y
        self.door_size_width=door_size_width
        self.door_size_height=door_size_height
        self.tp_x=tp_x
        self.tp_y=tp_y
        self.tp_location=tp_location

        self.image=Surface((self.door_size_width,self.door_size_height))
        self.image.fill((251, 255, 94))

        self.rect = self.image.get_rect()
        self.rect.x = self.door_x
        self.rect.y = self.door_y


    def update(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
        
    def teleportation(self):
        global location
        player_hero.rect.x=self.tp_x
        player_hero.rect.y=self.tp_y
        location=self.tp_location 


class Decor(sprite.Sprite):
    def __init__(self, x, y, width, height, decor_image):
        sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.image = transform.scale(image.load(decor_image), (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class items(Wall):
    def __init__(self,width,height,x,y,col1,col2,col3,item_number):
        self.width=width
        self.height=height
        self.col1=col1
        self.col2=col2
        self.col3=col3
        self.image=Surface((self.width,self.height))
        self.image.fill((self.col1,self.col2,self.col3))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.item_number=item_number
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
def it_update(player,item,question,need_item):
    b=False
    keys = key.get_pressed()
    if keys[K_e]:
        b=True
    if b== True and sprite.collide_rect(player,item):
        if need_item ==None:
            item.rect.x+=10000
        else:
            pass    
        question=True
        return question
question_start=False
breaking_table=False
item1=items(30,30,400,400,0,180,0,1)
item2=items(30,30,600,400,180,180,0,2)

b=False
b1=False
def hero_item_collide(GG,item,b):
    if sprite.collide_rect(GG,item):
        b=True

#----FUNCTION----
def wall_collide(walls_list, decor_list):
    global values_up, values_down, values_right, values_left
    values_up = values_down = values_right = values_left = True

    #player_hero.rect.y<walls_list[i].rect.y and 
    for i in range(0,len(walls_list)):
        #UP
        if  abs(player_hero.rect.y-(walls_list[i].rect.y+walls_list[i].wall_size_height))<10 and walls_list[i].rect.x-player_size_height< player_hero.rect.x <  (walls_list[i].rect.x+ walls_list[i].wall_size_width):
            values_up=False
        #DOWN
        if  abs((player_hero.rect.y+player_size_height)-walls_list[i].rect.y)<10 and walls_list[i].rect.x-player_size_height< player_hero.rect.x <  (walls_list[i].rect.x+ walls_list[i].wall_size_width):
            values_down=False
        #RIGHT
        if  abs((player_hero.rect.x+player_size_width)-walls_list[i].rect.x)<10 and walls_list[i].rect.y-player_size_height < player_hero.rect.y <  (walls_list[i].rect.y+ walls_list[i].wall_size_height):
            values_right=False
        #LEFT
        if  abs(player_hero.rect.x-(walls_list[i].rect.x+walls_list[i].wall_size_width))<10 and walls_list[i].rect.y-player_size_height < player_hero.rect.y <  (walls_list[i].rect.y+ walls_list[i].wall_size_height):
            values_left=False

    for i in range(0,len(decor_list)):
        #UP
        if  abs(player_hero.rect.y-(decor_list[i].rect.y+decor_list[i].height))<10 and decor_list[i].rect.x-player_size_height< player_hero.rect.x <  (decor_list[i].rect.x+ decor_list[i].width):
            values_up=False
        #DOWN
        if  abs((player_hero.rect.y+player_size_height)-decor_list[i].rect.y)<10 and decor_list[i].rect.x-player_size_height< player_hero.rect.x <  (decor_list[i].rect.x+ decor_list[i].width):
            values_down=False
        #RIGHT
        if  abs((player_hero.rect.x+player_size_width)-decor_list[i].rect.x)<10 and decor_list[i].rect.y-player_size_height < player_hero.rect.y <  (decor_list[i].rect.y+ decor_list[i].height):
            values_right=False
        #LEFT
        if  abs(player_hero.rect.x-(decor_list[i].rect.x+decor_list[i].width))<10 and decor_list[i].rect.y-player_size_height < player_hero.rect.y <  (decor_list[i].rect.y+ decor_list[i].height):
            values_left=False

def walls_draw(walls_list):
    walls_room_group=sprite.Group()
    for i in range(len(walls_list)):
        walls_room_group.add(walls_list[i])
    walls_room_group.draw(window)




#----OGJECT_GAME----
player_hero=Player(600, 385)
backgraund = transform.scale(image.load(img_backgraund), (win_width, win_height))

yesno = transform.scale(image.load("answer.png"), (300, 100))
#----ROOMS----

#Decor for rooms
bed_img, bed2_img, bed3_img, bed4_img = "bed.png", "bed2.png", "bed3.png", "bed4.png"
carpet_img = "carpet.png"
book_img1, book_img2 = "bookshelf1.png", "bookshelf2.png"
round_tbl_img = "round_table.png"
tbl_img = "table.png"
book_img3, book_img4 = "bookshelf3.png","bookshelf4.png"
book_img5, book_img6 = "bookshelf5.png", "bookshelf6.png"

#room-1
#room-1 border

room1_wall1= Wall(0, 0, 550, 20)
room1_wall2= Wall(650, 0, 600, 20)
room1_wall3= Wall(0, 0, 20, 300)
room1_wall4= Wall(0, 400, 20, 300)
room1_wall5= Wall(0, 680, 1200, 20)
room1_wall6= Wall(1180, 0, 20, 685)

wall_room1_list = [room1_wall1,room1_wall2,room1_wall3,room1_wall4,room1_wall5,room1_wall6]

#Двери
door1_room1=Door(550, 0, 97, 18, 600, 610,'location-2')
door2_room1=Door(0, 300, 20, 100, 1060, 305,'location-3')

#Декор
bed = Decor(1045, 15, 150, 200, bed_img)
bookshelf1, bookshelf2 = Decor(20, 10, 130, 150, book_img1), Decor(150, 20, 130, 150, book_img2)
round_tbl = Decor(80, 160, 130, 85, round_tbl_img)
tbl = Decor(480, 590, 260, 100, tbl_img)
#Не смотрите с подозрением на этот ковер, точнее на его размер и координаты. Так получилось, что ковер СЛИШКОМ МАЛЕНЬКИЙ и его никак иначе нормально не поставить.
#И еще одна просьба: НЕ НАДО ДОБАВЛЯТЬ ЕГО В СПИСОК ДЕКОРА, ЕСЛИ НЕ ХОТИТЕ ЧТОБЫ ПЕРСОНАЖ КУДА-ТО УЛЕТЕЛ!
carpet = Decor(-15, 440, 1000, 200, carpet_img)

#room-2
#room-2 border
room2_wall1 = Wall(0, 0, 500, 20)
room2_wall2 = Wall(0, 0, 20, 700)
room2_wall3 = Wall(700, 0, 495, 20)
room2_wall4 = Wall(0, 680, 560, 20)
room2_wall5 = Wall(645, 680, 550, 20)
room2_wall6 = Wall(1185, 0, 20, 695)

wall_room2_list = [room2_wall1,room2_wall2,room2_wall3,room2_wall4,room2_wall5,room2_wall6]

#Двери
door1_room2=Door(550, 680, 97, 18, 600, 70,'location-1')
door2_room2=Door(500, 0, 200, 20, 600, 620,'location-4')

#Декор
round_tbl2 = Decor(985, 525, 145, 125, round_tbl_img)
bookshelf3, bookshelf4 = Decor(870, 10, 175, 130, book_img1), Decor(1045, 15, 115, 135, book_img2)
bookshelf5, bookshelf6 = Decor(20, 10, 130, 140, book_img3), Decor(145, 20, 130, 140, book_img4)
bed2 = Decor(20, 475, 165, 200, bed2_img)
tbl2 = Decor(480, 300, 255, 100, tbl_img)

#room-3
#room-3 border

room3_wall1 = Wall(0, 0, 1195, 20)
room3_wall2 = Wall(0, 0, 20, 680)
room3_wall3 = Wall(0, 680, 1200, 20)
room3_wall4 = Wall(1190, 0, 20, 260)
room3_wall5 = Wall(1190, 350, 20, 335)

wall_room3_list = [room3_wall1,room3_wall2,room3_wall3,room3_wall4,room3_wall5]

#Двери
door1_room3=Door(1190, 250, 20, 100, 115, 345,'location-1')
door2_room1=Door(0, 300, 20, 100, 1060, 305,'location-3')

#Декор
bookshelf7 = Decor(20, 10, 150, 190, book_img3)
round_tbl3 = Decor(200, 70, 120, 120, round_tbl_img)
tbl3 = Decor(560, 220, 125, 230, tbl_img)

#room-4
#room-4 border
room4_wall1= Wall(0, 0, 20, 375)
room4_wall2= Wall(0, 500, 20, 190)
room4_wall3= Wall(0, 685, 510, 20)
room4_wall4= Wall(700, 685, 510, 20)
room4_wall5= Wall(0, 0, 1200, 20)
room4_wall6= Wall(1185, 0, 20, 690)

wall_room4_list = [room4_wall1,room4_wall2,room4_wall3,room4_wall4,room4_wall5,room4_wall6]

#Двери
door1_room4=Door(500, 685, 200, 20, 600, 90,'location-2')
door2_room4=Door(0, 375, 20, 125, 1100, 420,'location-5')

#Декор
tbl4 = Decor(435, 15, 330, 105, tbl_img)
round_tbl4 = Decor(1000, 275, 140, 125, round_tbl_img)
bed3 = Decor(20, 520, 115, 165, bed3_img)

#room-5
#room-5 border
room5_wall1 = Wall(0, 0, 20, 190)
room5_wall2 = Wall(0, 310, 20, 380)
room5_wall3 = Wall(0, 0, 1200, 20)
room5_wall4 = Wall(1185, 0, 20, 375)
room5_wall5 = Wall(1185, 495, 20, 200)
room5_wall6 = Wall(0, 685, 1200, 20)

wall_room5_list = [room5_wall1,room5_wall2,room5_wall3,room5_wall4,room5_wall5,room5_wall6]

#Двери
door1_room5=Door(1185, 375, 20, 125, 100, 300,'location-4')
door2_room5=Door(0, 190, 20, 120, 1105, 190,'location-6')

#Декор
bed4 = Decor(20, 500, 175, 180, bed4_img)
bookshelf8, bookshelf9 = Decor(440, 20, 140, 140, book_img5), Decor(580, 20, 180, 140, book_img6) 
tbl5 = Decor(480, 145, 190, 70, tbl_img)

#room-6
#room-6 border
room6_wall1 = Wall(1185, 0, 20, 170)
room6_wall2 = Wall(1185, 280, 20, 410)
room6_wall3 = Wall(0, 685, 1200, 20)
room6_wall4 = Wall(0, 0, 20, 690)
room6_wall5 = Wall(0, 0, 1190, 20)
wall_room6_list = [room6_wall1,room6_wall2,room6_wall3,room6_wall4,room6_wall5]

#Двери
door1_room6=Door(1185, 170, 20, 120, 80, 300,'location-5')

#Декор
bookshelf10, bookshelf11 = Decor(455, 130, 110, 180, book_img5), Decor(560, 130, 150, 180, book_img6)
tbl6 = Decor(460, 310, 245, 80, tbl_img)

#список декора по комнатам: 1 - первая комната и т.д.
decor_list1 = [bed, bookshelf1, bookshelf2, round_tbl, tbl]
decor_list2 = [round_tbl2, bookshelf3, bookshelf4, bookshelf5, bookshelf6, bed2, tbl2]
decor_list3 = [bookshelf7, tbl3, round_tbl3]
decor_list4 = [bed3, tbl4, round_tbl4]
decor_list5 = [bed4, bookshelf8, bookshelf9, tbl5]
decor_list6 = [tbl6, bookshelf10, bookshelf11]
decor_list = [decor_list1, decor_list2, decor_list3, decor_list4, decor_list5, decor_list6]

#VARIABLE
values_up = values_down = values_right = values_left = True
location='location-1' 
walls_list=wall_room1_list

carpet_checker=False
gold_key=False
while True:
    keys = key.get_pressed()

    for e in event.get():
        if e.type==QUIT:
            exit()

    if location == 'menu':
        window.fill('#D2D2D2')
        wall_collide(wall_room1_list, decor_list1)
        player_hero.update()
        player_hero.reset()
        walls_draw(wall_room1_list)

    elif location == 'location-1':
        window.blit(backgraund,(0, 0))
        wall_collide(wall_room1_list, decor_list1)
        door1_room1.update(), door2_room1.update()
        item1.reset()
        item2.reset()
        bed.update()
        bookshelf1.update(), bookshelf2.update()
        round_tbl.update()
        tbl.update()
        carpet.update()
        player_hero.update()
        player_hero.reset()
        walls_draw(wall_room1_list)
        if sprite.collide_rect(door1_room1, player_hero):
            door1_room1.teleportation()
        elif sprite.collide_rect(door2_room1, player_hero) and gold_key ==True:
            door2_room1.teleportation()

        question1 = transform.scale(image.load(text_question1),(200,250))
        if it_update(player_hero,item1,question_start,None)==True:
            quest_with_numbers('96',question1)
            carpet_checker=True
            a=False
            question_start=False
        if it_update(player_hero,item2,None,carpet_checker)== True and carpet_checker==True:            
            if quest_with_yesno('Да','Нет',question1)== 'Да':
                ok('Ты получил что-то наподобие ключика')    
                gold_key=True
                item2.rect.x+=1000
            elif quest_with_yesno('Да','Нет',question1)== 'Да':
                gold_key=False        
            a=False
        
    elif location == 'location-2':
        window.blit(backgraund,(0, 0))
        wall_collide(wall_room2_list, decor_list2)
        door1_room2.update(), door2_room2.update()
        round_tbl2.update()
        bookshelf3.update(), bookshelf4.update()
        bookshelf5.update(), bookshelf6.update()
        bed2.update()
        tbl2.update()
        player_hero.update()
        player_hero.reset()
        walls_draw(wall_room2_list)
        if sprite.collide_rect(door1_room2, player_hero):
            door1_room2.teleportation()
        elif sprite.collide_rect(door2_room2, player_hero):
            door2_room2.teleportation()

    elif location == 'location-3':
        window.blit(backgraund,(0, 0))
        wall_collide(wall_room3_list, decor_list3)
        player_hero.update()
        door1_room3.update()
        bookshelf7.update()
        round_tbl3.update(), tbl3.update()
        player_hero.reset()
        walls_draw(wall_room3_list)
        if sprite.collide_rect(door1_room3, player_hero):
            door1_room3.teleportation()

    elif location == 'location-4':
        window.blit(backgraund,(0, 0))
        wall_collide(wall_room4_list, decor_list4)
        player_hero.update()
        door1_room4.update(), door2_room4.update()
        tbl4.update(), round_tbl4.update()
        bed3.update()
        player_hero.reset()
        walls_draw(wall_room4_list)
        if sprite.collide_rect(door1_room4, player_hero):
            door1_room4.teleportation()
        elif sprite.collide_rect(door2_room4, player_hero):
            door2_room4.teleportation()

    elif location == 'location-5':
        window.blit(backgraund,(0, 0))
        wall_collide(wall_room5_list, decor_list5)
        player_hero.update()
        door1_room5.update(), door2_room5.update()
        bed4.update()
        bookshelf8.update(), bookshelf9.update()
        tbl5.update()
        player_hero.reset()
        walls_draw(wall_room5_list)
        if sprite.collide_rect(door1_room5, player_hero):
            door1_room5.teleportation()
        elif sprite.collide_rect(door2_room5, player_hero):
            door2_room5.teleportation()

    elif location == 'location-6':
        window.blit(backgraund,(0, 0))
        wall_collide(wall_room6_list, decor_list6)
        player_hero.update()
        door1_room6.update()
        bookshelf10.update(), bookshelf11.update()
        tbl6.update()
        player_hero.reset()
        walls_draw(wall_room6_list)
        if sprite.collide_rect(door1_room6, player_hero):
            door1_room6.teleportation()

    display.update()
    clock.tick(FPS)