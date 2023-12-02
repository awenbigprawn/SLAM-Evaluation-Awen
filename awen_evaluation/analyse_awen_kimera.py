import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from awen_plotter import awenplotter
from awen_datagetter_kimera import awenDataGetter
import os
from evo.core import trajectory, sync, metrics

evo_result_path1="./evo_result"
namelist_full_euroc = ['MH_01_easy','MH_02_easy','MH_03_medium','MH_04_difficult','MH_05_difficult',\
                        'V1_01_easy','V1_02_medium','V1_03_difficult',\
                        'V2_01_easy','V2_02_medium','V2_03_difficult']


kimera_evaluater = awenDataGetter()
#df_time = kimera_evaluater.get_Frontend_timing_dataframe('./vins_result_awen')
#df_time.to_csv('./evo_result_vins_history/vins_Frontend_timing.csv',index=False)
[df_rmse,df_mean,df_median,df_rmse_rot,df_mean_rot,df_median_rot,namelist_full_euroc] = kimera_evaluater.putEurocAPEinOneTable(namelist = namelist_full_euroc, evo_result_path = evo_result_path1)
[df_relativ_rmse,df_relativ_mean,df_relativ_median,df_relativ_rmse_rot,df_relativ_mean_rot,df_relativ_median_rot,namelist_full_euroc] = \
                kimera_evaluater.putEurocRPEinOneTable(namelist = namelist_full_euroc, evo_result_path = evo_result_path1)

plotter = awenplotter()
plotter.awen_barplot(df_rmse, title='kimera_vio_euroc_APE_trans_rmse', save_path=evo_result_path1, ylabel='APE_trans_rmse/m')
#plotter.awen_barplot(df_mean, title='vins_vio_euroc_APE_trans_mean', save_path=evo_result_path1, ylabel='APE_trans_mean/m')
plotter.awen_barplot(df_rmse_rot, title='kimera_vio_euroc_APE_rot_rmse', save_path=evo_result_path1, ylabel='APE_rot_rmse/deg')
#plotter.awen_barplot(df_mean_rot, title='vins_vio_euroc_APE_rot_mean', save_path=evo_result_path1, ylabel='APE_rot_mean/deg')
plotter.awen_barplot(df_relativ_rmse, title='kimera_vio_euroc_RPE_trans_rmse', save_path=evo_result_path1, ylabel='RPE_trans_rmse/m')
#plotter.awen_barplot(df_relativ_mean, title='vins_vio_euroc_RPE_trans_mean', save_path=evo_result_path1, ylabel='RPE_trans_mean/m')
plotter.awen_barplot(df_relativ_rmse_rot, title='kimera_vio_euroc_RPE_rot_rmse', save_path=evo_result_path1, ylabel='RPE_rot_rmse/deg')
#plotter.awen_barplot(df_relativ_mean_rot, title='vins_vio_euroc_RPE_rot_mean', save_path=evo_result_path1, ylabel='RPE_rot_mean/deg')

df_all_in_one = pd.DataFrame(columns=namelist_full_euroc)
df_all_in_one = df_all_in_one.append(df_mean)
df_all_in_one = df_all_in_one.append(df_median)
df_all_in_one = df_all_in_one.append(df_rmse)
df_all_in_one = df_all_in_one.append(df_mean_rot)
df_all_in_one = df_all_in_one.append(df_median_rot)
df_all_in_one = df_all_in_one.append(df_rmse_rot)
rel_df_all_in_one = pd.DataFrame(columns=namelist_full_euroc)
rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_mean)
rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_median)
rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_rmse)
rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_mean_rot)
rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_median_rot)
rel_df_all_in_one = rel_df_all_in_one.append(df_relativ_rmse_rot)

df_all_in_one=df_all_in_one.transpose()
rel_df_all_in_one=rel_df_all_in_one.transpose()

df_all_in_one_trans = pd.DataFrame(columns=namelist_full_euroc)
df_all_in_one_trans = df_all_in_one_trans.append(df_mean)
df_all_in_one_trans = df_all_in_one_trans.append(df_median)
df_all_in_one_trans = df_all_in_one_trans.append(df_rmse)

df_all_in_one_rot = pd.DataFrame(columns=namelist_full_euroc)
df_all_in_one_rot = df_all_in_one_rot.append(df_mean_rot)
df_all_in_one_rot = df_all_in_one_rot.append(df_median_rot)
df_all_in_one_rot = df_all_in_one_rot.append(df_rmse_rot)

#print(df_all_in_one_trans)
#print(df_all_in_one_trans.columns)

#plotter.awen_barplot_mean_median_rmse(df_all_in_one_trans, title='vins_vio_euroc_APE_trans', save_path=evo_result_path1, ylabel='APE_trans/m')
#plotter.awen_barplot_mean_median_rmse(df_all_in_one_rot, title='vins_vio_euroc_APE_rot', save_path=evo_result_path1, ylabel='APE_trans/m')

df_all_in_one.to_csv(evo_result_path1+'/kimera_vio_euroc_APE_trans_rmse.csv')
rel_df_all_in_one.to_csv(evo_result_path1+'/kimera_vio_euroc_RPE_trans_rmse.csv')