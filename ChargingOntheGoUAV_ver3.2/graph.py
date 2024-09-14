from tkinter import HORIZONTAL
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.ticker import FormatStrFormatter


plt.rcParams['font.family'] = 'Times New Roman'
plt.rc('font', size=11)

choice = 2  # 0: Charge Fee Sensitivity Analysis
            # 1: Charge Fee vs. Flight cost
            # 2: Charge Fee (over $10) vs. Flight cost ($0.265/kW·h)
            # 3: Depot location
            # 4: Computation time
            
if choice == 3:
    # 2. Charging Fee_04292022
    
    Charge_1_EV_10 = [2,0,2,0,0,0,2,0,0,0]
    Charge_1_EV_50 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,2,0,0,0,2,0]
    Charge_1_EV_100 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,2,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0]

    Charge_2_EV_10 = [2,0,2,0,0,0,2,0,0,0]
    Charge_2_EV_50 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,2,0,0,0,2,0]
    Charge_2_EV_100 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,2,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0]

    Charge_3_EV_10 = [2,0,2,0,0,0,2,0,0,0]
    Charge_3_EV_50 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,2,0,0,0,2,0]
    Charge_3_EV_100 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,2,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0]

    Charge_4_EV_10 = [1,0,2,0,0,0,2,0,0,0]
    Charge_4_EV_50 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,2,0,0,0,2,0]
    Charge_4_EV_100 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,2,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0]

    Charge_5_EV_10 = [1,0,2,0,0,0,2,0,0,0]
    Charge_5_EV_50 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,1,0,1,0,0,2,0,0]
    Charge_5_EV_100 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,2,0,1,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0]
            
    Charge_6_EV_10 = [1,0,2,0,0,0,2,0,0,0]
    Charge_6_EV_50 = [1,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,1,0,0,2,0,0,0,0,1,0,2,0,1,0,0,2,0,0,1,0,0,2,0,0]
    Charge_6_EV_100 = [1,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,1,0,0,2,0,0,0,0,1,0,2,0,1,0,0,2,0,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,1,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0]
                       
    Charge_7_EV_10 = [1,0,2,0,0,0,2,0,0,0]
    Charge_7_EV_50 = [1,1,0,0,0,2,0,0,1,0,0,2,0,1,0,0,0,2,0,1,0,0,0,2,0,0,1,0,0,2,0,0,0,0,1,0,2,0,1,0,0,2,0,0,1,0,0,2,0,0]
    Charge_7_EV_100 = [1,1,0,0,0,2,0,0,1,0,0,2,0,1,0,0,0,2,0,1,0,0,0,2,0,0,1,0,0,2,0,0,0,0,1,0,2,0,1,0,0,2,0,0,1,0,0,2,0,1,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,1,0,0,0,2,0,0,0,1,0,2,0,1,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0]           
    
    Charge_8_EV_10 = [1,1,0,0,1,0,2,0,0,0]
    Charge_8_EV_50 = [1,1,0,0,0,2,0,1,0,0,0,2,0,1,0,0,1,0,1,0,1,0,0,2,0,0,1,0,0,1,0,2,0,0,0,0,2,0,1,0,0,2,0,0,1,0,0,2,0,0]
    Charge_8_EV_100 = [1,1,0,0,0,2,0,1,0,0,0,2,0,1,0,0,1,0,1,0,1,0,0,2,0,0,1,0,0,1,0,2,0,0,0,0,2,0,1,0,0,2,0,0,1,0,0,2,0,1,0,0,0,2,0,0,2,0,0,0,2,0,0,0,1,0,2,0,0,0,2,0,0,2,0,0,0,2,0,1,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0]           
    
    Charge_9_EV_10 = [1,1,0,0,1,0,2,0,0,0]
    Charge_9_EV_50 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0,1,0,0,0,1,0,2,0,1,0,0,1,0,1,0,0,1,0,2,0]
    Charge_9_EV_100 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0,1,0,0,0,1,0,2,0,1,0,0,1,0,1,0,0,1,0,2,0,0,1,0,0,2,0,0,0,2,0,0,1,0,0,1,0,2,0,0,0,2,0,1,0,0,1,0,1,1,1,0,0,0,2,0,0,0,1,0,0,2,0,0,0,1,0,2,0,0,0]           
    
    Charge_10_EV_10 = [1,1,0,0,1,0,2,0,0,0]
    Charge_10_EV_50 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0,1,0,0,0,1,0,2,0,1,0,0,1,0,1,0,0,1,0,2,0]
    Charge_10_EV_100 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0,1,0,0,0,1,0,2,0,1,0,0,1,0,1,0,0,1,0,2,0,0,1,0,0,2,0,0,0,2,0,0,1,0,0,1,0,2,0,0,0,2,0,1,0,0,1,0,1,1,1,0,0,0,2,0,0,0,1,0,0,2,0,0,0,1,0,2,0,0,0]            
            
    EV_10_array = np.zeros([10, 2])  # [0]: return ratio (charge fee = 1 ~ 10), [1]: charge ratio  (charge fee = 1 ~ 10)
    EV_50_array = np.zeros([10, 2])  # [0]: return ratio (charge fee = 1 ~ 10), [1]: charge ratio  (charge fee = 1 ~ 10)
    EV_100_array = np.zeros([10, 2])  # [0]: return ratio (charge fee = 1 ~ 10), [1]: charge ratio  (charge fee = 1 ~ 10)
    
    # EV_10
    cnt_1 = 0
    cnt_2 = 0
    for i in range(10):
        if Charge_1_EV_10[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_EV_10[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_10_array[0][0] = round(cnt_1 / 10.0, 2)
    EV_10_array[0][1] = round(cnt_2 / 10.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(10):
        if Charge_2_EV_10[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_2_EV_10[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_10_array[1][0] = round(cnt_1 / 10.0, 2)
    EV_10_array[1][1] = round(cnt_2 / 10.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(10):
        if Charge_3_EV_10[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_3_EV_10[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_10_array[2][0] = round(cnt_1 / 10.0, 2)
    EV_10_array[2][1] = round(cnt_2 / 10.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(10):
        if Charge_4_EV_10[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_4_EV_10[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_10_array[3][0] = round(cnt_1 / 10.0, 2)
    EV_10_array[3][1] = round(cnt_2 / 10.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(10):
        if Charge_5_EV_10[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_5_EV_10[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_10_array[4][0] = round(cnt_1 / 10.0, 2)
    EV_10_array[4][1] = round(cnt_2 / 10.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(10):
        if Charge_6_EV_10[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_6_EV_10[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_10_array[5][0] = round(cnt_1 / 10.0, 2)
    EV_10_array[5][1] = round(cnt_2 / 10.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(10):
        if Charge_7_EV_10[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_7_EV_10[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_10_array[6][0] = round(cnt_1 / 10.0, 2)
    EV_10_array[6][1] = round(cnt_2 / 10.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(10):
        if Charge_8_EV_10[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_8_EV_10[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_10_array[7][0] = round(cnt_1 / 10.0, 2)
    EV_10_array[7][1] = round(cnt_2 / 10.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(10):
        if Charge_9_EV_10[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_9_EV_10[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_10_array[8][0] = round(cnt_1 / 10.0, 2)
    EV_10_array[8][1] = round(cnt_2 / 10.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(10):
        if Charge_10_EV_10[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_EV_10[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_10_array[9][0] = round(cnt_1 / 10.0, 2)
    EV_10_array[9][1] = round(cnt_2 / 10.0, 2)
    
    # EV_50
    cnt_1 = 0
    cnt_2 = 0
    for i in range(50):
        if Charge_1_EV_50[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_EV_50[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_50_array[0][0] = round(cnt_1 / 50.0, 2)
    EV_50_array[0][1] = round(cnt_2 / 50.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(50):
        if Charge_2_EV_50[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_2_EV_50[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_50_array[1][0] = round(cnt_1 / 50.0, 2)
    EV_50_array[1][1] = round(cnt_2 / 50.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(50):
        if Charge_3_EV_50[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_3_EV_50[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_50_array[2][0] = round(cnt_1 / 50.0, 2)
    EV_50_array[2][1] = round(cnt_2 / 50.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(50):
        if Charge_4_EV_50[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_4_EV_50[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_50_array[3][0] = round(cnt_1 / 50.0, 2)
    EV_50_array[3][1] = round(cnt_2 / 50.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(50):
        if Charge_5_EV_50[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_5_EV_50[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_50_array[4][0] = round(cnt_1 / 50.0, 2)
    EV_50_array[4][1] = round(cnt_2 / 50.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(50):
        if Charge_6_EV_50[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_6_EV_50[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_50_array[5][0] = round(cnt_1 / 50.0, 2)
    EV_50_array[5][1] = round(cnt_2 / 50.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(50):
        if Charge_7_EV_50[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_7_EV_50[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_50_array[6][0] = round(cnt_1 / 50.0, 2)
    EV_50_array[6][1] = round(cnt_2 / 50.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(50):
        if Charge_8_EV_50[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_8_EV_50[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_50_array[7][0] = round(cnt_1 / 50.0, 2)
    EV_50_array[7][1] = round(cnt_2 / 50.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(50):
        if Charge_9_EV_50[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_9_EV_50[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_50_array[8][0] = round(cnt_1 / 50.0, 2)
    EV_50_array[8][1] = round(cnt_2 / 50.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(50):
        if Charge_10_EV_50[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_EV_50[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_50_array[9][0] = round(cnt_1 / 50.0, 2)
    EV_50_array[9][1] = round(cnt_2 / 50.0, 2)
    
    
    
    # EV_100
    cnt_1 = 0
    cnt_2 = 0
    for i in range(100):
        if Charge_1_EV_100[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_EV_100[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_100_array[0][0] = round(cnt_1 / 100.0, 2)
    EV_100_array[0][1] = round(cnt_2 / 100.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(100):
        if Charge_2_EV_100[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_2_EV_100[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_100_array[1][0] = round(cnt_1 / 100.0, 2)
    EV_100_array[1][1] = round(cnt_2 / 100.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(100):
        if Charge_3_EV_100[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_3_EV_100[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_100_array[2][0] = round(cnt_1 / 100.0, 2)
    EV_100_array[2][1] = round(cnt_2 / 100.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(100):
        if Charge_4_EV_100[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_4_EV_100[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_100_array[3][0] = round(cnt_1 / 100.0, 2)
    EV_100_array[3][1] = round(cnt_2 / 100.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(100):
        if Charge_5_EV_100[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_5_EV_100[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_100_array[4][0] = round(cnt_1 / 100.0, 2)
    EV_100_array[4][1] = round(cnt_2 / 100.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(100):
        if Charge_6_EV_100[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_6_EV_100[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_100_array[5][0] = round(cnt_1 / 100.0, 2)
    EV_100_array[5][1] = round(cnt_2 / 100.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(100):
        if Charge_7_EV_100[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_7_EV_100[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_100_array[6][0] = round(cnt_1 / 100.0, 2)
    EV_100_array[6][1] = round(cnt_2 / 100.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(100):
        if Charge_8_EV_100[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_8_EV_100[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_100_array[7][0] = round(cnt_1 / 100.0, 2)
    EV_100_array[7][1] = round(cnt_2 / 100.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(100):
        if Charge_9_EV_100[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_9_EV_100[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_100_array[8][0] = round(cnt_1 / 100.0, 2)
    EV_100_array[8][1] = round(cnt_2 / 100.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(100):
        if Charge_10_EV_100[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_EV_100[i] == 2:
            cnt_2 = cnt_2 + 1
    EV_100_array[9][0] = round(cnt_1 / 100.0, 2)
    EV_100_array[9][1] = round(cnt_2 / 100.0, 2)
    
    
    
    # Draw
    xAxis = range(1,11)
    plt.figure(1)
    ax = plt.subplot(121)
    plt.plot(xAxis, EV_10_array[:,0], '^', color='b', label='# EVs = 10')
    plt.plot(xAxis, EV_50_array[:,0], 's', color='g', label='# EVs = 50')
    plt.plot(xAxis, EV_100_array[:,0], '.', color='k', label='# EVs = 100')
    plt.xticks(range(1, 11), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    
    
    plt.xlabel('Charge fee ($) \n (a)')
    plt.ylabel('Depot return rate')
    
    
    ax = plt.subplot(122)
    plt.plot(xAxis, EV_10_array[:,1], '^', color='b', label='# EVs = 10')
    plt.plot(xAxis, EV_50_array[:,1], 's', color='g', label='# EVs = 50')
    plt.plot(xAxis, EV_100_array[:,1], '.', color='k', label='# EVs = 100')
    plt.xticks(range(1, 11), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    
    
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel('Charge fee ($) \n (b)')
    plt.ylabel('Charge at destination node rate')
    
    
    
    
    plt.tight_layout()
    plt.savefig('ChargeFeeSensitivity.jpg', dpi=500)
    plt.show()

    
if choice == 1:
    # 3. Charging Fee vs. Flight Cost_04292022
    
    Charge_1_Flight_097 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_1_Flight_13 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_1_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]

    Charge_2_Flight_097 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_2_Flight_13 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_2_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    Charge_3_Flight_097 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_3_Flight_13 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_3_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    Charge_4_Flight_097 = [1,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_4_Flight_13 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_4_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    Charge_5_Flight_097 = [1,1,0,0,0,2,0,0,0,1,0,2,0,1,0,0,0,2,0,0,1,0,0,2,0,0,2,0,0,0]
    Charge_5_Flight_13 = [1,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_5_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    Charge_6_Flight_097 = [1,1,0,0,0,2,0,1,0,0,0,2,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0]
    Charge_6_Flight_13 = [1,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_6_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    Charge_7_Flight_097 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0]
    Charge_7_Flight_13 = [1,1,0,0,0,2,0,0,0,1,0,2,0,1,0,0,0,2,0,0,1,0,0,2,0,0,2,0,0,0]
    Charge_7_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    Charge_8_Flight_097 = [1,1,0,0,0,2,0,1,0,0,0,2,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0]
    Charge_8_Flight_13 = [1,1,0,0,1,0,2,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,1,0,1,1,0,0,1,0]
    Charge_8_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    Charge_9_Flight_097 = [1,1,0,0,1,0,2,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0]
    Charge_9_Flight_13 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0]
    Charge_9_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    Charge_10_Flight_097 = [1,1,0,0,1,0,2,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0]
    Charge_10_Flight_13 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0]
    Charge_10_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
 
    
    Flight_097_array = np.zeros([10, 2])  # [0]: return ratio (charge fee = 1 ~ 10), [1]: charge ratio  (charge fee = 1 ~ 10)
    Flight_13_array = np.zeros([10, 2])  # [0]: return ratio (charge fee = 1 ~ 10), [1]: charge ratio  (charge fee = 1 ~ 10)
    Flight_265_array = np.zeros([10, 2])  # [0]: return ratio (charge fee = 1 ~ 10), [1]: charge ratio  (charge fee = 1 ~ 10)
    
    
    # Flight_097
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Flight_097[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Flight_097[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_097_array[0][0] = round(cnt_1 / 30.0, 2)
    Flight_097_array[0][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_2_Flight_097[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_2_Flight_097[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_097_array[1][0] = round(cnt_1 / 30.0, 2)
    Flight_097_array[1][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_3_Flight_097[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_3_Flight_097[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_097_array[2][0] = round(cnt_1 / 30.0, 2)
    Flight_097_array[2][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_4_Flight_097[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_4_Flight_097[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_097_array[3][0] = round(cnt_1 / 30.0, 2)
    Flight_097_array[3][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_5_Flight_097[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_5_Flight_097[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_097_array[4][0] = round(cnt_1 / 30.0, 2)
    Flight_097_array[4][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_6_Flight_097[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_6_Flight_097[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_097_array[5][0] = round(cnt_1 / 30.0, 2)
    Flight_097_array[5][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_7_Flight_097[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_7_Flight_097[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_097_array[6][0] = round(cnt_1 / 30.0, 2)
    Flight_097_array[6][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_8_Flight_097[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_8_Flight_097[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_097_array[7][0] = round(cnt_1 / 30.0, 2)
    Flight_097_array[7][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_9_Flight_097[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_9_Flight_097[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_097_array[8][0] = round(cnt_1 / 30.0, 2)
    Flight_097_array[8][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Flight_097[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Flight_097[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_097_array[9][0] = round(cnt_1 / 30.0, 2)
    Flight_097_array[9][1] = round(cnt_2 / 30.0, 2)

    # Flight_13
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Flight_13[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Flight_13[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_13_array[0][0] = round(cnt_1 / 30.0, 2)
    Flight_13_array[0][1] = round(cnt_2 / 30.0, 2)

    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_2_Flight_13[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_2_Flight_13[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_13_array[1][0] = round(cnt_1 / 30.0, 2)
    Flight_13_array[1][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_3_Flight_13[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_3_Flight_13[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_13_array[2][0] = round(cnt_1 / 30.0, 2)
    Flight_13_array[2][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_4_Flight_13[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_4_Flight_13[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_13_array[3][0] = round(cnt_1 / 30.0, 2)
    Flight_13_array[3][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_5_Flight_13[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_5_Flight_13[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_13_array[4][0] = round(cnt_1 / 30.0, 2)
    Flight_13_array[4][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_6_Flight_13[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_6_Flight_13[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_13_array[5][0] = round(cnt_1 / 30.0, 2)
    Flight_13_array[5][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_7_Flight_13[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_7_Flight_13[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_13_array[6][0] = round(cnt_1 / 30.0, 2)
    Flight_13_array[6][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_8_Flight_13[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_8_Flight_13[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_13_array[7][0] = round(cnt_1 / 30.0, 2)
    Flight_13_array[7][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_9_Flight_13[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_9_Flight_13[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_13_array[8][0] = round(cnt_1 / 30.0, 2)
    Flight_13_array[8][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Flight_13[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Flight_13[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_13_array[9][0] = round(cnt_1 / 30.0, 2)
    Flight_13_array[9][1] = round(cnt_2 / 30.0, 2)

    # Flight_265
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[0][0] = round(cnt_1 / 30.0, 2)
    Flight_265_array[0][1] = round(cnt_2 / 30.0, 2)

    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_2_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_2_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[1][0] = round(cnt_1 / 30.0, 2)
    Flight_265_array[1][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_3_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_3_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[2][0] = round(cnt_1 / 30.0, 2)
    Flight_265_array[2][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_4_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_4_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[3][0] = round(cnt_1 / 30.0, 2)
    Flight_265_array[3][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_5_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_5_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[4][0] = round(cnt_1 / 30.0, 2)
    Flight_265_array[4][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_6_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_6_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[5][0] = round(cnt_1 / 30.0, 2)
    Flight_265_array[5][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_7_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_7_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[6][0] = round(cnt_1 / 30.0, 2)
    Flight_265_array[6][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_8_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_8_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[7][0] = round(cnt_1 / 30.0, 2)
    Flight_265_array[7][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_9_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_9_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[8][0] = round(cnt_1 / 30.0, 2)
    Flight_265_array[8][1] = round(cnt_2 / 30.0, 2)
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[9][0] = round(cnt_1 / 30.0, 2)
    Flight_265_array[9][1] = round(cnt_2 / 30.0, 2)
    

    # Draw
    xAxis = range(1,11)
    plt.figure(1)
    ax = plt.subplot(121)
    plt.plot(xAxis, Flight_097_array[:,0], '^', color='b', label='Flight cost = $0.097/kW·h')
    plt.plot(xAxis, Flight_13_array[:,0], 's', color='g', label='Flight cost = $0.130/kW·h')
    plt.plot(xAxis, Flight_265_array[:,0], '.', color='k', label='Flight cost = $0.265/kW·h')
    plt.xticks(range(1, 11), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    
    
    plt.xlabel('Charge fee ($) \n (a)')
    plt.ylabel('Depot return rate')
    
    
    
    
    ax = plt.subplot(122)
    plt.plot(xAxis, Flight_097_array[:,1], '^', color='b', label='Flight cost = $0.097/kW·h')
    plt.plot(xAxis, Flight_13_array[:,1], 's', color='g', label='Flight cost = $0.130/kW·h')
    plt.plot(xAxis, Flight_265_array[:,1], '.', color='k', label='Flight cost = $0.265/kW·h')
    plt.xticks(range(1, 11), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel('Charge fee ($) \n (b)')
    plt.ylabel('Charge at destination node rate')
    
    
    
    
    plt.tight_layout()
    plt.savefig('ChargeFeeVSFlightCost.jpg', dpi=500)
    plt.show()
     
    
if choice == 2:
    # 4. Charging Fee vs. Flight Cost (0.265)_04302022
    
    Charge_1_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_2_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_3_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_4_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_5_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_6_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_7_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_8_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_9_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_10_Flight_265 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_11_Flight_265 = [1,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0] 
    Charge_12_Flight_265 = [1,0,2,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    Charge_13_Flight_265 = [1,0,2,0,0,0,2,0,0,0,1,0,2,0,0,0,0,2,0,0,1,0,0,2,0,0,2,0,0,0]
    Charge_14_Flight_265 = [1,1,0,0,0,2,0,0,0,1,0,2,0,1,0,0,0,2,0,0,1,0,0,2,0,0,2,0,0,0]
    Charge_15_Flight_265 = [1,1,0,0,0,2,0,1,0,0,0,2,0,1,0,0,0,1,0,2,0,0,0,0,2,0,0,1,0,0]
    Charge_16_Flight_265 = [1,1,0,0,0,2,0,1,0,0,0,2,0,1,0,0,0,1,0,2,0,0,0,0,2,0,0,1,0,0]
    Charge_17_Flight_265 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,2,0,0,1,0,1,0]
    Charge_18_Flight_265 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0]
    Charge_19_Flight_265 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0]
    Charge_20_Flight_265 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0]
 
 
    
    Flight_265_array = np.zeros([20, 2])  # [0]: return ratio (charge fee = 1 ~ 20), [1]: charge ratio  (charge fee = 1 ~ 20)
    
    
    
    # Flight_265
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[0][0] = cnt_1 / 30.0
    Flight_265_array[0][1] = cnt_2 / 30.0

    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_2_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_2_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[1][0] = cnt_1 / 30.0
    Flight_265_array[1][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_3_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_3_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[2][0] = cnt_1 / 30.0
    Flight_265_array[2][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_4_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_4_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[3][0] = cnt_1 / 30.0
    Flight_265_array[3][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_5_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_5_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[4][0] = cnt_1 / 30.0
    Flight_265_array[4][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_6_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_6_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[5][0] = cnt_1 / 30.0
    Flight_265_array[5][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_7_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_7_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[6][0] = cnt_1 / 30.0
    Flight_265_array[6][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_8_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_8_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[7][0] = cnt_1 / 30.0
    Flight_265_array[7][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_9_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_9_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[8][0] = cnt_1 / 30.0
    Flight_265_array[8][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[9][0] = cnt_1 / 30.0
    Flight_265_array[9][1] = cnt_2 / 30.0
    

    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_11_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_11_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[10][0] = cnt_1 / 30.0
    Flight_265_array[10][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_12_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_12_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[11][0] = cnt_1 / 30.0
    Flight_265_array[11][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_13_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_13_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[12][0] = cnt_1 / 30.0
    Flight_265_array[12][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_14_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_14_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[13][0] = cnt_1 / 30.0
    Flight_265_array[13][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_15_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_15_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[14][0] = cnt_1 / 30.0
    Flight_265_array[14][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_16_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_16_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[15][0] = cnt_1 / 30.0
    Flight_265_array[15][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_17_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_17_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[16][0] = cnt_1 / 30.0
    Flight_265_array[16][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_18_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_18_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[17][0] = cnt_1 / 30.0
    Flight_265_array[17][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_19_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_19_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[18][0] = cnt_1 / 30.0
    Flight_265_array[18][1] = cnt_2 / 30.0
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_20_Flight_265[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_20_Flight_265[i] == 2:
            cnt_2 = cnt_2 + 1
    Flight_265_array[19][0] = cnt_1 / 30.0
    Flight_265_array[19][1] = cnt_2 / 30.0


    # Draw
    xAxis = range(1,21)
    plt.figure(1)
    plt.plot(xAxis, Flight_265_array[:,0], '.', color='k', label='Flight cost = $0.265/kW·h')
    plt.xticks(range(1, 21), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    
    plt.legend()
    plt.xlabel('Charge fee ($)')
    plt.ylabel('Depot return rate')
    
    plt.savefig('ChargeFeeVSFlightCost_265.jpg', dpi=500)
    plt.show()
    
    
if choice == 3:
    # 5. Depot Location
    
    # Shorter5
    Charge_1_Distance_1 = [0,2,0,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    # Shorter4
    Charge_1_Distance_2 = [0,2,0,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    # Shorter3
    Charge_1_Distance_3 = [0,2,0,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    # Shorter2
    Charge_1_Distance_4 = [0,2,0,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    # Shorter1
    Charge_1_Distance_5 = [0,2,0,0,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    # Default
    Charge_1_Distance_6 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    # Farther1
    Charge_1_Distance_7 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    # Farther2
    Charge_1_Distance_8 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,2,0,0,2,0,0,0]
    
    # Farther3
    Charge_1_Distance_9 = [2,0,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,2,0,2,0,0,0,2,0,2,0,0,0]
    
    
    # Shorter5
    Charge_10_Distance_1 = [1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0]
    
    # Shorter4
    Charge_10_Distance_2 = [1,0,0,1,0,0,2,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0]
    
    # Shorter3
    Charge_10_Distance_3 = [1,0,0,1,0,1,1,0,0,0,2,0,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0]
    
    # Shorter2
    Charge_10_Distance_4 = [1,1,0,0,1,0,1,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0]
    
    # Shorter1
    Charge_10_Distance_5 = [1,1,0,0,1,0,1,1,0,0,1,0,2,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0]
    
    # Default
    Charge_10_Distance_6 = [1,1,0,0,1,0,2,0,0,0,1,0,2,0,0,0,1,0,1,0,1,0,0,1,0,2,0,0,1,0]
    
    # Farther1
    Charge_10_Distance_7 = [1,1,0,0,0,2,0,0,1,0,0,2,0,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0]
    
    # Farther2
    Charge_10_Distance_8 = [1,1,0,0,0,2,0,0,1,0,0,2,0,0,1,0,0,2,0,0,1,0,0,2,0,0,1,0,1,0]
    
    # Farther3
    Charge_10_Distance_9 = [1,1,0,0,0,2,0,0,1,0,0,2,0,0,1,0,0,2,0,0,1,0,0,2,0,0,1,0,1,0]
    
    
    
    Charge_1_array = np.zeros([9, 2])  # [0]: return ratio (distance = 1 ~ 9), [1]: charge ratio  (distance = 1 ~ 9)   
    Charge_10_array = np.zeros([9, 2])  # [0]: return ratio (distance = 1 ~ 9), [1]: charge ratio  (distance = 1 ~ 9)   
    
    
    # Charge_1
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Distance_1[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Distance_1[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_1_array[0][0] = round(cnt_1 / 30.0, 2)
    Charge_1_array[0][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Distance_2[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Distance_2[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_1_array[1][0] = round(cnt_1 / 30.0, 2)
    Charge_1_array[1][1] = round(cnt_2 / 30.0, 2)
    

    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Distance_3[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Distance_3[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_1_array[2][0] = round(cnt_1 / 30.0, 2)
    Charge_1_array[2][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Distance_4[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Distance_4[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_1_array[3][0] = round(cnt_1 / 30.0, 2)
    Charge_1_array[3][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Distance_5[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Distance_5[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_1_array[4][0] = round(cnt_1 / 30.0, 2)
    Charge_1_array[4][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Distance_6[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Distance_6[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_1_array[5][0] = round(cnt_1 / 30.0, 2)
    Charge_1_array[5][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Distance_7[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Distance_7[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_1_array[6][0] = round(cnt_1 / 30.0, 2)
    Charge_1_array[6][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Distance_8[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Distance_8[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_1_array[7][0] = round(cnt_1 / 30.0, 2)
    Charge_1_array[7][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_1_Distance_9[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_1_Distance_9[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_1_array[8][0] = round(cnt_1 / 30.0, 2)
    Charge_1_array[8][1] = round(cnt_2 / 30.0, 2)
    
    
    
    
    # Charge_10
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Distance_1[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Distance_1[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_10_array[0][0] = round(cnt_1 / 30.0, 2)
    Charge_10_array[0][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Distance_2[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Distance_2[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_10_array[1][0] = round(cnt_1 / 30.0, 2)
    Charge_10_array[1][1] = round(cnt_2 / 30.0, 2)
    

    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Distance_3[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Distance_3[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_10_array[2][0] = round(cnt_1 / 30.0, 2)
    Charge_10_array[2][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Distance_4[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Distance_4[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_10_array[3][0] = round(cnt_1 / 30.0, 2)
    Charge_10_array[3][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Distance_5[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Distance_5[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_10_array[4][0] = round(cnt_1 / 30.0, 2)
    Charge_10_array[4][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Distance_6[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Distance_6[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_10_array[5][0] = round(cnt_1 / 30.0, 2)
    Charge_10_array[5][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Distance_7[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Distance_7[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_10_array[6][0] = round(cnt_1 / 30.0, 2)
    Charge_10_array[6][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Distance_8[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Distance_8[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_10_array[7][0] = round(cnt_1 / 30.0, 2)
    Charge_10_array[7][1] = round(cnt_2 / 30.0, 2)
    
    
    cnt_1 = 0
    cnt_2 = 0
    for i in range(30):
        if Charge_10_Distance_9[i] == 1:
            cnt_1 = cnt_1 + 1
        elif Charge_10_Distance_9[i] == 2:
            cnt_2 = cnt_2 + 1
    Charge_10_array[8][0] = round(cnt_1 / 30.0, 2)
    Charge_10_array[8][1] = round(cnt_2 / 30.0, 2)
    
    
    
    # Draw
    xAxis = range(1,10)
    plt.figure(1)
    ax = plt.subplot(121)
    plt.plot(xAxis, Charge_1_array[:,0], '^', color='b', label='Charge fee = $1')
    plt.plot(xAxis, Charge_10_array[:,0], '.', color='k', label='Charge fee = $10')
    plt.xticks(range(1, 10), ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)'])
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    
    
    plt.xlabel('Distance Cases')
    plt.ylabel('Depot return rate')
    
    
    
    
    ax = plt.subplot(122)
    plt.plot(xAxis, Charge_1_array[:,1], '^', color='b', label='Charge fee = $1')
    plt.plot(xAxis, Charge_10_array[:,1], '.', color='k', label='Charge fee = $10')
    plt.xticks(range(1, 10), ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)'])
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel('Distance Cases')
    plt.ylabel('Charge at destination node rate')
    
    
    
    
    plt.tight_layout()
    plt.savefig('DepotLocation.jpg', dpi=500)
    plt.show()
    
    
if choice == 4:
    # 1. General Result_05102022
    
    numEVs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
    cpuTime_DP = [0.03772,0.07674,0.10987,0.14765,0.20848,0.2305,0.29019,0.33959,0.38534,0.38998,0.41509,0.47009,0.5649,0.52635,0.71996,0.61945,0.74495,0.72235,0.74092,0.81556,0.8959,1.13509,0.95891,1.0203,1.10465,1.25527,1.09214,1.311,1.23796,1.24108]
    cpuTime_Policy = [0.00558,0.00512,0.00698,0.00615,0.00303,0.00967,0.00399,0.00399,0.00901,0.00483,0.00868,0.00651,0.01247,0.01377,0.01197,0.00898,0.01355,0.0102,0.0104,0.01144,0.01301,0.01602,0.01696,0.01321,0.01557,0.01751,0.0134,0.02036,0.01795,0.01894]
    
    
    # Draw
    xAxis = range(1,31)
    plt.figure(1)
    
    ax = plt.axes()
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
    
    
    plt.plot(xAxis, cpuTime_DP, '^', color='b', label='Dynamic programming')
    plt.plot(xAxis, cpuTime_Policy, 's', color='g', label='Optimal policy theorem')
    
    plt.xticks(range(1, 31), numEVs)
    plt.locator_params(axis='x', nbins=len(numEVs)/4)
    
    
    
    plt.xlabel('# EVs')
    plt.ylabel('CPU time (sec.)')
    
    
    
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    
    plt.tight_layout()
    plt.savefig('CPUTime.jpg', dpi=500)
    plt.show()