import random

x = [0,1,2,3,4,5,6,7,8,9,]

while True:
    print(*random.choices(x, k=80))  