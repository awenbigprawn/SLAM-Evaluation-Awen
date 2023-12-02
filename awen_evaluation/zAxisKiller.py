import pandas as pd
import numpy as np
import os


if(os.path.exists("/home/yuwen/all_result_z0/kimera_traj_bigclosure.txt")):
    data = pd.read_csv('/home/yuwen/urbant_GPS_result/kimera_traj_bigclosure.txt', encoding='utf-8',header=None,sep=' ')
    if(data.iloc[1,0]>=1e17):
        data.iloc[:,0] *= 1e-9
    print(data.head())
else:
    print("file doesn't exist!")

f = open("/home/yuwen/urbant_GPS_result/kimera_traj_bigclosure.txt", mode="w+")

for i in range(0,len(data)):
    for k in range(0,3):
        f.write(str(data.iloc[i,k])+ " ")
    f.write("0 0 0 0 1\n")

f.close()