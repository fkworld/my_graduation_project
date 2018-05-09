'''
    01背包问题的动态规划实现
    阶段：在前N件物品中，选取若干件物品放入背包中
    状态：在前N件物品中，选取若干件物品放入所剩空间为W的背包中的所能获得的最大价值
    决策：第N件物品放或者不放

    缺点：时间复杂度（number*weight）太高了！在实际使用中耗费的资源太大
'''

from numpy import zeros
from random import randint

def solve(vlist,wlist,totalWeight,totalLength):
    resArr = zeros((totalLength+1,totalWeight+1))
    for i in range(1,totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
            else:
                resArr[i,j] = resArr[i-1,j]
    return resArr[-1,-1] # 数组的负索引：list[-n] == list[len(list) - n]

if __name__ == '__main__':
    v = [0,60,100,120]
    w = [0,60,100,120]
    weight = 160
    n = 3
    result = solve(v,w,weight,n)
    print(result)