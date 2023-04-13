import pandas as pd
import numpy as np
#from scipy.stats import ks_2samp
from scipy.stats import anderson_ksamp

chat_id = 664256606
alpha = 0.05

def solution(x: np.array, y: np.array) -> bool:
    _, _, p_value = anderson_ksamp([x, y])
    return p_value < alpha
