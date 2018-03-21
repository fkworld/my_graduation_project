# 实验：利用psutil模块获取系统的实时信息
# 包含：CPU相关，内存相关，磁盘IO相关

import psutil

# CPU相关输出
# CPU逻辑个数
print("CPU逻辑个数：", psutil.cpu_count())
# CPU物理个数
print("CPU物理个数：", psutil.cpu_count(logical=False))

# 内存相关输出
# 系统物理内存（单位MB）
print("系统总内存：", psutil.virtual_memory().total / 1000000)
print("系统可用内存：", psutil.virtual_memory().available / 1000000)
print("系统使用内存：", psutil.virtual_memory().used / 1000000)

# 磁盘IO相关输出
print("磁盘IO：", psutil.disk_io_counters())
