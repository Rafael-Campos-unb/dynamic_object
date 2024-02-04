import math
import numpy as np


# Translation Matrix
def translate_M(point):
    tx, ty, tz = point
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx, ty, tz, 1]
    ])


# Rotate Matrix:
# Rotate X
def rotate_X(n):
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(n), math.sin(n), 0],
        [0, -math.sin(n), math.cos(n), 0],
        [0, 0, 0, 1]
    ])


# Rotate Y
def rotate_Y(n):
    return np.array([
        [math.cos(n), 0, -math.sin(n), 0],
        [0, 1, 0, 0],
        [math.sin(n), 0, math.cos(n), 0],
        [0, 0, 0, 1]
    ])


# Rotate Z
def rotate_Z(n):
    return np.array([
        [math.cos(n), math.sin(n), 0, 0],
        [-math.sin(n), math.cos(n), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


# Scaling Matrix
def scale_M(n):
    return np.array([
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, n, 0],
        [0, 0, 0, 1]
    ])
