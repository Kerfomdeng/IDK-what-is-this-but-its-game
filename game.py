from cgitb import reset
from pygame import *
from random import randint
import os,sys

white = color.Color("#FFFFFF")
black = color.Color("#0083ff")
width = 242

app_folder = os.path.dirname(os.path.realpath(sys.argv[0]))

font.init()

#классы
class Player(sprite.Sprite):
    def __init__(self,player_imaged,player_imageu,player_imagel,player_imager, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.imaged = transform.scale(image.load(player_imaged), (size_x, size_y))
        self.imageu = transform.scale(image.load(player_imageu), (size_x, size_y))
        self.imagel = transform.scale(image.load(player_imagel), (size_x, size_y))
        self.imager = transform.scale(image.load(player_imager), (size_x, size_y))
        self.speed_def=player_speed
        self.speed = player_speed+10
        self.list_img=[self.imaged,self.imageu,self.imagel,self.imager]
        self.s=0
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.imaged.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.list_img[self.s], (self.rect.x, self.rect.y))

    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        global width
        global ch
        global win_x
        global win_y
        global up
        global down
        global right
        global left
        global collide
        keys = key.get_pressed()

        if keys[K_UP] and not self.rect.y <= 0 and left == False and right == False <= 0 or keys[K_w] and not self.rect.y <= 0 and left == False and right == False:
            self.rect.y -= self.speed
            self.s = 1
            up = True
        else:
            up = False

        if keys[K_DOWN] and not self.rect.y >= win_y - 150 and left == False and right == False >= win_y or keys[K_s] and not self.rect.y >= win_y and right == False and left == False:
            self.rect.y += self.speed
            self.s = 0
            down = True
        else:
            down = False

        if keys[K_LEFT] and not self.rect.x <= 0 and down == False and up == False <= 0 or keys[K_a] and not self.rect.x <= 0 and down == False and up == False:
            self.rect.x -= self.speed
            self.s = 2
            left = True
        else:
            left = False

        if keys[K_RIGHT] and not self.rect.x >= win_x and down == False and up == False >= win_x or keys[K_d] and not self.rect.x >= win_x and down == False and up == False:
            self.rect.x += self.speed
            self.s = 3
            right = True
        else:
            right = False

        if keys[K_LSHIFT] and keys[K_LEFT] or keys[K_LSHIFT] and keys[K_s] or keys[K_LSHIFT] and keys[K_d] or keys[K_LSHIFT] and keys[K_w] or keys[K_LSHIFT] and keys[K_a] or keys[K_LSHIFT] and keys[K_RIGHT] or keys[K_LSHIFT] and keys[K_DOWN] or keys[K_LSHIFT] and keys[K_UP]:
            if collide == False:    
                self.speed = self.speed_def + 2
                width -= 2
        elif keys[K_LSHIFT]:
            width+=1
        if width<10:
            self.speed = self.speed_def
        if not keys[K_LSHIFT]:    
            width += 1
            self.speed = self.speed_def
        if width > 242:
            width = 242
        elif width < 1:
            width = 1

class Wall(sprite.Sprite):
    def __init__(self,width,height,x,y,col1,col2,col3):
        sprite.Sprite.__init__(self)
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

    def reset(self):
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
    def update(self):
        global b
        global b1
        global question_start
        keys = key.get_pressed()
        if keys[K_e]:
            b=True
        if b== True and b1 ==True:
            self.rect.x+=10000
            question_start = True
question_start=False                
question1=Wall(500,150,400,550, 255,255,200)
question1_text=Wall(450,50,425,575,0,255,200)
question1_answer1=Wall(100,50,425,630,0,180,200)
question1_answer2=Wall(100,50,540,630,0,255,200)
question1_answer3=Wall(100,50,655,630,0,255,200)
question1_answer4=Wall(105,50,770,630,0,255,200)
list=list()
list.append(question1)
list.append(question1_text)
list.append(question1_answer1)
list.append(question1_answer2)
list.append(question1_answer3)
list.append(question1_answer4)
def right_button_cliked():
    global list
    if Right_answer==True:
        for i in list:
            i.rect.x+=1000000
