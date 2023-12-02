import pandas as pd
import os
 
if(os.path.exists("/home/yuwen/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc/traj_pgo.csv")):
    data = pd.read_csv('/home/yuwen/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc/traj_pgo.csv', encoding='utf-8')
    if(data.iloc[1,0]>=1e17):
        data.iloc[:,0] *= 1e-9
    cols = list(data)
    cols.insert(7,cols.pop(cols.index('qw')))
    data = data.loc[:,cols]
    #print(data)
    data.to_csv('/home/yuwen/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc/traj_pgo.txt', header=None, index=None, sep=' ', mode='a')

if(os.path.exists("/home/yuwen/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc/traj_vio.csv")):
    data = pd.read_csv('/home/yuwen/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc/traj_vio.csv', encoding='utf-8')
    data=data.drop(['vx','vy','vz','bgx','bgy','bgz','bax','bay','baz'],axis=1)
    if(data.iloc[1,0]>=1e17):
        data.iloc[:,0] *= 1e-9
    cols = list(data)
    cols.insert(7,cols.pop(cols.index('qw')))
    data = data.loc[:,cols]
    #print(data)
    data.to_csv('/home/yuwen/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc/traj_vio.txt', header=None, index=None, sep=' ', mode='a')

# elif(os.path.exists("/home/yuwen/catkin_ws/src/Kimera-VIO/output_logs/traj_pgo.csv")):
#     data = pd.read_csv('/home/yuwen/catkin_ws/src/Kimera-VIO/output_logs/traj_pgo.csv', encoding='utf-8')
#     if(data.iloc[1,0]>=1e17):
#         data.iloc[:,0] *= 1e-9
#     cols = list(data)
#     cols.insert(7,cols.pop(cols.index('qw')))
#     data = data.loc[:,cols]
#     #print(data)
#     data.to_csv('/home/yuwen/catkin_ws/src/Kimera-VIO/output_logs/traj_pgo.txt', header=None, index=None, sep=' ', mode='a')
else:
    print("traj_pgo.csv is not found!")
    print(os.path.exists("/home/yuwen/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc/traj_pgo.csv"))
    print(os.path.exists("/home/yuwen/catkin_ws/src/Kimera-VIO/output_logs/traj_pgo.csv"))