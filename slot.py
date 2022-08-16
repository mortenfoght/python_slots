
import random
moneyLine1 = 0
moneyLine2 = 0
moneyLine3 = 0
moneyLine4 = 0
moneyLine5 = 0
moneyLine6 = 0
moneyLine7 = 0
moneyLine8 = 0
moneyLine9 = 0
stake = 1
win1 = 170
win2 = 56
win3 = 28
win4 = 16
win5 = 12
win6 = 10
win7 = 4
win8 = 2
win9 = 1
reelSymbols = ["bar", "cherry", "plum", "bell", "orange", "lemon"]
reelList = []
reel1 = [0, 1, 4, 3, 2, 0, 1, 5, 3, 2, 4, 5, 3, 2, 4, 1, 5, 0, 4, 3, 5]
reel2 = [0, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5, 1]
reel3 = [0, 4, 5, 3, 2, 4, 1, 3, 5, 4, 2, 5, 1, 4, 5, 3, 4, 5, 3, 2, 5]
rnd1 = random.randint(0, (len(reel1)-1))
rnd2 = random.randint(0, (len(reel2)-1))
rnd3 = random.randint(0, (len(reel3)-1))
pick1 = reel1[rnd1]
pick2 = reel2[rnd2]
pick3 = reel3[rnd3]
symbol1 = reelSymbols[pick1]
symbol2 = reelSymbols[pick2]
symbol3 = reelSymbols[pick3]
if pick1 == 0 and pick2 == 0 and pick3 == 0:
    moneyLine1 = moneyLine1+1
if pick1 == 1 and pick2 == 1 and pick3 == 1:
    moneyLine2 = moneyLine2+1
if pick1 == 2 and pick2 == 2 and pick3 == 2:
    moneyLine3 = moneyLine3+1
if pick1 == 3 and pick2 == 3 and pick3 == 3:
    moneyLine4 = moneyLine4+1
if pick1 == 4 and pick2 == 4 and pick3 == 4:
    moneyLine5 = moneyLine5+1
if pick1 == 5 and pick2 == 5 and pick3 == 5:
    moneyLine6 = moneyLine6+1
if (pick1 == 0 and pick2 == 0) or (pick1 == 0 and pick3 == 0) or (pick2 == 0 and pick3 == 0):
    moneyLine7 = moneyLine7+1
if (pick1 == 1 and pick2 == 1) or (pick1 == 1 and pick3 == 1) or (pick2 == 1 and pick3 == 1):
    moneyLine8 = moneyLine8+1
if (pick1 == 2 and pick2 == 2) or (pick1 == 2 and pick3 == 2) or (pick2 == 2 and pick3 == 2):
    moneyLine9 = moneyLine9+1
print(symbol1, symbol2, symbol3)
if ((moneyLine1*win1)-(moneyLine2*win2)-(moneyLine3*win3)-(moneyLine4*win4)-(moneyLine5*win5)-(moneyLine6*win6)-(moneyLine7*win7)-(moneyLine8*win8)-(moneyLine9*win9)) != 0:
    print('won ' + str(-((moneyLine1*win1)-(moneyLine2*win2)-(moneyLine3*win3)-(moneyLine4*win4) -
          (moneyLine5*win5)-(moneyLine6*win6)-(moneyLine7*win7)-(moneyLine8*win8)-(moneyLine9*win9))) + ' BTC')