b=False
b1=False
Right_answer=None
item1=items(30,30,700,400,0,180,0,1)

def hero_item_collide(GG,item):
    global b1
    if sprite.collide_rect(GG,item):
        b1=True


#нужные функции
def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

#изображения нужные

bg1_img = os.path.join(app_folder, "map.jpg")
bg2_img = os.path.join(app_folder,"bg.jpg")
bg_lobby_img = os.path.join(app_folder,"lobby_bg.png")
play_img = os.path.join(app_folder,"play.png")
quit_img= os.path.join(app_folder,"QUIT.png")

menu_img = os.path.join(app_folder,"menu.png")
player_imgl = os.path.join(app_folder,"pl_left.png")
player_imgr = os.path.join(app_folder,"pl_right.png")
player_imgu = os.path.join(app_folder,"pl_up.png")
player_imgd = os.path.join(app_folder,"pl_down.png")
sett_img = os.path.join(app_folder, "Settings.png")
sett_menu_img = os.path.join(app_folder, "setting_menu.png")

#параметры окна
window = display.set_mode((1000, 700))
display.set_caption("Logika-game")

but_menu = transform.scale(image.load(menu_img),(150, 75))
but_play = transform.scale(image.load(play_img),(200, 150))
but_quit = transform.scale(image.load(quit_img),(140, 60))
but_sett = transform.scale(image.load(sett_img),(100, 80))
menu_sett = transform.scale(image.load(sett_menu_img),(450, 500))
background_lbl = transform.scale(image.load(bg_lobby_img),(1000, 700))
background1 = transform.scale(image.load(bg1_img),(1000,700))
background2 = transform.scale(image.load(bg2_img),(1000,700))

x=0
z=0
rv=0 

#спрайт игрока
hero = Player(player_imgd,player_imgu,player_imgl,player_imgr, 730, 150, 30, 30,2)

##############################################################################
walls = sprite.Group()
room = []
room2 = []
room3 = []
room4 = []
room5 = []
room6 = []
room7 = []

##############################################################################
ch=True
clock=time.Clock()

finish=False
speed_vis = False
visible = False

run=True
game="stop"

#window size
base_font = font.Font(None, 32)
window_x, window_y =  window.get_size()
text = base_font.render("X", True, (0,0,0))
color = (98, 98, 98)
up = False
down = False
right = False
left = False

collide = False

