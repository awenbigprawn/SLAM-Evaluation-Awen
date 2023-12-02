import pandas as pd
import os
 
namelist = ['MH_01_easy','MH_02_easy','MH_03_medium','MH_04_difficult','MH_05_difficult',\
                        'V1_01_easy','V1_02_medium','V1_03_difficult',\
                        'V2_01_easy','V2_02_medium','V2_03_difficult']
# for onename in namelist:
#     if(os.path.exists('/home/yuwen/vins_result_awen/'+onename+'/pose_graph_path.csv')):
#         data = pd.read_csv('/home/yuwen/vins_result_awen/'+onename+'/pose_graph_path.csv', encoding='utf-8')
#         data.iloc[:,0] *= 1e-9
#         data.to_csv('/home/yuwen/vins_result_awen/'+onename+'/evo_readable_txt/pose_graph_path.txt', header=None, index=None, sep=' ', mode='a')

#         #data = pd.read_csv('~/vins_result/pose_graph_path.csv', encoding='utf-8')
#         #data.iloc[:,0] *= 1e-9
#         #data.to_csv('~/vins_result/evo_readable_txt/pose_graph_path.txt', header=None, index=None, sep=' ', mode='a')
#     else:
#         print(onename+'does not exist')

if(os.path.exists("/home/yuwen/ORB_SLAM3/ORB_SLAM3/Examples/f_dataset-MH01_stereoi.txt")):
    data = pd.read_csv('/home/yuwen/ORB_SLAM3/ORB_SLAM3/Examples/f_dataset-MH01_stereoi.txt',sep=' ')
    if(data.iloc[1,0]>=1e17):
        data.iloc[:,0] *= 1e-9
    data.to_csv('/home/yuwen/ORB_SLAM3/ORB_SLAM3/Examples/f_dataset-MH01_stereoi_evo.txt', header=None, index=None, sep=' ', mode='a')
else:
    print('csv don\'t found')