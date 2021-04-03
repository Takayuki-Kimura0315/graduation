from gurobipy import *
import random

model=Model("Rnurse")
Early,Late,Night,Off=0,1,2,3
Sun,Mon,Tue,Wen,Thu,Fri,Sat=0,1,2,3,4,5,6
FullTime,PartTime,DayOnly=0,1,2

Shift,Ho=multidict({Early:8, Late:8, Night:8, Off:0})#シフトの種類と一回あたりの勤務時間
Day=[Sun,Mon,Tue,Wen,Thu,Fri,Sat]#曜日の種類
Week=[i for i in range(4)]#４週間のスケジューリング
Nursename={}
Estatus,Homax=multidict({FullTime:144, PartTime:144, DayOnly:72})
ESNurse={}
Necessary={}
Shortagecost={}
Surpluscost={}
Nallocation={}
Rallocation={}
Confusion={}
allocation={}

def readNursedata():#ナースの名前、雇用形態を読み取る関数
    global N
    file=open("Nursedata.txt")
    f=file.readline().split()
    N=int(f[0])
    for i in range(N):
        f=file.readline().split()
        Nursename[i]=f[0]#ナースの名前
        ESNurse[i]=int(f[1])#各ナースの雇用形態
    return 0

def readNecessaryandCost():#必要人数、人数不足コスト、人数余剰コストを読み取る関数
    file=open("NecessaryandCost.txt")
    for i in range(4):#週
        for j in range(7):#曜日
            for k in range(3):#休暇以外の3勤務
                f=file.readline().split()
                Necessary[i,j,k]=int(f[0])#各シフトの必要人数
                Shortagecost[i,j,k]=int(f[1])#一人当たりの人数不足コスト
                Surpluscost[i,j,k]=int(f[2])#一人当たりの人数余剰コスト
            Necessary[i,j,3]=0#各シフトの必要人数
            Shortagecost[i,j,3]=0#一人当たりの人数不足コスト
            Surpluscost[i,j,3]=0#一人当たりの人数余剰コスト
    return 0

def readNallocation():#元の勤務表
    file=open("NSOutput.txt")
    for n in range(N):
        f=file.readline().split()
        for i in range(4):
            for j in range(7):
                for k in range(4):
                    Nallocation[n,i,j,k]=int(f[28*i+4*j+k])

def readConfusion():
    file=open("Confusion.txt")
    for n in range(N):
        f=file.readline().split()
        for k in range(4):
            for r in range(4):
                Confusion[n,k,r]=int(f[4*k+r])

def absent(n,i,j):
    model.addConstr(allocation[n,i,j,3]==1)


def firstabsent():
    file=open("absent.txt")
    f=file.readline().split()
    number=int(f[0])
    for number in range(number):
        f=file.readline().split()
        n=int(f[0])
        i=int(f[1])
        j=int(f[2])
        model.addConstr(allocation[n,i,j,3]==1)
    return 0

def oneonemanyabsent(times):
    for loop in range(times):
        n=random.randint(0,N-1)
        i=random.randint(0,3)
        j=random.randint(0,6)
        model.addConstr(allocation[n,i,j,3]==1)

def onemanyabsent(long):
    n=random.randint(0,N-1)
    i=random.randint(0,3)
    j=random.randint(0,6)
    #print(n,i,j)
    for l in range(long):
        model.addConstr(allocation[n,i,j,3]==1)
        if j!=6:#週を跨がない時
            j=j+1
        else:
            if i!=3:#月を跨がない時
                i=i+1
                j=0
            else:
                break

def manyoneabsent(long,number):
    week=random.randint(0,3)
    day=random.randint(0,6)
    for n in range(number):
        n=random.randint(0,N-1)
        i=week
        j=day
        #print(n,i,j)
        for l in range(long):
            model.addConstr(allocation[n,i,j,3]==1)
            if j!=6:#週を跨がない時
                j=j+1
            else:
                if i!=3:#月を跨がない時
                    i=i+1
                    j=0
                else:
                    break

def lastabsent1():
    file=open("lastabsent1.txt")
    f=file.readline().split()
    number=int(f[0])
    for number in range(number):
        f=file.readline().split()
        n=int(f[0])
        i=int(f[1])
        j=int(f[2])
        model.addConstr(allocation[n,i,j,3]==1)
    return 0

def lastabsent2():
    file=open("lastabsent2.txt")
    f=file.readline().split()
    number=int(f[0])
    for number in range(number):
        f=file.readline().split()
        n=int(f[0])
        i=int(f[1])
        j=int(f[2])
        model.addConstr(allocation[n,i,j,3]==1)
    return 0

def lastabsent3():
    file=open("lastabsent3.txt")
    f=file.readline().split()
    number=int(f[0])
    for number in range(number):
        f=file.readline().split()
        n=int(f[0])
        i=int(f[1])
        j=int(f[2])
        model.addConstr(allocation[n,i,j,3]==1)
    return 0

