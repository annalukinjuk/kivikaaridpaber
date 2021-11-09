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
