print("камень ножницы бумага")
import random
a=0
while(a==0):
        player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
        if (player == 1 or player == 2 or player == 3):
            ver = 1    
if player == 1:
        print("камень")  
if player == 2:
        print("ножницы") 
if player == 3:
        print("бумагa")  
b = random.randint(1, 3)
if b== 1:
        print("камень.") 
if b== 2:
        print("ножницы")
if b== 3:
        print("бумагa")
