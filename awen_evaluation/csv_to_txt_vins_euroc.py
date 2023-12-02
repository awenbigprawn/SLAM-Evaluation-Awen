import pandas as pd
import os
 
namelist = ['MH_01_easy','MH_02_easy','MH_03_medium','MH_04_difficult','MH_05_difficult',\
                        'V1_01_easy','V1_02_medium','V1_03_difficult',\
                        'V2_01_easy','V2_02_medium','V2_03_difficult']

result_folder_path = '/home/yuwen/vins_result_awen/'

for onename in namelist:
    if(os.path.exists(result_folder_path + onename+'/pose_graph_path.csv')):
        data = pd.read_csv(result_folder_path +onename+'/pose_graph_path.csv', encoding='utf-8')
        data.iloc[:,0] *= 1e-9
        data.to_csv(result_folder_path +onename+'/evo_readable_txt/pose_graph_path.txt', header=None, index=None, sep=' ', mode='a')

        #data = pd.read_csv('~/vins_result/pose_graph_path.csv', encoding='utf-8')
        #data.iloc[:,0] *= 1e-9
        #data.to_csv('~/vins_result/evo_readable_txt/pose_graph_path.txt', header=None, index=None, sep=' ', mode='a')
    else:
        print(onename+'does not exist')

# if(os.path.exists("/home/yuwen/vins_result/pose_graph_path.csv")):
#     data = pd.read_csv('/home/yuwen/vins_result/pose_graph_path.csv', encoding='utf-8')
#     if(data.iloc[1,0]>=1e17):
#         data.iloc[:,0] *= 1e-9
#     data.to_csv('/home/yuwen/vins_result/pose_graph_path.txt', header=None, index=None, sep=' ', mode='a')

# if(os.path.exists("/home/yuwen/vins_result/vins_estimator_path.csv")):
#     data2 = pd.read_csv('/home/yuwen/vins_result/vins_estimator_path.csv', encoding='utf-8')
#     if(data2.iloc[1,0]>=1e17):
#         data2.iloc[:,0] *= 1e-9
#     data2.to_csv('/home/yuwen/vins_result/vins_estimator_path.txt', header=None, index=None, sep=' ', mode='a')