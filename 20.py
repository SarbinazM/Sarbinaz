#======================================20-apreldin uy jumisi=======================================
#=================================Maxambetalieva Sarbinaz Dawletbay qizi=====================
# Bas dizim
jonelis = []

print("jurer joldi kiritin (aldiga, artqa, onga, shep)")
print("Toqtatiw ushin 'stop' dep jazin")

while True:
    soz = input("Juretin jolinis qaysi:")

    if soz == "stop":
        break

    jonelis.append(soz)

# Esaplaw
print("\nNatiyje:")

print("aldiga", jonelis.count("aldiga"))
print("Artqa", jonelis.count("artqa"))
print("onga", jonelis.count("onga"))
print("shepke", jonelis.count("shepke"))