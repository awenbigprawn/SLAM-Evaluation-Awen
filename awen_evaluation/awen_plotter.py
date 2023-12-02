import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

class awenplotter:

    def awen_barplot(self, dataset, title, save_path, ylabel='timeuse/us', ci=None):
        fig2 = plt.figure(2)
        #plt.subplots(constrained_layout = True)
        sns.set_style('whitegrid')
        sns.barplot(data=dataset, color = 'royalblue', ci = ci)
        plt.xticks(rotation=30)
        plt.xlabel('dataset')
        plt.ylabel(ylabel)
        plt.title(title)
        fig2.subplots_adjust(bottom = 0.2)
        plt.savefig(save_path+'/'+title+'.png')
        plt.close()
        
    def awen_barplot_mean_median_rmse(self, dataset, title,save_path, hue='mean,median,rmse', ylabel='timeuse/us', ci=None):
        
        fig2 = plt.figure(2)
        #plt.subplots(constrained_layout = True)
        sns.set_style('whitegrid')
        #sns.barplot(data=dataset, color = 'royalblue', ci = ci)
        plt.xticks(rotation=30)
        plt.xlabel('dataset')
        plt.ylabel(ylabel)
        plt.title(title)
        fig2.subplots_adjust(bottom = 0.2)
        plt.savefig(save_path+'/'+title+'.png')
        plt.close()
        

    def awen_boxplot(self, dataset, title, save_path):
        fig1 = plt.figure(1)
        #plt.subplots()
        plt.subplots(constrained_layout = True)
        sns.set_style('whitegrid')
        sns.boxplot(data = dataset)

        plt.xticks(rotation=30)
        plt.xlabel('dataset')
        plt.ylabel('timeuse/us')
        plt.title(title)
        #plt.rcParams['figure.constrained_layout.use'] = True
        fig1.subplots_adjust(bottom = 0.2)

        plt.savefig(save_path+'/'+title+'.png')