# import random
# moneyLine1 = 0
# moneyLine2 = 0
# moneyLine3 = 0
# moneyLine4 = 0
# moneyLine5 = 0
# moneyLine6 = 0
# moneyLine7 = 0
# moneyLine8 = 0
# moneyLine9 = 0
# win1 = 170
# win2 = 56
# win3 = 28
# win4 = 16
# win5 = 12
# win6 = 10
# win7 = 4
# win8 = 2
# win9 = 1
# stake = 1
# for n in range(1):
#     reelSymbols = ["bar","cherry","plum","bell","orange","lemon"]
#     reelList = []
#     reel1 = [0,1,4,3,2,0,1,5,3,2,4,5,3,2,4,1,5,0,4,3,5]
#     reel2 = [0,2,3,4,5,0,1,2,3,4,5,1,2,3,4,5,2,3,4,5,1]
#     reel3 = [0,4,5,3,2,4,1,3,5,4,2,5,1,4,5,3,4,5,3,2,5]
#     rnd1 = random.randint(0,(len(reel1)-1))
#     rnd2 = random.randint(0,(len(reel2)-1))
#     rnd3 = random.randint(0,(len(reel3)-1))
#     pick1 = reel1[rnd1]
#     pick2 = reel2[rnd2]
#     pick3 = reel3[rnd3]
#     symbol1 = reelSymbols[pick1]
#     symbol2 = reelSymbols[pick2]
#     symbol3 = reelSymbols[pick3]
#     if pick1 == 0 and pick2==0 and pick3==0:
#         moneyLine1=moneyLine1+1
#     if pick1 == 1 and pick2 == 1 and pick3 == 1:
#         moneyLine2=moneyLine2+1
#     if pick1 == 2 and pick2 == 2 and pick3 == 2:
#         moneyLine3=moneyLine3+1
#     if pick1 == 3 and pick2 == 3 and pick3 == 3:
#         moneyLine4=moneyLine4+1
#     if pick1 == 4 and pick2 == 4 and pick3 == 4:
#         moneyLine5=moneyLine5+1
#     if pick1 == 5 and pick2 == 5 and pick3 == 5:
#         moneyLine6=moneyLine6+1
#     if (pick1 == 0 and pick2 == 0) or (pick1 == 0 and pick3 == 0) or (pick2 == 0 and pick3 == 0):
#         moneyLine7=moneyLine7+1
#     if (pick1 == 1 and pick2 == 1) or (pick1 == 1 and pick3 == 1) or (pick2 == 1 and pick3 == 1):
#         moneyLine8=moneyLine8+1
#     if (pick1 == 2 and pick2 == 2) or (pick1 == 2 and pick3 == 2) or (pick2 == 2 and pick3 == 2):
#         moneyLine9=moneyLine9+1
#     n=n+1
# print(symbol1,symbol2,symbol3)
# if ((moneyLine1*win1)-(moneyLine2*win2)-(moneyLine3*win3)-(moneyLine4*win4)-(moneyLine5*win5)-(moneyLine6*win6)-(moneyLine7*win7)-(moneyLine8*win8)-(moneyLine9*win9)) != 0:
#     print('win ' + str(-((moneyLine1*win1)-(moneyLine2*win2)-(moneyLine3*win3)-(moneyLine4*win4)-(moneyLine5*win5)-(moneyLine6*win6)-(moneyLine7*win7)-(moneyLine8*win8)-(moneyLine9*win9))))
# print((stake*n)-(moneyLine1*win1)-(moneyLine2*win2)-(moneyLine3*win3)-(moneyLine4*win4)-(moneyLine5*win5)-(moneyLine6*win6)-(moneyLine7*win7)-(moneyLine8*win8)-(moneyLine9*win9))

# print(moneyLine2*win2)
# print(moneyLine3*win3)
# print(moneyLine4*win4)
# print(moneyLine5*win5)
# print(moneyLine6*win6)
# print(moneyLine7*win7)
# print(moneyLine8*win8)
# print(moneyLine9*win9)
# print(n)

# print(symbol1,symbol2,symbol3)

 #  if(r1==0&&r2==0&&r3==0) ml1
 #    return(170);
 #  if(r1==1&&r2==1&&r3==1) ml2
 #    return(56);
 #  if(r1==2&&r2==2&&r3==2) ml3
 #    return(28);
 #  if(r1==3&&r2==3&&r3==3) ml4
 #    return(16);
 #  if(r1==4&&r2==4&&r3==4) ml5
 #    return(12);
 #  if(r1==5&&r2==5&&r3==5) ml6
 #    return(10);
 # if((r1==0&&r2==0)||(r1==0&&r3==0)||(r2==0&&r3==0)) ml7
 #   return(4);
 # if((r1==1&&r2==1)||(r1==1&&r3==1)||(r2==1&&r3==1)) ml8
 #   return(2);
 # if((r1==2&&r2==2)||(r1==2&&r3==2)||(r2==2&&r3==2)) ml9
 #   return(1);
 #  return(0);
 #  }


# import random
# win = 0
# n = 0
# while n < 10000:
#     reelSymbols = ["bar","cherry","plum","bell","orange","lemon"]
#     reelList = []
#     reel1 = [0,1,4,3,2,0,1,5,3,2,4,5,3,2,4,1,5,0,4,3,5]
#     reel2 = [0,2,3,4,5,0,1,2,3,4,5,1,2,3,4,5,2,3,4,5,1]
#     reel3 = [0,4,5,3,2,4,1,3,5,4,2,5,1,4,5,3,4,5,3,2,5]
#     rnd1 = random.randint(0,(len(reel1)-1))
#     rnd2 = random.randint(0,(len(reel2)-1))
#     rnd3 = random.randint(0,(len(reel3)-1))
#     pick1 = reel1[rnd1]
#     pick2 = reel2[rnd2]
#     pick3 = reel3[rnd3]
#     symbol1 = reelSymbols[pick1]
#     symbol2 = reelSymbols[pick2]
#     symbol3 = reelSymbols[pick3]
#     if pick1 == 0 and pick2==0 and pick3==0:
#         win=win+1
#     n=n+1
# print(win)
