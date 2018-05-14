'''
绘制论文中的相关实验结果图片
'''

import matplotlib.pyplot as plt
import numpy


def main():
    x = [3]
    y = [1, 2, 1]
    draw_line_chart(x, y, "test")


def draw_line_chart(x, y, label):
    '''绘制折线图
    参数：
    x,y - []
    x_label,y_label - string
    '''
    # 载入数据
    # 如果x只有一个值n，则重新给x赋值0~n
    if(len(x) == 1):
        x = [i for i in range(x[0])]
    x = numpy.array(x)
    y = numpy.array(y)

    # 检验数据
    print('x=', x)
    print('y=', y)

    # 绘制
    plt.plot(x, y, color="blue", linewidth=2.5, linestyle="-", label=label)

    # 设置边界
    plt.xlim(x.min() - 1, x.max() + 1)
    plt.ylim(y.min() - 1, y.max() + 1)

    # 设置刻度
    plt.xticks(x)
    plt.yticks([y.min(), y.max()])

    # 设置刻度标签
    # 暂时用不到，不学了

    # 移动轴线
    ax = plt.gca()
    # 右边和上边的轴线设置为无
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    # 添加图例
    plt.legend(loc='upper left')

    # 显示
    plt.show()


if __name__ == '__main__':
    main()
