#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v2.0 04AE7702 maqiang <maqiang626@qq.com> [2020-10-18 22:52 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# 哲学家就餐问题
#
# ==================================================================
#

import random
import threading
import time
import queue


class DiningPhilosophersThread(threading.Thread):
    def __init__(self, id, forks, eat_num, output_queue):
        threading.Thread.__init__(self)
        self.id = id
        self.forks = forks
        self.eat_num = eat_num
        self.output_queue = output_queue
        self.dishes = 0

    def run(self):
        self.run_eat()

        if self.dishes < self.eat_num:
            time.sleep(2)
            self.run()

    def run_eat(self):
        try:
            left_fork = self.id
            right_fork = (self.id + 1) % len(self.forks)

            if self.forks[left_fork].acquire(False):
                # 拿起左边叉子
                self.output_queue.put((f'{self.id},1,1'))
                print(f'{time.time()} Philosopher {self.id} pick up the left fork')

                if self.forks[right_fork].acquire(False):
                    # 拿起右边叉子
                    self.output_queue.put((f'{self.id},2,1'))
                    print(
                        f'{time.time()} Philosopher {self.id} pick up the right fork')

                    # 吃面 (吃面次数加 1)
                    self.output_queue.put((f'{self.id},0,3'))
                    self.dishes += 1
                    time.sleep(random.uniform(2, 6))
                    print(f'{time.time()} Philosopher {self.id} is eating')

                    # 放下右边叉子
                    self.output_queue.put((f'{self.id},2,2'))
                    self.forks[right_fork].release()
                    print(
                        f'{time.time()} Philosopher {self.id} put down the right fork')

                    # 放下左边叉子
                    self.output_queue.put((f'{self.id},1,2'))
                    self.forks[left_fork].release()
                    print(
                        f'{time.time()} Philosopher {self.id} put down the left fork')
                else:
                    # 当不能获取右边叉子时，放下左边已经拿到的叉子
                    self.forks[left_fork].release()
                    time.sleep(1)
                    self.run()
            else:
                time.sleep(1)
                self.run()

        except Exception as e:
            print(f'Error: {e}')


def get_eat_num():
    """获取用户输入次数

    输入：n = 1 （1<=n<=60，n 表示每个哲学家需要进餐的次数。）
    """

    while True:
        try:
            global eat_num
            eat_num = int(input('请输入每个哲学家需要进餐的次数(1-60)：'))
            if type(eat_num) != int:
                continue
            else:
                print(f'每个哲学家需要进餐的次数：{eat_num}')
                print(f'开始进餐...\n')
                break
        except:
            print('请输入合法数字！')


eat_num = 0                       # 每个哲学家需要进餐的次数
philosophers_num = 5              # 哲学家数量
forks = []                        # 线程锁
philosophers_threads = []         # 开启多线程列表
output_queue = queue.Queue(2626)  # 输出列表对应队列
behavior_record = []              # 所有哲学家的具体行为对应列表


if __name__ == '__main__':
    get_eat_num()  # 获取用户输入次数

    # 获取所有哲学家的线程锁
    for i in range(philosophers_num):
        forks.append(threading.RLock())

    # 开启多线程列表
    for id in range(philosophers_num):
        philosophers_threads.append(
            DiningPhilosophersThread(id, forks, eat_num, output_queue))

    # 启动多线程
    for philosophers_thread in philosophers_threads:
        philosophers_thread.start()

    for philosophers_thread in philosophers_threads:
        philosophers_thread.join()

    while not output_queue.empty():
        behavior_record.append(output_queue.get())

    print(f'======================= {time.time()} =======================')
    print(f'每个哲学家已进餐的次数：{philosophers_thread.dishes}')
    print(f'所有哲学家的行为总次数：{len(behavior_record)}')
    print(f'所有哲学家具体行为记录：{behavior_record}')
