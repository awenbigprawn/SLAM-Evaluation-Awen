from numpy.core.fromnumeric import mean
import pandas as pd
import numpy as np
import os
#import seaborn as sns

class awenDataGetterVins:

    def putEurocAPEinOneTable(self, namelist, evo_result_path):
            
        dataframe_list=[]
        dataframe_list_rot=[]
        for one_name in namelist:
            dataframe_list.append(pd.read_csv(evo_result_path+'/vins_plot_'+one_name+'/trans_table.csv', index_col=0, header=0))
            dataframe_list_rot.append(pd.read_csv(evo_result_path+'/vins_plot_'+one_name+'/rot_table.csv', index_col=0, header=0))
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
            rmse_list.append(one_dataframe.loc['pose_graph_path.txt','rmse'])
            mean_list.append(one_dataframe.loc['pose_graph_path.txt','mean'])
            median_list.append(one_dataframe.loc['pose_graph_path.txt','median'])
            df_mean_ci.append(one_dataframe.loc['pose_graph_path.txt','std'])

        for one_dataframe in dataframe_list_rot:
            rmse_list_rot.append(one_dataframe.loc['pose_graph_path.txt','rmse'])
            mean_list_rot.append(one_dataframe.loc['pose_graph_path.txt','mean'])
            median_list_rot.append(one_dataframe.loc['pose_graph_path.txt','median'])
            df_mean_rot_ci.append(one_dataframe.loc['pose_graph_path.txt','std'])
            
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
            dataframe_list.append(pd.read_csv(evo_result_path+'/vins_plot_'+one_name+'/trans_relativ_table.csv', index_col=0, header=0))
            dataframe_list_rot.append(pd.read_csv(evo_result_path+'/vins_plot_'+one_name+'/rot_relativ_table.csv', index_col=0, header=0))

        rmse_list=[]
        mean_list=[]
        median_list=[]
        rmse_list_rot=[]
        mean_list_rot=[]
        median_list_rot=[]
        df_mean_ci=[]
        df_mean_rot_ci=[]            

        for one_dataframe in dataframe_list:
            rmse_list.append(one_dataframe.loc['pose_graph_path.txt','rmse'])
            mean_list.append(one_dataframe.loc['pose_graph_path.txt','mean'])
            median_list.append(one_dataframe.loc['pose_graph_path.txt','median'])
            df_mean_ci.append(one_dataframe.loc['pose_graph_path.txt','std'])

        for one_dataframe in dataframe_list_rot:
            rmse_list_rot.append(one_dataframe.loc['pose_graph_path.txt','rmse'])
            mean_list_rot.append(one_dataframe.loc['pose_graph_path.txt','mean'])
            median_list_rot.append(one_dataframe.loc['pose_graph_path.txt','median'])
            df_mean_rot_ci.append(one_dataframe.loc['pose_graph_path.txt','std'])
            
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
            if(os.path.exists(full_euroc_path+'/'+one_name+'/vins_result/trackImage_time.csv')):
                df_full_euroc.append(pd.read_csv(full_euroc_path+'/'+one_name+'/vins_result/trackImage_time.csv'))
            elif(os.path.exists(full_euroc_path+'/'+one_name+'/trackImage_time.csv')):
                df_full_euroc.append(pd.read_csv(full_euroc_path+'/'+one_name+'/trackImage_time.csv'))
            else:
                print(one_name+' timing file does not exist!')

        temp_opt_flow_time = []
        set_mask_time = []
        feature_detection_time=[]
        feature_stereo_time=[]
        some_assignment_time=[]

        for one_df in df_full_euroc:
            temp_opt_flow_time.append(one_df['temp_opt_flow_time'].mean())
            set_mask_time.append(one_df['set_mask_time'].mean())
            feature_detection_time.append(one_df['feature_detection_time'].mean())
            feature_stereo_time.append(one_df['feature_stereo_time'].mean())
            some_assignment_time.append(one_df['some_assignment_time'].mean())
        
        output_in_list = [namelist,temp_opt_flow_time,set_mask_time,\
                            feature_detection_time,feature_stereo_time,\
                            some_assignment_time]
        
        df_output = pd.DataFrame(output_in_list).transpose()
        df_output.columns=['dataset','temp_opt_flow_time','set_mask_time',\
                    'feature_detection_time','feature_stereo_time',\
                    'some_assignment_time']

        return df_output
        
        



