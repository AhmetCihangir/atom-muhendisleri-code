from random import randrange
#import pymysql
import sqlite3



class YapayZeka:
    def __init__(self):
        global cr
        super(YapayZeka,self).__init__()
        # connection = pymysql.connect(
        #     host='localhost',user='root',password='',db='karistiran',cursorclass='pymysql.cursors.DictCursor'
        # )
        connection = sqlite3.connect("all.db")
        cr = connection.cursor()
        global amebil1,amebil2,amebil3,metal1,metal2,cevap,txt,cevap5

        
        x = randrange(1,3)
        cevap5 = [] 
        if x == 1:
            sqlmetal = "SELECT * FROM elements WHERE iyon > 0 "
            sqlamebil = "SELECT * FROM elements WHERE iyon < 0 "
            global metal, amebil

            cr.execute(sqlmetal)
            metalgrup = cr.fetchall()

            cr.execute(sqlamebil)
            amebilgrup = cr.fetchall()

            metal_sayi = randrange(0,len(metalgrup))
            amebil_sayi = randrange(0,len(amebilgrup))

            metal = metalgrup[metal_sayi]
            amebil = amebilgrup[amebil_sayi]

            okuma = randrange(1,2)
            
            if okuma == 1:
                if metal[1] == "NH4":
                    metal1,metal2 = 3,2
                    if amebil[3] == -1:
                        amebil2 = 2
                        self.iyonik_yazma_1()
                    elif amebil[5] != 0:
                        ferri = randrange(1,3)
                        amebil2 = 2
                        if ferri == 1:
                            self.iyonik_yazma_1()
                            cevap1 = f"({metal[1]}){abs(amebil[3])}{amebil[1]}"
                            cevap.remove(cevap[0])
                            cevap.append(cevap1)
                        else:
                            self.iyonik_yazma_1()
                            cevap1 = f"({metal[1]}){abs(amebil[5])}{amebil[1]}"    
                            cevap.remove(cevap[0])
                            cevap.append(cevap1)
                    else:
                        amebil2 = 2
                        self.iyonik_yazma_1()
                        cevap1 = f"({metal[1]}){abs(amebil[3])}{amebil[1]}"
                        cevap.remove(cevap[0])
                        cevap.append(cevap1)

                elif amebil[5] == 0:
                    amebil3,amebil1,amebil2 = 3,3,2
                    self.iyonik_islem_yazma()
                else:
                    ferri = randrange(1,3)
                    if ferri == 1:
                        amebil3,amebil1,amebil2 = 3,3,2
                        self.iyonik_islem_yazma()
                    else:
                        amebil3,amebil1,amebil2 = 5,5,4
                        self.iyonik_islem_yazma()

            else:
                if metal[1] == "NH4":
                    metal1,metal2 = 3,2
                    if amebil[3] == -1:
                        self.iyonik_okuma_1()
                    elif amebil[5] != 0:
                        ferri = randrange(1,3)
                        if ferri == 1:
                            self.iyonik_okuma_1()
                            txt = f"{metal[1]}{abs(amebil[3])}{amebil[1]}"
                        else:
                            self.iyonik_okuma_1()
                            txt = f"{metal[1]}{abs(amebil[5])}{amebil[1]}"    
                    else:
                        self.iyonik_okuma_1()
                        txt = f"{metal[1]}{abs(amebil[3])}{amebil[1]}"
                elif amebil[5] == 0:
                    amebil3,amebil1,amebil2 = 3,3,2
                    self.iyonik_islem_okuma()
                else:
                    ferri = randrange(1,3)
                    if ferri == 1:
                        amebil3,amebil1,amebil2 = 3,3,2
                        self.iyonik_islem_okuma()
                    else:
                        amebil3,amebil1,amebil2 = 5,5,4
                        self.iyonik_islem_okuma()
        else:
            global amebil2_sayi,amebil2grup,amebilsayi_1,amebilsayi_2
            sqlamebil1 = "SELECT * FROM elements WHERE iyon < 0 "     
            sqlamebil2 = "SELECT * FROM elements WHERE iyon < 0 "   
            sqlamebil_sayi = "SELECT * FROM sayilar"   

            cr.execute(sqlamebil1)
            amebil1grup = cr.fetchall()

            cr.execute(sqlamebil2)
            amebil2grup = cr.fetchall()

            cr.execute(sqlamebil_sayi)
            sayilar = cr.fetchall()

            amebil1_sayi = randrange(0,len(amebil1grup))
            while True:
                amebil2_sayi = randrange(0,len(amebil2grup))
                if amebil1_sayi == amebil2_sayi:
                    continue
                else:
                    break

            amebilsayi_11 = randrange(0,len(sayilar))
            amebilsayi_22 = randrange(0,len(sayilar))
            amebilsayi_1 = sayilar[amebilsayi_11]
            amebilsayi_2 = sayilar[amebilsayi_22]
            amebil1 = amebil1grup[amebil1_sayi]
            amebil2 = amebil2grup[amebil2_sayi]

            okuma = randrange(1,3)
            if okuma == 1:
                self.kovalent_islem_okuma()
            else:
                self.kovalent_islem_yazma()

        self.txt = txt
        self.cevap5 = cevap5
        self.cevap = cevap
        self.answer = answer

    def kovalent_islem_yazma(self):
        global amebil1_name,amebil2_name,txt
        if amebil1[8] == "amet":
            amebil1_name = 4
            if amebil2[8] == "amet":
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_1('_12amet')
                    else:
                        self.kovalent_yazma_3('_12amet')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_2('_12amet')
                    else:
                        self.kovalent_yazma_4('_12amet')
            elif amebil1[5] != 0:
                deg = randrange(1,3)
                if deg == 1:
                    amebil2_name = 2
                else:
                    amebil2_name = 4
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_1('_1amet')
                    else:
                        self.kovalent_yazma_3('_1amet')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_2('_1amet')
                    else:
                        self.kovalent_yazma_4('_1amet')
            else:
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_1('_1amet')
                    else:
                        self.kovalent_yazma_3('_1amet')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_2('_1amet')
                    else:
                        self.kovalent_okuma_4('_1amet')
        
        elif amebil1[5] != 0:
            deg = randrange(1,3)
            if deg == 1:
                amebil1_name = 2
            else:
                amebil1_name = 4

            if amebil2[8] == "amet":
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_1('_2amet')
                    else:
                        self.kovalent_yazma_3('_2amet')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_2('_2amet')
                    else:
                        self.kovalent_yazma_4('_2amet')
            elif amebil1[5] != 0:
                deg = randrange(1,3)
                if deg == 1:
                    amebil2_name = 2
                else:
                    amebil2_name = 4
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_1('')
                    else:
                        self.kovalent_yazma_3('')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_2('')
                    else:
                        self.kovalent_yazma_4('')
            else:
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_1('')
                    else:
                        self.kovalent_yazma_3('')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_2('')
                    else:
                        self.kovalent_yazma_4('')
        
        else:
            amebil1_name = 2
            if amebil2[8] == "amet":
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_1('_2amet')
                    else:
                        self.kovalent_yazma_3('_2amet')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_2('_2amet')
                    else:
                        self.kovalent_yazma_4('_2amet')
            elif amebil1[5] != 0:
                deg = randrange(1,3)
                if deg == 1:
                    amebil2_name = 2
                else:
                    amebil2_name = 4
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_1('')
                    else:
                        self.kovalent_yazma_3('')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_2('')
                    else:
                        self.kovalent_yazma_4('')
            else:
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_1('')
                    else:
                        self.kovalent_yazma_3('')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_yazma_2('')
                    else:
                        self.kovalent_yazma_4('')
        

    def kovalent_islem_okuma(self):
        global amebil1_name,amebil2_name,txt
        if amebil1[8] == "amet":
            amebil1_name = 4
            if amebil2[8] == "amet":
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_1('_12amet')
                    else:
                        self.kovalent_okuma_3('_12amet')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_2('_12amet')
                    else:
                        self.kovalent_okuma_4('_12amet')
            elif amebil1[5] != 0:
                deg = randrange(1,3)
                if deg == 1:
                    amebil2_name = 2
                else:
                    amebil2_name = 4
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_1('_1amet')
                    else:
                        self.kovalent_okuma_3('_1amet')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_2('_1amet')
                    else:
                        self.kovalent_okuma_4('_1amet')
            else:
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_1('_1amet')
                    else:
                        self.kovalent_okuma_3('_1amet')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_2('_1amet')
                    else:
                        self.kovalent_okuma_4('_1amet')

        
        elif amebil1[5] != 0:
            deg = randrange(1,3)
            if deg == 1:
                amebil1_name = 2
            else:
                amebil1_name = 4

            if amebil2[8] == "amet":
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_1('_2amet')
                    else:
                        self.kovalent_okuma_3('_2amet')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_2('_2amet')
                    else:
                        self.kovalent_okuma_4('_2amet')
            elif amebil1[5] != 0:
                deg = randrange(1,3)
                if deg == 1:
                    amebil2_name = 2
                else:
                    amebil2_name = 4
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_1('')
                    else:
                        self.kovalent_okuma_3('')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_2('')
                    else:
                        self.kovalent_okuma_4('')
            else:
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_1('')
                    else:
                        self.kovalent_okuma_3('')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_2('')
                    else:
                        self.kovalent_okuma_4('')
        
        else:
            amebil1_name = 2
            if amebil2[8] == "amet":
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_1('_2amet')
                    else:
                        self.kovalent_okuma_3('_2amet')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_2('_2amet')
                    else:
                        self.kovalent_okuma_4('_2amet')
            elif amebil1[5] != 0:
                deg = randrange(1,3)
                if deg == 1:
                    amebil2_name = 2
                else:
                    amebil2_name = 4
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_1('')
                    else:
                        self.kovalent_okuma_3('')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_2('')
                    else:
                        self.kovalent_okuma_4('')
            else:
                amebil2_name = 2
                if amebilsayi_1[0] == 1:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_1('')
                    else:
                        self.kovalent_okuma_3('')
                else:
                    if amebilsayi_2[0] == 1:
                        self.kovalent_okuma_2('')
                    else:
                        self.kovalent_okuma_4('')
           
    def yIyonik(self,metal_id,amebil_id,type,wrong_type):
        global amebil1,amebil2,amebil3,metal1,metal2,cevap,metal,amebil
        if wrong_type == 'metal':
            sql_metal = f'SELECT * FROM elements WHERE id={metal_id} AND iyon > 0 '
            sql_amebil = f'SELECT * FROM elements WHERE id!={amebil_id} AND iyon < 0 '
        else:
            sql_metal = f'SELECT * FROM elements WHERE id!={metal_id} AND iyon > 0'
            sql_amebil = f'SELECT * FROM elements WHERE id={amebil_id} AND iyon < 0'

        cr.execute(sql_metal)
        metals = cr.fetchall()

        cr.execute(sql_amebil)
        amebils = cr.fetchall()

        metal_chooser = randrange(0,len(metals))
        amebil_chooser = randrange(0,len(amebils))

        metal = metals[metal_chooser]
        amebil = amebils[amebil_chooser]

        if type == 'o':
            if amebil[5] == 0:
                amebil3,amebil1,amebil2 = 3,3,2
                self.iyonik_islem_okuma()
            else:
                ferri = randrange(1,3)
                if ferri == 1:
                    amebil3,amebil1,amebil2 = 3,3,2
                    self.iyonik_islem_okuma()
                else:
                    amebil3,amebil1,amebil2 = 5,5,4
                    self.iyonik_islem_okuma()
            cevap = cevap[1]
        else:
            if amebil[5] == 0:
                amebil3,amebil1,amebil2 = 3,3,2
                self.iyonik_islem_yazma()
            else:
                ferri = randrange(1,3)
                if ferri == 1:
                    amebil3,amebil1,amebil2 = 3,3,2
                    self.iyonik_islem_yazma()
                else:
                    amebil3,amebil1,amebil2 = 5,5,4
                    self.iyonik_islem_yazma()
        cr.close()
        return cevap 




    def kovalent_yazma_1(self,type):
        global amebil1_name,amebil2_name,cevap,txt,cevap1,answer
        txt = f"{amebil1[amebil1_name]}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap = []
        answer = [amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2,'_KY1']
        answer.append(type)
        cevap1 = f"{amebil1[1]}{amebil2[1]}"
        cevap.append(cevap1)
    def kovalent_yazma_2(self,type):
        global amebil1_name,amebil2_name,cevap,txt,cevap1,answer
        txt = f"{amebilsayi_1[1]}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap = []
        answer = [amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2,'_KY2']    
        answer.append(type)    
        if type in ['_1amet','_12amet']:
            cevap1 = f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}"
        else:
            cevap1 = f"({amebil1[1]}){amebilsayi_1[0]}{amebil2[1]}"
        cevap.append(cevap1)
    def kovalent_yazma_3(self,type):
        global amebil1_name,amebil2_name,cevap,txt,cevap1,answer
        txt = f"{amebil1[amebil1_name]}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap = []
        answer = [amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2,'_KY3']   
        if type in ['_2amet' , '_12amet']:  
            cevap1 = f"{amebil1[1]}{amebil2[1]}{amebilsayi_2[0]}"
        else:
            cevap1 = f"{amebil1[1]}({amebil2[1]}){amebilsayi_2[0]}"
        cevap.append(cevap1)
    def kovalent_yazma_4(self,type):
        global amebil1_name,amebil2_name,cevap,txt,cevap1,answer
        txt = f"{amebilsayi_1[1]}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap = []
        answer = [amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2,'_KY4']  
        answer.append(type)
        if type == '_1amet':
            cevap1 = f"{amebil1[1]}{amebilsayi_1[0]}({amebil2[1]}){amebilsayi_2[0]}"
        elif type == '_2amet':
            cevap1 = f"({amebil1[1]}){amebilsayi_1[0]}{amebil2[1]}{amebilsayi_2[0]}"
        elif type ==  '_12amet':
            cevap1 = f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}{amebilsayi_2[0]}"
        else: 
            cevap1 = f"({amebil1[1]}){amebilsayi_1[0]}({amebil2[1]}){amebilsayi_2[0]}"
        cevap.append(cevap1)

    def kovalent_okuma_1(self,type):
        global amebil1_name,amebil2_name,cevap,txt,answer
        txt = f"{amebil1[1]}{amebil2[1]}"
        cevap = []
        answer = [amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2,'_KO1']     
        answer.append(type)   
        cevap1 = f"{amebil1[amebil1_name]}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap.append(cevap1)
        cevap2 = f"{amebil1[amebil1_name].upper()}{amebilsayi_2[1].upper()}{amebil2[amebil2_name].upper()}"
        cevap.append(cevap2)
        cevap3 = f"{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap.append(cevap3)
        cevap4 = f"{amebil1[amebil1_name]}{amebilsayi_2[1]}{amebil2[amebil2_name]}"
        cevap.append(cevap4)
    def kovalent_okuma_2(self,type):
        global amebil1_name,amebil2_name,cevap,txt,answer
        if type in ['_1amet','_12amet']:
            txt = f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}"
        else:
            txt = f"({amebil1[1]}){amebilsayi_1[0]}{amebil2[1]}"
        cevap = []
        answer = [amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2,'_KO2']    
        answer.append(type)    
        cevap1 = f"{amebilsayi_1[1]}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap.append(cevap1)
        cevap2 = f"{amebilsayi_1[1].upper()}{amebil1[amebil1_name].upper()}{amebilsayi_2[1].upper()}{amebil2[amebil2_name].upper()}"
        cevap.append(cevap2)
        cevap3 = f"{amebilsayi_1[1].lower()}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap.append(cevap3)
        cevap4 = f"{amebilsayi_1[1]}{amebil1[amebil1_name]}{amebilsayi_2[1]}{amebil2[amebil2_name]}"
        cevap.append(cevap4)
    def kovalent_okuma_3(self,type):
        global amebil1_name,amebil2_name,cevap,txt,answer
        if type in ['_2amet','_12amet']:
            txt = f"{amebil1[1]}{amebil2[1]}{amebilsayi_2[0]}"
        else:
            txt = f"{amebil1[1]}({amebil2[1]}){amebilsayi_2[0]}"
        cevap = []
        answer = [amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2,'_KO3']        
        cevap1 = f"{amebil1[amebil1_name]}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap.append(cevap1)
        cevap2 = f"{amebil1[amebil1_name].upper()}{amebilsayi_2[1].upper()}{amebil2[amebil2_name].upper()}"
        cevap.append(cevap2)
        cevap3 = f"{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap.append(cevap3)
        cevap4 = f"{amebil1[amebil1_name]}{amebilsayi_2[1]}{amebil2[amebil2_name]}"
        cevap.append(cevap4)
    def kovalent_okuma_4(self,type):
        global amebil1_name,amebil2_name,cevap,txt,answer
        answer = [amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2,'_KO4'] 
        answer.append(type)
        if type == '_1amet':
            txt = f"{amebil1[1]}{amebilsayi_1[0]}({amebil2[1]}){amebilsayi_2[0]}"
        elif type == '_2amet':
            txt = f"({amebil1[1]}){amebilsayi_1[0]}{amebil2[1]}{amebilsayi_2[0]}"
        elif type == '_12amet':
            txt = f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}{amebilsayi_2[0]}"
        else:
            txt = f"({amebil1[1]}){amebilsayi_1[0]}({amebil2[1]}){amebilsayi_2[0]}"
        cevap = []       
        cevap1 = f"{amebilsayi_1[1]}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap.append(cevap1)
        cevap2 = f"{amebilsayi_1[1].upper()}{amebil1[amebil1_name].upper()}{amebilsayi_2[1].upper()}{amebil2[amebil2_name].upper()}"
        cevap.append(cevap2)
        cevap3 = f"{amebilsayi_1[1].lower()}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        cevap.append(cevap3)
        cevap4 = f"{amebilsayi_1[1]}{amebil1[amebil1_name]}{amebilsayi_2[1]}{amebil2[amebil2_name]}"
        cevap.append(cevap4)


    def iyonik_islem_okuma(self):
        global metal1, metal2,txt,cevap
        if metal[5] > 0:
            ddm = randrange(1,3)
            if ddm == 1:
                metal2 = 2
                metal1 = 3
                if metal[3] == 1:
                    if amebil[amebil3] == -1:
                        self.iyonik_okuma_1()
                    else:
                        self.iyonik_okuma_2()
                elif metal[3] == 2:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_3_amet()
                        else:
                            self.iyonik_okuma_3()
                    elif amebil[amebil3] == -2:
                        self.iyonik_okuma_1()
                        answer.append('_IS1')
                    elif amebil[amebil3] == -4:
                        self.iyonik_okuma_2()
                        txt = f"{metal[1]}2{amebil[1]}"
                        answer.append('_IS3')
                    else:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_4_amet()
                        else:
                            self.iyonik_okuma_4()
                elif metal[3] == 4:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_3_amet()
                        else:
                            self.iyonik_okuma_3()
                    elif amebil[amebil3] == -2:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_3_amet()
                            txt = f"{metal[1]}{amebil[1]}2"
                        else:
                            self.iyonik_okuma_3()
                            txt = f"{metal[1]}({amebil[1]})2"   
                        answer.append('_IS4')
                    elif amebil[amebil3] == 4:
                        self.iyonik_okuma_1()
                        answer.append('_IS2')
                    else:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_4_amet()
                        else:
                            self.iyonik_okuma_4()
                elif metal[3] == 3 and amebil[amebil3]==3:
                    self.iyonik_okuma_1()
                    answer.append('_IS3')
                else:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_3_amet()
                        else:
                            self.iyonik_okuma_3()       
                    else:                 
                        if amebil[8] == "amet":
                            self.iyonik_okuma_4_amet()
                        else:
                            self.iyonik_okuma_4()            
            else:
                metal2 = 4
                metal1 = 5
                if metal[5] == 1:
                    if amebil[3] == -1:
                        self.iyonik_okuma_1()
                    else:
                        self.iyonik_okuma_2()
                elif metal[5] == 2:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_3_amet()
                        else:
                            self.iyonik_okuma_3()
                    elif amebil[amebil3] == -2:
                        self.iyonik_okuma_1()
                    elif amebil[amebil3] == -4:
                        self.iyonik_okuma_2()
                        txt = f"{metal[1]}2{amebil[1]}"
                    else:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_4_amet()
                        else:
                            self.iyonik_okuma_4()
                elif metal[5] == 4:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_3_amet()
                        else:
                            self.iyonik_okuma_3()
                    elif amebil[amebil3] == -2:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_3_amet()
                            txt = f"{metal[1]}{amebil[1]}2"
                        else:
                            self.iyonik_okuma_3()
                            txt = f"{metal[1]}({amebil[1]})2"   
                    elif amebil[amebil3] == -4:
                        self.iyonik_okuma_1()
                    else:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_4_amet()
                        else:
                            self.iyonik_okuma_4()
                elif metal[5] == 3 and amebil[amebil3]==3:
                    self.iyonik_okuma_1()
                else:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_okuma_3_amet()
                        else:
                            self.iyonik_okuma_3()       
                    else:                 
                        if amebil[8] == "amet":
                            self.iyonik_okuma_4_amet()
                        else:
                            self.iyonik_okuma_4()               
        else:
            metal2 = 2
            metal1 = 3
            if metal[3] == 1:
                if amebil[amebil3] == -1:
                    self.iyonik_okuma_1()
                else:
                    self.iyonik_okuma_2()
            elif metal[3] == 2:
                if amebil[amebil3] == -1:
                    if amebil[8] == "amet":
                        self.iyonik_okuma_3_amet()
                    else:
                        self.iyonik_okuma_3()
                elif amebil[amebil3] == -2:
                    self.iyonik_okuma_1()
                    answer.append('_IS1')
                elif amebil[amebil3] == -4:
                    self.iyonik_okuma_2()
                    txt = f"{metal[1]}2{amebil[1]}"
                    answer.append('_IS3')
                else:
                    if amebil[8] == "amet":
                        self.iyonik_okuma_4_amet()
                    else:
                        self.iyonik_okuma_4()
            elif metal[3] == 4:
                if amebil[amebil3] == -1:
                    if amebil[8] == "amet":
                        self.iyonik_okuma_3_amet()
                    else:
                        self.iyonik_okuma_3()
                elif amebil[amebil3] == -2:
                    if amebil[8] == "amet":
                        self.iyonik_okuma_3_amet()
                        answer.append('_IS4')
                    else:
                        self.iyonik_okuma_3()
                    txt = f"{metal[1]}2{metal[metal1]}"   
                elif amebil[amebil3] == 4:
                    self.iyonik_okuma_1()
                    answer.append('_IS2')
                else:
                    if amebil[8] == "amet":
                        self.iyonik_okuma_4_amet()
                    else:
                        self.iyonik_okuma_4()
            elif metal[3] == 3 and amebil[amebil3]==3:
                self.iyonik_okuma_1()
                answer.append('_IS5')
            else:
                if amebil[amebil3] == -1:
                    if amebil[8] == "amet":
                        self.iyonik_okuma_3_amet()
                    else:
                        self.iyonik_okuma_3()       
                else:                 
                    if amebil[8] == "amet":
                        self.iyonik_okuma_4_amet()
                    else:
                        self.iyonik_okuma_4()             



    def iyonik_islem_yazma(self):
        global metal1, metal2,txt,cevap1,cevap
        if metal[5] > 0:
            ddm = randrange(1,3)
            if ddm == 1:
                metal2 = 2
                metal1 = 3
                if metal[3] == 1:
                    if amebil[amebil3] == -1:
                        self.iyonik_yazma_1()
                    else:
                        self.iyonik_yazma_2()
                elif metal[3] == 2:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_3_amet()
                        else:
                            self.iyonik_yazma_3()
                    elif amebil[amebil3] == -2:
                        self.iyonik_yazma_1()
                    elif amebil[amebil3] == -4:
                        self.iyonik_yazma_2()
                        cevap1 = f"{metal[1]}2{amebil[1]}"
                        cevap.remove(cevap[0])
                        cevap.append(cevap1)
                    else:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_4_amet()
                        else:
                            self.iyonik_yazma_4()
                elif metal[3] == 4:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_3_amet()
                        else:
                            self.iyonik_yazma_3()
                    elif amebil[amebil3] == -2:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_3_amet()
                            cevap1 = f"{metal[1]}{amebil[1]}2"
                            cevap.remove(cevap[0])
                            cevap.append(cevap1)
                        else:
                            self.iyonik_yazma_3()
                            cevap1 = f"{metal[1]}({amebil[1]})2"   
                            cevap.remove(cevap[0])
                            cevap.append(cevap1)
                    elif amebil[amebil3] == 4:
                        self.iyonik_yazma_1()
                    else:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_4_amet()
                        else:
                            self.iyonik_yazma_4()
                elif metal[3] == 3 and amebil[amebil3]==3:
                    self.iyonik_yazma_1()
                else:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_3_amet()
                        else:
                            self.iyonik_yazma_3()       
                    else:                 
                        if amebil[8] == "amet":
                            self.iyonik_yazma_4_amet()
                        else:
                            self.iyonik_yazma_4()            
            else:
                metal2 = 4
                metal1 = 5
                if metal[5] == 1:
                    if amebil[3] == -1:
                        self.iyonik_yazma_1()
                    else:
                        self.iyonik_yazma_2()
                elif metal[5] == 2:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_3_amet()
                        else:
                            self.iyonik_yazma_3()
                    elif amebil[amebil3] == -2:
                        self.iyonik_yazma_1()
                    elif amebil[amebil3] == -4:
                        self.iyonik_yazma_2()
                        cevap1 = f"{metal[1]}2{amebil[1]}"
                        cevap.remove(cevap[0])
                        cevap.append(cevap1)
                    else:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_4_amet()
                        else:
                            self.iyonik_yazma_4()
                elif metal[5] == 4:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_3_amet()
                        else:
                            self.iyonik_yazma_3()
                    elif amebil[amebil3] == -2:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_3_amet()
                            cevap1 = f"{metal[1]}{amebil[1]}2"
                            cevap.remove(cevap[0])
                            cevap.append(cevap1)
                        else:
                            self.iyonik_yazma_3()
                            cevap1 = f"{metal[1]}({amebil[1]})2"   
                            cevap.remove(cevap[0])
                            cevap.append(cevap1)
                    elif amebil[amebil3] == -4:
                        self.iyonik_yazma_1()
                    else:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_4_amet()
                        else:
                            self.iyonik_yazma_4()
                elif metal[5] == 3 and amebil[amebil3]==3:
                    self.iyonik_yazma_1()
                else:
                    if amebil[amebil3] == -1:
                        if amebil[8] == "amet":
                            self.iyonik_yazma_3_amet()
                        else:
                            self.iyonik_yazma_3()       
                    else:                 
                        if amebil[8] == "amet":
                            self.iyonik_yazma_4_amet()
                        else:
                            self.iyonik_yazma_4()               
        else:
            metal2 = 2
            metal1 = 3
            if metal[3] == 1:
                if amebil[amebil3] == -1:
                    self.iyonik_yazma_1()
                else:
                    self.iyonik_yazma_2()
            elif metal[3] == 2:
                if amebil[amebil3] == -1:
                    if amebil[8] == "amet":
                        self.iyonik_yazma_3_amet()
                    else:
                        self.iyonik_yazma_3()
                elif amebil[amebil3] == -2:
                    self.iyonik_yazma_1()
                elif amebil[amebil3] == -4:
                    self.iyonik_yazma_2()
                    cevap1 = f"{metal[1]}2{amebil[1]}"
                    cevap.remove(cevap[0])
                    cevap.append(cevap1)
                else:
                    if amebil[8] == "amet":
                        self.iyonik_yazma_4_amet()
                    else:
                        self.iyonik_yazma_4()
            elif metal[3] == 4:
                if amebil[amebil3] == -1:
                    if amebil[8] == "amet":
                        self.iyonik_yazma_3_amet()
                    else:
                        self.iyonik_yazma_3()
                elif amebil[amebil3] == -2:
                    if amebil[8] == "amet":
                        self.iyonik_yazma_3_amet()
                    else:
                        self.iyonik_yazma_3()
                    cevap1 = f"{metal[1]}2{metal[metal1]}"   
                    cevap.remove(cevap[0])
                    cevap.append(cevap1)
                elif amebil[amebil3] == 4:
                    self.iyonik_yazma_1()
                else:
                    if amebil[8] == "amet":
                        self.iyonik_yazma_4_amet()
                    else:
                        self.iyonik_yazma_4()
            elif metal[3] == 3 and amebil[amebil3] == 3:
                self.iyonik_yazma_1()
            else:
                if amebil[amebil3] == -1:
                    if amebil[8] == "amet":
                        self.iyonik_yazma_3_amet()
                    else:
                        self.iyonik_yazma_3()       
                else:                 
                    if amebil[8] == "amet":
                        self.iyonik_yazma_4_amet()
                    else:
                        self.iyonik_yazma_4()             



    def iyonik_okuma_1(self):
        global txt,cevap,answer
        txt = f"{metal[1]}{amebil[1]}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IO1']
        cevap1 = f"{metal[metal2]}{amebil[amebil2]}"
        cevap.append(cevap1)
        cevap2 = f"{metal[metal2]}{amebil[amebil2].lower()}"
        cevap.append(cevap2)
        cevap3 = f"{metal[metal2].upper()}{amebil[amebil2].upper()}"
        cevap.append(cevap3)
        cevap4 = f"{metal[metal2].lower()}{amebil[amebil2].lower()}"
        cevap.append(cevap4)      
    def iyonik_okuma_2(self):
        global txt,cevap,answer
        txt = f"{metal[1]}{abs(amebil[amebil1])}{amebil[1]}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IO2']
        cevap1 = f"{metal[metal2]}{amebil[amebil2]}"
        cevap.append(cevap1)
        cevap2 = f"{metal[metal2]}{amebil[amebil2].lower()}"
        cevap.append(cevap2)
        cevap3 = f"{metal[metal2].upper()}{amebil[amebil2].upper()}"
        cevap.append(cevap3)
        cevap4 = f"{metal[metal2].lower()}{amebil[amebil2].lower()}"
        cevap.append(cevap4)      
    def iyonik_okuma_3(self):
        global txt,cevap,answer
        txt = f"{metal[1]}({amebil[1]}){metal[metal1]}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IO3']
        cevap1 = f"{metal[metal2]}{amebil[amebil2]}"
        cevap.append(cevap1)
        cevap2 = f"{metal[metal2]}{amebil[amebil2].lower()}"
        cevap.append(cevap2)
        cevap3 = f"{metal[metal2].upper()}{amebil[amebil2].upper()}"
        cevap.append(cevap3)
        cevap4 = f"{metal[metal2].lower()}{amebil[amebil2].lower()}"
        cevap.append(cevap4)      
    def iyonik_okuma_3_amet(self):
        global txt,cevap,answer
        txt = f"{metal[1]}{amebil[1]}{metal[metal1]}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IO3A']
        cevap1 = f"{metal[metal2]}{amebil[amebil2]}"
        cevap.append(cevap1)
        cevap2 = f"{metal[metal2]}{amebil[amebil2].lower()}"
        cevap.append(cevap2)
        cevap3 = f"{metal[metal2].upper()}{amebil[amebil2].upper()}"
        cevap.append(cevap3)
        cevap4 = f"{metal[metal2].lower()}{amebil[amebil2].lower()}"
        cevap.append(cevap4) 
    def iyonik_okuma_4(self):
        global txt,cevap,answer
        txt = f"{metal[1]}{abs(amebil[amebil1])}({amebil[1]}){metal[metal1]}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IO4']
        cevap1 = f"{metal[metal2]}{amebil[amebil2]}"
        cevap.append(cevap1)
        cevap2 = f"{metal[metal2]}{amebil[amebil2].lower()}"
        cevap.append(cevap2)
        cevap3 = f"{metal[metal2].upper()}{amebil[amebil2].upper()}"
        cevap.append(cevap3)
        cevap4 = f"{metal[metal2].lower()}{amebil[amebil2].lower()}"
        cevap.append(cevap4)      
    def iyonik_okuma_4_amet(self):
        global txt,cevap,answer
        txt = f"{metal[1]}{abs(amebil[amebil1])}{amebil[1]}{metal[metal1]}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IO4A']
        cevap1 = f"{metal[metal2]}{amebil[amebil2]}"
        cevap.append(cevap1)
        cevap2 = f"{metal[metal2]}{amebil[amebil2].lower()}"
        cevap.append(cevap2)
        cevap3 = f"{metal[metal2].upper()}{amebil[amebil2].upper()}"
        cevap.append(cevap3)
        cevap4 = f"{metal[metal2].lower()}{amebil[amebil2].lower()}"
        cevap.append(cevap4)   

    def iyonik_yazma_1(self):
        global txt,cevap,cevap1,answer
        txt = f"{metal[metal2]}{amebil[amebil2].lower()}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IY1']
        cevap1 = f"{metal[1]}{amebil[1]}"
        cevap.append(cevap1)
    def iyonik_yazma_2(self):
        global txt,cevap,cevap1,answer
        txt = f"{metal[metal2]}{amebil[amebil2].lower()}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IY2']
        cevap1 = f"{metal[1]}{abs(amebil[amebil1])}{amebil[1]}"
        cevap.append(cevap1)
    def iyonik_yazma_3(self):
        global txt,cevap,cevap1,answer
        txt = f"{metal[metal2]}{amebil[amebil2].lower()}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IY3']
        cevap1 = f"{metal[1]}({amebil[1]}){metal[metal1]}"
        cevap.append(cevap1)
    def iyonik_yazma_3_amet(self):
        global txt,cevap,cevap1,answer
        txt = f"{metal[metal2]}{amebil[amebil2].lower()}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IY3A']
        cevap1 = f"{metal[1]}{amebil[1]}{metal[metal1]}"
        cevap.append(cevap1)
    def iyonik_yazma_4(self):
        global txt,cevap,cevap1,answer
        txt = f"{metal[metal2]}{amebil[amebil2]}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IY4']
        cevap1 = f"{metal[1]}{abs(amebil[amebil1])}({amebil[1]}){metal[metal1]}"
        cevap.append(cevap1)
    def iyonik_yazma_4_amet(self):
        global txt,cevap,cevap1,answer
        txt = f"{metal[metal2]}{amebil[amebil2]}"
        cevap = []
        answer = [metal,amebil,metal2,amebil2,'_IY4A']
        cevap1 = f"{metal[1]}{abs(amebil[amebil1])}{amebil[1]}{metal[metal1]}"
        cevap.append(cevap1) 
