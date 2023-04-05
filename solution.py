import pandas as pd
import numpy as np


chat_id = 808572568

def solution(x: np.array) -> float:
    t = 76
    n_cars = x.size
    a = 2 * x.sum()/(n_cars * t ** 2)
    return a
