import random
import os
######################
#     Naval Battle
#         v.1.1 
#     By. Corrix
######################

pcat = [(i,e) for i in range(5) for e in range(5)]

def gril():
   boat = []
   catalog = ["⛵", "@⛵@", "⛵@"]
   for _ in range(5):
      al = []
      for _ in range(5):
         if random.randint(0,3) == 1:
            al.append(random.choice(catalog))
         else:
            al.append("≈≈")
      boat.append(al)
   del(al)
   for i, sublist in enumerate(boat): #Anti empty system!
      if "⛵" in sublist or "⛵@" in sublist or "@⛵@" in sublist:
         return boat
      else:
         return gril()

navi = gril()
navi_mie = gril()
def printab():
   print("  \033[1m     IL TUO MARE: \033[0m                \033[1m  IL MARE PC: \033[0m")
   print("     1.  2.  3.  4.  5.                          1. 2. 3. 4. 5.")
   for i in range(5):
      print(str(i+1) + ". ", end ="")
      print("|", end="")
      for e in range(5):
         if navi_mie[i][e] == "X ":
            print("\033[91mXXXXXX\033[0m", end="")
         elif navi_mie[i][e] == "≈≈":
            print("\033[94m≈≈≈≈≈≈\033[0m", end="")
         elif navi_mie[i][e] == "@⛵@":
            print("\033[94m⛵⛵⛵\033[0m", end="")
         elif navi_mie[i][e] == "@⛵":
            print("\033[94m≈\033[0\033[94m⛵⛵\033[94m≈\033[0m", end="")
         elif navi_mie[i][e] == "@⛵x":
            print("\033[94m≈\033[0\033[94m⛵⛵\033[91mX\033[0m", end="")
         elif navi_mie[i][e] == "⛵xx":
             print("⛵\033[91mXX\033[0m", end="")
         elif navi_mie[i][e] == "≈≈x":
            print("\033[91m≈≈≈≈≈≈\033[0m", end="")
         else:
            print("\033[94m≈≈⛵\033[94m≈≈\033[0m", end="")
      print("| ", end="       ")
      print(str(i+1) + ". ", end ="")
      print("[ ", end="")
      for e in range(5):
         if navi[i][e] == "X ":
            print("\033[91mXXX\033[0m", end="")
         elif navi[i][e] == "x⛵@":
            print("\033[94m≈≈\033[0m\033[91mX\033[0m", end="")
         elif navi[i][e] == "⛵X":                             
            print("\033[94m≈\033[0m\033[91mXX\033[0m", end="")
         elif navi[i][e] == "≈≈x":
            print("\033[94m≈≈≈\033[0m", end="")
         else:
            print(" ? ", end="")
      print(" ] ")
printab()
attemps = []
pc_attemps = []

def sipuo():
   if len(attemps) >= 25:
      return False
   for i, sublist in enumerate(navi):
      if "⛵" in sublist or "⛵@" in sublist or "@⛵@" in sublist or "x⛵@" in sublist or "@⛵@" in sublist or "⛵X" in sublist:
         return True
      else:
         print('{:^24s}'.format("\033[96m\033[1mHAI VINTOOOOOOOO!!!\033[0m"))
         [print(emoticon(True)) for _ in range(5)]
         exit()
   for i, sublist in enumerate(navi_mie):
      if "⛵" in sublist or "⛵@" in sublist or "@⛵@" in sublist:
         return True
      else:
         print('{:^24s}'.format("\033[93m\033[1mHAI PERSOOOOOOOOOOO\033[0m"))
         [print(emoticon(False)) for _ in range(5)]
   
def emoticon(vit):
   if vit:
      victory = ["""ᕕ( ᐛ )ᕗ""", "ԅ(≖◡≖ԅ)", "♪┏(・o･)┛♪┗ ( ･o･) ┓♪┏ ( ･o･) ┛♪┗ (･o･ ) ┓♪┏(･o･)┛♪", "◉‿◉", ":)", ":-)", "٩(ᐛ )و"]
      return random.choice(victory)
   else:
      acqua = ["""( T⌓T)""", """( •̩̩̩́ _ •̩̩̩̀)""", "( ಥ _ಥ)", ":っ(", "(˘̩̩̩̩̩̩∩˘̩̩̩̩̩̩)", ">:[", "(◕‸◕ )", "(ノಠ益ಠ)ノ彡┻━┻"]
      return random.choice(acqua)

def gia(x, y):
   c = False
   try:
      attemps.index((x,y))
   except:
      c = True
   if c == False and navi[x][y] == "≈≈x":
      return False
   return True