def Rscheduling(ab):#再スケジューリング
    shortage={}
    surplus={}
    for i in range(4):#週
        for j in range(7):#曜日
            for k in range(4):
                shortage[i,j,k]=model.addVar(vtype="I",lb=0)
                surplus[i,j,k]=model.addVar(vtype="I",lb=0)
                for n in range(N):
                    allocation[n,i,j,k]=model.addVar(vtype="B")#Bは0-1変数,[ナース,週,曜日,シフト]

    model.update()

    firstabsent()

    if ab==1:
        oneonemanyabsent(6)
    elif ab==2:
        onemanyabsent(4)
    elif ab==3:
        manyoneabsent(3,3)
    elif ab==4:
        lastabsent1()
    elif ab==5:
        lastabsent2()
    elif ab==6:
        lastabsent3()

    #割当人数＋不足人数＋余剰人数＝必要人数の制約
    for i in range(4):#週
        for j in range(7):#曜日
            for k in range(3):#休暇以外の3勤務
                #print(quicksum(allocation[n,i,j,k] for n in range(N))+shortage[i,j,k]+surplus[i,j,k]==Necessary[i,j,k])
                model.addConstr(quicksum(allocation[n,i,j,k] for n in range(N)) + shortage[i,j,k] + surplus[i,j,k] == Necessary[i,j,k])
                #model.addConstr(quicksum(allocation[n,i,j,k] for n in range(N))== Necessary[i,j,k])
    #1日1勤務割当制約
    for n in range(N):#ナース
        for i in range(4):#週
            for j in range(7):#曜日
                model.addConstr(quicksum(allocation[n,i,j,k] for k in range(4))==1)#kは休暇を含めた4勤務

    #1週5日勤務まで制約
    for n in range(N):#ナース
        for i in range(4):#週
            model.addConstr(quicksum(allocation[n,i,j,k] for j in range(7) for k in range(3))<=5)#jは曜日,kは休暇以外の3勤務

    #FullTimeのナースは週に夜勤は２回まで
    #FullTime以外のナースは夜勤は無し
    for n in range(N):#ナース
        if ESNurse[n]==0:#FullTimeのナース
            for i in range(4):#週
                model.addConstr(quicksum(allocation[n,i,j,Night] for j in range(7))<=2)
        else:
            for i in range(4):#週
                model.addConstr(quicksum(allocation[n,i,j,Night] for j in range(7))==0)

    #労働時間
    for n in range(N):
        model.addConstr(quicksum(Ho[k]*allocation[n,i,j,k] for i in range(4) for j in range(7) for k in range(4))<=Homax[ESNurse[n]])

    #Nightの次の日はEarlyとLateに割り当てられない,Nightでない日の次の日はEarlyかLateに割り当てられる(一時的に後ろの条件をなくしている)
    for n in range(N):#ナース
        for i in range(4):#週
            for j in range(7):#曜日
                if j!=6:#週を跨がない時
                    model.addConstr(allocation[n,i,j,Night]+allocation[n,i,j+1,Early]+allocation[n,i,j+1,Late]<=1)
                else:#週を跨ぐ時
                    if i!=3:
                        model.addConstr(allocation[n,i,6,Night]+allocation[n,i+1,1,Early]+allocation[n,i+1,1,Late]<=1)


    #Lateの次の日はEarlyに割り当てられない
    for n in range(N):#ナース
        for i in range(4):#週
            for j in range(7):#曜日
                if j!=6:#週を跨がない時
                    model.addConstr(allocation[n,i,j,Late]+allocation[n,i,j+1,Early]<=1)
                else:#週を跨がぐ時
                    if i!=3:#月を跨がない時
                            model.addConstr(allocation[n,i,6,Late]+allocation[n,i+1,1,Early]<=1)

    model.setObjective(quicksum(shortage[i,j,k]*Shortagecost[i,j,k]+surplus[i,j,k]*Surpluscost[i,j,k]+quicksum(Confusion[n,k,r]*Nallocation[n,i,j,k]*allocation[n,i,j,r]*100 for n in range(N) for r in range(4)) for i in range(4) for j in range(7) for k in range(4)),GRB.MINIMIZE)
    model.optimize()

    file=open("RNSOutput.txt","w")

    for n in range(N):
        #print(Nursename[n])
        for i in range(4):
            for j in range(7):
                for k in range(4):
                    Rallocation[n,i,j,k]=int(allocation[n,i,j,k].X)
                    file.write(str(Rallocation[n,i,j,k]))
                    file.write("\t")
                """if Rallocation[n,i,j,0]==1:
                    print("Early",end=" ")
                elif Rallocation[n,i,j,1]==1:
                    print("Late",end=" ")
                elif Rallocation[n,i,j,2]==1:
                    print("Night",end=" ")
                elif Rallocation[n,i,j,3]==1:
                    print("Off",end=" ")
            print("\n")"""
        file.write("\n")
        #print("\n")

    return model.ObjVal

def do(n):
    print("--------------------ここからRcost-------------------------")
    readNursedata()
    readNecessaryandCost()
    readNallocation()
    readConfusion()
    cost=Rscheduling(n)
    return cost

if __name__ == '__main__':
    do()
