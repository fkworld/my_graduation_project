'''
    01背包问题的动态规划实现
    阶段：在前N件物品中，选取若干件物品放入背包中
    状态：在前N件物品中，选取若干件物品放入所剩空间为W的背包中的所能获得的最大价值
    决策：第N件物品放或者不放
'''

from numpy import zeros
from random import randint


class Item(object):
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value



def f(items, number, weight_max):
    o = 0
    result = zeros((number+1, weight_max+1))  # 初始化结果二维数组
    for i in range(1, number+1):
        for j in range(1, weight_max+1):
            o += 1
            if weight_max < items[i].weight:
                # 如果第i个物品
                result[i][j] = result[i - 1][j]
            else:
                v1 = result[i - 1][j]
                v2 = result[i - 1][j - items[i].weight] + items[i].value
                result[i][j] = max(v1, v2)
    print(o)
    print(result[number][weight_max])

def init_items(number):
    items = list()
    for i in range(number):
        random_number = randint(0,20)
        print(random_number,end=' ')
        item = Item(i,random_number, random_number)
        items.append(item)
    return items


if __name__ == '__main__':
    items = init_items(11)
    f(items, 10, 100)
