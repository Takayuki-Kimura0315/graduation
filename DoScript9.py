import nurse2cost
import nurse2time
import nurse2night
import Rnurse2cost
import random
import time

global N

file=open("Nursedata.txt")
f=file.readline().split()
N=int(f[0])

file=open("absent.txt","w")
number=random.randint(70,90)
file.write(str(number))
file.write("\n")

for loop in range(number):
    n=random.randint(0,N-1)
    i=random.randint(0,3)
    j=random.randint(0,6)
    file.write(str(n))
    file.write("\t")
    file.write(str(i))
    file.write("\t")
    file.write(str(j))
    file.write("\n")

file.close()

#パターン1チェック用のtxt
file=open("lastabsent1.txt","w")
file.write(str(6))
file.write("\n")

for loop in range(6):
    n=random.randint(0,N-1)
    i=random.randint(0,3)
    j=random.randint(0,6)
    file.write(str(n))
    file.write("\t")
    file.write(str(i))
    file.write("\t")
    file.write(str(j))
    file.write("\n")

file.close()

#パターン2チェック用のtxt
file=open("lastabsent2.txt","w")
file.write(str(4))
file.write("\n")

n=random.randint(0,N-1)
i=random.randint(0,3)
if i==3:
    j=random.randint(0,3)
else:
    j=random.randint(0,6)
#print(n,i,j)
for l in range(4):
    file.write(str(n))
    file.write("\t")
    file.write(str(i))
    file.write("\t")
    file.write(str(j))
    file.write("\n")
    if j!=6:#週を跨がない時
        j=j+1
    else:
        if i!=3:#月を跨がない時
            i=i+1
            j=0
        else:
            break
file.close()

#パターン3チェック用のtxt
file=open("lastabsent3.txt","w")
file.write(str(9))
file.write("\n")

week=random.randint(0,3)
if week==3:
    day=random.randint(0,3)
else:
    day=random.randint(0,6)
for n in range(3):
    n=random.randint(0,N-1)
    i=week
    j=day
    #print(n,i,j)
    for l in range(3):
        file.write(str(n))
        file.write("\t")
        file.write(str(i))
        file.write("\t")
        file.write(str(j))
        file.write("\n")
        if j!=6:#週を跨がない時
            j=j+1
        else:
            if i!=3:#月を跨がない時
                i=i+1
                j=0
            else:
                break

file.close()
