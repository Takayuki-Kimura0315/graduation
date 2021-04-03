import nurse2cost
import nurse2time
import nurse2night
import Rnurse2cost
import random
import time

global N


file=open("absent.txt")
f=file.readline().split()
number=int(f[0])
file.close()

file=open("costlog.txt","a")
start=time.time()
file.write(str(number))
file.write("\t")

loopnumber=50
file.write(str(loopnumber))
file.write("\t")

#costcost計算
costcost=0
Ncostcost=nurse2cost.do(0)
for n in range(loopnumber):
    Rcostcost=Rnurse2cost.do(1)
    costcost+=(Rcostcost-Ncostcost)*3

for n in range(loopnumber):
    Rcostcost=Rnurse2cost.do(2)
    costcost+=(Rcostcost-Ncostcost)*2

for n in range(loopnumber):
    Rcostcost=Rnurse2cost.do(3)
    costcost+=(Rcostcost-Ncostcost)*1

#timecost計算
timecost=0
Ntimecost=nurse2time.do(0)
for n in range(loopnumber):
    Rtimecost=Rnurse2cost.do(1)
    timecost+=(Rtimecost-Ntimecost)*3

for n in range(loopnumber):
    Rtimecost=Rnurse2cost.do(2)
    timecost+=(Rtimecost-Ntimecost)*2

for n in range(loopnumber):
    Rtimecost=Rnurse2cost.do(3)
    timecost+=(Rtimecost-Ntimecost)*1

#nightcost計算
nightcost=0
Nnightcost=nurse2night.do(0)
for n in range(loopnumber):
    Rnightcost=Rnurse2cost.do(1)
    nightcost+=(Rnightcost-Nnightcost)*3

for n in range(loopnumber):
    Rnightcost=Rnurse2cost.do(2)
    nightcost+=(Rnightcost-Nnightcost)*2

for n in range(loopnumber):
    Rnightcost=Rnurse2cost.do(3)
    nightcost+=(Rnightcost-Nnightcost)*1


print(costcost)
print(timecost)
print(nightcost)

file.write(str(costcost))
file.write("\t")
file.write(str(timecost))
file.write("\t")
file.write(str(nightcost))
file.write("\t")


if costcost>timecost:
    if timecost>nightcost:
        print("nightcost")
        file.write("night\t")
        finalNcost=nurse2night.do(0)
    else:
        print("timecost")
        file.write("time\t")
        finalNcost=nurse2time.do(0)
else:
    if costcost>nightcost:
        print("nightcost")
        file.write("night\t")
        finalNcost=nurse2night.do(0)
    else:
        print("costcost")
        file.write("cost\t")
        finalNcost=nurse2cost.do(0)


elapsed_time=time.time()-start
print("elapsed_time:{0}".format(elapsed_time)+"[sec]")
file.write("{0}".format(elapsed_time))
file.write("\t")

#パターン1のチェック
finalRcost=Rnurse2cost.do(4)
finalcost=finalRcost-finalNcost
print(finalcost)
file.write(str(finalcost))
file.write("\t")

#パターン2のチェック
finalRcost=Rnurse2cost.do(5)
finalcost=finalRcost-finalNcost
print(finalcost)
file.write(str(finalcost))
file.write("\t")

#パターン3のチェック
finalRcost=Rnurse2cost.do(6)
finalcost=finalRcost-finalNcost
print(finalcost)
file.write(str(finalcost))
file.write("\t")

#比較のためのコスト基準スケジューリング
start=time.time()
finalNcost=nurse2cost.do(0)
elapsed_time=time.time()-start
print("elapsed_time:{0}".format(elapsed_time)+"[sec]")
file.write("{0}".format(elapsed_time))
file.write("\t")
#パターン1
finalRcost=Rnurse2cost.do(4)
finalcost=finalRcost-finalNcost
print(finalcost)
file.write(str(finalcost))
file.write("\t")

#パターン2
finalRcost=Rnurse2cost.do(5)
finalcost=finalRcost-finalNcost
print(finalcost)
file.write(str(finalcost))
file.write("\t")

#パターン3
finalRcost=Rnurse2cost.do(6)
finalcost=finalRcost-finalNcost
print(finalcost)
file.write(str(finalcost))
file.write("\n")
