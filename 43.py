#✨✨ 10 sandi kiritemiz ham oni saqlaymiz✨✨
numbers = []
for i in range(10):
    num = int(input(f"{i+1}-✨✨sandi kiritin oqiwshilar✨✨: "))
    numbers.append(num)

# ✨✨Generator funksiyasi ✨✨

g = (i for i in range(10) if i % 2 == 0)

for i in g:
     print(i)









