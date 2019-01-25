from __future__ import division
import pandas as pd
import utils
import numpy as np
import math
import matplotlib.pyplot as plt

citys=pd.read_csv('cities.csv')  #sep='\t',header=None
citys.drop(['CityId'], axis=1, inplace=True)
#print (citys.head(5))

start=list(citys.iloc[0])
end=list(citys.iloc[0])
citys=citys.drop([0])
citys.index=[i for i in range(len(citys))]
paths=[i for i in range(len(citys))]# initiate path

#random path and calculate distance to sreach for optimal initiate temperature
distance1=0
distance2=0
dif=0
for i in range(10):
    #np.random.shuffle(path)
    newPaths1=list(np.random.permutation(paths))
    newPaths2=list(np.random.permutation(paths))
    distance1=utils.CalLength(citys,newPaths1,start,end)
    distance2=utils.CalLength(citys,newPaths2,start,end)
    difNew=abs(distance1-distance2)
    if difNew>=dif:
        dif=difNew

Pr=0.5 #initiate accept possibility
T0=dif/Pr#initiate terperature
T=T0
Tmin=T/50
k=10*len(paths) #times of internal circulation
length=0#initiate distance according to the initiate path
length=utils.CalLength(citys,paths,start,end)

t=0 #time
'''
while T>Tmin:
    for i in range(k):
        a=0
        b=0
        newPaths=paths
        while a==b:
            a=np.random.randint(0,len(paths))
            b=np.random.randint(0,len(paths))
        te=newPaths[a]
        newPaths[a]=newPaths[b]
        newPaths[b]=te
        newLength=utils.CalLength(citys,newPaths,start,end)
        if newLength<length:
            length=newLength
        else:
             #metropolis principle
             p=math.exp(-(newLength-length)/T)
             r=np.random.uniform(low=0,high=1)
             if r<p:
                 length=newLength
    t+=1
    print t
    T=T0/(1+t)
print length
'''
paths=list(np.random.permutation(paths))
length=utils.CalLength(citys,paths,start,end)
print (length)
while T>Tmin:
    for i in range(k):
        newPaths=paths
        for j in range(int(T0/500)):
            a=0
            b=0
            while a==b:
                a=np.random.randint(0,len(paths))
                b=np.random.randint(0,len(paths))
            te=newPaths[a]
            newPaths[a]=newPaths[b]
            newPaths[b]=te
        newLength=utils.CalLength(citys,newPaths,start,end)
        if newLength<length:
            length=newLength
        else:
             #metropolis principle
             p=math.exp(-(newLength-length)/T)
             r=np.random.uniform(low=0,high=1)
             if r<p:
                 length=newLength
    back=np.random.uniform(low=0,high=1)
    if back>=0.85:
        T=T*2
        continue
    t+=1
    print (t)
    T=T0/(1+t)
print (length)

citys['order']=paths
citys_order=citys.sort_values(by=['order'])
plt.plot(citys_order['X'],citys_order['Y'])
print(paths)

###模拟退火：兔子喝醉了。它随机地跳了很长时间。这期间，它可能走向高处，也可能踏入平地。但是，它渐渐清醒了并朝最高方向跳去。这就是模拟退火。
###旅行商问题属于所谓的NP完全问题（是世界七大数学难题之一。NP的英文全称是Non-deterministicPolynomial的问题，即多项式复杂程度的非确定性问题），精确的解决TSP只能通过穷举所有的路径组合，其时间复杂度是O(N!) 。
###使用模拟退火算法可以比较快的求出TSP的一条近似最优路径。模拟退火解决TSP的思路：
###1. 产生一条新的遍历路径P(i+1)，计算路径P(i+1)的长度L( P(i+1))
###2. 若L(P(i+1))< L(P(i))，则接受P(i+1)为新的路径，否则以模拟退火的那个概率接受P(i+1) ，然后降温
###3. 重复步骤1，2直到满足退出条件
###产生新的遍历路径的方法有很多，下面列举其中3种：
###1. 随机选择2个节点，交换路径中的这2个节点的顺序。
###2. 随机选择2个节点，将路径中这2个节点间的节点顺序逆转。
###3. 随机选择3个节点m，n，k，然后将节点m与n间的节点移位到节点k后面。

