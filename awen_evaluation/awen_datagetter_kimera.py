import pandas as pd
import numpy as np
import os
#import seaborn as sns

class awenDataGetter:
    #String full_euroc_path
    namelist_=[]

    def get_Frontend_timing_dataframe(self, full_euroc_path):
        namelist = ['MH_01_easy','MH_02_easy','MH_03_medium','MH_04_difficult','MH_05_difficult',\
                    'V1_01_easy','V1_02_medium','V1_03_difficult',\
                    'V2_01_easy','V2_02_medium','V2_03_difficult']
        df_full_euroc=[]
        for one_name in namelist:
            df_full_euroc.append(pd.read_csv(full_euroc_path+'/'+one_name+'/Euroc/output_frontend_stats.csv'))

        # df_MH_01_easy = pd.read_csv(full_euroc_path + "/MH_01_easy/Euroc/output_frontend_stats.csv")
        # df_MH_02_easy = pd.read_csv(full_euroc_path + "/MH_02_easy/Euroc/output_frontend_stats.csv")
        # df_MH_03_medium = pd.read_csv(full_euroc_path + "/MH_03_medium/Euroc/output_frontend_stats.csv")
        # df_MH_04_difficult = pd.read_csv(full_euroc_path + "/MH_04_difficult/Euroc/output_frontend_stats.csv")
        # df_MH_05_difficult = pd.read_csv(full_euroc_path + "/MH_05_difficult/Euroc/output_frontend_stats.csv")
        # df_V1_01_easy = pd.read_csv(full_euroc_path + "/V1_01_easy/Euroc/output_frontend_stats.csv")
        # df_V1_02_medium = pd.read_csv(full_euroc_path + "/V1_02_medium/Euroc/output_frontend_stats.csv")
        # df_V1_03_difficult = pd.read_csv(full_euroc_path + "/V1_03_difficult/Euroc/output_frontend_stats.csv")
        # df_V2_01_easy = pd.read_csv(full_euroc_path + "/V2_01_easy/Euroc/output_frontend_stats.csv")
        # df_V2_02_medium = pd.read_csv(full_euroc_path + "/V2_02_medium/Euroc/output_frontend_stats.csv")
        # df_V2_03_difficult = pd.read_csv(full_euroc_path + "/V2_03_difficult/Euroc/output_frontend_stats.csv")

        # df_full_euroc = [df_MH_01_easy, df_MH_02_easy, df_MH_03_medium, df_MH_04_difficult, df_MH_05_difficult,\
        #                     df_V1_01_easy, df_V1_02_medium, df_V1_03_difficult,\
        #                     df_V2_01_easy, df_V2_02_medium, df_V2_03_difficult]

        full_euroc_IMU_preInter_time = []
        feature_tracking_time = []
        feature_detection_time = []
        stereo_matching_time = []
        outlier_rejection_time = []
        feature_detection_fifth_part_time = []

        for one_df in df_full_euroc:
            full_euroc_IMU_preInter_time.append(one_df['full_preint_duration'].mean())
            feature_tracking_time.append(one_df['featureTrackingTime'].mean())
            feature_detection_time.append(one_df['featureDetectionTime'].mean())
            stereo_matching_time.append(one_df['sparse_stereo_time_'].mean()\
                                        +one_df['sparseStereoMatching_time_'].mean())
            outlier_rejection_time.append(one_df['outlierRejectionStereo_time_'].mean())
            feature_detection_fifth_part_time.append(one_df['Feature_Detection_Fifth_Part_'].mean())
        
        output_in_list = [  namelist, full_euroc_IMU_preInter_time,\
                            feature_tracking_time,\
                            feature_detection_time,\
                            stereo_matching_time,\
                            outlier_rejection_time,\
                            feature_detection_fifth_part_time]
        
        df_output = pd.DataFrame(output_in_list).transpose()
        df_output.columns=['dataset','IMU pre-intergration',\
                                                'feature tracking','feature detection',\
                                                'stereo matching','outlier rejection',\
                                                'cv::cornerSubPix()']

        return df_output
        

    def putEurocAPEinOneTable(self, namelist, evo_result_path):
        namelist_=[]
        dataframe_list=[]
        dataframe_list_rot=[]
        for one_name in namelist:
            print(os.path.exists(evo_result_path+'/kimera_plot_'+one_name+'/trans_table.csv'))
            if(os.path.exists(evo_result_path+'/kimera_plot_'+one_name+'/trans_table.csv')):
                dataframe_list.append(pd.read_csv(evo_result_path+'/kimera_plot_'+one_name+'/trans_table.csv', index_col=0, header=0))
                dataframe_list_rot.append(pd.read_csv(evo_result_path+'/kimera_plot_'+one_name+'/rot_table.csv', index_col=0, header=0))
                namelist_.append(one_name)
                
        print('namelist=')
        print(namelist_)
        rmse_list=[]
        mean_list=[]
        median_list=[]
        rmse_list_rot=[]
        mean_list_rot=[]
        median_list_rot=[]
        df_mean_ci=[]
        df_mean_rot_ci=[]

        for one_dataframe in dataframe_list:
            rmse_list.append(one_dataframe.loc['traj_pgo.txt','rmse'])
            mean_list.append(one_dataframe.loc['traj_pgo.txt','mean'])
            median_list.append(one_dataframe.loc['traj_pgo.txt','median'])
            df_mean_ci.append(one_dataframe.loc['traj_pgo.txt','std'])

        for one_dataframe in dataframe_list_rot:
            rmse_list_rot.append(one_dataframe.loc['traj_pgo.txt','rmse'])
            mean_list_rot.append(one_dataframe.loc['traj_pgo.txt','mean'])
            median_list_rot.append(one_dataframe.loc['traj_pgo.txt','median'])
            df_mean_rot_ci.append(one_dataframe.loc['traj_pgo.txt','std'])
            
        df_rmse = pd.DataFrame(rmse_list,index=namelist_)
        df_mean = pd.DataFrame(mean_list,index=namelist_)
        df_median = pd.DataFrame(median_list, index=namelist_)
        df_rmse_rot = pd.DataFrame(rmse_list_rot,index=namelist_)
        df_mean_rot = pd.DataFrame(mean_list_rot,index=namelist_)
        df_median_rot = pd.DataFrame(median_list_rot,index=namelist_)            

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

        return [df_rmse,df_mean,df_median,df_rmse_rot,df_mean_rot,df_median_rot,namelist_]

    def putEurocRPEinOneTable(self, namelist, evo_result_path):
        namelist_=[]
        dataframe_list=[]
        dataframe_list_rot=[]
        for one_name in namelist:
            print(os.path.exists(evo_result_path+'/kimera_plot_'+one_name+'/trans_relativ_table.csv'))
            if(os.path.exists(evo_result_path+'/kimera_plot_'+one_name+'/trans_relativ_table.csv')):
                dataframe_list.append(pd.read_csv(evo_result_path+'/kimera_plot_'+one_name+'/trans_relativ_table.csv', index_col=0, header=0))
                dataframe_list_rot.append(pd.read_csv(evo_result_path+'/kimera_plot_'+one_name+'/rot_relativ_table.csv', index_col=0, header=0))
                namelist_.append(one_name)
        
        rmse_list=[]
        mean_list=[]
        median_list=[]
        rmse_list_rot=[]
        mean_list_rot=[]
        median_list_rot=[]
        df_mean_ci=[]
        df_mean_rot_ci=[]            

        for one_dataframe in dataframe_list:
            rmse_list.append(one_dataframe.loc['traj_pgo.txt','rmse'])
            mean_list.append(one_dataframe.loc['traj_pgo.txt','mean'])
            median_list.append(one_dataframe.loc['traj_pgo.txt','median'])
            df_mean_ci.append(one_dataframe.loc['traj_pgo.txt','std'])

        for one_dataframe in dataframe_list_rot:
            rmse_list_rot.append(one_dataframe.loc['traj_pgo.txt','rmse'])
            mean_list_rot.append(one_dataframe.loc['traj_pgo.txt','mean'])
            median_list_rot.append(one_dataframe.loc['traj_pgo.txt','median'])
            df_mean_rot_ci.append(one_dataframe.loc['traj_pgo.txt','std'])
            
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
        
        return [df_rmse,df_mean,df_median,df_rmse_rot,df_mean_rot,df_median_rot,namelist_]