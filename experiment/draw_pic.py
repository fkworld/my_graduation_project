'''
绘制论文中的相关实验结果图片
'''

import matplotlib.pyplot as plt
import numpy


def main():
    draw_ex1_pic()


def draw_ex1_pic():
    x, y1, y2, y3, y4 = set_ex1_data()
    draw_line_chart(x, [y1], 'labelx', ['系统CPU利用率'], 'title')
    draw_line_chart(x, [y2], 'labelx', ['系统已用内存'], 'title')
    draw_line_chart(x, [y3, y4], 'labelx', ['磁盘总读个数', '磁盘总写个数'], 'title')


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


def set_ex3_data():
    '''设置实验三数据
    '''
    kinds = ["渲染过程中无附加条件", "渲染过程中加入死循环进程", "渲染过程中加入FTP下载进程"]
    values = [42.3, 83.3, 73.4]
    x = [20]
    y_1_1 = [10, 10, 42, 70, 70, 70, 71, 70,
             70, 67, 10, 10]  # 任务前后CPU利用率变化队列（单位：%）
    # 任务前后系统内存变化队列（单位：GB）
    y_1_2 = [5.1, 5.1, 9.0, 9.1, 9.1, 9.1, 9.1, 9.1, 9.1, 9.2, 5.2, 5.2]
    y_2_1 = [10, 10, 45, 70, 100, 100, 100, 100, 100,
             100, 100, 100, 71, 70, 70, 70, 72, 67, 15, 10]
    y_2_2 = [5.0, 5.0, 9.1, 9.1, 15.5, 15.5, 15.5, 15.5, 15.5, 15.5,
             15.5, 15.5, 9.0, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 5.1, 5.1]
    y_3_1 = [10, 10, 41, 75, 80, 81, 80, 82, 83, 80, 80, 68, 40, 10]
    y_3_2 = [5.0, 5.0, 9.1, 11.1, 10.5, 10.5,
             10.6, 10.6, 10.6, 10.6, 10.6, 9.1, 5.1]
    return kinds, values, x, y_1_1, y_1_2, y_2_1, y_2_2, y_3_1, y_3_2


def set_ex4_data():
    '''设置实验四数据
    '''
    kinds = ["FIFO算法", "分级负载均衡算法", "条件分级负载均衡算法"]
    # 100个任务复杂度相同的渲染任务队列统计表
    values_1_1 = [417, 334, 315]  # 渲染队列整体完成时间（单位秒）
    values_1_2 = [100, 696, 651]  # 主控节点通信次数（单位次）
    # 20个高任务复杂度加上80个低任务复杂度的渲染任务队列统计表
    values_2_1 = [588, 443, 383]
    values_2_2 = [100, 1103, 796]
    return kinds, values_1_1, values_1_2, values_2_1, values_2_2


def draw_line_chart(x, ylist, labelx, labelylist, title):
    '''绘制折线图
    参数：
    x - []
    ylist - [[]]
    labelx - string
    labelylist - [string]
    title - string
    '''
    # 载入数据
    # 如果x只有一个值n，则重新给x赋值0~n，再+1到1~n+1
    if(len(x) == 1):
        x = [i for i in range(x[0])]
    x = numpy.array(x)
    x += 1
    for y in ylist:
        y = numpy.array(y)

    # 检验数据
    print("x=", x)
    print("ylist=", ylist)

    # 绘制
    # 4种linestyle
    draw_linestyle = ['-', ':', '--', '-.']  # 依次是：直线，点线，虚线，虚线带点
    # n种marker，选择4种
    draw_marker = ['o', 'D', '*', 'v']  # 依次是：圆形，棱形，星型，三角型
    # 选择4种color
    draw_color = ['blue', 'red', 'green', 'gray']

    for i, y in enumerate(ylist):
        plt.plot(x, y, color=draw_color[i], linewidth=2.5,
                 linestyle=draw_linestyle[i], marker=draw_marker[i], label=labelylist[i])

    # 设置边界
    plt.xlim(0, x.max() * 1.1)
    plt.ylim(0, numpy.array([numpy.array(y).max() for y in ylist]).max() * 1.1)

    # 设置刻度

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
