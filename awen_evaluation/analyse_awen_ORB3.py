import pandas as pd
#from matplotlib import pyplot as plt
#import seaborn as sns
from awen_plotter import awenplotter
from awen_datagetter_orb import awenDataGetterOrb
import os
import sys

def analyse_awen_vins(result_path,read_path):
    # evo_result_path="./evo_result"
    # evo_result_path="./evo_result_vins_history/evo_result_01_se3"
    # evo_result_path="./evo_result_vins_history/evo_result_with_align_original_point"
    evo_result_path1="/home/yuwen/result_orb/euroc_result_06"
    #evo_result_path1=result_path
    read_path="/home/yuwen/result_orb/euroc_result_06"
    namelist_full_euroc = ['MH01','MH02','MH03','MH04','MH05',\
                        'V101','V102','V103',\
                        'V201','V202','V203']
    # namelist_full_euroc = []

    # for onename in namelist_full_euroc_org:
    #     if(os.path.exists('/home/yuwen/vins_result_awen/'+onename+'/pose_graph_path.csv')):
    #         namelist_full_euroc.append(onename)

    vin_evaluater = awenDataGetterOrb()
    
    df_time = vin_evaluater.get_Frontend_timing_dataframe(read_path, namelist=namelist_full_euroc)
    df_time.to_csv(evo_result_path1+'/ORB_Frontend_timing.csv',index=False)
    # [df_rmse,df_mean,df_median,df_rmse_rot,df_mean_rot,df_median_rot] = vin_evaluater.putEurocAPEinOneTable(namelist = namelist_full_euroc, evo_result_path = evo_result_path1)
    # [df_relativ_rmse,df_relativ_mean,df_relativ_median,df_relativ_rmse_rot,df_relativ_mean_rot,df_relativ_median_rot] = \
    #                 vin_evaluater.putEurocRPEinOneTable(namelist = namelist_full_euroc, evo_result_path = evo_result_path1)

    # plotter = awenplotter()
    # plotter.awen_barplot(df_rmse, title='ORB SLAM EuRoC RMSE ATE', save_path=evo_result_path1, ylabel='ATE/m')
    # #plotter.awen_barplot(df_mean, title='vins_vio_euroc_APE_trans_mean', save_path=evo_result_path1, ylabel='APE_trans_mean/m')
    # plotter.awen_barplot(df_rmse_rot, title='ORB SLAM EuRoC RMSE ARE', save_path=evo_result_path1, ylabel='ARE/deg')
    # #plotter.awen_barplot(df_mean_rot, title='vins_vio_euroc_APE_rot_mean', save_path=evo_result_path1, ylabel='APE_rot_mean/deg')
    # plotter.awen_barplot(df_relativ_rmse, title='orb_vio_euroc_RPE_trans_rmse', save_path=evo_result_path1, ylabel='RPE_trans_rmse/m')
    # #plotter.awen_barplot(df_relativ_mean, title='vins_vio_euroc_RPE_trans_mean', save_path=evo_result_path1, ylabel='RPE_trans_mean/m')
    # plotter.awen_barplot(df_relativ_rmse_rot, title='orb_vio_euroc_RPE_rot_rmse', save_path=evo_result_path1, ylabel='RPE_rot_rmse/deg')
    # #plotter.awen_barplot(df_relativ_mean_rot, title='vins_vio_euroc_RPE_rot_mean', save_path=evo_result_path1, ylabel='RPE_rot_mean/deg')

    # df_all_in_one = pd.DataFrame(columns=namelist_full_euroc)
    # df_all_in_one = df_all_in_one.append(df_mean)
    # df_all_in_one = df_all_in_one.append(df_median)
    # df_all_in_one = df_all_in_one.append(df_rmse)
    # df_all_in_one = df_all_in_one.append(df_mean_rot)
    # df_all_in_one = df_all_in_one.append(df_median_rot)
    # df_all_in_one = df_all_in_one.append(df_rmse_rot)
    # rel_df_all_in_one = pd.DataFrame(columns=namelist_full_euroc)
    # rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_mean)
    # rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_median)
    # rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_rmse)
    # rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_mean_rot)
    # rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_median_rot)
    # rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_rmse_rot)

    # df_all_in_one=df_all_in_one.transpose()
    # rel_df_all_in_one=rel_df_all_in_one.transpose()

    # df_all_in_one_trans = pd.DataFrame(columns=namelist_full_euroc)
    # df_all_in_one_trans = df_all_in_one_trans.append(df_mean)
    # df_all_in_one_trans = df_all_in_one_trans.append(df_median)
    # df_all_in_one_trans = df_all_in_one_trans.append(df_rmse)

    # df_all_in_one_rot = pd.DataFrame(columns=namelist_full_euroc)
    # df_all_in_one_rot = df_all_in_one_rot.append(df_mean_rot)
    # df_all_in_one_rot = df_all_in_one_rot.append(df_median_rot)
    # df_all_in_one_rot = df_all_in_one_rot.append(df_rmse_rot)

    # #print(df_all_in_one_trans)
    # #print(df_all_in_one_trans.columns)

    # plotter.awen_barplot_mean_median_rmse(df_all_in_one_trans, title='vins_vio_euroc_APE_trans', save_path=evo_result_path1, ylabel='APE_trans/m')
    # plotter.awen_barplot_mean_median_rmse(df_all_in_one_rot, title='vins_vio_euroc_APE_rot', save_path=evo_result_path1, ylabel='APE_trans/m')

    # df_all_in_one.to_csv(evo_result_path1+'/orb_vio_euroc_APE_trans_rmse.csv')
    # rel_df_all_in_one.to_csv(evo_result_path1+'/orb_vio_euroc_RPE_trans_rmse.csv')

if __name__ =='__main__':
    analyse_awen_vins()

