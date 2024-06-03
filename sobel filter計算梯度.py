# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:12:55 2023

@author: 陳怡秀
"""

import numpy as np

# 定义3x3的Sobel滤波器核
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# 创建一个3x3的图像区域（示例数据）
image_region = np.array([[1, 2, 3],
                        [6, 5, 4],
                        [7, 8, 9]])

# 应用Sobel滤波器核计算水平方向和垂直方向的梯度
gradient_x = np.sum(image_region * sobel_x)
gradient_y = np.sum(image_region * sobel_y)

# 计算梯度大小
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

print("水平方向梯度:", gradient_x)
print("垂直方向梯度:", gradient_y)
print("梯度大小:", gradient_magnitude)
