def bag(n, c, w, v):
    res = [[-1 for j in range(c + 1)] for i in range(n + 1)]
    print(res) # 初始化状态
    for j in range(c + 1):
        res[0][j] = 0
    print(res) # 初始化第0次的状态
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            res[i][j] = res[i - 1][j]
            if j >= w[i - 1] and res[i][j] < res[i - 1][j - w[i - 1]] + v[i - 1]:
                res[i][j] = res[i - 1][j - w[i - 1]] + v[i - 1]
        print(res)
    print(res)
    return res


def show(n, c, w, res):
    print('最大价值为:', res[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(1, n + 1):
        if res[i][j] > res[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('选择的物品为:')
    for i in range(n):
        if x[i]:
            print('第', i, '个,', end='')
    print('')


if __name__ == '__main__':
    n = 3
    c = 3
    w = [2, 6, 6]
    v = [1, 1, 1]
    res = bag(n, c, w, v)
    show(n, c, w, res)
