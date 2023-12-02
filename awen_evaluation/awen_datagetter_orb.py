from numpy.core.fromnumeric import mean
import pandas as pd
import numpy as np
import os
#import seaborn as sns

class awenDataGetterOrb:

    def putEurocAPEinOneTable(self, namelist, evo_result_path):
            
        dataframe_list=[]
        dataframe_list_rot=[]
        for one_name in namelist:
            dataframe_list.append(pd.read_csv(evo_result_path+'/orb_plot_'+one_name+'/trans_table.csv', index_col=0, header=0))
            dataframe_list_rot.append(pd.read_csv(evo_result_path+'/orb_plot_'+one_name+'/rot_table.csv', index_col=0, header=0))
        print('dataframe_list is:')
        print(dataframe_list)
        rmse_list=[]
        mean_list=[]
        median_list=[]
        rmse_list_rot=[]
        mean_list_rot=[]
        median_list_rot=[]
        df_mean_ci=[]
        df_mean_rot_ci=[]            

        for one_dataframe in dataframe_list:
            rmse_list.append(one_dataframe.loc['traj_evo.txt','rmse'])
            mean_list.append(one_dataframe.loc['traj_evo.txt','mean'])
            median_list.append(one_dataframe.loc['traj_evo.txt','median'])
            df_mean_ci.append(one_dataframe.loc['traj_evo.txt','std'])

        for one_dataframe in dataframe_list_rot:
            rmse_list_rot.append(one_dataframe.loc['traj_evo.txt','rmse'])
            mean_list_rot.append(one_dataframe.loc['traj_evo.txt','mean'])
            median_list_rot.append(one_dataframe.loc['traj_evo.txt','median'])
            df_mean_rot_ci.append(one_dataframe.loc['traj_evo.txt','std'])
            
        df_rmse = pd.DataFrame(rmse_list,index=namelist)
        df_mean = pd.DataFrame(mean_list,index=namelist)
        df_median = pd.DataFrame(median_list, index=namelist)
        df_rmse_rot = pd.DataFrame(rmse_list_rot,index=namelist)
        df_mean_rot = pd.DataFrame(mean_list_rot,index=namelist)
        df_median_rot = pd.DataFrame(median_list_rot,index=namelist)

        #df_rmse = df_rmse.transpose()
        df_rmse.columns=['rmse']
        df_rmse = df_rmse.transpose()
        
        df_mean.columns=['mean']
        df_mean = df_mean.transpose()
        #print(df_mean)
        df_median.columns=['median']
        df_median = df_median.transpose()

        df_rmse_rot.columns=['rot_rmse']
        df_rmse_rot=df_rmse_rot.transpose()

        df_mean_rot.columns=['rot_mean']
        df_mean_rot=df_mean_rot.transpose()

        df_median_rot.columns=['rot_median']
        df_median_rot=df_median_rot.transpose()

        return [df_rmse,df_mean,df_median,df_rmse_rot,df_mean_rot,df_median_rot]

    def putEurocRPEinOneTable(self, namelist, evo_result_path):
        dataframe_list=[]
        dataframe_list_rot=[]
        for one_name in namelist:
            dataframe_list.append(pd.read_csv(evo_result_path+'/orb_plot_'+one_name+'/trans_relativ_table.csv', index_col=0, header=0))
            dataframe_list_rot.append(pd.read_csv(evo_result_path+'/orb_plot_'+one_name+'/rot_relativ_table.csv', index_col=0, header=0))

        rmse_list=[]
        mean_list=[]
        median_list=[]
        rmse_list_rot=[]
        mean_list_rot=[]
        median_list_rot=[]
        df_mean_ci=[]
        df_mean_rot_ci=[]            

        for one_dataframe in dataframe_list:
            rmse_list.append(one_dataframe.loc['traj_evo.txt','rmse'])
            mean_list.append(one_dataframe.loc['traj_evo.txt','mean'])
            median_list.append(one_dataframe.loc['traj_evo.txt','median'])
            df_mean_ci.append(one_dataframe.loc['traj_evo.txt','std'])

        for one_dataframe in dataframe_list_rot:
            rmse_list_rot.append(one_dataframe.loc['traj_evo.txt','rmse'])
            mean_list_rot.append(one_dataframe.loc['traj_evo.txt','mean'])
            median_list_rot.append(one_dataframe.loc['traj_evo.txt','median'])
            df_mean_rot_ci.append(one_dataframe.loc['traj_evo.txt','std'])
            
        df_rmse = pd.DataFrame(rmse_list,index=namelist)
        df_mean = pd.DataFrame(mean_list,index=namelist)
        df_median = pd.DataFrame(median_list, index=namelist)
        df_rmse_rot = pd.DataFrame(rmse_list_rot,index=namelist)
        df_mean_rot = pd.DataFrame(mean_list_rot,index=namelist)
        df_median_rot = pd.DataFrame(median_list_rot,index=namelist)            

        #df_rmse = df_rmse.transpose()
        df_rmse.columns=['rmse']
        df_rmse = df_rmse.transpose()
        #print(df_rmse)
        df_mean.columns=['mean']
        df_mean = df_mean.transpose()
        #print(df_mean)
        df_median.columns=['median']
        df_median = df_median.transpose()

        df_rmse_rot.columns=['rot_rmse']
        df_rmse_rot=df_rmse_rot.transpose()

        df_mean_rot.columns=['rot_mean']
        df_mean_rot=df_mean_rot.transpose()

        df_median_rot.columns=['rot_median']
        df_median_rot=df_median_rot.transpose()
        
        return [df_rmse,df_mean,df_median,df_rmse_rot,df_mean_rot,df_median_rot]

    def get_Frontend_timing_dataframe(self, full_euroc_path, namelist):
        
        df_full_euroc=[]
        for one_name in namelist:
            if(os.path.exists(full_euroc_path+'/'+one_name+'/TrackingTimeStats.txt')):
                df_full_euroc.append(pd.read_csv(full_euroc_path+'/'+one_name+'/TrackingTimeStats.txt'))
            else:
                print(one_name+' timing file does not exist!')

        KF_insert_time = []
        ORB_ext_time = []
        Stereo_match_time=[]
        imu_preint_time=[]
        pose_pred_time=[]
        LM_track_time=[]
        KF_dec=[]
        total_time=[]



        for one_df in df_full_euroc:
            print(one_df.head())
            KF_insert_time.append(one_df['#KF insert[ms]'].mean())
            ORB_ext_time.append(one_df[' ORB ext[ms]'].mean())
            Stereo_match_time.append(one_df[' Stereo match[ms]'].mean())
            imu_preint_time.append(one_df[' IMU preint[ms]'].mean())
            pose_pred_time.append(one_df[' Pose pred[ms]'].mean())
            LM_track_time.append(one_df[' LM track[ms]'].mean())
            KF_dec.append(one_df[' KF dec[ms]'].mean())
            total_time.append(one_df[' Total[ms]'].mean())
        
        output_in_list = [namelist,KF_insert_time,ORB_ext_time,\
                            Stereo_match_time,imu_preint_time,\
                            pose_pred_time,LM_track_time,KF_dec,total_time]
        
        df_output = pd.DataFrame(output_in_list).transpose()
        df_output.columns=['dataset','KF_insert_time','ORB_ext_time',\
                    'Stereo_match_time','imu_preint_time',\
                    'pose_pred_time','LM_track_time','KF_dec','total_time']

        return df_output
        
        



