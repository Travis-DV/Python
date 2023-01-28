from random import randint
import time
count = 20
player1s = 0
player2s = 0
player1 = []
player2 = []
go = 0
while count > 0:
    ran = randint(1,20)
    player1.append(ran)
    ran = randint(1,20)
    player2.append(ran)
    count = count-1
while player1s < 5 and player2s < 5:
    while 0 == go:
        ran = randint(0,19)
        player1n = player1[ran]
        player2[ran] = 0
        ran = randint(0,19)
        player2n = player2[ran]
        player2[ran] = 0
        go = 1
    go = 0
    while player1n != 0 and player2n != 0 and 0 == go:
        player1n = str(player1n)
        print("Player one drew:" + player1n)
        player1n = int(player1n)
        time.sleep(0.3)
        player2n = str(player2n)
        print("Player two drew:" + player2n)
        player2n = int(player2n)
        time.sleep(0.3)
        go = 1
    go = 0
    if player1n > player2n:
        player1s = player1s+1
        player1s = str(player1s)
        print("Player one's score is now:" + player1s)
        player1s = int(player1s)
        time.sleep(0.3)
    elif player2n > player1n:
        player2s = player2s+1
        player2s = str(player2s)
        print("Player two's score is now:" + player2s)
        player2s = int(player2s)
        time.sleep(0.3)
    else:
        print ("TIE")
        time.sleep(1)
    if player1s > player2s:
        by = player1s-player2s
        by = str(by)
        print("Player one is now in the lead by:" + by)
        time.sleep(1)
    elif player2s > player1s:
        by = player2s-player1s
        by = str(by)
        print("Player two is now in the lead by:" + by)
        time.sleep(1)
    else:
        print("TIE")
        time.sleep(1)