while run:
    win_x, win_y = window.get_size()
    win_x1 = int(win_x) - 120
    win_y1 = int(win_y) - 100
    window.blit(background_lbl,(0,0))
    window.blit(but_play, (win_x / 2 - 100, win_y / 2 - 100))
    window.blit(but_quit, (win_x / 2 - 100 + 35, win_y / 2 - 100 + 135))

    if visible == True:
        window.blit(menu_sett, (win_x1 - 220, win_y1 - 420))

        if (win_x, win_y) == (1000, 700):
            input_rect = Rect(820, 350, 50, 32)
            input_rect2 = Rect(890, 350, 50, 32)
        elif (win_x, win_y) == (800, 600):
            input_rect = Rect(win_x1 - 60, win_y1 - 225, 50, 32)
            input_rect2 = Rect(win_x1 + 10, win_y1 - 225, 50, 32)
        elif (win_x, win_y) == (1200, 800):
            input_rect = Rect(win_x1 - 60, win_y1 - 195, 50, 32)
            input_rect2 = Rect(win_x1 + 10, win_y1 - 195, 50, 32)
        elif (win_x, win_y) == (1400, 850):
            input_rect = Rect(win_x1 - 60, win_y1 - 160, 50, 32)
            input_rect2 = Rect(win_x1 + 10, win_y1 - 160, 50, 32)

        draw.rect(window, color, input_rect)
        draw.rect(window, color, input_rect2)

        text_surface = base_font.render(str(window_x), True, (0, 0, 0))
        window.blit(text_surface, (win_x1 - 60, win_y1 - 250 + 5))
        window.blit(text, (win_x1 - 60 + 52, win_y1 - 250 + 5))
        text_surface2 = base_font.render(str(window_y), True, (0, 0, 0))
        window.blit(text_surface2, (win_x1 + 10, win_y1 - 250 + 5))

        text_surface = base_font.render(str(window_x - 200), True, (0, 0, 0))
        window.blit(text_surface, (win_x1 - 60 + 10, win_y1 - 250 + 35))
        window.blit(text, (win_x1 - 60 + 52, win_y1 - 250 + 35))
        text_surface2 = base_font.render(str(window_y - 100), True, (0, 0, 0))
        window.blit(text_surface2, (win_x1 + 10, win_y1 - 250 + 35))

        text_surface = base_font.render(str(window_x + 200), True, (0, 0, 0))
        window.blit(text_surface, (win_x1 - 60, win_y1 - 250 + 65))
        window.blit(text, (win_x1 - 60 + 52, win_y1 - 250 + 65))
        text_surface2 = base_font.render(str(window_y + 100), True, (0, 0, 0))
        window.blit(text_surface2, (win_x1 + 10, win_y1 - 250 + 65))

        text_surface = base_font.render(str(window_x + 400), True, (0, 0, 0))
        window.blit(text_surface, (win_x1 - 60, win_y1 - 250 + 95))
        window.blit(text, (win_x1 - 60 + 52, win_y1 - 250 + 95))
        text_surface2 = base_font.render(str(window_y + 150), True, (0, 0, 0))
        window.blit(text_surface2, (win_x1 + 10, win_y1 - 250 + 95))

    window.blit(but_sett, (win_x1, win_y1))

    #проверка событий
    for e in event.get():
        if e.type==QUIT:
            run=False
        if e.type == MOUSEBUTTONDOWN:
            x, y = mouse.get_pos()
            print(x,y)
            if x >= win_x / 2 - 80 and x <= win_x / 2 + 70:
                if y >= win_y / 2 - 50 and y <= win_y / 2:
                    game='start'
                    speed_vis = True
            if x >= 20 and x <= 130:
                if y >= 15 and y <= 60:
                    game='stop'
                    speed_vis = False
            if x >= win_x / 2 - 65 and x <= win_x / 2 + 70 and game == 'stop':
                if y >= win_y / 2 + 20 and y <= win_y / 2 + 85:
                    run=False
            if x >= win_x1 - 10 and x <= win_x and visible == True:
                if y >= win_y1 + 10 and y <= win_y1 + 70 and visible == True:
                    visible = False 
            elif x >= win_x1 - 10 and x <= win_x and visible == False:
                if y >= win_y1 + 10 and y <= win_y1 + 70 and visible == False:
                    visible = True 

            if x >= win_x - 65 and x <= win_x - 45 and visible == True:
                if y >= win_y1 - 235 and y <= win_y1 - 220 and visible == True:
                    visible2 = True

            elif x >= win_x - 65 and x <= win_x - 45 and visible == True:
                if y >= win_y1 - 235 and y <= win_y1 - 220 and visible == True:
                    visible2 = False
                    
            if x >= win_x1 - 60 and x <= win_x - 60 and visible == True:
                if y >= win_y1 - 210 and y <= win_y1 - 180 and visible == True:
                    window = display.set_mode((800, 600)) 
                    background_lbl = transform.scale(image.load(bg_lobby_img),(800, 600))
                    background1 = transform.scale(image.load(bg1_img),(800, 600))
                    background2 = transform.scale(image.load(bg2_img),(800, 600))
                    hero.rect.x, hero.rect.y = ((800 / 1000 * 730), (600 / 700 * 145))

            if x >= win_x1 - 60 and x <= win_x - 60 and visible == True:
                if y >= win_y1 - 250 and y <= win_y1 - 230 and visible == True:
                    window = display.set_mode((1000, 700)) 
                    background_lbl = transform.scale(image.load(bg_lobby_img),(1000, 700))
                    background1 = transform.scale(image.load(bg1_img),(1000, 700))
                    background2 = transform.scale(image.load(bg2_img),(1000, 700))
                    hero.rect.x, hero.rect.y = ((1000 / 1000 * 730), (700 / 700 * 145))

            if x >= win_x1 - 60 and x <= win_x - 60 and visible == True:
                if y >= win_y1 - 190 and y <= win_y1 - 165  and visible == True:
                    window = display.set_mode((1200, 800)) 
                    background_lbl = transform.scale(image.load(bg_lobby_img),(1200, 800))
                    background1 = transform.scale(image.load(bg1_img),(1200, 800))
                    background2 = transform.scale(image.load(bg2_img),(1200, 800))
                    hero.rect.x, hero.rect.y = ((1200 / 1000 * 730), (800 / 700 * 145))

            if x >= win_x1 - 60 and x <= win_x - 60 and visible == True:
                if y >= win_y1 - 160 and y <= win_y1 - 140  and visible == True:
                    window = display.set_mode((1400, 850)) 
                    background_lbl = transform.scale(image.load(bg_lobby_img),(1400, 850))
                    background1 = transform.scale(image.load(bg1_img),(1400, 850))
                    background2 = transform.scale(image.load(bg2_img),(1400, 850))
                    hero.rect.x, hero.rect.y = ((1400 / 1000 * 730), (850 / 700 * 145))
            if x >= 424 and x <= 523 and question_start==True:
                if y >=629  and y <=680:
                    Right_answer=True


    #отоброжение комнат и среды
    if game == "start":
        window.blit(background1,(0,0))
        window.blit(but_menu,(0,0))
        visible = False
        visible2 = False

        #walls 
        for i in range(len(room)):
            room[i].kill()
        for i in range(len(room2)):
            room2[i].kill()
        for i in range(len(room3)):
            room3[i].kill()
        for i in range(len(room4)):
            room4[i].kill()
        for i in range(len(room5)):
            room5[i].kill()
        for i in range(len(room6)):
            room6[i].kill()
        for i in range(len(room7)):
            room7[i].kill()

        w1 = Wall(3, win_y/700 * 270, win_x/1000 * 335, win_y/700 * 90, 90, 90, 90)
        w2 = Wall(3, win_y/700 * 90, win_x/1000 * 335, win_y/700 * 425, 90, 90, 90)
        w3 = Wall(3, win_y/700 * 215, win_x/1000*662, win_y/700*90, 90, 90, 90)
        w4 = Wall(3, win_y/700*150, win_x/1000*662, win_y/700*370, 90, 90, 90)
        w5 = Wall(win_x/1000*660, 3, win_x/1000*335, win_y/700*89, 90, 90, 90)
        w6 = Wall(win_x/1000*330, 3, win_x/1000*335, win_y/700*515, 90, 90, 90)
        w7 = Wall(win_x/1000*130, 3, win_x/1000*340, win_y/700*280, 90, 90, 90)
        w8 = Wall(win_x/1000*140, 3, win_x/1000*520, win_y/700*280, 90, 90, 90)
        w9 = Wall(3, win_y/700*135, win_x/1000*793, win_y/700*90, 90, 90, 90)
        w10 = Wall(win_x/1000*135, 3, win_x/1000*793, win_y/700*226, 90, 90, 90)
        w11 = Wall(win_x/1000*20, 3, win_x/1000*974, win_y/700*226, 90, 90, 90)
        w12 = Wall(3, win_y/700*400, win_x/1000*990, win_y/700*90, 90, 90, 90)
        w13 = Wall(win_x/1000*55, 3, win_x/1000*660, win_y/700*382, 90, 90, 90)
        w14 = Wall(win_x/1000*220, 3, win_x/1000*770, win_y/700*382, 90, 90, 90)
        w15 = Wall(3, win_y/700*35, win_x/1000*807, win_y/700*380, 90, 90, 90)
        w16 = Wall(3, win_y/700*23, win_x/1000*807, win_y/700*468, 90, 90, 90)
        w17 = Wall(win_x/1000*148, 3, win_x/1000*667, win_y/700*490, 90, 90, 90)
        w18 = Wall(win_x/1000*130, 3, win_x/1000*18, win_y/700*288, 90, 90, 90)
        w19 = Wall(win_x/1000*120, 3, 215, win_y/700*288, 90, 90, 90)
        w20 = Wall(win_x/1000*322, 3, win_x/1000*13, win_y/700*177, 90, 90, 90)
        w21 = Wall(3, win_y/700*315, win_x/1000*15, win_y/700*177, 90, 90, 90)
        w22 = Wall(win_x/1000*320, 3, win_x/1000*15, win_y/700*490, 90, 90, 90)
        w23 = Wall(win_x/1000*40, 3, win_x/1000*19, win_y/700*358, 90, 90, 90)
        w24 = Wall(win_x/1000*23, 3, win_x/1000*110, win_y/700*358, 90, 90, 90)
        w25 = Wall(3, win_y/700*65, win_x/1000*134, win_y/700*292, 90, 90, 90)
        w26 = Wall(3, win_y/700*70, win_x/1000*212, win_y/700*290, 90, 90, 90)
        w27 = Wall(win_x/1000*35, 3, win_x/1000*215, win_y/700*358, 90, 90, 90)
        w28 = Wall(win_x/1000*30, 3, win_x/1000*305, win_y/700*358, 90, 90, 90)
        w29 = Wall(win_x/1000*36, 3, win_x/1000*19, win_y/700*425, 90, 90, 90)
        w30 = Wall(win_x/1000*48, 3, win_x/1000*107, win_y/700*425, 90, 90, 90)
        w31 = Wall(win_x/1000*55, 3, win_x/1000*204, win_y/700*425, 90, 90, 90)
        w32 = Wall(win_x/1000*32, 3, win_x/1000*308, win_y/700*425, 90, 90, 90)
        w33 = Wall(3, win_y/700*60, win_x/1000*120, win_y/700*430, 90, 90, 90)
        w34 = Wall(3, win_y/700*60, win_x/1000*228, win_y/700*430, 90, 90, 90)

        room = [w1, w2, w3, w4, w5, w6, w7, w8]
        room2 = [w9, w10, w11, w12]
        room3 = [w13, w14, w15, w16, w17]
        room4 = [w18, w19, w20, w21, w22]
        room5 = [w23, w24, w25]
        room6 = [w26, w27, w28]
        room7 = [w29, w30, w31, w32, w33, w34]
                
        for i in range(len(room)):
            walls.add(room[i])
        for i in range(len(room2)):
            walls.add(room2[i])
        for i in range(len(room3)):
            walls.add(room3[i])
        for i in range(len(room4)):
            walls.add(room4[i])
        for i in range(len(room5)):
            walls.add(room5[i])
        for i in range(len(room6)):
            walls.add(room6[i])
        for i in range(len(room7)):
            walls.add(room7[i])
        hero_item_collide(hero,item1)
        item1.reset()
        item1.update()
        walls.draw(window)
        if question_start==True:    
            question1.reset()
            question1_text.reset()
            question1_answer1.reset()
            question1_answer2.reset()
            question1_answer3.reset()
            question1_answer4.reset()
        right_button_cliked()
        hero.update()
        hero.reset()

    #проверка столкновений
    if sprite.spritecollide(hero, walls, False):
        collide = True
        if hero.s == 0 or down == True:
            hero.rect.y = hero.rect.y - hero.speed
            
        elif hero.s == 1 or up == True:
            hero.rect.y = hero.rect.y + hero.speed

        elif hero.s == 2 or left == True:
            hero.rect.x = hero.rect.x + hero.speed

        elif hero.s == 3 or right == True:
            hero.rect.x = hero.rect.x - hero.speed
    else:
        collide = False

    if speed_vis == True:
        draw.rect(window, black, [25, win_y1, 252, 34])
        draw.rect(window, white, [26, win_y1 + 1, 250, 32])
        draw.rect(window, black, [30, win_y1 + 5, width, 24])
        
        

    display.update()
    # цикл срабатывает каждую 0.06 секунд
    clock.tick(60)