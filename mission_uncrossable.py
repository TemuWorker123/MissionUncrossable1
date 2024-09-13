#mission uncrossable
#Daniil
#Minwoo

from random import *
random = randint(1, 20)
cash = int(input("how much bet: "))
cash2 = cash
more = 0
total_cash = 100

while True:
    a = int(input("go more? 1=yes 2=no: "))
    if a == 1:
        more += 1
        if more > 10:
            cash *= 1.3
        else:
            cash *= 1.1
        print(round(cash), "$")
        print(more, "/20")
    if more == random:
        print("loser")
        total_cash -= cash2
        print("total cash: ", round(total_cash), "$")
        play = int(input("play gain 1=yes 2=no"))
        if play == 1:
            random = randint(1, 20)
            more = 0
            cash = int(input("how much bet: "))
            cash2 = cash
        if play == 2:
            break
    if a == 2 or a == 20:
        print(round(cash), "$")
        total_cash += cash
        print("total cash: ", round(total_cash), "$")
        play = int(input("play gain 1=yes 2=no"))
        if play == 1:
            random = randint(1, 20)
            more = 0
            cash = int(input("how much bet: "))
            cash2 = cash
        if play == 2:
            break
            