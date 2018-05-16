'''
绘制论文中的相关实验结果图片
'''

import matplotlib.pyplot as plt
import numpy

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 设置负号
plt.figure(figsize=(8, 5))  # 设置输出图像大小（单位：英寸） # 实际大小800*500


def main():
    draw_ex1_pic()
    draw_ex3_pic()
    draw_ex4_pic()


def draw_ex1_pic():
    '''绘制实验1图片
    '''
    y1, y2, y3, y4 = set_ex1_data()
    draw_line_chart([y1], ['系统CPU利用率'], xlabel='次序',
                    ylabel='CPU利用率（单位：%）', title='系统CPU利用率变化图', save_filename='ex1_1')
    draw_line_chart([y2], ['系统已用内存'], xlabel='次序',
                    ylabel='系统已用内存（单位：MB）', title='系统已用内存变化图', save_filename="ex1_2")
    draw_line_chart([y3, y4], ['磁盘总读个数', '磁盘总写个数'], xlabel='次序',
                    ylabel='磁盘读写连接（单位：个）', title='系统磁盘IO变化图', save_filename='ex1_3')


def draw_ex3_pic():
    '''绘制实验3图片
    '''
    kinds, values, y_1_1, y_1_2, y_2_1, y_2_2, y_3_1, y_3_2 = set_ex3_data()
    draw_line_chart(
        ylist=[y_1_1, y_2_1, y_3_1],
        labelylist=['渲染过程中无附加条件', '渲染过程中加入死循环', '渲染过程中加入FTP下载进程'],
        xlabel='次序',
        ylabel='系统CPU利用率（单位：%）',
        title='任务前后CPU利用率变化图',
        save_filename='ex2_1'
    )
    draw_line_chart(
        ylist=[y_1_2, y_2_2, y_3_2],
        labelylist=['渲染过程中无附加条件', '渲染过程中加入死循环', '渲染过程中加入FTP下载进程'],
        xlabel='次序',
        ylabel='系统已用内存（单位：GB）',
        title='任务前后系统已用内存变化图',
        save_filename='ex2_2'
    )
    draw_barh(kinds, values, '渲染时长（单位：s）', '平均渲染时长对比图', 'ex2_3')


def draw_ex4_pic():
    '''绘制实验4图片
    '''
    kinds, values_1_1, values_1_2, values_2_1, values_2_2 = set_ex4_data()
    draw_barh(kinds, values_1_1, "渲染任务队列完成时间（单位：s）",
              "渲染任务队列一完成时间对比图", "ex4_1")
    draw_barh(kinds, values_1_2, "主控节点通信次数（单位：次）",
              "渲染任务队列一主控节点通信次数对比图", "ex4_2")
    draw_barh(kinds, values_2_1, "渲染任务队列完成时间（单位：s）",
              "渲染任务队列二完成时间对比图", "ex4_3")
    draw_barh(kinds, values_2_2, "主控节点通信次数（单位：次）",
              "渲染任务队列二主控节点通信次数对比图", "ex4_4")


def set_ex1_data():
    '''设置实验一数据
    返回值：y1,y2,y3,y4
    '''
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
    return y1, y2, y3, y4


def set_ex3_data():
    '''设置实验三数据
    返回值：kinds, values, y_1_1, y_1_2, y_2_1, y_2_2, y_3_1, y_3_2
    '''
    kinds = ["渲染过程中无附加条件", "渲染过程中加入死循环进程", "渲染过程中加入FTP下载进程"]
    values = [42.3, 83.3, 73.4]
    y_1_1 = [10, 10, 42, 70, 70, 70, 71, 70,
             70, 67, 10, 10]  # 任务前后CPU利用率变化队列（单位：%）
    # 任务前后系统内存变化队列（单位：GB）
    y_1_2 = [5.1, 5.1, 9.0, 9.1, 9.1, 9.1, 9.1, 9.1, 9.1, 9.2, 5.2, 5.2]
    y_2_1 = [10, 10, 45, 70, 100, 100, 100, 100, 100,
             100, 100, 100, 71, 70, 70, 70, 72, 67, 15, 10]
    y_2_2 = [5.0, 5.0, 9.1, 9.1, 15.5, 15.5, 15.5, 15.5, 15.5, 15.5,
             15.5, 15.5, 9.0, 9.2, 9.2, 9.2, 9.2, 9.2, 5.1, 5.1]
    y_3_1 = [10, 10, 41, 75, 80, 81, 80, 82, 83, 80, 80, 68, 40, 10]
    y_3_2 = [5.0, 5.0, 9.1, 11.1, 10.5, 10.5,
             10.6, 10.6, 10.6, 10.6, 10.6, 9.1, 5.1, 5.1]
    # 验证数据是否合理
    print("y1.len=", len(y_1_1), len(y_1_2))
    print("y2.len=", len(y_2_1), len(y_2_2))
    print("y3.len=", len(y_3_1), len(y_3_2))
    return kinds, values, y_1_1, y_1_2, y_2_1, y_2_2, y_3_1, y_3_2


