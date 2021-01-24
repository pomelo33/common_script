#!/usr/bin/env python3
# 脚本内容为系统监控脚本
import psutil
import datetime
import os

# 获取磁盘信息
def Disk_Use():
    # 获取磁盘信息
    disks = psutil.disk_partitions()
    for disk in disks:
        try:
            # 获取disk总空间
            disk_total = (psutil.disk_usage(disk.mountpoint).total)/1024/1024/1024
            # 获取disk使用空间
            disk_use = (psutil.disk_usage(disk.mountpoint).used)/1024/1024/1024
            # 获取disk空闲空间
            disk_free = (psutil.disk_usage(disk.mountpoint).free)/1024/1024/1024
            # disk使用率
            disk_rate = (disk_use / disk_total * 100)
            print(disk.mountpoint + " 磁盘总空间: {:.2f}GB".format(disk_total)  + " 磁盘空闲空间: {:.2f}GB".format(disk_free) + " 使用率: {:.1f}%".format(disk_rate))
        except OSError as error:
            print(disk.device + "获取失败")

# 获取内存信息
def Mem_Use():
    # 获取总内存
    mem_total = (psutil.virtual_memory().total)/1024/1024/1024
    # 获取空闲内存
    mem_free = (psutil.virtual_memory().free)/1024/1024/1024
    # 获取使用内存
    mem_use = (psutil.virtual_memory().used)/1024/1024/1024
    # 内存使用率
    mem_rate = (mem_use / mem_total * 100)
    # 获取交换分区总内存
    swap_total = (psutil.swap_memory().total)/1024/1024/1024
    # 获取交换分区使用内存
    swap_use = (psutil.swap_memory().used)/1024/1024/1024
    # 获取交换分区空闲内存
    swap_free = (psutil.swap_memory().free)/1024/1024/1024
    # 交换分区使用率
    swap_rate = (swap_use / swap_total * 100 )

    print("总内存: {:.2f}G".format(mem_total) + " 空闲内存: {:.2f}G".format(mem_free) + " 内存使用率: {:.0f}%".format(mem_rate) + "\nswap总空间: {:.2f}G".format(swap_total) + " swap空闲空间: {:.2f}G".format(swap_free) + " swap使用率: {:.0f}%".format(swap_rate))

if __name__ == "__main__":
    Disk_Use()
    Mem_Use()