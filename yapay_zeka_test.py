import yapay_zeka
from random import choices


class YapayZekaTest():

   def __init__(self):
      global diziler,fonksiyonlar,answer
      super().__init__()
      self.YapayZeka = yapay_zeka.YapayZeka()
      answer = self.YapayZeka.answer
      cevap = self.YapayZeka.cevap
      txt = self.YapayZeka.txt
        
      diziler = {
            'simpli' : ['_IS1','_IS2','_IS3','_IS4','_IS5'],
            'iyonik' : ['_IO1','_IO2','_IO3','_IO3A','_IO4','_IO4A','_IY1','_IY2','_IY3','_IY3A','_IY4','_IY4A'],
            'kovalent' : ['_KO1','_KO2','_KO3','_KO4','_KY1','_KY2','_KY3','_KY4']
            }

      fonksiyonlar = {
            'iyonik' : self.iyonik_question,
            'kovalent' : self.kovalent_question,
            'kovalent_answers_ko': self.kovalent_question_answers_ko,
            'kovalent_answers_ky' : self.kovalent_question_answers_ky,
            'iyonik_answers_io': self.iyonik_question_answers_io,
            'iyonik_answers_iy': self.iyonik_question_answers_iy,
        }

      sade = list(filter(lambda a : a in diziler['simpli'],answer))
      if sade == []:
         iyonik_mi = list(filter(lambda a : a in diziler['iyonik'],answer))
         if iyonik_mi != []:
            answers = fonksiyonlar['iyonik'](iyonik_mi)
         else:
            answers = fonksiyonlar['kovalent']()

      self.txt = txt
      self.cevap = cevap
      self.answers = choices(answers,k=3)
      

 # Ana Kısım 
    
   def iyonik_question(self,iyonik):
      if iyonik[0] in ['_IO1','_IO2','_IO3','_IO4']:
         answers = fonksiyonlar['iyonik_answers_io']()
      else:
         answers = fonksiyonlar['iyonik_answers_iy']()
      return answers

   def kovalent_question(self):
      kovalent = list(filter(lambda a : a in diziler['kovalent'],answer))
      type = list(filter(lambda a : a in ['_1amet','_2amet','_12amet'],answer))


      if type != []:type = type[0]
      
      if kovalent[0] in ['_KO1','_KO2','_KO3','_KO4'] :
         answers = fonksiyonlar['kovalent_answers_ko'](type,kovalent[0])
      else:
         answers = fonksiyonlar['kovalent_answers_ky'](type,kovalent[0])
      return answers
        

    
 # Kovalent Kısmı 
    
    # '_1amet' , '_2amet' , '_12amet'
    #answer = [amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2,'_KO2'] 



   def kovalent_question_answers_ko(self,type,kovalent):
        answers = []
        amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2 = answer[0],answer[1],answer[2],answer[3],answer[4],answer[5]


        #f"{amebilsayi_1[1]}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
        if kovalent in ['_KO4','_KO2']:
         # Sayi bolumu
            #Sayi yok

            answer_1 = f"{amebil1[amebil1_name]}{amebil2[amebil2_name].lower()}"
            answers.append(answer_1)

            #Sayi degisik
            #answer_2 kapali
            # answer_2 = f"{amebilsayi_2[1]}{amebil1[amebil1_name].lower()}{amebilsayi_1[1].lower()}{amebil2[amebil2_name].lower()}"
            # answers.append(answer_2)

            #Sayi 1 yok

            answer_3 = f"{amebil1[amebil1_name]}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
            answers.append(answer_3)

            #Sayi 2 yok

            answer_4 = f"{amebilsayi_1[1]}{amebil1[amebil1_name].lower()}{amebil2[amebil2_name].lower()}"
            answers.append(answer_4)
        
         #Element Bolumu
            # Element degisik
            
            answer_5 = f"{amebilsayi_1[1]}{amebil2[amebil2_name].lower()}{amebilsayi_2[1].lower()}{amebil1[amebil1_name].lower()}"
            answers.append(answer_5)
        
         # Hem Element Hem Sayi

            # Element Degisik Sayi yok
            
            answer_6 = f"{amebil2[amebil2_name]}{amebil1[amebil1_name].lower()}"
            answers.append(answer_6)
        
         # Ametal 

            if type == '_1amet':
                if amebil1_name == 2 : amebil1_ = 4
                if amebil1_name == 4 : amebil1_ = 2

                answer_7 = f"{amebilsayi_1[1]}{amebil1[amebil1_].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
                answers.append(answer_7)
                answer_8 = f"{amebilsayi_1[1]}{amebil2[amebil2_name].lower()}{amebilsayi_2[1].lower()}{amebil1[amebil1_].lower()}"
                answers.append(answer_8)
            
            elif type == '_2amet':
                if amebil2_name == 2 : amebil2_ = 4
                if amebil2_name == 4 : amebil2_ = 2

                answer_7 = f"{amebilsayi_1[1]}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_].lower()}"
                answers.append(answer_7)
                answer_8 = f"{amebilsayi_1[1]}{amebil2[amebil2_].lower()}{amebilsayi_2[1].lower()}{amebil1[amebil1_name].lower()}"
                answers.append(answer_8)

            elif type == '_12amet': 
                if amebil1_name == 2 : amebil1_ = 4
                if amebil1_name == 4 : amebil1_ = 2
                if amebil2_name == 2 : amebil2_ = 4
                if amebil2_name == 4 : amebil2_ = 2

                answer_7 = f"{amebilsayi_1[1]}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_].lower()}"
                answers.append(answer_7)
                answer_8 = f"{amebilsayi_1[1]}{amebil2[amebil2_].lower()}{amebilsayi_2[1].lower()}{amebil1[amebil1_name].lower()}"
                answers.append(answer_8)
                answer_9 = f"{amebilsayi_1[1]}{amebil1[amebil1_].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_].lower()}"
                answers.append(answer_9)
                answer_10 = f"{amebilsayi_1[1]}{amebil2[amebil2_].lower()}{amebilsayi_2[1].lower()}{amebil1[amebil1_].lower()}"
                answers.append(answer_10)
                answer_11 = f"{amebilsayi_1[1]}{amebil1[amebil1_].lower()}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
                answers.append(answer_11)
                answer_12 = f"{amebilsayi_1[1]}{amebil2[amebil2_name].lower()}{amebilsayi_2[1].lower()}{amebil1[amebil1_].lower()}"
                answers.append(answer_12)
        else:
         #f"{amebil1[amebil1_name]}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
         #Sayi bolumu

            # Sayi yok
            answer_1 = f"{amebil1[amebil1_name]}{amebil2[amebil2_name].lower()}"
            answers.append(answer_1)

            #Sayi degisik
            #answer_2 kapali
            # answer_2 =f"{amebilsayi_2[1]}{amebil1[amebil1_name].lower()}{amebil2[amebil2_name].lower()}"
            # answers.append(answer_2)

            #Sayi sonda
            answer_3 =f"{amebil1[amebil1_name]}{amebil2[amebil2_name].lower()}{amebilsayi_2[1].lower()}"
            answers.append(answer_3)
        
         #Element Bolumu

            answer_4 =f"{amebil2[amebil2_name]}{amebilsayi_2[1].lower()}{amebil1[amebil1_name].lower()}"
            answers.append(answer_4)

         #Hem Element Hem Sayi Bolumu

            # Sayi yok Yer degisik
            answer_5 = f"{amebil2[amebil2_name]}{amebil1[amebil1_name].lower()}"
            answers.append(answer_5)

            #Sayi sonda Yer degisik
            answer_6 = f"{amebil2[amebil2_name]}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}"
            answers.append(answer_6)

            #Sayi basta Yer degisik
            answer_7 = f"{amebilsayi_2[1]}{amebil2[amebil2_name].lower()}{amebil1[amebil1_name].lower()}"
            answers.append(answer_7)

         #Ametal
            if type == '_1amet':
                if amebil1_name == 2 : amebil1_ = 4
                if amebil1_name == 4 : amebil1_ = 2
                # Sayi yok Yer degisik
                answer_8 = f"{amebil2[amebil2_name]}{amebil1[amebil1_].lower()}"
                answers.append(answer_8)

                #Sayi sonda Yer degisik
                answer_9 = f"{amebil2[amebil2_name]}{amebil1[amebil1_].lower()}{amebilsayi_2[1].lower()}"
                answers.append(answer_9)

                #Sayi basta Yer degisik
                answer_10 = f"{amebilsayi_2[1]}{amebil2[amebil2_name].lower()}{amebil1[amebil1_].lower()}"
                answers.append(answer_10)

                # Amet y
                answer_11 = f"{amebil1[amebil1_]}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
                answers.append(answer_11)

            elif type == '_2amet' :
                if amebil2_name == 2 : amebil2_ = 4
                if amebil2_name == 4 : amebil2_ = 2
                # Sayi yok Yer degisik
                answer_8 = f"{amebil2[amebil2_]}{amebil1[amebil1_name].lower()}"
                answers.append(answer_8)

                #Sayi sonda Yer degisik
                answer_9 = f"{amebil2[amebil2_]}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}"
                answers.append(answer_9)

                #Sayi basta Yer degisik
                answer_10 = f"{amebilsayi_2[1]}{amebil2[amebil2_].lower()}{amebil1[amebil1_name].lower()}"
                answers.append(answer_10)

                # Amet y
                answer_11 = f"{amebil1[amebil1_name]}{amebilsayi_2[1].lower()}{amebil2[amebil2_].lower()}"
                answers.append(answer_11)

            else:
                if amebil1_name == 2 : amebil1_ = 4
                if amebil1_name == 4 : amebil1_ = 2
                if amebil2_name == 2 : amebil2_ = 4
                if amebil2_name == 4 : amebil2_ = 2

                # Sayi yok Yer degisik
                answer_8 = f"{amebil2[amebil2_]}{amebil1[amebil1_name].lower()}"
                answers.append(answer_8)

                #Sayi sonda Yer degisik
                answer_9 = f"{amebil2[amebil2_]}{amebil1[amebil1_name].lower()}{amebilsayi_2[1].lower()}"
                answers.append(answer_9)

                #Sayi basta Yer degisik
                answer_10 = f"{amebilsayi_2[1]}{amebil2[amebil2_].lower()}{amebil1[amebil1_name].lower()}"
                answers.append(answer_10)

                # Sayi yok Yer degisik
                answer_11 = f"{amebil2[amebil2_name]}{amebil1[amebil1_].lower()}"
                answers.append(answer_11)

                #Sayi sonda Yer degisik
                answer_12 = f"{amebil2[amebil2_name]}{amebil1[amebil1_].lower()}{amebilsayi_2[1].lower()}"
                answers.append(answer_12)

                #Sayi basta Yer degisik
                answer_13 = f"{amebilsayi_2[1]}{amebil2[amebil2_name].lower()}{amebil1[amebil1_].lower()}"
                answers.append(answer_13)

                # Amet y
                answer_14 = f"{amebil1[amebil1_]}{amebilsayi_2[1].lower()}{amebil2[amebil2_name].lower()}"
                answers.append(answer_14)

                # Amet y
                answer_15 = f"{amebil1[amebil1_name]}{amebilsayi_2[1].lower()}{amebil2[amebil2_].lower()}"
                answers.append(answer_15)



        return answers

   def kovalent_question_answers_ky(self,type,kovalent):
        answers = []
        amebil1,amebil2,amebil1_name,amebil2_name,amebilsayi_1,amebilsayi_2 = answer[0],answer[1],answer[2],answer[3],answer[4],answer[5]


        if kovalent == '_KY1':
            # f"{amebil1[1]}{amebil2[1]}"
         #Sayi Bolumu
            # Sayi 1 var
            answer_1 = f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}"
            answers.append(answer_1)

            # Sayi 2 var
            answer_2 = f"{amebil1[1]}{amebil2[1]}{amebilsayi_2[0]}"
            answers.append(answer_2)
        
            # Sayi 12 var
            answer_3 = f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}{amebilsayi_2[0]}"
            answers.append(answer_3)
         #Element Bolumu
            # Element Yer degisik
            answer_4 = f"{amebil2[1]}{amebil1[1]}"
            answers.append(answer_4)
         #Hem Sayi hem element bolumu
            # Yer degisik sayi 12 var
            answer_5 = f"{amebil2[1]}{amebilsayi_1[0]}{amebil1[1]}{amebilsayi_2[0]}"
            answers.append(answer_5)

            # Yer degisik sayi 2 var
            answer_6 = f"{amebil2[1]}{amebil1[1]}{amebilsayi_2[0]}"
            answers.append(answer_6)

            # Yer degisik sayi 1 var
            answer_7 = f"{amebil2[1]}{amebilsayi_1[0]}{amebil1[1]}"
            answers.append(answer_7)
            

        elif kovalent == '_KY2':
            #f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}"
         #Sayi Bolumu 

            #Sayi 2 var 1 yok
            answer_1 = f"{amebil1[1]}{amebil2[1]}{amebilsayi_2[0]}"
            answers.append(answer_1)

            #Sayi 2 var 1 yok p
            answer_2 = f"{amebil1[1]}({amebil2[1]}){amebilsayi_2[0]}"
            answers.append(answer_2)

            #Sayi yok 
            answer_3 = f"{amebil1[1]}{amebil2[1]}"
            answers.append(answer_3)

            #Sayi 1 var ama degisik
            answer_4 = f"{amebil1[1]}{amebil2[1]}{amebilsayi_1[0]}"
            answers.append(answer_4)

            #Sayi 1 var ama degisik p
            answer_5 = f"{amebil1[1]}({amebil2[1]}){amebilsayi_1[0]}"
            answers.append(answer_5)
         #Element Bolumu
            #Yer degisik 
            answer_6 = f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}"
            answers.append(answer_6)

            #Yer degisik p
            answer_7 = f"({amebil1[1]}){amebilsayi_1[0]}{amebil2[1]}"
            answers.append(answer_7)
         #Hem Sayi Hem Element Bolumu

            #Sayi 2 var 1 yok yer degisik
            answer_8 = f"{amebil2[1]}{amebil1[1]}{amebilsayi_2[0]}"
            answers.append(answer_8)

            #Sayi 2 var 1 yok yer degisik p
            answer_9 = f"{amebil2[1]}({amebil1[1]}){amebilsayi_2[0]}"
            answers.append(answer_9)

            #Sayi yok yer degisik
            answer_10 = f"{amebil2[1]}{amebil1[1]}"
            answers.append(answer_10)

            #Sayi 1 var ama degisik yer degisik
            answer_11 = f"{amebil2[1]}{amebil1[1]}{amebilsayi_1[0]}"
            answers.append(answer_11)

            #Sayi 1 var ama degisik p
            answer_12 = f"{amebil2[1]}({amebil1[1]}){amebilsayi_1[0]}"
            answers.append(answer_12)

        elif kovalent == '_KY3':
            #f"{amebil1[1]}{amebil2[1]}{amebilsayi_2[0]}"
         #Sayi Bolumu
            #Sayi 1 var 2 yok 
            answer_1 = f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}"
            answers.append(answer_1)

            #Sayi 1 var 2 yok p
            answer_2 = f"({amebil1[1]}){amebilsayi_1[0]}{amebil2[1]}"
            answers.append(answer_2)

            #Sayi yok 
            answer_3 = f"{amebil1[1]}{amebil2[1]}"
            answers.append(answer_3)

            #Sayi 1 var ama degisik
            answer_4 = f"{amebil1[1]}{amebil2[1]}{amebilsayi_1[0]}"
            answers.append(answer_4)

            #Sayi 1 var ama degisik p
            answer_5 = f"{amebil1[1]}({amebil2[1]}){amebilsayi_1[0]}"
            answers.append(answer_5)
         #Element Bolumu
            #Yer Degisik
            answer_6 = f"{amebil2[1]}{amebil1[1]}{amebilsayi_2[0]}"
            answers.append(answer_6)

            #Yer Degisik p
            answer_7 = f"{amebil2[1]}({amebil1[1]}){amebilsayi_2[0]}"
            answers.append(answer_7)
         #Hem Sayi Hem Element Bolumu
            #Sayi 1 var 2 yok yer degisik
            answer_8 = f"{amebil2[1]}{amebilsayi_1[0]}{amebil1[1]}"
            answers.append(answer_8)

            #Sayi 1 var 2 yok yer degisik p
            answer_9 = f"({amebil2[1]}){amebilsayi_1[0]}{amebil1[1]}"
            answers.append(answer_9)

            #Sayi yok yer degisik
            answer_10 = f"{amebil2[1]}{amebil1[1]}"
            answers.append(answer_10)

            #Sayi 1 var ama degisik yer degisik
            answer_11 = f"{amebil2[1]}{amebil1[1]}{amebilsayi_1[0]}"
            answers.append(answer_11)

            #Sayi 1 var ama degisik yer degisik p
            answer_12 = f"{amebil2[1]}({amebil1[1]}){amebilsayi_1[0]}"
            answers.append(answer_12)
        else:
            #f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}{amebilsayi_2[0]}"
         #Sayi Bolumu
            #Sayi 1 yok 
            answer_1 = f"{amebil1[1]}{amebil2[1]}{amebilsayi_2[0]}"
            answers.append(answer_1)

            #Sayi 1 yok p
            answer_2 = f"{amebil1[1]}({amebil2[1]}){amebilsayi_2[0]}"
            answers.append(answer_2)

            #Sayi yok 
            answer_3 = f"{amebil1[1]}{amebil2[1]}"
            answers.append(answer_3)

            #Sayi 2 yok 
            answer_4 = f"{amebil1[1]}{amebilsayi_1[0]}{amebil2[1]}"
            answers.append(answer_4)

            #Sayi 2 yok p
            answer_5 = f"({amebil1[1]}){amebilsayi_1[0]}{amebil2[1]}"
            answers.append(answer_5)
         #Element Bolumu
            #Yer degisik
            answer_6 = f"{amebil2[1]}{amebilsayi_1[0]}{amebil1[1]}{amebilsayi_2[0]}"
            answers.append(answer_6)

            #Yer degisik 1p
            answer_7 = f"({amebil2[1]}){amebilsayi_1[0]}{amebil1[1]}{amebilsayi_2[0]}"
            answers.append(answer_7)

            #Yer degisik 2p
            answer_8 = f"{amebil2[1]}{amebilsayi_1[0]}({amebil1[1]}){amebilsayi_2[0]}"
            answers.append(answer_8)

            #Yer degisik 12p
            answer_9 = f"({amebil2[1]}){amebilsayi_1[0]}({amebil1[1]}){amebilsayi_2[0]}"
            answers.append(answer_9)
         #Hem Element Hem Sayi Bolumu
            #Sayi 1 yok yer degisik
            answer_10 = f"{amebil2[1]}{amebil1[1]}{amebilsayi_2[0]}"
            answers.append(answer_10)

            #Sayi 1 yok p
            answer_11 = f"{amebil2[1]}({amebil1[1]}){amebilsayi_2[0]}"
            answers.append(answer_11)

            #Sayi yok 
            answer_12 = f"{amebil2[1]}{amebil1[1]}"
            answers.append(answer_12)

            #Sayi 2 yok 
            answer_13 = f"({amebil2[1]}){amebilsayi_1[0]}{amebil1[1]}"
            answers.append(answer_13)

            #Sayi 2 yok p
            answer_14 = f"({amebil2[1]}){amebilsayi_1[0]}{amebil1[1]}"
            answers.append(answer_14)

        return answers

 #Iyonik kisim
   def iyonik_question_answers_io(self):
      answers = []
      metal,amebil,metal2,amebil2 = answer[0],answer[1],answer[2],answer[3]



      for i in range(1,4):
         answer_1 = self.tekrar(metal[0],amebil[0],'o','metal')
         answers.append(answer_1)
      
      for i in range(1,4):
         answer_1 = self.tekrar(metal[0],amebil[0],'o','amebil')
         answers.append(answer_1)
      return answers

   def tekrar(self,metal_id,amebil_id,type,wrong_type):
      self.YapayZeka.yIyonik_metal = yapay_zeka.YapayZeka().yIyonik

      answer = self.YapayZeka.yIyonik(metal_id,amebil_id,type,wrong_type)

      return answer


   def iyonik_question_answers_iy(self):
      answers = []
      metal,amebil,metal2,amebil2 = answer[0],answer[1],answer[2],answer[3]



      for i in range(1,4):
         answer_1 = self.tekrar(metal[0],amebil[0],'y','metal')
         answers.append(answer_1[0])

      
      for i in range(1,4):
         answer_1 = self.tekrar(metal[0],amebil[0],'y','amebil')
         answers.append(answer_1[0])
      return answers   
    
