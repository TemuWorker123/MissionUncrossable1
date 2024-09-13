#mission uncrossable
#Daniil
#Minwoo

from random import *
random = randint(0, 20)
total_cash = 100
cash = int(input("how much bet: "))
if cash > total_cash:
    print("u only have", total_cash, "dumbass")
    cash = int(input("how much bet: "))
cash2 = cash
more = 0

while True:
    a = int(input("go more? 1=yes 2=no: "))
    if a == 1:
        more += 1
        if 10 < more < 15:
            cash *= 1.2
        elif more > 15:
            cash *= 1.3
        elif more == 20:
            cash *= 2
        else:
            cash *= 1.1
        print(round(cash), "$")
        print(more, "/20")
    if more == random:
        print("loser")
        total_cash -= cash2
        print("total cash: ", round(total_cash), "$")
        if total_cash <= 0:
            print("BROKIE")
            break
        else:
            play = int(input("play gain 1=yes 2=no"))
            if play == 1:
                random = randint(1, 20)
                more = 0
                cash = int(input("how much bet: "))
                if cash >= 101:
                    print("u only have 100 dumbass")
                    cash = int(input("how much bet: "))
                cash2 = cash
            if play == 2:
                break
    if a == 2 or a == 20:
        print(round(cash), "$")
        print("where u would die: ", random)
        cash -= cash2
        total_cash += cash
        print("total cash: ", round(total_cash), "$")
        play = int(input("play gain 1=yes 2=no"))
        if play == 1:
            random = randint(1, 20)
            more = 0
            cash = int(input("how much bet: "))
            if cash > total_cash:
                print("u only have 100 dumbass")
                cash = int(input("how much bet: "))
            cash2 = cash
        if play == 2:
            break
