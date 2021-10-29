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

from keyboard import* 
print("kivi käärid paber")
while True:
    try:
        if read_key()== "k":
            print("oli valitud kivi")
            break
    except:
        ValueError
m=3
while m not in [1,2]:
    try:
        m=int(input("kellega mängime?\n1-inimestega\n2-roobotiga"))
    except:
        ValueError
if m==1:
    while 1:
        pass
elif m==2:
    while 1:
        pass

a=0
while(a==0):
        mangija1=int(input("1-kivi,2-käärid,3-paber"))
        if (mangija1==1 or mangija1==2 or mangija1==3):
            a=1
if mangija1==1:
        print("kivi")
elif mangija1==2:
        print("käärid")
elif mangija1==3:
        print("paber")
b=0
while(b==0):
    mangija2=int(input("1-kivi,2-käärid,3-paber"))
    if (mangija2==1 or mangija2==2 or mangija2==3):
        b=1
    if mangija2==1:
        print("kivi")
    elif mangija2==2:
        print("käärid")
    elif mangija2==3:
        print("paber")
win=1
win=2
win=0
if mang==1 and b==2:
        win=1
        if win==0:
            print("withdraw")
if win==1:
        print("sa võinud")
if win==2:
        print("sa ei võinud")