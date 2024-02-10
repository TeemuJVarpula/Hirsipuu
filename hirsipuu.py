import pygame
import time

class Hirsipuu():
    def __init__(self):        
        pygame.init()
        self.fontti = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()
        self.miss=0
        self.correct=0
        self.c_letter=0
        self.game_cont=True
        self.word = list("karvakameli")
        self.init_screen()
        self.set_word()
        
    def init_screen(self):
        pygame.display.set_caption("Hirsipuu")           
        self.naytto = pygame.display.set_mode((640, 350))
        self.naytto.fill((0, 0, 0))
        
    def set_word(self):
        self.line=list("Arvaa sana: ")
        for i in range (0,len(self.word)):
            self.line.append("_")
        
    def check_happenings(self):
        for happening in pygame.event.get():
            if happening.type == pygame.KEYDOWN:
                if happening.key == pygame.K_a:
                    self.c_letter="a"
                if happening.key == pygame.K_b:
                   self.c_letter="b"
                if happening.key == pygame.K_c:
                   self.c_letter="c"
                if happening.key == pygame.K_d:
                   self.c_letter="d"
                if happening.key == pygame.K_e:
                   self.c_letter="e"
                if happening.key == pygame.K_f:
                   self.c_letter="f"
                if happening.key == pygame.K_g:
                   self.c_letter="g"
                if happening.key == pygame.K_h:
                   self.c_letter="h"
                if happening.key == pygame.K_i:
                   self.c_letter="i"
                if happening.key == pygame.K_j:
                   self.c_letter="j"
                if happening.key == pygame.K_k:
                   self.c_letter="k"
                if happening.key == pygame.K_l:
                   self.c_letter="l"
                if happening.key == pygame.K_m:
                   self.c_letter="m"
                if happening.key == pygame.K_n:
                   self.c_letter="n"
                if happening.key == pygame.K_o:
                   self.c_letter="o"
                if happening.key == pygame.K_p:
                   self.c_letter="p"
                if happening.key == pygame.K_q:
                   self.c_letter="q"
                if happening.key == pygame.K_r:
                   self.c_letter="r"
                if happening.key == pygame.K_s:
                   self.c_letter="s"
                if happening.key == pygame.K_t:
                   self.c_letter="t"
                if happening.key == pygame.K_u:
                   self.c_letter="u"
                if happening.key == pygame.K_v:
                   self.c_letter="v"
                if happening.key == pygame.K_w:
                   self.c_letter="w"
                if happening.key == pygame.K_x:
                   self.c_letter="x"
                if happening.key == pygame.K_y:
                   self.c_letter="y"
                if happening.key == pygame.K_z:
                   self.c_letter="z"
                if happening.key == pygame.K_ESCAPE:
                    exit()
            if happening.type == pygame.QUIT:
                exit(0)
                
    def draw_error(self):
        if self.miss==0:
            pygame.draw.circle(self.naytto, (0, 0, 255), (400, 240),50,width=2, draw_top_right=True, draw_top_left=True)
        elif self.miss==1:
            pygame.draw.circle(self.naytto, (0, 0, 255), (400, 240),50,width=2, draw_top_right=True, draw_top_left=True)
            pygame.draw.line(self.naytto, (0, 0, 255), (400, 190), (400, 50), 2)
        elif self.miss==2:
            pygame.draw.circle(self.naytto, (0, 0, 255), (400, 240),50,width=2, draw_top_right=True, draw_top_left=True)
            pygame.draw.line(self.naytto, (0, 0, 255), (400, 190), (400, 50), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (400,  50), (500, 50), 2)
        elif self.miss==3:
            pygame.draw.circle(self.naytto, (0, 0, 255), (400, 240),50,width=2, draw_top_right=True, draw_top_left=True)
            pygame.draw.line(self.naytto, (0, 0, 255), (400, 190), (400, 50), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (400,  50), (500, 50), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (400,  70), (420,50), 2)
        elif self.miss==4:
            pygame.draw.circle(self.naytto, (0, 0, 255), (400, 240),50,width=2, draw_top_right=True, draw_top_left=True)
            pygame.draw.line(self.naytto, (0, 0, 255), (400, 190), (400, 50), 2)
            
            pygame.draw.line(self.naytto, (0, 0, 255), (400,  50), (500, 50), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (400,  70), (420,50), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (500,  50), (500,100), 2)
        elif self.miss==5:
            pygame.draw.circle(self.naytto, (0, 0, 255), (400, 240),50,width=2, draw_top_right=True, draw_top_left=True)
            pygame.draw.line(self.naytto, (0, 0, 255), (400, 190), (400, 50), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (400,  50), (500, 50), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (500,  50), (500,100), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (500,  50), (500,100), 2)
            pygame.draw.circle(self.naytto, (0, 0, 255), (500, 120),20,width=2)
            pygame.draw.line(self.naytto, (0, 0, 255), (500, 140), (500,200), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (480, 160), (520,160), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (500, 200), (520,220), 2)
            pygame.draw.line(self.naytto, (0, 0, 255), (500, 200), (480,220), 2)
        
                  
    def draw_screen(self):
        self.naytto.fill((0,102,204))
    
        text = self.fontti.render(f"Hirsipuu", True, (10, 0, 0))
        self.naytto.blit(text, (10, 10))
        
        text = self.fontti.render("".join(self.line), True, (10, 0, 0))
        self.naytto.blit(text, (10, 40))
        
        text = self.fontti.render(f"Anna kirjain: ", True, (30, 0, 0))
        self.naytto.blit(text, (10, 300))
        
        if self.correct==len(self.word):
            game_cont=False
            text = self.fontti.render("".join(self.line), True, (10, 0, 0))
            self.naytto.blit(text, (10, 40))
   
            text = self.fontti.render(f"Onneksi olkoon, Arvasit sanan oikein", True, (30, 0, 0))
            self.naytto.blit(text, (100, 200))
            
        self.draw_error()  
         
        if self.miss>5:
            game_cont=False
            text = self.fontti.render(f"Peli päättyi, Arvasit liian monta kertaa väärin ", True, (30, 0, 0))
            self.naytto.blit(text, (100, 200))
            
    def check_letter(self):
        if self.c_letter in self.word:
            for i in range(0,len(self.word)):
                if self.word[i]==self.c_letter:
                    self.line[12+i]=self.c_letter
                    self.word[i]="="
                    self.correct +=1
            self.c_letter=0
                    
            print(self.correct)
        elif (self.c_letter not in self.word) and (self.c_letter!=0) and self.correct!=len(self.word):
            text = self.fontti.render(f"Kirjain ei ollut sanassa ", True, (30, 0, 0))
            self.naytto.blit(text, (100, 200))
            print("Pöö")
            self.miss +=1
            
            self.c_letter=0
                   
    def game_loop(self):
               
        while True:
            self.check_happenings()
    
            if self.game_cont==True:
                self.check_letter()
                self.draw_screen()
                self.clock.tick(10)
                pygame.display.flip()    
            else:
                print("terve")
                
                
                
if __name__ == "__main__":
    peli=Hirsipuu()
    peli.game_loop()