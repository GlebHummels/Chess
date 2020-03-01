import pygame, os
import sys

pygame.init()
pygame.mixer.init()
fps = 30
clock = pygame.time.Clock()
LETTERS = list(reversed(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']))
NUMBERS = list(reversed(['1', '2', '3', '4', '5', '6', '7', '8']))
tile_width = tile_height = 50
#nik
H_C = 'W'
Er = []
S = []


def load_image(name, colorkey=None):
  #  fullname = os.path.join('data', name)
    image = pygame.image.load(os.path.join('data', name))#.convert_alpha()
    '''if colorkey is not None:
         if colorkey == -1:
            colorkey = image.get_at((0, 0))
         image.set_colorkey(colorkey)
     else:
        image = image.convert_alpha()'''
    return image

###########################################################################
def JRt(se, M, K):
    x, y = se
    if [x, y] not in M:
        K.append([x, y])

def c_m_p(x, y):
    for i in range(len(S)):
        if S[i].cords[0] == x and S[i].cords[1] == y:
            return False
    return True

def c_m_p_2(a, c):
    x, y = a[0], a[1]
    for i in range(len(S)):
        if S[i].cords[0] == x and S[i].cords[1] == y and S[i].color != c:
            return True
    return False

def c_m_p_3(a, c):
    if c_m_p(a[0], a[1]) or c_m_p_2(a, c):
        return True
    return False

def c_m_b(self):
    voz = []
    c = self.color
    x, y = self.cords
    if x > y:
        z = x
    else:
        z = y
    z = 7
    for i in range(z):
        i += 1
        if c_m_p_2([x + i, y + i], c):
            voz.append([x + i, y + i])
            break
        if c_m_p(x + i, y + i):
            voz.append([x + i, y + i])
        else:
            break
        
    for i in range(z):
        i += 1
        if c_m_p_2([x + i, y - i], c):
            voz.append([x + i, y - i])
            break
        if c_m_p(x + i, y - i):
            voz.append([x + i, y - i])
        else:
            break
        
    for i in range(z):
        i += 1
        if c_m_p_2([x - i, y + i], c):
            voz.append([x - i, y + i])
            break
        if c_m_p(x - i, y + i):
            voz.append([x - i, y + i])
        else:
            break
        
    for i in range(z):
        i += 1
        if c_m_p_2([x - i, y - i], c):
            voz.append([x - i, y - i])
            break
        if c_m_p(x - i, y - i):
            voz.append([x - i, y - i])
        else:
            break
    return voz

def c_m_r(self):
    voz = []
    x, y = self.cords
    c = self.color
    for i in range(x + 1, 8, 1):
        if c_m_p_2([i, y], c):
            voz.append([i, y])
            break
        if c_m_p(i, y):
            voz.append([i, y])
        else:
            break
        
    for i in range(x - 1, -1, -1):
        if c_m_p_2([i, y], c):
            voz.append([i, y])
            break
        if c_m_p(i, y):
            voz.append([i, y])
        else:
            break
        
    for i in range(y + 1, 8, 1):
        if c_m_p_2([x, i], c):
            voz.append([x, i])
            break
        if c_m_p(x, i):
            voz.append([x, i])
        else:
            break
        
    for i in range(y - 1, -1, -1):
        if c_m_p_2([x, i], c):
            voz.append([x, i])
            break
        if c_m_p(x, i):
            voz.append([x, i])
        else:
            break
    return voz

##########################################################################


class Pawn:
    def __init__(self, x, y, c):
        self.cords = [x, y]
        self.color = c
        self.ch = False
        self.v = False
        self.cost = 1
        if c == 'W':
            self.pic = load_image('white_pawn2.png')
        elif c == 'B':
            self.pic = load_image('black_pawn2.png')
        else:
            Er.append('1')
        self.voz = []
        self.can_move()

    def can_move(self):
        self.voz = []
        if self.color == 'W':
            if self.cords[1] == 1:
                if c_m_p(self.cords[0], 2):
                    self.voz.append([self.cords[0], 2])
                if c_m_p(self.cords[0], 3):
                    self.voz.append([self.cords[0], 3])
            else:
                if c_m_p(self.cords[0], self.cords[1] + 1):
                    self.voz.append([self.cords[0], self.cords[1] + 1])
            if c_m_p_2([self.cords[0] + 1, self.cords[1] + 1], 'W'):
                self.voz.append([self.cords[0] + 1, self.cords[1] + 1])
            if c_m_p_2([self.cords[0] - 1, self.cords[1] + 1], 'W'):
                self.voz.append([self.cords[0] - 1, self.cords[1] + 1])
                
        elif self.color == 'B':
            if self.cords[1] == 6:
                if c_m_p(self.cords[0], 5):
                    self.voz.append([self.cords[0], 5])
                if c_m_p(self.cords[0], 4):
                    self.voz.append([self.cords[0], 4])
            else:
                if c_m_p(self.cords[0], self.cords[1] - 1):
                    self.voz.append([self.cords[0], self.cords[1] - 1])
            if c_m_p_2([self.cords[0] + 1, self.cords[1] - 1], 'B'):
                self.voz.append([self.cords[0] + 1, self.cords[1] - 1])
            if c_m_p_2([self.cords[0] - 1, self.cords[1] - 1], 'B'):
                self.voz.append([self.cords[0] - 1, self.cords[1] - 1])
        else:
            Er.append('2')
        
    def pr(self, x, y):
        D = False
        for i in range(len(self.voz)):
            if [x, y] == i:
                D = True
        return D
    

class Rook:
    def __init__(self, x, y, c):
        self.cords = [x, y]
        self.color = c
        self.ch = False
        self.v = False
        self.cost = 5
        if c == 'W':
            self.pic = load_image('white_rook2.png')
        elif c == 'B':
            self.pic = load_image('black_rook2.png')
        else:
            Er.append('1')
        self.voz = []
        self.can_move()

    def can_move(self):
        if self.color == 'W':
            self.voz = c_m_r(self)
        elif self.color == 'B':
            self.voz = c_m_r(self)
        else:
            Er.append('2')


class Elephant:
    def __init__(self, x, y, c):
        self.cords = [x, y]
        self.color = c
        self.ch = False
        self.v = False
        self.cost = 4
        if c == 'W':
            self.pic = load_image('white_elephant2.png')
        elif c == 'B':
            self.pic = load_image('black_elephant2.png')
        else:
            Er.append('1')
        self.voz = []
        self.can_move()

    def can_move(self):
        self.voz = []
        if self.color == 'W':
            self.voz = c_m_b(self)
        elif self.color == 'B':
            self.voz = c_m_b(self)
        else:
            Er.append('2')

class Queen:
    def __init__(self, x, y, c):
        self.cords = [x, y]
        self.color = c
        self.ch = False
        self.v = False
        self.cost = 9
        if c == 'W':
            self.pic = load_image('white_queen2.png')
        elif c == 'B':
            self.pic = load_image('black_queen2.png')
        else:
            Er.append('1')
        self.voz = []
        self.can_move()

    def can_move(self):
        self.voz = []
        if self.color == 'W':
            for i in c_m_b(self):
                self.voz.append(i)
            for i in c_m_r(self):
                self.voz.append(i)
        elif self.color == 'B':
            for i in c_m_b(self):
                self.voz.append(i)
            for i in c_m_r(self):
                self.voz.append(i)            
        else:
            Er.append('2')
            

class Horse:
    def __init__(self, x, y, c):
        self.cords = [x, y]
        self.color = c
        self.ch = False
        self.v = False
        self.cost = 3
        if c == 'W':
            self.pic = load_image('white_horse2.png')
        elif c == 'B':
            self.pic = load_image('black_horse2.png')
        else:
            Er.append('1')
        self.voz = []
        self.can_move()

    def can_move(self):
        self.voz = []
        if self.color == 'W':
            if c_m_p_3([self.cords[0] + 2, self.cords[1] + 1], 'W'):
                self.voz.append([self.cords[0] + 2, self.cords[1] + 1])
            if c_m_p_3([self.cords[0] + 2, self.cords[1] - 1], 'W'):
                self.voz.append([self.cords[0] + 2, self.cords[1] - 1])
            if c_m_p_3([self.cords[0] - 2, self.cords[1] + 1], 'W'):
                self.voz.append([self.cords[0] - 2, self.cords[1] + 1])
            if c_m_p_3([self.cords[0] - 2, self.cords[1] - 1], 'W'):
                self.voz.append([self.cords[0] - 2, self.cords[1] - 1])
            if c_m_p_3([self.cords[0] + 1, self.cords[1] + 2], 'W'):
                self.voz.append([self.cords[0] + 1, self.cords[1] + 2])
            if c_m_p_3([self.cords[0] + 1, self.cords[1] - 2], 'W'):
                self.voz.append([self.cords[0] + 1, self.cords[1] - 2])
            if c_m_p_3([self.cords[0] - 1, self.cords[1] + 2], 'W'):
                self.voz.append([self.cords[0] - 1, self.cords[1] + 2])
            if c_m_p_3([self.cords[0] - 1, self.cords[1] - 2], 'W'):
                self.voz.append([self.cords[0] - 1, self.cords[1] - 2])
        elif self.color == 'B':
            if c_m_p_3([self.cords[0] + 2, self.cords[1] + 1], 'B'):
                self.voz.append([self.cords[0] + 2, self.cords[1] + 1])
            if c_m_p_3([self.cords[0] + 2, self.cords[1] - 1], 'B'):
                self.voz.append([self.cords[0] + 2, self.cords[1] - 1])
            if c_m_p_3([self.cords[0] - 2, self.cords[1] + 1], 'B'):
                self.voz.append([self.cords[0] - 2, self.cords[1] + 1])
            if c_m_p_3([self.cords[0] - 2, self.cords[1] - 1], 'B'):
                self.voz.append([self.cords[0] - 2, self.cords[1] - 1])
            if c_m_p_3([self.cords[0] + 1, self.cords[1] + 2], 'B'):
                self.voz.append([self.cords[0] + 1, self.cords[1] + 2])
            if c_m_p_3([self.cords[0] + 1, self.cords[1] - 2], 'B'):
                self.voz.append([self.cords[0] + 1, self.cords[1] - 2])
            if c_m_p_3([self.cords[0] - 1, self.cords[1] + 2], 'B'):
                self.voz.append([self.cords[0] - 1, self.cords[1] + 2])
            if c_m_p_3([self.cords[0] - 1, self.cords[1] - 2], 'B'):
                self.voz.append([self.cords[0] - 1, self.cords[1] - 2])        
        else:
            Er.append('2')
            

class King:
    def __init__(self, x, y, c):
        self.cords = [x, y]
        self.color = c
        self.ch = False
        self.v = False
        self.cost = 10
        if c == 'W':
            self.pic = load_image('white_king2.png')
        elif c == 'B':
            self.pic = load_image('black_king2.png')
        else:
            Er.append('1')
        self.voz = []
        self.can_move()
    
    def can_move(self):
        NH = []
        self.voz = []
        x, y = self.cords
        for i in S:
            if i.color != self.color:
                for j in i.voz:
                    NH.append(j)
        JRt([x, y + 1], NH, self.voz)
        JRt([x, y - 1], NH, self.voz)
        JRt([x + 1, y], NH, self.voz)
        JRt([x - 1, y], NH, self.voz)        
        JRt([x + 1, y + 1], NH, self.voz)
        JRt([x + 1, y - 1], NH, self.voz)
        JRt([x - 1, y + 1], NH, self.voz)
        JRt([x - 1, y - 1], NH, self.voz)
#nik


def terminate():
    channel.stop()
    pygame.quit()
    sys.exit()
   
def start_screen():
    fon = pygame.transform.scale(pygame.image.load(os.path.join('data', "fon.jpg")), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру  
        pygame.display.flip()
        clock.tick(fps)
       
def get_cell(coords):
    x = coords[0] // 50 - 1
    y = coords[1] // 50 - 2
    if 0 <= x <= 7 and 0 <= y <= 7:
        hod(x, y)

       
class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 50
        self.top = 100
        self.cell_size = 50
       
    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size  
               
    def render(self):
        for i in range(0, self.width, 2):
            for j in range(0, self.height, 2):
                pygame.draw.rect(screen, (255, 239, 213),
                                    (self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size, self.cell_size), 0)

        for i in range(1, self.width + 1, 2):
            for j in range(0, self.height, 2):
                pygame.draw.rect(screen, (117, 51, 19),
                                    (self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size, self.cell_size), 0)
               
        for i in range(0, self.width, 2):
            for j in range(1, self.height + 1, 2):
                pygame.draw.rect(screen, (117, 51, 19),
                                    (self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size, self.cell_size), 0)
        for i in range(1, self.width + 1, 2):
            for j in range(1, self.height + 1, 2):
                pygame.draw.rect(screen, (255, 239, 213),
                                    (self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size, self.cell_size), 0)
               
        for i in range(8):
            font = pygame.font.Font(None, 30)
            text = font.render(LETTERS[i], 1, (255, 239, 213))
            screen.blit(text, (i * self.cell_size + self.left + 15, 8 * self.cell_size + self.top + 10))            
               
        for j in range(7, -1, -1):
            font = pygame.font.Font(None, 30)
            text = font.render(NUMBERS[j], 1, (255, 239, 213))
            screen.blit(text, (self.left - 30, (7 - j) * self.cell_size + self.top + 15))        
       
        pygame.draw.rect(screen, (255, 255, 255), (self.left - 40, 25,
                                                    700, 50), 1)
       
        pygame.draw.rect(screen, (255, 255, 255), (self.left - 40, self.top + 8 * self.cell_size + 50,
                                                    700, 50), 1)  
        
        pygame.draw.rect(screen, (255, 255, 255), (50, 100,
                                                    400, 400), 1)         
       
        font = pygame.font.Font(None, 50)
        text = font.render("СДАТЬСЯ", 1, (89, 40, 18))
        text_x = self.left + 9 * self.cell_size + 10
        text_y = self.top + 4 * self.cell_size - 65
        text_w = text.get_width()
        text_h = text.get_height()
        pygame.draw.rect(screen, (255, 239, 213), (text_x, text_y - 10,
                                                   text_w + 20, text_h + 20), 0)
        screen.blit(text, (text_x + 10, text_y))
       
        pygame.draw.rect(screen, (255, 255, 255), (10, 85,
                                                   9 * self.cell_size + 25, 9 * self.cell_size), 1)
       
        font = pygame.font.Font(None, 40)
        text = font.render("НОВАЯ ИГРА", 1, (89, 40, 18))
        text_y = self.top + 4 * self.cell_size + 60
        text_w = text.get_width()
        text_h = text.get_height()
        pygame.draw.rect(screen, (255, 239, 213), (text_x - 5, text_y - 10,
                                                   text_w + 20, text_h + 20), 0)  
        screen.blit(text, (text_x + 5, text_y))
        
        font = pygame.font.Font(None, 30)
        if music_playing:
            text = font.render("ВЫКЛЮЧИТЬ ЗВУК", 1, (89, 40, 18))
            difference = 0
        else:
            text = font.render("ВКЛЮЧИТЬ ЗВУК", 1, (89, 40, 18))
            difference = 16
        text_x -= 10
        text_y = self.top + 4 * self.cell_size + 5
        text_w = text.get_width()
        text_h = text.get_height()
        pygame.draw.rect(screen, (255, 239, 213), (text_x, text_y - 10,
                                                   text_w + 20 + difference, text_h + 20), 0)
        screen.blit(text, (text_x + 10 + difference / 2, text_y))
        
class Clock:
    def __init__(self):
            self.black_time = 600      
            self.white_time = 600
            self.turn = 'W'
            self.t = True
            
    def update(self):
        self.turn = H_C
        if self.t:
            if self.turn == 'W':
                self.white_time -= 1/30
            else:
                self.black_time -= 1/30
        self.render()
    
    def render(self):
        self.left = 50
        self.cell_size = 50
        font = pygame.font.Font(None, 100)
        t = int(self.black_time % 60)
        if t < 10:
            t = '0' + str(t)
        text = font.render(str(int(self.black_time // 60)) + ':' + str(t), 1, (255, 239, 213))
        text_y = 410
        text_x = self.left + 8 * self.cell_size + 85
        screen.blit(text, (text_x, text_y))
        t = int(self.white_time % 60)
        if t < 10:
            t = '0' + str(t)
        text = font.render((str(int(self.white_time // 60)) + ':' + str(t)), 1, (255, 239, 213))
        text_y = 125
        screen.blit(text, (text_x, text_y))

def render_f():
    global V
    for i in S:
        screen.blit(i.pic, (i.cords[0] * 50 + 50, i.cords[1] * 50 + 100))
    V = sorted(V, key = lambda x: x.cost)
    V_W, V_B = [], []
    for i in V:
        if i.color == 'W':
            V_W.append(i)
        else:
            V_B.append(i)
    for i in range(len(V_W)):
        screen.blit(V_W[i].pic, (50 * i + 50, 550))
    for i in range(len(V_B)):
        screen.blit(V_B[i].pic, (50 * i + 50, 25))
        
        
def finish(c):
    global running, clock, Going
    clock.t = False #Останавливает часы
    font = pygame.font.Font(None, 50)
    Going = False
    if c == 'W':
        screen.blit(font.render("Белые победили", 1, (255, 239, 213)), (500, 500))
    else:
        screen.blit(font.render("Чёрные победили", 1, (255, 239, 213)), (500, 500))
    
def restart():
    global S, clock, H_C, V, Going
    S = [Pawn(0, 1, 'W'), Pawn(1, 1, 'W'), Pawn(2, 1, 'W'), Pawn(3, 1, 'W'), Pawn(4, 1, 'W'), Pawn(5, 1, 'W'), Pawn(6, 1, 'W'), Pawn(7, 1, 'W'),
     Pawn(0, 6, 'B'), Pawn(1, 6, 'B'), Pawn(2, 6, 'B'), Pawn(3, 6, 'B'), Pawn(4, 6, 'B'), Pawn(5, 6, 'B'), Pawn(6, 6, 'B'), Pawn(7, 6, 'B'),
     Rook(0, 0, 'W'), Rook(7, 0, 'W'), Rook(0, 7, 'B'), Rook(7, 7, 'B'), Horse(1, 0, 'W'), Horse(6, 0, 'W'), Horse(1, 7, 'B'), Horse(6, 7, 'B'),
     Elephant(2, 0, 'W'), Elephant(5, 0, 'W'), Elephant(2, 7, 'B'), Elephant(5, 7, 'B'), Queen(4, 0, 'W'), Queen(4, 7, 'B'), King(3, 0, 'W'), King(3, 7, 'B')]
    V = []
    for i in S:
        i.can_move()
    clock.black_time = 600      
    clock.white_time = 600
    clock.turn = 'W'
    clock.t = True
    Going = True
    H_C = 'W'
    
def hod(x, y):
    global H_C
    if Going:
        render_f()
        L_B = False
        for i in S:
            if i.v:
                if H_C == i.color:
                    L_B = True
                    if [x, y] in i.voz:
                        for j in S:
                            if j.cords == [x, y]:
                                S.remove(j)
                                V.append(j)
                        i.cords = [x, y]
                        for j in S:
                            j.can_move()
                        if H_C == 'W':
                            H_C = 'B'
                        else:
                            H_C = 'W'                    
                        i.v = False
                    else:
                        print(False)
                        print(i.voz)
                        print([x, y])
                        i.v = False
                else:
                    i.v = False
        for i in S:
            if isinstance(i, Pawn):
                if i.color == 'B' and i.cords[1] == 0:
                    S.append(Queen(i.cords[0], i.cords[1], 'B'))
                    S.remove(i)
                if i.color == 'W' and i.cords[1] == 7:
                    S.remove(i)
                    S.append(Queen(i.cords[0], i.cords[1], 'W'))
                    
        if L_B == False:
            for i in S:
                if [x, y] == i.cords:
                    i.v = True
        render_f()
        q = True
        for i in S:
            if isinstance(i, King) and i.color == 'W':
                q = False
        if q:
            finish('B')
        q = True
        for i in S:
            if isinstance(i, King) and i.color == 'B':
                q = False
        if q:
            finish('W')        
    
V = []
S = [Pawn(0, 1, 'W'), Pawn(1, 1, 'W'), Pawn(2, 1, 'W'), Pawn(3, 1, 'W'), Pawn(4, 1, 'W'), Pawn(5, 1, 'W'), Pawn(6, 1, 'W'), Pawn(7, 1, 'W'),
     Pawn(0, 6, 'B'), Pawn(1, 6, 'B'), Pawn(2, 6, 'B'), Pawn(3, 6, 'B'), Pawn(4, 6, 'B'), Pawn(5, 6, 'B'), Pawn(6, 6, 'B'), Pawn(7, 6, 'B'),
     Rook(0, 0, 'W'), Rook(7, 0, 'W'), Rook(0, 7, 'B'), Rook(7, 7, 'B'), Horse(1, 0, 'W'), Horse(6, 0, 'W'), Horse(1, 7, 'B'), Horse(6, 7, 'B'),
     Elephant(2, 0, 'W'), Elephant(5, 0, 'W'), Elephant(2, 7, 'B'), Elephant(5, 7, 'B'), Queen(4, 0, 'W'), Queen(4, 7, 'B'), King(3, 0, 'W'), King(3, 7, 'B')]
for i in S:
    i.can_move()
Going = True
    
size = WIDTH, HEIGHT = 900, 620
screen = pygame.display.set_mode(size)
screen.fill((89, 40, 18))
music = pygame.mixer.Sound('data/We-are-the-champions.wav')
music.set_volume(0.3)
channel = pygame.mixer.Channel(0)
start_screen()
board = Board(8, 8)
time = pygame.sprite.Group()
clock = Clock()
time.draw(screen)
running = True
channel.play(music, -1)
pygame.display.flip()
music_playing = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            channel.stop()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 510 <= event.pos[0] <= 680 and 225 <= event.pos[1] <= 275:
                if H_C == 'W':
                    finish('B')
                else:
                    finish('W')
            elif 500 <= event.pos[0] <= 690 and 295 <= event.pos[1] <= 335:
                if music_playing:
                    channel.pause()
                    music_playing = False
                else:
                    channel.unpause()
                    music_playing = True
            elif 505 <= event.pos[0] <= 705 and 350 <= event.pos[1] <= 395:
                restart()
            else:
                get_cell([event.pos[0], event.pos[1]])
    clock.render()
    screen.fill((89, 40, 18))
    board.render()
    time.draw(screen)
    clock.update()
    if clock.black_time <= 1:
        finish('W')
    elif clock.white_time <= 1:
        finish('B')    
    render_f()
    pygame.display.flip()
pygame.quit()