import pandas as pd
import numpy as np


chat_id = 808572568

def solution(x: np.array) -> float:
    num = x.size
    X = x.mean()
    a = (2 * num) / (76 ** 2) * X
    return a


