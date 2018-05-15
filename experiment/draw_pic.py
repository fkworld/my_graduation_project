'''
绘制论文中的相关实验结果图片
'''

import matplotlib.pyplot as plt
import numpy


def main():
    x = [3]
    kinds = ['James', 'Durant', 'Kobe']
    values = [4, 5, 6]
    # draw_line_chart(x, y1, y2, "y1", "y2", "test")
    draw_barh(y1, y2, "test")


def draw_line_chart(x, y, label_y, title):
    '''绘制折线图
    参数：
    x,y - []
    label_y - string
    title - string
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
    plt.plot(x, y, color="blue", linewidth=2.5,
             linestyle="-", marker="o", label=label_y)
    '''4种linestyle
    - 直线
    -- 虚线
    -. 虚线带点
    : 点线
    '''
    '''n多种marker，列举几种常用的
    o circle marker
    D,d diamond marker
    * star marker
    v triangle_down marker
    + plus marker
    x x marker
    '''

    # 设置边界
    plt.xlim(0, x.max() + 1)
    plt.ylim(0, y.max() + 1)

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

    # 添加图标题
    plt.title(title, bbox=dict(
        facecolor='white', edgecolor='blue', alpha=0.65))

    # 显示
    plt.show()


def draw_line_chart(x, y1, y2, label_y1, label_y2, title):
    '''绘制折线图
    参数：
    x,y1,y2 - []
    label_y1,label_y2 - string
    title - string
    '''
    # 载入数据
    # 如果x只有一个值n，则重新给x赋值0~n
    if(len(x) == 1):
        x = [i for i in range(x[0])]
    x = numpy.array(x)
    y1 = numpy.array(y1)
    y2 = numpy.array(y2)
    y = y1 + y2  # 绘制数据

    # 检验数据
    print('x=', x)
    print('y1=', y1)
    print('y2=', y2)

    # 绘制
    plt.plot(x, y1, color="blue", linewidth=2.5,
             linestyle="-", marker="o", label=label_y1)
    plt.plot(x, y2, color="red", linewidth=2.5,
             linestyle="--", marker="D", label=label_y2)
    '''4种linestyle
    - 直线
    -- 虚线
    -. 虚线带点
    : 点线
    '''
    '''n多种marker，列举几种常用的
    o circle marker
    D,d diamond marker
    * star marker
    v triangle_down marker
    + plus marker
    x x marker
    '''

    # 设置边界
    plt.xlim(0, x.max() * 1.1)
    plt.ylim(0, y.max() * 1.1)

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

    # 添加图标题
    plt.title(title, bbox=dict(
        facecolor='white', edgecolor='blue', alpha=0.65))

    # 显示
    plt.show()


def draw_barh(kinds, values, title):
    '''绘制柱状图
    '''

    # 转换数据
    kinds = numpy.arange(len(kind))
    values = numpy.arange()

    plt.barh(y_pos, performance, xerr=error, align='center',
             alpha=0.4)  # 这里是产生横向柱状图 barh h--horizontal
    plt.yticks(y_pos, people)
    plt.xlabel('Performance')

    # 添加图标题
    plt.title(title, bbox=dict(
        facecolor='white', edgecolor='blue', alpha=0.65))

    # 显示
    plt.show()


if __name__ == '__main__':
    main()
