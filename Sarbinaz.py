  #=============================Sarbinaz Sozi Terminalda====================
print("  SSSS   AAAAA  RRRRR  BBBBB  IIIII  N   N  AAA   ZZZZZ")
print(" S       A   A  R   R  B   B    I    NN  N A   A     Z ")
print("  SSSS   AAAAA  RRRRR  BBBBB    I    N N N A A A    Z  ")
print(" S       A   A  R  R   B   B    I    N  NN A   A   Z   ")
print(" SSSS    A   A  R   R  BBBBB  IIIII  N   N A    A ZZZZZ")

menyu=[]
#===========================================Qosimsha=====================================================
while True:
    print("\n1. Sortlaw")
    print("2. Teris aylandiriw")
    print("3. 1-haripti bas harip qiliw")
    print("4. Barin bas harip qiliw")
    print("5. Barin sanlarga aylandiriw")
    print("6. Listke jana san qosiw")
    print("7. Listke jazilgan sanlar,siz jazgan 8 san")
    print("8. Oshiriw yaki listti toliq tazalaw")

    san=input("birewin tanlan:")
    if san=='1':
        ati=input("Qaysisin isleyjaqsiz?")
        menyu.sort()
        print("sortlandi")

    elif san=='2':
        ati=input("aylandiriw:")
        if ati==menyu:
            menyu.reverse(ati)
            print("aylandirildi")
        else:
            print("aylandirilmadi")

    elif san=='3':
        ati=input("1-haripti bas harip qilajaqsizba?")