def set_ex4_data():
    '''设置实验四数据
    '''
    kinds = ["FIFO", "分级负载均衡", "条件分级负载均衡"]
    # 100个任务复杂度相同的渲染任务队列统计表
    values_1_1 = [417, 334, 315]  # 渲染队列整体完成时间（单位秒）
    values_1_2 = [100, 696, 651]  # 主控节点通信次数（单位次）
    # 20个高任务复杂度加上80个低任务复杂度的渲染任务队列统计表
    values_2_1 = [588, 443, 383]
    values_2_2 = [100, 1103, 796]
    return kinds, values_1_1, values_1_2, values_2_1, values_2_2


def draw_line_chart(ylist, labelylist, xlabel, ylabel, title, save_filename):
    """绘制折线图
    参数：
    ylist - [[]]，y的数据集
    labelylist - [string]，每一组y数据集的含义（label）
    xlabel,ylabel - string，坐标轴名称
    title - string
    save_filename - string，保存的文件名
    """
    # 载入数据
    # 将ylist中的每一项转换成numpy.array格式，外部不变
    for i, y in enumerate(ylist):
        ylist[i] = numpy.array(y)
    # 根据ylist中的每一项的个数写入xlist
    xlist = []
    for y in ylist:
        x = [i for i in range(y.size)]
        x = numpy.array(x)
        x += 1  # 从1开始
        xlist.append(x)

    # 检验数据
    print("xlist=", xlist)
    print("ylist=", ylist)

    # 绘制
    # 4种linestyle
    draw_linestyle = ['-', ':', '--', '-.']  # 依次是：直线，点线，虚线，虚线带点
    # n种marker，选择4种
    draw_marker = ['o', 'D', '*', 'v']  # 依次是：圆形，棱形，星型，三角型
    # 选择4种color
    draw_color = ['blue', 'red', 'green', 'gray']

    for i, y in enumerate(ylist):
        plt.plot(xlist[i], y, color=draw_color[i], linewidth=2.5,
                 linestyle=draw_linestyle[i], marker=draw_marker[i], label=labelylist[i])

    # 设置坐标轴名称
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # 获取最大值
    x_max = numpy.array([x.max() for x in xlist]).max()
    y_max = numpy.array([y.max() for y in ylist]).max()
    # 设置边界
    plt.xlim(0, x_max * 1.1)
    plt.ylim(0, y_max * 1.1)

    # 设置刻度
    plt.xticks(numpy.arange(0, x_max + 2, 1))

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
    plt.legend(loc='best')  # 位置为自动选择

    # 添加图标题
    plt.title(title)

    # 保存
    # 注意要先保存后显示，否则会保存一个空白图片
    # 在 plt.show() 后实际上已经创建了一个新的空白的图片（坐标轴），这时候你再 plt.savefig() 就会保存这个新生成的空白图片。
    plt.savefig(save_filename + '.png')
    plt.clf()  # 保存之后及时清理，否则会在原有图的基础上进行绘制

    # 显示
    # plt.show()


def draw_barh(kinds, values, ylabel, title, save_filename):
    '''绘制柱状图
    '''

    # 绘制
    # 还是改成了bar()，barh()函数的资料太少了
    plt.bar(kinds, values, width=0.3, alpha=0.8)

    # 添加图标题
    plt.title(title)

    # 设置坐标轴名称
    plt.ylabel(ylabel)

    # 设置边界
    # 获取最大值
    value_max = numpy.array(values).max()
    # 设置边界
    plt.xlim(0, value_max * 1.1)

    # 自动改变大小，我也不知道为什么要加。
    plt.autoscale()

    # 保存，同上
    plt.savefig(save_filename + '.png')
    plt.clf()

    # 显示
    # plt.show()


if __name__ == '__main__':
    main()
