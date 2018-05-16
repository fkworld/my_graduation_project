'''
绘制论文中的相关实验结果图片
'''

import matplotlib.pyplot as plt
import numpy


def main():
    x, y1, y2, y3, y4 = set_ex1_data()
    draw_line_chart_single(x, y1, "label", "title")
    draw_line_chart_single(x, y2, "label", "title")
    draw_line_chart(x, y3, y4, "label", "label", "title")


def set_ex1_data():
    '''设置实验一数据
    返回值：x,y1,y2,y3,y4
    '''
    x = [20]
    y1 = [
        10.9,
        10.9,
        10.9,
        10.8,
        10.9,
        11.0,
        25.5,
        73.8,
        74.0,
        74.1,
        77.6,
        73.5,
        77.1,
        70.4,
        46.0,
        10.9,
        10.9,
        11.0,
        10.9,
        10.9
    ]
    y2 = [
        5161,
        5149,
        5169,
        5180,
        5191,
        5174,
        9106,
        9098,
        9099,
        9107,
        9111,
        9111,
        9113,
        9117,
        9123,
        5313,
        5383,
        5305,
        5371,
        5341
    ]
    y3 = [
        723739,
        723741,
        724190,
        724281,
        724530,
        724643,
        724659,
        724678,
        724643,
        724656,
        724648,
        724649,
        724647,
        724648,
        724712,
        724888,
        724394,
        724678,
        724976,
        724504
    ]
    y4 = [
        69584,
        69584,
        69584,
        69584,
        69584,
        69584,
        69665,
        69651,
        69653,
        69659,
        69644,
        69676,
        69678,
        69679,
        69688,
        69679,
        69670,
        69670,
        69670,
        69670
    ]
    return x, y1, y2, y3, y4


def draw_line_chart_single(x, y, label_y, title):
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
    x = x + 1
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
    x += 1
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
