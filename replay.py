import numpy as np
import os
import sys
sys.path.insert(0, './src')
from colorama import Fore, Back, Style
from input import *
from time import sleep

class grid:
    def __init__(self):
        self.w = 100
        self.n = 60
        self.l = 27
        self.m = 25
        self.count = [0, 0 ,0 ,0, 0, 0, 0, 0] #[T, h, C, B, A, O, W]
        self.total = [0, 0, 0] #[B, A, O]
        self.timestep = 0
    
    def boundary(self):
        for i in range(self.n):
            self.vill[0][i] = "H"
        for i in range(1,self.m-1):
            self.vill[i][0] = "I"
            for j in range(1,self.n-1):
                self.vill[i][j] = " "
            self.vill[i][self.n-1] = "I"
        for i in range(self.n):
            self.vill[self.m-1][i] = "H"
    
    def vill_arr(self):
        self.vill = np.empty((self.l,self.n), dtype=str)
        self.type_arr = np.empty((self.l,self.n),dtype=list)
        self.pseudo_arr = [[' ' for i in range(self.n)] for j in range(self.m)]
    
    def display(self):
        for i in range(self.l):
            for j in range(self.n):
                
                    
                    
                if self.type_arr[i][j] == None:
                    print(self.vill[i][j], end="")
                elif self.type_arr[i][j][1] == "0":
                    print(Style.BRIGHT + Fore.GREEN + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "1":
                    print(Style.BRIGHT + Fore.YELLOW + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "2":
                    print(Style.BRIGHT + Fore.RED + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "3":
                    #self.vill[i][j] = " "
                    print(self.vill[i][j], end="")
                elif self.type_arr[i][j][1] == "4":
                    print(Back.GREEN + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "5":
                    print(Back.YELLOW + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "6":
                    print(Back.RED + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "7":
                    print(self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "8":
                    print(Back.WHITE + Fore.BLACK + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "9":
                    print(Style.BRIGHT + Fore.MAGENTA + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "10":
                    print(Style.BRIGHT + Fore.BLUE + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "11":
                    print(Fore.CYAN + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "12":
                    print(Style.BRIGHT + Fore.CYAN + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "13":
                    print(Style.BRIGHT + Fore.WHITE + self.vill[i][j] + Style.RESET_ALL, end="")
                else:
                    print(Back.GREEN + self.vill[i][j] + Style.RESET_ALL, end="")
            
                if i == self.l//8 and j == self.n-1:
                    print("\t\t\tBarbarian spawn: 1/2/3", end="")
                if i == ((self.l//8)+2) and j == self.n-1:
                    print("\t\t\tArcher spawn: 4/5/6", end="")
                if i == ((self.l//8)+4) and j == self.n-1:
                    print("\t\t\tBalloon spawn: 7/8/9", end="")
                if i == ((self.l//8)+6) and j == self.n-1:
                    print("\t\t\tMovement: W/A/S/D", end="")
                if i == ((self.l//8)+8) and j == self.n-1:
                    print("\t\t\tAttack: SPACEBAR", end="")
                if i == ((self.l//8)+10) and j == self.n-1:
                    print("\t\t\tSpecial Attack: E", end="")
                if i == ((self.l//8)+12) and j == self.n-1:
                    print("\t\t\tRage spell: G", end="")
                if i == ((self.l//8)+14) and j == self.n-1:
                    print("\t\t\tHeal spell: F", end="")
                if i == ((self.l//8)+16) and j == self.n-1:
                    print("\t\t\tLightning spell: V", end="")
            print()
        
grd1 = grid()
grd1.vill_arr()
grd1.boundary()

grd2 = grid()
grd2.vill_arr()
grd2.boundary()

grd3 = grid()
grd3.vill_arr()
grd3.boundary()

grd = grd1

grd_list = [grd1,grd2,grd3]

    
#m1=11, m2=14, n1=28, n2=32
class buildings:
    def __init__(self, max_hp, letter, m1, m2, n1, n2):
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.m1 = m1
        self.m2 = m2
        self.n1 = n1
        self.n2 = n2
        self.letter = letter
        self.shot = False   #only for cannon
        self.dead = False   #only for cannon
    
    def damaged(self, dmg):
        self.curr_hp -= dmg
        
    def b_display(self):
        for i in range(self.m1, self.m2):
            for j in range(self.n1, self.n2):
                #if self.letter == "X":
                #print(self.curr_hp/self.max_hp)
                #print(self.shot)
                if self.curr_hp/self.max_hp > 0.5:
                    #print("$$$")
                    grd.type_arr[i][j] = [self.letter,"0"]
                    #print(grd.type_arr[i][j])
                elif self.curr_hp/self.max_hp > 0.2:
                    grd.type_arr[i][j] = [self.letter,"1"]
                elif self.curr_hp/self.max_hp > 0:
                    grd.type_arr[i][j] = [self.letter,"2"]
                elif self.curr_hp/self.max_hp <= 0:
                    #print("$$",i,j)
                    self.dead = True
                    grd.pseudo_arr[i][j] = " " 
                    self.letter = " "
                    grd.type_arr[i][j] = [self.letter,"3"]
                    
                if self.shot == True and self.letter == "C":
                    grd.type_arr[self.m1+1][self.n1+1] = [self.letter, "8"]
                    
                if self.shot == True and self.letter == "W":
                    grd.type_arr[self.m1][self.n1] = [self.letter, "8"]
                    grd.type_arr[self.m1][self.n1+1] = [self.letter, "8"]

                grd.vill[i][j] = self.letter
                

class town_hall(buildings):
    def __init__(self):
        super().__init__(500, "T", 11, 14, 28, 32)
        grd.count[0] += 1
        for i in range(self.m1, self.m2):
            for j in range(self.n1, self.n2):
                grd.pseudo_arr[i][j] = self.letter+str(grd.count[0])
    
    def twn_display(self):
        self.b_display()
        
    def twn_damaged(self, dmg):
        self.damaged(dmg) 
               
class huts(buildings):
    def __init__(self, m1, m2, n1, n2):
        super().__init__(200, "h", m1, m2, n1, n2)
        grd.count[1] += 1
        for i in range(self.m1, self.m2):
            for j in range(self.n1, self.n2):
                grd.pseudo_arr[i][j] = self.letter+str(grd.count[1])
    
    def hut_display(self):
        self.b_display()
        
    ''' def hut_position(self):
        if grd.level == 1:
            hut1 = huts(5,8,29,31)
            hut2 = huts(9,12,21,23)
            hut3 = huts(9,12,37,39)
            hut4 = huts(14,17,23,25)
            hut5 = huts(14,17,35,37) '''
    
    def hut_damaged(self, dmg):
        self.damaged(dmg) 

class cannon(buildings):
    def __init__(self, m1, m2, n1, n2):
        super().__init__(320, "C", m1, m2, n1, n2)
        grd.count[2] += 1
        self.min_d = 1000
        self.pos = [m1+1,n1+1]
        self.min_pos = self.pos
        self.damage = 5
        self.range = 9
        for i in range(self.m1, self.m2):
            for j in range(self.n1, self.n2):
                grd.pseudo_arr[i][j] = 'C' + str(grd.count[2])
                #print(grd.pseudo_arr[i][j])
                #print(self.letter+str(grd.count[2]))
    
    def re_init(self):
        grd.count[2] += 1
        for i in range(self.m1, self.m2):
            for j in range(self.n1, self.n2):
                grd.pseudo_arr[i][j] = 'C' + str(grd.count[2])
                
    def cnn_display(self):
        if self.dead == True:
            self.shot = False
        self.b_display()
        
    def cnn_damaged(self, dmg):
        self.damaged(dmg) 
        
    def check_dist(self, targ_pos, min_d, troop_id):
        #print(self.pos, targ_pos)
        x_diff = self.pos[1] - targ_pos[1]
        y_diff = self.pos[0] - targ_pos[0]
        dist = abs(x_diff) + abs(y_diff)
        #print(dist)
        
        if dist <= self.range:
            #print(dist, end="$ ")
            if min_d <= dist:
                return min_d, self.min_pos, self.troop_select
            else:
                return dist, targ_pos, "C"+troop_id 
        else:
            #print(dist)
            return min_d, self.min_pos, self.troop_select
        
    def shoot(self):
        self.min_d = 1000
        self.min_pos = self.pos
        self.troop_select = " "
        #print(kng.pos)
        if kng.deployed == True and kng.dead == False:
            self.min_d, self.min_pos, self.troop_select = self.check_dist(kng.pos, self.min_d, "K")
            
        if qun.deployed == True and qun.dead == False:
                self.min_d, self.min_pos, self.troop_select = self.check_dist(qun.pos, self.min_d, "Q")
        for i in range(grd.count[4]):
            brb_pos = brb_arr[i].pos
            self.min_d, self.min_pos, self.troop_select = self.check_dist(brb_pos, self.min_d, "B"+str(i))
            
        for i in range(grd.count[5]):
            arc_pos = arc_arr[i].pos
            self.min_d, self.min_pos, self.troop_select = self.check_dist(arc_pos, self.min_d, "A"+str(i))
            
        if self.troop_select[0] == "C":
            if self.troop_select[1] == "K":
                kng.damaged(self.damage)
            if self.troop_select[1] == "Q":
                qun.damaged(self.damage)
            elif self.troop_select[1] == "B":
                label = int(self.troop_select[2:])
                brb_arr[label].damaged(self.damage)
                brb_arr[label].brb_display()
            elif self.troop_select[1] == "A":
                label = int(self.troop_select[2:])
                arc_arr[label].damaged(self.damage)
                arc_arr[label].arc_display()
            
        if self.min_pos != self.pos:
            #print(self.min_d)
            self.shot = True
            #print(grd.vill[self.m1+1][self.n1+1])
        else:
            self.shot = False
            
class wizard_tower(buildings):
    def __init__(self, m1, m2, n1, n2):
        super().__init__(200, "W", m1, m2, n1, n2)
        grd.count[7] += 1
        self.min_d = 1000
        self.pos = [m1+1,n1+1]
        self.min_pos = self.pos
        self.damage = 5
        self.range = 9
        for i in range(self.m1, self.m2):
            for j in range(self.n1, self.n2):
                grd.pseudo_arr[i][j] = 'W' + str(grd.count[7])
    
    def re_init(self):
        grd.count[7] += 1
        for i in range(self.m1, self.m2):
            for j in range(self.n1, self.n2):
                grd.pseudo_arr[i][j] = 'W' + str(grd.count[7])
                
    def wiz_display(self):
        if self.dead == True:
            self.shot = False
        self.b_display()
        
    def wiz_damaged(self, dmg):
        self.damaged(dmg) 
        
    def check_dist(self, targ_pos, min_d, troop_id):
        x_diff = self.pos[1] - targ_pos[1]
        y_diff = self.pos[0] - targ_pos[0]
        dist = abs(x_diff) + abs(y_diff)
        
        if dist <= self.range:
            if min_d <= dist:
                return min_d, self.min_pos, self.troop_select
            else:
                return dist, targ_pos, "C"+troop_id 
        else:
            return min_d, self.min_pos, self.troop_select
        
    def shoot(self):
        self.min_d = 1000
        self.min_pos = self.pos
        self.troop_select = " "
        #print(kng.pos)
        if kng.deployed == True and kng.dead == False:
            self.min_d, self.min_pos, self.troop_select = self.check_dist(kng.pos, self.min_d, "K")
            
        if qun.deployed == True and qun.dead == False:
            self.min_d, self.min_pos, self.troop_select = self.check_dist(qun.pos, self.min_d, "Q")
            
        for i in range(grd.count[4]):
            brb_pos = brb_arr[i].pos
            self.min_d, self.min_pos, self.troop_select = self.check_dist(brb_pos, self.min_d, "B"+str(i))
            
        for i in range(grd.count[5]):
            arc_pos = arc_arr[i].pos
            self.min_d, self.min_pos, self.troop_select = self.check_dist(arc_pos, self.min_d, "A"+str(i))
            
        for i in range(grd.count[6]):
            bln_pos = bln_arr[i].pos
            self.min_d, self.min_pos, self.troop_select = self.check_dist(bln_pos, self.min_d, "O"+str(i))   
            
        if self.troop_select[0] == "C":
            if self.troop_select[1] == "K":
                kng.damaged(self.damage)
                
            if self.troop_select[1] == "Q":
                qun.damaged(self.damage)
                
        for i in range(grd.count[4]):
            #print(brb_arr[i].pos,self.min_pos)
            if brb_arr[i].pos[0] >= self.min_pos[0]-1 and brb_arr[i].pos[0] <= self.min_pos[0]+1 and brb_arr[i].pos[1] >= self.min_pos[1]-1 and brb_arr[i].pos[1] <= self.min_pos[1]+1:
                brb_arr[i].damaged(self.damage)
                brb_arr[i].brb_display()
        for i in range(grd.count[5]):
            if arc_arr[i].pos[0] >= self.min_pos[0]-1 and arc_arr[i].pos[0] <= self.min_pos[0]+1 and arc_arr[i].pos[1] >= self.min_pos[1]-1 and arc_arr[i].pos[1] <= self.min_pos[1]+1:
                arc_arr[i].damaged(self.damage)
                arc_arr[i].arc_display()
        for i in range(grd.count[6]):
            if bln_arr[i].pos[0] >= self.min_pos[0]-1 and bln_arr[i].pos[0] <= self.min_pos[0]+1 and bln_arr[i].pos[1] >= self.min_pos[1]-1 and bln_arr[i].pos[1] <= self.min_pos[1]+1:
                bln_arr[i].damaged(self.damage)
                bln_arr[i].bln_display()
            
        if self.min_pos != self.pos:
            self.shot = True
        else:
            self.shot = False
        

class walls(buildings):
    def __init__(self, m, n):
        super().__init__(60, "X", m, m+1, n, n+1)
        #print(self.m2)
        #print(self.n2)
        
    def wll_damaged(self, dmg):
        self.damaged(dmg)

    def wll_display(self):
        self.b_display()     



class troop:
    def __init__(self, max_hp, damage, letter):
        self.dmg = damage
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.letter = letter
        self.pos = []
        self.temp_type = None
        self.temp_build = " "
        self.dead = False
        self.total = 0
    
        
    def attack(self, b_id):
        if b_id == "T1":
            twn.twn_damaged(self.dmg)
        if b_id[0] == "h":
            if len(hut_arr) >= int(b_id[1]):
                hut_arr[int(b_id[1]) - 1].hut_damaged(self.dmg)
        if b_id[0] == "C":
            if len(cnn_arr) >= int(b_id[1]):
                cnn_arr[int(b_id[1]) - 1].cnn_damaged(self.dmg)
        if b_id[0] == "W":
            if len(wiz_arr) >= int(b_id[1]):
                wiz_arr[int(b_id[1]) - 1].wiz_damaged(self.dmg)
        if b_id[0] == "X":
            label = int(b_id[1:])
            wll_arr[label].wll_damaged(self.dmg)
            wll_arr[label].wll_display()  
            
    def check_dist(self, targ_pos, min_d):
        x_diff = self.pos[1] - targ_pos[1]
        y_diff = self.pos[0] - targ_pos[0]
        dist = abs(x_diff) + abs(y_diff)
        if min_d <= dist:
            return min_d, self.min_pos
        else:
            return dist, targ_pos
               
    def damaged(self, dmg):
        self.curr_hp -= dmg
        
    def remaining(self):
        pass
        
class balloon(troop):
    def __init__(self):
        super().__init__(40,40,"O")
    
    def movement(self):
        self.min_d = max(grd.m,grd.n)*2
        self.min_pos = self.pos
        for i in range(grd.m):
            for j in range(grd.n):
                #print(grd.pseudo_arr[i][j], end="")
                if (grd.count[2] > 0 or grd.count[7] > 0):
                    if grd.pseudo_arr[i][j][0] == "C" or grd.pseudo_arr[i][j][0] == "W":
                        self.min_d, self.min_pos = self.check_dist([i,j], self.min_d)
                        
                else:
                    if grd.pseudo_arr[i][j][0] == "T" or grd.pseudo_arr[i][j][0] == "h":
                        self.min_d, self.min_pos = self.check_dist([i,j], self.min_d)
        
        self.min_x = self.pos[1] - self.min_pos[1]
        self.min_y = self.pos[0] - self.min_pos[0]
        next_block = " "
        
        if self.min_y == -1 and self.min_x == 0:
            grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
            grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
            self.pos[0] += 1
            self.temp_build = next_block[0]
            self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
            
        elif self.min_y == 1 and self.min_x == 0:
            grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
            grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
            self.pos[0] -= 1
            self.temp_build = next_block[0]
            self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
            
        elif self.min_y == 0 and self.min_x == -1:
            grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
            grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
            self.pos[1] += 1
            self.temp_build = next_block[0]
            self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
            
        elif self.min_y == 0 and self.min_x == 1:
            grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
            grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
            self.pos[1] -= 1
            self.temp_build = next_block[0]
            self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
            
        if self.min_d == 0:
            self.attack(grd.pseudo_arr[self.pos[0]][self.pos[1]])
        
        elif self.min_y < 0:
            next_block = grd.pseudo_arr[self.pos[0] + 1][self.pos[1]]
            if next_block == " ":
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[0] += 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif (next_block[0] == "T" or next_block[0] == "h" or next_block[0] == "X") and (grd.count[2] > 0 or grd.count[7] > 0):
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[0] += 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif (next_block[0] == "X") and grd.count[2] <= 0 and grd.count[7] <= 0:
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[0] += 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                    
                
            elif next_block[0] != " " and next_block[0] != "B" and next_block[0] != "K" and next_block[0] != "A" and next_block[0] != "O":
                self.attack(next_block)
            
        elif self.min_y > 0:
            next_block = grd.pseudo_arr[self.pos[0] - 1][self.pos[1]]
            if next_block == " ":
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[0] -= 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif (next_block[0] == "T" or next_block[0] == "h" or next_block[0] == "X") and (grd.count[2] > 0 or grd.count[7] > 0):
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[0] -= 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
            
            elif (next_block[0] == "X") and grd.count[2] <= 0 and grd.count[7] <= 0:
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[0] -= 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif next_block[0] != " " and next_block[0] != "B" and next_block[0] != "K" and next_block[0] != "A" and next_block[0] != "O":
                self.attack(next_block)
                
        
        elif self.min_x < 0:
            next_block = grd.pseudo_arr[self.pos[0]][self.pos[1] + 1]
            if next_block == " ":
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[1] += 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif (next_block[0] == "T" or next_block[0] == "h" or next_block[0] == "X") and (grd.count[2] > 0 or grd.count[7] > 0):
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[1] += 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
            
            elif (next_block[0] == "X") and grd.count[2] <= 0 and grd.count[7] <= 0:
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[1] += 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif next_block[0] != " " and next_block[0] != "B" and next_block[0] != "K" and next_block[0] != "A" and next_block[0] != "O":
                self.attack(next_block)
        
        elif self.min_x > 0:
            next_block = grd.pseudo_arr[self.pos[0]][self.pos[1] - 1]
            if next_block == " ":
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[1] -= 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif (next_block[0] == "T" or next_block[0] == "h" or next_block[0] == "X") and (grd.count[2] > 0 or grd.count[7] > 0):
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[1] -= 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
            
            elif (next_block[0] == "X") and grd.count[2] <= 0 and grd.count[7] <= 0:
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                grd.vill[self.pos[0]][self.pos[1]] = self.temp_build
                self.pos[1] -= 1
                self.temp_build = next_block[0]
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif next_block[0] != " " and next_block[0] != "B" and next_block[0] != "K" and next_block[0] != "A" and next_block[0] != "O":
                self.attack(next_block)
        
    def bln_display(self):
        grd.vill[self.pos[0]][self.pos[1]] = self.letter
        if self.curr_hp/self.max_hp > 0.6:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"9"]
        elif self.curr_hp/self.max_hp > 0.3:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"10"]
        elif self.curr_hp/self.max_hp > 0.2:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"11"]
        elif self.curr_hp/self.max_hp > 0.1:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"12"]
        elif self.curr_hp/self.max_hp > 0:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"13"]
        elif self.curr_hp/self.max_hp <= 0:
            self.dead = True
            self.letter = " "
            grd.vill[self.pos[0]][self.pos[1]] = self.letter
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"3"]
   
class archer(troop):
    def __init__(self):
        super().__init__(20,10,"A")
        self.range = 7
        
    def arc_attack(self, b_id):
        
        if b_id == "T1":
            twn.twn_damaged(self.dmg)
        if b_id[0] == "h":
            if len(hut_arr) >= int(b_id[1]):
                hut_arr[int(b_id[1]) - 1].hut_damaged(self.dmg)
        if b_id[0] == "C":
            if len(cnn_arr) >= int(b_id[1]):
                cnn_arr[int(b_id[1]) - 1].cnn_damaged(self.dmg)
        if b_id[0] == "W":
            if len(wiz_arr) >= int(b_id[1]):
                wiz_arr[int(b_id[1]) - 1].wiz_damaged(self.dmg)
        if b_id[0] == "X":
            label = int(b_id[1:])
            wll_arr[label].wll_damaged(self.dmg)
            wll_arr[label].wll_display()
            
    def movement(self):
        self.min_d = max(grd.m,grd.n)*2
        self.min_pos = self.pos
        for i in range(grd.m):
            for j in range(grd.n):
                if grd.pseudo_arr[i][j][0] == "T" or grd.pseudo_arr[i][j][0] == "C" or grd.pseudo_arr[i][j][0] == "h" or grd.pseudo_arr[i][j][0] == "W":                    self.min_d, self.min_pos = self.check_dist([i,j], self.min_d)

        
        if self.min_d <= self.range:
            self.arc_attack(grd.pseudo_arr[self.min_pos[0]][self.min_pos[1]])
            
        else:
            self.min_x = self.pos[1] - self.min_pos[1]
            self.min_y = self.pos[0] - self.min_pos[0]
            next_block = " "
            if self.min_y < 0:
                next_block = grd.pseudo_arr[self.pos[0] + 1][self.pos[1]]
                if next_block == " ":
                    grd.vill[self.pos[0]][self.pos[1]] = " "
                    grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                    self.pos[0] += 1
                    self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                    
                elif next_block[0] == "X":
                    self.arc_attack(next_block)
            
            elif self.min_y > 0:
                next_block = grd.pseudo_arr[self.pos[0] - 1][self.pos[1]]
                if next_block == " ":
                    grd.vill[self.pos[0]][self.pos[1]] = " "
                    grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                    self.pos[0] -= 1
                    self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                    
                elif next_block[0] == "X":
                    self.arc_attack(next_block)
                    
            
            elif self.min_x < 0:
                next_block = grd.pseudo_arr[self.pos[0]][self.pos[1] + 1]
                if next_block == " ":
                    grd.vill[self.pos[0]][self.pos[1]] = " "
                    grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                    self.pos[1] += 1
                    self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
                elif next_block[0] == "X":
                    self.arc_attack(next_block)
            
            elif self.min_x > 0:
                next_block = grd.pseudo_arr[self.pos[0]][self.pos[1] - 1]
                if next_block == " ":
                    grd.vill[self.pos[0]][self.pos[1]] = " "
                    grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                    self.pos[1] -= 1
                    self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
                elif next_block[0] == "X":
                    self.arc_attack(next_block)
                        
    def arc_display(self):
        #print("wow3")
        grd.vill[self.pos[0]][self.pos[1]] = self.letter
        #self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
        if self.curr_hp/self.max_hp > 0.6:
            #print("$$$")
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"9"]
            #print(grd.type_arr[i][j])
        elif self.curr_hp/self.max_hp > 0.3:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"10"]
        elif self.curr_hp/self.max_hp > 0.2:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"11"]
        elif self.curr_hp/self.max_hp > 0.1:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"12"]
        elif self.curr_hp/self.max_hp > 0:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"13"]
        elif self.curr_hp/self.max_hp <= 0:
            #print("$$")
            self.dead = True
            self.letter = " "
            grd.vill[self.pos[0]][self.pos[1]] = self.letter
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"3"]
                    
class barbarian(troop):
    def __init__(self):
        super().__init__(40,20,"B")
    
    def movement(self):
        self.min_d = max(grd.m,grd.n)*2
        self.min_pos = self.pos
        for i in range(grd.m):
            for j in range(grd.n):
                #print(grd.pseudo_arr[i][j], end="")
                if grd.pseudo_arr[i][j][0] == "T" or grd.pseudo_arr[i][j][0] == "C" or grd.pseudo_arr[i][j][0] == "h" or grd.pseudo_arr[i][j][0] == "W":
                    #print(grd.pseudo_arr[i][j], i, j, end=" ")
                    self.min_d, self.min_pos = self.check_dist([i,j], self.min_d)
            #print()
        
        self.min_x = self.pos[1] - self.min_pos[1]
        self.min_y = self.pos[0] - self.min_pos[0]
        next_block = " "
        if self.min_y < 0:
            next_block = grd.pseudo_arr[self.pos[0] + 1][self.pos[1]]
            if next_block == " ":
                grd.vill[self.pos[0]][self.pos[1]] = " "
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                self.pos[0] += 1
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif next_block[0] != " " and next_block[0] != "B" and next_block[0] != "K":
                self.attack(next_block)
            
        elif self.min_y > 0:
            next_block = grd.pseudo_arr[self.pos[0] - 1][self.pos[1]]
            if next_block == " ":
                grd.vill[self.pos[0]][self.pos[1]] = " "
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                self.pos[0] -= 1
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif next_block[0] != " " and next_block[0] != "B" and next_block[0] != "K":
                self.attack(next_block)
                
        
        elif self.min_x < 0:
            next_block = grd.pseudo_arr[self.pos[0]][self.pos[1] + 1]
            if next_block == " ":
                grd.vill[self.pos[0]][self.pos[1]] = " "
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                self.pos[1] += 1
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif next_block[0] != " " and next_block[0] != "B" and next_block[0] != "K":
                self.attack(next_block)
        
        elif self.min_x > 0:
            next_block = grd.pseudo_arr[self.pos[0]][self.pos[1] - 1]
            if next_block == " ":
                grd.vill[self.pos[0]][self.pos[1]] = " "
                grd.type_arr[self.pos[0]][self.pos[1]] = self.temp_type
                self.pos[1] -= 1
                self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
                
            elif next_block[0] != " " and next_block[0] != "B" and next_block[0] != "K":
                self.attack(next_block)
        
    def brb_display(self):
        #print("wow3")
        grd.vill[self.pos[0]][self.pos[1]] = self.letter
        #self.temp_type = grd.type_arr[self.pos[0]][self.pos[1]]
        if self.curr_hp/self.max_hp > 0.6:
            #print("$$$")
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"9"]
            #print(grd.type_arr[i][j])
        elif self.curr_hp/self.max_hp > 0.3:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"10"]
        elif self.curr_hp/self.max_hp > 0.2:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"11"]
        elif self.curr_hp/self.max_hp > 0.1:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"12"]
        elif self.curr_hp/self.max_hp > 0:
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"13"]
        elif self.curr_hp/self.max_hp <= 0:
            #print("$$")
            self.dead = True
            self.letter = " "
            grd.vill[self.pos[0]][self.pos[1]] = self.letter
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter,"3"]
    
class queen(troop):
    def __init__(self):
        super().__init__(80, 25, "Q")
        self.chosen = False
        self.deployed = False
        self.levi_attk = False
        self.facing = "N"     #{"N","W","S","I"}
    
    def check_dist(self, targ_pos, dist, range):
        x_diff = self.pos[1] - targ_pos[1]
        y_diff = self.pos[0] - targ_pos[0]
        
        if (self.facing == "N" and abs(x_diff) <= range and abs(y_diff-dist) <= range) or (self.facing == "S" and abs(x_diff) <= range and abs(y_diff+dist) <= range) or (self.facing == "E" and abs(x_diff+dist) <= range and abs(y_diff) <= range) or (self.facing == "W" and abs(x_diff-dist) <= range and abs(y_diff) <= range):
            #print("hamla")            
            return grd.pseudo_arr[targ_pos[0]][targ_pos[1]][0], grd.pseudo_arr[targ_pos[0]][targ_pos[1]][1:]
        else:
            return " ", "no"
            
    def queen_attack(self):
        dist = 6
        attk_range = 2
        structure_let = ""
        for i in range(grd.m):
            for j in range(grd.n):
                structure_let, b_id = self.check_dist([i,j], dist, attk_range)
                #print(structure_let)
                if structure_let == "T":
                    twn.twn_damaged(self.dmg)
                if structure_let == "h":
                    hut_arr[int(b_id) - 1].hut_damaged(self.dmg)
                if structure_let == "C":
                    cnn_arr[int(b_id) - 1].cnn_damaged(self.dmg)
                if structure_let == "W":
                    wiz_arr[int(b_id) - 1].wiz_damaged(self.dmg)
                if structure_let == "X":
                    label = int(b_id)
                    wll_arr[label].wll_damaged(self.dmg)
                    wll_arr[label].wll_display()
                    
    def queen_eagle(self):
        dist = 12
        attk_range = 4
        structure_let = ""
        for i in range(grd.m):
            for j in range(grd.n):
                structure_let, b_id = self.check_dist([i,j], dist, attk_range)
                if structure_let == "T":
                    twn.twn_damaged(self.dmg)
                if structure_let == "h":
                    hut_arr[int(b_id) - 1].hut_damaged(self.dmg)
                if structure_let == "C":
                    cnn_arr[int(b_id) - 1].cnn_damaged(self.dmg)
                if structure_let == "W":
                    wiz_arr[int(b_id) - 1].wiz_damaged(self.dmg)
                if structure_let == "X":
                    label = int(b_id)
                    wll_arr[label].wll_damaged(self.dmg)
                    wll_arr[label].wll_display()
            
    def movement(self, inp):
        self.frwd = "W"
        self.left = "A"
        self.back = "S"
        self.rght = "D"
        self.attk = " "
        self.switch = "E"
        
        if self.dead == True:
            self.deployed = False
            
        if self.deployed == True:
            
            if inp == self.frwd:
                if self.facing == "N":
                    if grd.vill[self.pos[0] - 1][self.pos[1]] == " ":
                        grd.vill[self.pos[0]][self.pos[1]] = " "
                        self.pos[0] -= 1
                    else:
                        pass
                else:
                    self.facing = "N"
            elif inp == self.left:
                if self.facing == "W":
                    if grd.vill[self.pos[0]][self.pos[1] - 1] == " ":
                        grd.vill[self.pos[0]][self.pos[1]] = " "
                        self.pos[1] -= 1
                    else:
                        pass
                else:
                    self.facing = "W"
            elif inp == self.back:
                if self.facing == "S":
                    if grd.vill[self.pos[0]+1][self.pos[1]] == " ":
                        grd.vill[self.pos[0]][self.pos[1]] = " "
                        self.pos[0] += 1
                    else:
                        pass
                else:
                    self.facing = "S"
            elif inp == self.rght:
                if self.facing == "E":
                    if grd.vill[self.pos[0]][self.pos[1] + 1] == " ":
                        grd.vill[self.pos[0]][self.pos[1]] = " "
                        self.pos[1] += 1
                    else:
                        pass
                else:
                    self.facing = "E"
                
            elif inp == self.attk:
                self.queen_attack()
        
    def health_bar(self):
        self.perc_hp = self.curr_hp/self.max_hp
        #print(self.dead)
        #print(self.perc_hp)
        for i in range(0,int(60*self.perc_hp)):
            grd.vill[26][i] = "#"
            grd.type_arr[26][i] = ["#",1] 
            
            if self.curr_hp/self.max_hp > 0.5:
                #print("$$$")
                grd.type_arr[26][i] = ["#","4"]
                #print(grd.type_arr[i][j])
            elif self.curr_hp/self.max_hp > 0.2:
                grd.type_arr[26][i] = ["#","5"]
            elif self.curr_hp/self.max_hp > 0:
                grd.type_arr[26][i] = ["#","6"]
                
        for i in range(max(0,int(60*self.perc_hp)),60):
            if self.perc_hp <= 0:
                self.dead = True
            grd.vill[26][i] = " "
            grd.type_arr[26][i] = [" ", "7"]
            
    def q_display(self):
        if self.dead == True:            
            grd.vill[self.pos[0]][self.pos[1]] = self.letter
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter, "2"]
            
        elif self.deployed == True:
            #print(kng.pos)
            grd.vill[self.pos[0]][self.pos[1]] = self.letter
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter, "7"]
                
class king(troop):
    def __init__(self):
        super().__init__(120, 50, "K")
        self.chosen = False
        self.deployed = False
        self.levi_attk = False
        self.facing = "N"     #{"N","W","S","E"}
    
    def check_dist(self, targ_pos):
        x_diff = self.pos[1] - targ_pos[1]
        y_diff = self.pos[0] - targ_pos[0]
        dist = abs(x_diff) + abs(y_diff)
        
        if dist <= self.max_dist:
            return grd.pseudo_arr[targ_pos[0]][targ_pos[1]][0], grd.pseudo_arr[targ_pos[0]][targ_pos[1]][1:]
        else:
            return " ", "no"
            
    def king_leviathan(self):
        self.max_dist = 5
        for i in range(grd.m):
            for j in range(grd.n):
                structure_let, b_id = self.check_dist([i,j])
                if structure_let == "T":
                    twn.twn_damaged(self.dmg)
                if structure_let == "h":
                    hut_arr[int(b_id) - 1].hut_damaged(self.dmg)
                if structure_let == "C":
                    cnn_arr[int(b_id) - 1].cnn_damaged(self.dmg)
                if structure_let == "W":
                    wiz_arr[int(b_id) - 1].wiz_damaged(self.dmg)
                if structure_let == "X":
                    
                    label = int(b_id)
                    wll_arr[label].wll_damaged(self.dmg)
                    wll_arr[label].wll_display()
        
    def king_attack_N(self):
        b_id = grd.pseudo_arr[kng.pos[0] - 1][kng.pos[1]]
        if b_id == "T1":
            twn.twn_damaged(self.dmg)
        if b_id[0] == "h":
            hut_arr[int(b_id[1]) - 1].hut_damaged(self.dmg)
        if b_id[0] == "C":
            cnn_arr[int(b_id[1]) - 1].cnn_damaged(self.dmg)
        if b_id[0] == "W":
                    wiz_arr[int(b_id[1]) - 1].wiz_damaged(self.dmg)
        if b_id[0] == "X":
            #print(b_id)
            #print("yay")
            label = int(b_id[1:])
            if re8.rage == True:
                wll_arr[label].wll_damaged(2*self.dmg)
            else:
                wll_arr[label].wll_damaged(self.dmg)
            wll_arr[label].wll_display()
            
    def king_attack_W(self):
        b_id = grd.pseudo_arr[kng.pos[0]][kng.pos[1] - 1]
        if b_id == "T1":
            twn.twn_damaged(self.dmg)
        if b_id[0] == "h":
            hut_arr[int(b_id[1]) - 1].hut_damaged(self.dmg)
        if b_id[0] == "C":
            cnn_arr[int(b_id[1]) - 1].cnn_damaged(self.dmg)
        if b_id[0] == "W":
                    wiz_arr[int(b_id[1]) - 1].wiz_damaged(self.dmg)
        if b_id[0] == "X":
            #print("yay")
            label = int(b_id[1:])
            if re8.rage == True:
                wll_arr[label].wll_damaged(2*self.dmg)
            else:
                wll_arr[label].wll_damaged(self.dmg)
            wll_arr[label].wll_display()
            
    def king_attack_S(self):
        b_id = grd.pseudo_arr[kng.pos[0] + 1][kng.pos[1]]
        if b_id == "T1":
            twn.twn_damaged(self.dmg)
        if b_id[0] == "h":
            hut_arr[int(b_id[1]) - 1].hut_damaged(self.dmg)
        if b_id[0] == "C":
            cnn_arr[int(b_id[1]) - 1].cnn_damaged(self.dmg)
        if b_id[0] == "W":
                    wiz_arr[int(b_id[1]) - 1].wiz_damaged(self.dmg)
        if b_id[0] == "X":
            #print("yay")
            label = int(b_id[1:])
            if re8.rage == True:
                wll_arr[label].wll_damaged(2*self.dmg)
            else:
                wll_arr[label].wll_damaged(self.dmg)
            wll_arr[label].wll_display()
    
    def king_attack_E(self):
        b_id = grd.pseudo_arr[kng.pos[0]][kng.pos[1] + 1]
        if b_id == "T1":
            twn.twn_damaged(self.dmg)
        if b_id[0] == "h":
            hut_arr[int(b_id[1]) - 1].hut_damaged(self.dmg)
        if b_id[0] == "C":
            cnn_arr[int(b_id[1]) - 1].cnn_damaged(self.dmg)
        if b_id[0] == "W":
                    wiz_arr[int(b_id[1]) - 1].wiz_damaged(self.dmg)
        if b_id[0] == "X":
            #print("yay")
            label = int(b_id[1:])
            if re8.rage == True:
                wll_arr[label].wll_damaged(2*self.dmg)
            else:
                wll_arr[label].wll_damaged(self.dmg)
            wll_arr[label].wll_display()
            
    def movement(self, inp):
        self.frwd = "W"
        self.left = "A"
        self.back = "S"
        self.rght = "D"
        self.attk = " "
        self.switch = "E"
        
        if self.dead == True:
            kng.deployed = False
            
        if kng.deployed == True:
            
            if inp == self.frwd:
                if kng.facing == "N":
                    if grd.vill[kng.pos[0] - 1][kng.pos[1]] == " ":
                        grd.vill[kng.pos[0]][kng.pos[1]] = " "
                        kng.pos[0] -= 1
                    else:
                        pass
                else:
                    kng.facing = "N"
            elif inp == self.left:
                if kng.facing == "W":
                    if grd.vill[kng.pos[0]][kng.pos[1] - 1] == " ":
                        grd.vill[kng.pos[0]][kng.pos[1]] = " "
                        kng.pos[1] -= 1
                    else:
                        pass
                else:
                    kng.facing = "W"
            elif inp == self.back:
                if kng.facing == "S":
                    if grd.vill[kng.pos[0]+1][kng.pos[1]] == " ":
                        grd.vill[kng.pos[0]][kng.pos[1]] = " "
                        kng.pos[0] += 1
                    else:
                        pass
                else:
                    kng.facing = "S"
            elif inp == self.rght:
                if kng.facing == "D":
                    if grd.vill[kng.pos[0]][kng.pos[1] + 1] == " ":
                        grd.vill[kng.pos[0]][kng.pos[1]] = " "
                        kng.pos[1] += 1
                    else:
                        pass
                else:
                    kng.facing = "D"
            elif inp == self.switch:
                self.levi_attk = not self.levi_attk
                
            elif inp == self.attk:
                if self.levi_attk == True:
                    self.king_leviathan()
                else:
                    if kng.facing == "N":
                        if grd.vill[kng.pos[0] - 1][kng.pos[1]] != " ":
                            self.king_attack_N()
                    
                    elif kng.facing == "W":
                        if grd.vill[kng.pos[0]][kng.pos[1] - 1] != " ":
                            self.king_attack_W()
                    
                    elif kng.facing == "S":
                        if grd.vill[kng.pos[0] + 1][kng.pos[1]] != " ":
                            self.king_attack_S()
                            
                    elif kng.facing == "D":
                        if grd.vill[kng.pos[0]][kng.pos[1] + 1] != " ":
                            self.king_attack_E()
        
    def health_bar(self):
        self.perc_hp = self.curr_hp/self.max_hp
        #print(self.dead)
        #print(self.perc_hp)
        for i in range(0,int(60*self.perc_hp)):
            grd.vill[26][i] = "#"
            grd.type_arr[26][i] = ["#",1] 
            
            if self.curr_hp/self.max_hp > 0.5:
                #print("$$$")
                grd.type_arr[26][i] = ["#","4"]
                #print(grd.type_arr[i][j])
            elif self.curr_hp/self.max_hp > 0.2:
                grd.type_arr[26][i] = ["#","5"]
            elif self.curr_hp/self.max_hp > 0:
                grd.type_arr[26][i] = ["#","6"]
                
        for i in range(max(0,int(60*self.perc_hp)),60):
            if self.perc_hp <= 0:
                self.dead = True
            grd.vill[26][i] = " "
            grd.type_arr[26][i] = [" ", "7"]
            
    def k_display(self):
        if self.dead == True:            
            grd.vill[self.pos[0]][self.pos[1]] = self.letter
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter, "2"]
            
        elif self.deployed == True:
            #print(kng.pos)
            grd.vill[self.pos[0]][self.pos[1]] = self.letter
            grd.type_arr[self.pos[0]][self.pos[1]] = [self.letter, "7"]



class village():
    def __init__(self):
        self.win = False
        self.lose = False
        self.rage = False
        self.lvl = 1
        """ grd.vill_arr()
        grd.boundary() """
    
    def wll_init(self, m1, m2, n1, n2):
        for i in range(m1, m2):
            for j in range(n1, n2):
                wll_arr.append(walls(i,j))
                grd.pseudo_arr[i][j] = wll_arr[grd.count[3]].letter+str(grd.count[3])
                grd.count[3] += 1
                #print(grd.count[3])
    
    def display_all(self):
        twn.twn_display()
        for i in range(grd.count[1]):
            hut_arr[i].hut_display()
        for i in range(grd.count[2]):
            cnn_arr[i].cnn_display()
        for i in range(grd.count[7]):
            wiz_arr[i].wiz_display()
        for i in range(grd.count[3]):
            wll_arr[i].wll_display()
        for i in range(grd.count[4]):
            brb_arr[i].brb_display()
        for i in range(grd.count[5]):
            arc_arr[i].arc_display()
        for i in range(grd.count[6]):
            bln_arr[i].bln_display()
        if kng.chosen == True:
            kng.health_bar()
            kng.k_display()
        elif qun.chosen == True:
            qun.health_bar()
            qun.q_display()
        grd.display()
    
    
    def spawning(self, inp):
        if kng.chosen == True and kng.deployed == False and kng.dead == False:
            if inp == "1":
                kng.pos = [int(grd.m/2),1]
                kng.deployed = True
                kng.facing = "E"
                #kng.k_display()
            elif inp == "2":
                kng.pos = [1,int(grd.n/2)]
                kng.deployed = True
                kng.facing = "S"
                #kng.k_display()
            elif inp == "3":
                kng.pos = [int(grd.m/2),grd.n-2]
                kng.deployed = True
                kng.facing = "W"
                #kng.k_display()
            
        elif qun.chosen == True and qun.deployed == False and qun.dead == False:
            if inp == "4":
                qun.pos = [int(grd.m/2),1]
                qun.deployed = True
                qun.facing = "E"
                #qun.k_display()
            elif inp == "5":
                qun.pos = [1,int(grd.n/2)]
                qun.deployed = True
                qun.facing = "S"
                #qun.k_display()
            elif inp == "6":
                qun.pos = [int(grd.m/2),grd.n-2]
                qun.deployed = True
                qun.facing = "W"
                #qun.k_display()
                
        else:
            if (inp == "1" or inp == "2" or inp == "3") and grd.total[0] < 5:
                brb_arr.append(barbarian())
                grd.count[4] += 1
                grd.total[0] += 1
                brb = brb_arr[grd.count[4] - 1]
                if inp == "1":
                    brb.pos = [int(grd.m/2),1]
                elif inp == "2":
                    brb.pos = [1,int(grd.n/2)]
                elif inp == "3":
                    brb.pos = [int(grd.m/2),grd.n-2]
            
            elif (inp == "4" or inp == "5" or inp == "6") and grd.total[1] < 2:
                arc_arr.append(archer())
                grd.count[5] += 1
                grd.total[1] += 1
                arc = arc_arr[grd.count[5] - 1]
                
                
                if inp == "4":
                    arc.pos = [int(grd.m/2),1]
                elif inp == "5":
                    arc.pos = [1,int(grd.n/2)]
                elif inp == "6":
                    arc.pos = [int(grd.m/2),grd.n-2]
                    
            elif (inp == "7" or inp == "8" or inp == "9") and grd.total[2] < 2:
                bln_arr.append(balloon())
                grd.count[6] += 1
                grd.total[2] += 1
                bln = bln_arr[grd.count[6] - 1]
                
                
                if inp == "7":
                    bln.pos = [int(grd.m/2),1]
                elif inp == "8":
                    bln.pos = [1,int(grd.n/2)]
                elif inp == "9":
                    bln.pos = [int(grd.m/2),grd.n-2]
    
    def endgame(self):
        if twn.curr_hp <= 0 and len(cnn_arr) == 0 and len(wiz_arr) == 0:
            self.win = True
            for i in range(grd.count[1]):
                if hut_arr[i].curr_hp > 0:
                    self.win = False
                
        if self.win == True:
            return 1
        
        if (kng.chosen == True and kng.curr_hp <= 0) or (qun.chosen == True and qun.curr_hp <= 0):
            self.lose = True
            if len(brb_arr) > 0:
                self.lose = False
                
        if self.lose == True:
            return -3
        
    def get_inp(self):
        inp = ""
        eagle_tstep = 0
        eagle_shot = False
        troop_speed = 2
        def_speed = 4
        
        print("Press number of the replay needed in this session...")
        while True:
            rep_num = input_to(Get())
            if rep_num != None:
                break

        print("Replay Number: ", rep_num)
        rep_num = int(rep_num)
        inp = ""
        with open("replays/output.txt", "r") as f:
            lines = f.readlines()
        count = 0
        b = 0
        while (count != rep_num-1):
            jin = str(lines[b][0])
            if jin == "E":
                count += 1
            b += 1
        line = b
        while inp != "0":
            ''' os.system("cls" if os.name == "nt" else "clear")
            self.display_all()
            if self.endgame():
                break
            grd.count[3] = 0
            #print(grd.pseudo_arr[11,28][1])
            #print(grd.count)
            inp = str(lines[line][0])
            line += 1
            sleep(0.25)
            with open("replays/output.txt", "a") as f:
                f.write(str(inp))
                f.write("\n") '''
            
            
            if True:
                os.system("cls" if os.name == "nt" else "clear")
                print("Level:", level)
                print()
                self.display_all()
                print("\nNumber of troop remaining:")
                print("Barbarians: ", 5 - grd.total[0], end="\t\t")
                print("Archers: ", 2 - grd.total[1], end="\t\t")
                print("Balloons: ", 2 - grd.total[2])
                print("Alive:", grd.count[4], end="\t\t")
                print("Alive:", grd.count[5], end="\t\t")
                print("Alive:", grd.count[6])
                if self.endgame():
                    break
                grd.count[3] = 0
                inp = str(lines[line][0])
                line += 1
                sleep(0.25)
                if eagle_shot == True and (grd.timestep - eagle_tstep) == 4:
                    qun.queen_eagle()
                    eagle_shot = False
                   
                if inp == "1" or inp == "2" or inp == "3" or inp == "4" or inp == "5" or inp == "6" or inp == "7" or inp =="8" or inp =="9":
                    self.spawning(inp)
                elif inp == "W" or inp == "A" or inp == "S" or inp == "D" or inp == "E" or inp ==" ":
                    if kng.chosen == True:
                        kng.movement(inp)
                        ''' if self.rage == True:
                            kng.movement(inp) '''
                            
                    if qun.chosen == True:
                        if inp == "E":
                            eagle_tstep = grd.timestep
                            eagle_shot = True
                        qun.movement(inp)
                        ''' if self.rage == True:
                            qun.movement(inp) '''
                    
                elif inp == "F":
                    if kng.chosen == True:
                        heal = kng.curr_hp*0.5
                        if kng.curr_hp*1.5 <= kng.max_hp:
                            kng.damaged(-1*heal)
                        else:
                            kng.damaged(kng.curr_hp - kng.max_hp)
                    elif qun.chosen == True:
                        heal = qun.curr_hp*0.5
                        if qun.curr_hp*1.5 <= qun.max_hp:
                            qun.damaged(-1*heal)
                        else:
                            qun.damaged(qun.curr_hp - qun.max_hp)
                            
                    for i in range(grd.count[4]):
                        heal = brb_arr[i].curr_hp*0.5
                        if brb_arr[i].curr_hp*1.5 <= brb_arr[i].max_hp:
                            brb_arr[i].damaged(-1*heal)
                        else:
                            brb_arr[i].damaged(brb_arr[i].curr_hp - brb_arr[i].max_hp)
                            
                    for i in range(grd.count[5]):
                        heal = arc_arr[i].curr_hp*0.5
                        if arc_arr[i].curr_hp*1.5 <= arc_arr[i].max_hp:
                            arc_arr[i].damaged(-1*heal)
                        else:
                            arc_arr[i].damaged(arc_arr[i].curr_hp - arc_arr[i].max_hp)
                            
                    for i in range(grd.count[6]):
                        heal = bln_arr[i].curr_hp*0.5
                        if bln_arr[i].curr_hp*1.5 <= bln_arr[i].max_hp:
                            bln_arr[i].damaged(-1*heal)
                        else:
                            bln_arr[i].damaged(bln_arr[i].curr_hp - bln_arr[i].max_hp)
                            
                elif inp == "G":
                    self.rage = True
                    troop_speed = 1
                    kng.dmg *= 2
                    qun.dmg *= 2
                    
                elif inp == "V":
                    twn.twn_damaged(twn.curr_hp/3)
                    for hut in hut_arr:
                        hut.hut_damaged(hut.curr_hp/3)
                    for cnn in cnn_arr:
                        cnn.cnn_damaged(cnn.curr_hp/3)
                    for wiz in wiz_arr:
                        wiz.wiz_damaged(wiz.curr_hp/3)
                        
                brb = 0
                arc = 0
                bln = 0
                cnn = 0
                wiz = 0
                if grd.timestep%troop_speed == 0:
                    while arc < grd.count[5]:
                        #print(grd.count[4], brb)
                        if arc_arr[arc].dead == True:
                            #print("$",brb)
                            arc_arr.pop(arc)
                            grd.count[5] -= 1
                            continue
                        arc_arr[arc].movement()
                        arc += 1 
                        
                    while bln < grd.count[6]:
                        if bln_arr[bln].dead == True:
                            bln_arr.pop(brb)
                            grd.count[6] -= 1
                            continue
                        bln_arr[bln].movement()
                        bln += 1
                        
                if grd.timestep%(troop_speed*2) == 0:
                    while brb < grd.count[4]:
                        if brb_arr[brb].dead == True:
                            brb_arr.pop(brb)
                            grd.count[4] -= 1
                            continue
                        brb_arr[brb].movement()
                        brb += 1
                if grd.timestep%(def_speed) == 0:
                    while cnn < grd.count[2]:
                        if cnn_arr[cnn].dead == True:
                            cnn_arr.pop(cnn)
                            temp = grd.count[2] - 1
                            grd.count[2] = 0
                            for j in range(temp):
                                cnn_arr[j].re_init()
                            
                            continue
                        cnn_arr[cnn].shoot()
                        cnn += 1
                    while wiz < grd.count[7]:
                        if wiz_arr[wiz].dead == True:
                            wiz_arr.pop(wiz)
                            temp = grd.count[7] - 1
                            grd.count[7] = 0
                            for j in range(temp):
                                wiz_arr[j].re_init()
                            
                            continue
                        wiz_arr[wiz].shoot()
                        wiz += 1
                        
            grd.timestep += 1
        return -3

result = 0
level = 0
hero =""
for i in range(3):
    level += 1
    grd  = grd_list[i]
    
    twn = town_hall()

    if i == 0:
        hut1 = huts(5,8,29,31)
        hut2 = huts(9,12,21,23)
        hut3 = huts(9,12,37,39)
        hut4 = huts(14,17,23,25)
        hut5 = huts(14,17,35,37)
        hut_arr = [hut1, hut2, hut3, hut4, hut5]

        cnn1 = cannon(6,9,23,26)
        cnn2 = cannon(6,9,34,37)
        cnn3 = cannon(13,16,19,22)
        cnn4 = cannon(13,16,38,41)
        cnn_arr = [cnn1, cnn2, cnn3, cnn4]

        wiz1 = wizard_tower(4,7,18,20)
        wiz2 = wizard_tower(4,7,40,42)
        wiz_arr = [wiz1, wiz2]
            
    elif i == 1:
        hut1 = huts(5,8,29,31)
        hut2 = huts(9,12,21,23)
        hut3 = huts(9,12,37,39)
        hut4 = huts(14,17,23,25)
        hut5 = huts(14,17,35,37)
        hut_arr = [hut1, hut2, hut3, hut4, hut5]

        cnn1 = cannon(6,9,23,26)
        cnn2 = cannon(6,9,34,37)
        cnn3 = cannon(13,16,19,22)
        cnn4 = cannon(13,16,38,41)
        cnn_arr = [cnn1, cnn2, cnn3, cnn4]

        wiz1 = wizard_tower(4,7,18,20)
        wiz2 = wizard_tower(4,7,40,42)
        wiz3 = wizard_tower(16,19,29,31)
        wiz_arr = [wiz1, wiz2, wiz3]
        
    elif i == 2:
        hut1 = huts(5,8,29,31)
        hut2 = huts(9,12,21,23)
        hut3 = huts(9,12,37,39)
        hut4 = huts(14,17,23,25)
        hut5 = huts(14,17,35,37)
        hut_arr = [hut1, hut2, hut3, hut4, hut5]

        cnn1 = cannon(6,9,23,26)
        cnn2 = cannon(6,9,34,37)
        cnn3 = cannon(13,16,19,22)
        cnn4 = cannon(13,16,38,41)
        cnn5 = cannon(18,21,13,16)
        cnn6 = cannon(18,21,44,47)
        cnn_arr = [cnn1, cnn2, cnn3, cnn4, cnn5, cnn6]

        wiz1 = wizard_tower(4,7,18,20)
        wiz2 = wizard_tower(4,7,40,42)
        wiz3 = wizard_tower(16,19,29,31)
        wiz_arr = [wiz1, wiz2, wiz3]
        
    wll_arr = []
    kng = king()
    qun = queen()
    brb_arr = []
    arc_arr = []
    bln_arr = []
    
    re8 = village()
    re8.wll_init(9,10,25,35)
    re8.wll_init(10,14,25,26)
    re8.wll_init(10,14,34,35)
    re8.wll_init(13,17,26,27)
    re8.wll_init(13,17,33,34)
    re8.wll_init(15,16,27,34)

    re8.wll_init(12,13,17,25)
    re8.wll_init(4,5,21,39)
    re8.wll_init(8,12,17,18)
    re8.wll_init(8,9,17,22)
    re8.wll_init(4,8,21,22)

    re8.wll_init(12,13,35,43)
    re8.wll_init(8,12,42,43)
    re8.wll_init(8,9,38,42)
    re8.wll_init(4,8,38,39)

    re8.wll_init(13,18,17,18)
    re8.wll_init(17,18,18,27)

    re8.wll_init(13,18,42,43)
    re8.wll_init(17,18,33,42)

    #re8.wll_init(5,20,5,55)

    if level == 1:
        hero = input("Choose King[K] or Queen[Q]\n")
    
    if hero == "K":
        kng.chosen = True
    elif hero == "Q":
        qun.chosen = True   
                      
    result += re8.get_inp()
    os.system("cls" if os.name == "nt" else "clear")
    re8.display_all()
    if result < 0:
        print(Style.BRIGHT + Back.WHITE + Fore.RED + " _  _  __   _  _    __     __   ____  ____ ")
        print("( \/ )/  \ / )( \  (  )   /  \ / ___)(  __)")
        print(" )  /(  O )) \/ (  / (_/\(  O )\___ \ ) _) ")
        print("(__/  \__/ \____/  \____/ \__/ (____/(____)" + Style.RESET_ALL) 
        break
    
    elif result == 3:
        print(Style.BRIGHT + Back.WHITE + Fore.GREEN + " _  _  __   _  _    _  _  __  __ _ ")
        print("( \/ )/  \ / )( \  / )( \(  )(  ( \\")
        print(" )  /(  O )) \/ (  \ /\ / )( /    /")
        print("(__/  \__/ \____/  (_/\_)(__)\_)__)" + Style.RESET_ALL)
    

        