import re

# 1. Jastı tekseriw
jas = input("Jasıńızdı kirgiziń: ")
if jas.isdigit(): # Kirgizilgen maǵlıwmattıń san ekenin tekseremiz
    jas = int(jas)
    if jas > 30:
        print("Qáte: Jas 30 dan aspawı kerek!")
    else:
        print(f"Jasıńız: {jas}")
else:
    print("Qáte: San kirgiziń!")

# 2. Atı-jóndi formatlaw
ati = input("Atıńızdı kirgiziń: ")
# capitalize() - birinshi háripti úlken, qalǵanların kishi qıladı
print(f"Sizdiń atıńız: {ati.capitalize()}") 

# 3. Gmail tekseriw
email = input("Gmail adresińizdi kirgiziń: ")
if "@" in email: # 'in' operatorı tekst ishinde belginiń bar-joǵın tekseredi
    print(f"Email qabıllandı: {email}")
else:
    print("Qáte: Gmail adresińizde '@' simvolı bolıwı shart!")

# 4. Parol tekseriw 
parol = input("Parol kirgiziń (keminde 8 simvol, 1 úlken hárip, 1 simvol): ")

# Shártlerdi tekseriw ushın flaglar (belgiler)
uzinliq = len(parol) >= 8
bar_ulken = any(c.isupper() for c in parol) # Keminde bir úlken hárip barma tekseriw ushin
bar_simvol = any(not c.isalnum() for c in parol) # Keminde bir simvol (san hám hárip emes) barma tekseriw ushin

if uzinliq and bar_ulken and bar_simvol:
    print("Parol durıs ornatıldı!")
else:
    print("Qáte: Parol shártlerge juwap bermeydi (8 belgi, úlken hárip hám simvol bolıwı shart).")

    '''def-container
    strip() -  bas harip penen jaziw ushin ham kereksiz zatlardi alip taslaw ushin
    try - hareket etiw,urinis
    return - natiyjeni qaytariw ushin
    valueerror - qateni aniqlaw ushin,except
    lower - hamme narseni kishi hariplerge otkeriw ushin
    endswith - cikldin aqiri
    any - 

    


    
    
    '''