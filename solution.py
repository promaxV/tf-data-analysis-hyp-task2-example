import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 664256606
alpha = 0.05

def solution(x: np.array, y: np.array) -> bool:
    statistic, p_value = ks_2samp(x, y)
    return p_value < alpha
