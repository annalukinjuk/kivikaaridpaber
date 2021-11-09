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