def myturn():
   colpo_x = input("Entera la x >")
   colpo_y = input("Entera la y >")
   if not colpo_x.isnumeric() or not colpo_y.isnumeric() or colpo_x == "" or colpo_y=="" or colpo_x == " " or colpo_y==" ":
      print("Coordinate invalide! NUMERI INTERI!")
      exit()
   colpo_x = abs(((int(colpo_x))-1)%5)
   colpo_y = abs(((int(colpo_y)-1)%5))
   if gia(colpo_x, colpo_y):
      attemps.append((colpo_x, colpo_y))
      if navi[colpo_x][colpo_y] == "⛵" or navi[colpo_x][colpo_y] == "⛵X":
         navi[colpo_x][colpo_y] = "X "
         print("COLPITO & AFFONDATO! ", emoticon(True))
      elif navi[colpo_x][colpo_y] == "@⛵@":
         navi[colpo_x][colpo_y] = "x⛵@"
         print("COLPITO!", emoticon(True))
      elif navi[colpo_x][colpo_y] == "⛵@":
         print("COLPITO!", emoticon(True))
         navi[colpo_x][colpo_y] = "⛵X"
      elif navi[colpo_x][colpo_y] == "x⛵@":
         print("COLPITO!", emoticon(True))
         navi[colpo_x][colpo_y] = "⛵X"
      else:
         navi[colpo_x][colpo_y] = "≈≈x"
         print("Acqua! ", emoticon(False))
   else:
      print("COORDINATE già inseriteeeeee!!")


def cheat():
   for i in range(5):
      print("|", end="")
      for e in range(5):
         if navi[i][e] == "X ":
            print("\033[91mXXXXXX\033[0m", end="")
         elif navi[i][e] == "≈≈":
            print("\033[94m≈≈≈≈≈≈\033[0m", end="")
         elif navi[i][e] == "@⛵@":
            print("\033[94m⛵⛵⛵\033[0m", end="")
         elif navi[i][e] == "@⛵":
            print("\033[94m≈\033[0\033[94m⛵⛵\033[94m≈\033[0m", end="")
         elif navi[i][e] == "≈≈x":
            print("\033[91m≈≈≈≈≈≈\033[0m", end="")
         else:
            print("\033[94m≈≈⛵\033[94m≈≈\033[0m", end="")
      print("| ")

def pc_turn():
   guess = random.choice(pcat)
   pcat.remove(guess)
   if navi_mie[guess[0]][guess[1]] == "⛵" or navi_mie[guess[0]][guess[1]] == "⛵xx":
      navi_mie[guess[0]][guess[1]] = "X "
      print('{:^24s}'.format("\033[91m>>>\033[0m PC Ha \033[1mCOLPITO & AFFONDATO\033[0m la tua nave in x:" +str(guess[0]+1) + " y:"+ str(guess[1]+1)))
   elif navi_mie[guess[0]][guess[1]] == "@⛵":
      navi_mie[guess[0]][guess[1]] = "⛵"
      print('{:^24s}'.format("\033[91m>>>\033[0m PC Ha \033[1mCOLPITO\033[0m la tua nave in x:" +str(guess[0]+1) + " y:"+ str(guess[1]+1)))
   elif navi_mie[guess[0]][guess[1]] == "@⛵x":
      navi_mie[guess[0]][guess[1]] = "⛵xx"
      print('{:^24s}'.format("\033[91m>>>\033[0m PC Ha \033[1mCOLPITO\033[0m la tua nave in x:" +str(guess[0]+1) + " y:"+ str(guess[1]+1)))
   elif navi_mie[guess[0]][guess[1]] == "@⛵@":
      navi_mie[guess[0]][guess[1]] = "@⛵x"
      print('{:^24s}'.format("\033[91m>>>\033[0m PC Ha \033[1mCOLPITO\033[0m la tua nave in x:" +str(guess[0]+1) + " y:"+ str(guess[1]+1)))
   else:
      print('{:^24s}'.format("\033[91m>>>\033[0m PC ha fatto acqua in x:" + str(guess[0]+1) + " y:" + str(guess[1]+1)))
      navi_mie[guess[0]][guess[1]] = "≈≈x"
      print("\r")
   printab()


switch = True # true --> myturn()
while sipuo():
   if switch:
      myturn()
      switch = False
   else:
      input("PC? >")
      os.system('clear')
      #cheat() solo per debug, va mostra mare nemico
      pc_turn()
      switch = True