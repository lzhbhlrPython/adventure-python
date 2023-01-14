"""
使用Numpy和Pygame可视化演绎三体问题的轨迹
显示动画
"""

import numpy as np
import pygame
import sys
from random import random

# 初始化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Three Body Problem")
clock = pygame.time.Clock()

# 随机定义三星的初始位置
star1 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)
star2 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)
star3 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)

# 随机定义三星的初始速度
v1 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)
v2 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)
v3 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)

# 定义三星的质量
m1 = 1
m2 = 1
m3 = 1

# 定义时间步长
dt = 0.01

# 定义重力常数
G = 1

# 定义三星的颜色
c1 = (255, 0, 0)
c2 = (0, 255, 0)
c3 = (0, 0, 255)

# 定义三星的半径
r1 = 10
r2 = 10
r3 = 10

# 定义三星的轨迹
track1 = []
track2 = []
track3 = []

# 定义三星的轨迹颜色
tc1 = (255, 0, 0)
tc2 = (0, 255, 0)
tc3 = (0, 0, 255)

# 定义三星的轨迹宽度
tw1 = 1
tw2 = 1
tw3 = 1

while True:
    #清屏
    screen.fill((0, 0, 0))
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                star1 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)
                star2 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)
                star3 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)
                v1 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)
                v2 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)
                v3 = np.array([random() * 2 - 1, random() * 2 - 1],dtype=np.float64)
                track1 = []
                track2 = []
                track3 = []
                m1=1
                m2=1
                m3=1
            elif event.key == pygame.K_s:
                m1 = m2 = m3 = 1
                star1 = np.array([1, 0], dtype=np.float64)
                star2 = np.array([-0.5, 0.866], dtype=np.float64)
                star3 = np.array([-0.5, -0.866], dtype=np.float64)
                v1 = np.array([0, 0.1], dtype=np.float64)
                v2 = np.array([0.1, -0.1], dtype=np.float64)
                v3 = np.array([-0.1, -0.1], dtype=np.float64)
                track1 = []
                track2 = []
                track3 = []


    # 计算星体之间的引力
    r12 = np.linalg.norm(star1 - star2)
    r13 = np.linalg.norm(star1 - star3)
    r23 = np.linalg.norm(star2 - star3)

    f12 = G * m1 * m2 / r12**2
    f13 = G * m1 * m3 / r13**2
    f23 = G * m2 * m3 / r23**2

    # 更新速度和位置
    v1 += (f12 * (star2 - star1) + f13 * (star3 - star1)) * dt / m1
    v2 += (f12 * (star1 - star2) + f23 * (star3 - star2)) * dt / m2
    v3 += (f13 * (star1 - star3) + f23 * (star2 - star3)) * dt / m3

    star1 += v1 * dt
    star2 += v2 * dt
    star3 += v3 * dt

    # 绘制星体
    pygame.draw.circle(screen, c1, (int(star1[0] * 400 + 400), int(star1[1] * 300 + 300)), r1)
    pygame.draw.circle(screen, c2, (int(star2[0] * 400 + 400), int(star2[1] * 300 + 300)), r2)
    pygame.draw.circle(screen, c3, (int(star3[0] * 400 + 400), int(star3[1] * 300 + 300)), r3)

    # 更新轨迹
    track1.append((int(star1[0] * 400 + 400), int(star1[1] * 300 + 300)))
    track2.append((int(star2[0] * 400 + 400), int(star2[1] * 300 + 300)))
    track3.append((int(star3[0] * 400 + 400), int(star3[1] * 300 + 300)))

    # 绘制轨迹
    if len(track1) > 1:
        pygame.draw.lines(screen, tc1, False, track1, tw1)
    if len(track2) > 1:
        pygame.draw.lines(screen, tc2, False, track2, tw2)
    if len(track3) > 1:
        pygame.draw.lines(screen, tc3, False, track3, tw3)

    # 更新屏幕
    pygame.display.update()
    clock.tick(30)

    
