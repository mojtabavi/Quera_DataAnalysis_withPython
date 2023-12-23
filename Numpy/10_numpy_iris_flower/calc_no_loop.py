# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    return np.sum((np.square(points - (new_points.reshape(30,1,4)))), axis=2)
