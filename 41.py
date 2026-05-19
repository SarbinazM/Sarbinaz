miyweler = ["Alma" "Almurt" "Portakol"]
it = iter(miyweler)
print(next(it))


def sanoq(n):
    i = 1
    while i <= n:
        yield i
        i += 1

        #Bul funkciya iterator qaytaradi
for son in sanoq(5):
    print(son)

