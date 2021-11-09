#print("kivi käärid paber")
#import random
#a=0
#while(a==0):
#        mang=int(input("1-kivi,2-käärid,3-paber"))
#        if (mang==1 or mang==2 or mang==3):
#            a=1
#if mang==1:
#        print("kivi")
#if mang==2:
#        print("käärid")
#if mang==3:
#        print("paber")
#b=random.randint(1, 3)
#if  b==1:
#        print("kivi")
#if b==2:
#        print("käärid")
#if b==3: 

#while(b==0):
 #   mang2=int(input("1-kivi,2-käärid,3-paber - "))
  #  if (mang2==1 or mang2==2 or mang2==3):
   #     b=1
   # if mang2==1:
    #    print("kivi")
   # elif mang2==2:
    #    print("käärid")
   # elif mang2==3:
       # print("paber")
#win=1
#win=2
#win=0
#if mang==1 and mang2==2:
#        win=1
 #       if win==0:
  #          print("viik")
#if win==1:
 #   print("sa võinud")
#if win==2:
 #   print("sa ei võinud")

#from keyboard import* 
#print("kivi käärid paber")
#while True:
#    try:
#        if read_key()== "k":
#            print("oli valitud kivi")
#            break
#    except:
#        ValueError
#v1=["kivi","käärid","paber"]
#v2=["kivi","käärid","paber"]
#if m==1:
#    while 1:
        #print("mängime")
        #if read_key()=="N": break
        #p1=choice(v1)
        #p2=choice(v2)
        #if p1==p2: print("viik")
        #if p1==v: print("2")
        #if p1=="3": print("3")
#m=3
#while m not in [1,2]:
#    try:
#        m=int(input("kellega mängime?\n1-inimestega\n2-roobotiga"))
#    except:
#        ValueError
#if m==1:
#    while 1:
#        a=0
#    while(a==0):
#        try:
#            mangija1=int(input("1-kivi,2-käärid,3-paber"))
#        except:
#            ValueError
#    if (mangija1==1 or mangija1==2 or mangija1==3):
#            a=1
#    if mangija1==1:
#        print("kivi")
#    elif mangija1==2:
#        print("käärid")
#    elif mangija1==3:
#        print("paber")
#    else:
#        TypeError
#    b=0
#    while(b==0):
#        try:
#            mangija2=int(input("1-kivi,2-käärid,3-paber - "))
#        except:
#            ValueError
#        if (mangija2==1 or mangija2==2 or mangija2==3):
#            b=1
#        if mangija2==1:
#            print("kivi")
#        elif mangija2==2:
#            print("käärid")
#        elif mangija2==3:
#            print("paber")
#        else:
#            TypeError
#win=1
#win=2
#win=0
#if mang==1 and b==2:
#        win=1
#        if win==0:
#            print("viik")
#if win==1:
#        print("sa võinud")
#if win==2:
#        print("sa ei võinud")
#else:
#    TypeError
#elif m==2:
#    while 1:
#        pass

#a=0
#while(a==0):
#    try:
#        mangija1=int(input("1-kivi,2-käärid,3-paber"))
#    except:
#        ValueError
#if (mangija1==1 or mangija1==2 or mangija1==3):
#            a=1
#if mangija1==1:
#        print("kivi")
#elif mangija1==2:
#        print("käärid")
#elif mangija1==3:
#        print("paber")
#else:
#    TypeError
#b=0
#while(b==0):
#    try:
#        mangija2=int(input("1-kivi,2-käärid,3-paber - "))
#    except:
#        ValueError
#    if (mangija2==1 or mangija2==2 or mangija2==3):
#        b=1
#if mangija2==1:
#        print("kivi")
#elif mangija2==2:
#        print("käärid")
#elif mangija2==3:
#        print("paber")
#else:
#    TypeError
#win=1
#win=2
#win=0
#if mang==1 and b==2:
#        win=1
#        if win==0:
#            print("viik")
#if win==1:
#        print("sa võinud")
#if win==2:
#        print("sa ei võinud")
#else:
#    TypeError
#v1=["kivi","käärid","paber"]
#v2=["kivi","käärid","paber"]
#if m==1:
#    while True:
#        print("Kas mängime? esc - välja, enter - mängima")
#        if read_key()=="esc":
#            break
#        elif read_key()=="enter":
#            p1=choise(v1)
#            print("esimene bot: ", p1)
#            p2=choise(v2)
#            print("teine bot: ", p2)
#            if p1==p2:
#                print("viik")
#            elif p1==v1[0] and p2==v2[2] and p2==v2[0] or p1==v1[1] and p2==v1[2]:
#                print("võitis 1")
#            else:
#                print("võitis 2")

from keyboard import*
from random import*
v1=["kivi","käärid","paber"]
v2=["kivi","käärid","paber"]
def start():
    """Teeme valik kellega mängime
    Tagastame m nuutuja int formaadis
    :rtype: int
    """
    print("Kivi, Paber, Käärid")
    m=3
    while m not in [1,2,3]:
        try:
            m=int(input("Kellega mängime?\n1 - inimestega\n2-robotiga\n3-robot-robotiga"))
        except:
            ValueError
    return m
m=start()
if m==1:
    while True:
        print("Kas mängime? esc - välja, enter - mängima")
        if read_key()=="esc":
            break
        elif read_key()=="enter":
            p1=choise(v1)
            print("esimene bot: ", p1)
            p2=choise(v2)
            print("teine bot: ", p2)
            if p1==p2:
                print("viik")
            elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                print("võitis 1")
            else:
                print("võitis 2")
from keyboard import*
from random import*
v1=["kivi","käärid","paber"]
v2=["kivi","käärid","paber"]
def start():
    """Teeme valik kellega mängime
    Tagastame m nuutuja int formaadis
    :rtype: int
    """
    print("Kivi, Paber, Käärid")
    m=3
    while m not in [1,2]:
        try:
            m=int(input("Kellega mängime?\n1 - inimestega\n2-robotiga"))
        except:
            ValueError
    return m
m=start()
if m==1:
    while True:
        print("Kas mängime? esc - välja, enter - mängima")
        if read_key()=="esc":
            break
        elif read_key()=="enter":
            p1=choise(v1)
            print("esimene bot: ", p1)
            p2=choise(v2)
            print("teine bot: ", p2)
            if p1==p2:
                print("viik")
            elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                print("võitis 1")
            else:
                print("võitis 2")

from keyboard import*
from random import*
from My_module import*
v1=["kivi","käärid","paber"]
v2=["kivi","käärid","paber"]

m=start()
if m==1:
    bot_vs_bot(v1,v2)
elif m==2:
    while 1:
        pass