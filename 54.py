# e = 4000
# a = int(input("Neshe nan alsiz?:"))
# print(a*e)

# b = 12000
# a = int(input("Neshe Sut alsiz?:"))
# print(a*b)

# d = 15000
# a = int(input("Neshe Mayek alsiz?:"))
# print(a*d)
#print(jami_nan + jami_sut + jami_mayek)


nan_bahasi = 4000
sut_bahasi = 12000
mayek_bahasi = 15000


a1 = int(input("Neshe nan alasiz?: "))
jami_nan = a1 * nan_bahasi
print(f"Nanlar ushin: {jami_nan} som")

a2 = int(input("Neshe sut alasiz?: "))
jami_sut = a2 * sut_bahasi
print(f"Sutlar ushin: {jami_sut} som")

a3 = int(input("Neshe máyek alasiz?: "))
jami_mayek = a3 * mayek_bahasi
print(f"Máyekler ushin: {jami_mayek} som")



uliwma_baha = jami_nan + jami_sut + jami_mayek
shegirme_muqdari = uliwma_baha * 0.15
toleytuǵin_baha = uliwma_baha - shegirme_muqdari


print(f"Hámmesi jami: {uliwma_baha} som")
print(f"Sizge 15% shegirme (skitka): {shegirme_muqdari} som")
print(f"Tóleytuǵin aqshańiz: {toleytuǵin_baha} som")