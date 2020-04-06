# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:53:20 2020

@author: LtdDan82
@github: https://github.com/LtdDan82
"""
#%%
#import matplotlib.pyplot as plt
import pandas as pd
#%%
def clean_data_for_param_vs_inspection(general_data):
    
    '''
    Cleans the data for the image generation - see detailed steps in comments
    
    Input:
        pd.dataframe / general_data after importing
    Returns:
        pd.dataframe / cleaned_data
    '''
    
    # Remove unnecessary data, material is always "Wax" and the 
    # experiment number # can be get by "index+1"
    general_data = general_data.copy(deep = True)
    general_data = general_data.drop(columns = ['material', 'No'])
    # Remove any NaN rows
    general_data = general_data.dropna(axis = 0, how = 'any')
    # Now we can see that in all cases the machining finalized so we drop that column as well
    general_data = general_data.drop(columns = ['machining_finalized'])
    # Set "passed_visual_inspection to True/False"
    general_data['passed_visual_inspection'] = general_data['passed_visual_inspection'] == 'yes'
    
#    exp_params = ['feedrate', 'clamp_pressure']
    result_params = ['tool_condition', 'passed_visual_inspection'] 
    tool_group = general_data.groupby(result_params).count()
   # print(tool_group)
    #print('There are datasets where the tool is worn'\
   #       + ' but it is not detected by visual inspection')  
    
    cleaned_data = general_data
    return cleaned_data

#%%
def param_vs_inspection(cleaned_data, param):
    '''
    Takes cleaned_data and returns x,y data for true and false cases for a
    specific parameter (param may be "feedrate" or "clamp_pressure")
    
    Input: 
        pd.dataframe. general_data after data cleansing
        str. name of the parameter, e.g. "feedrate", "clamp_pressure"
    Returns:
        None
    '''
    
    #Get data with worn tools
    worn_data = cleaned_data[cleaned_data['tool_condition'] == 'worn']
    #print(worn_data)
    vis_insp = 'passed_visual_inspection'
    # Extract true / false data for plotting
    true_data = worn_data[[param, vis_insp]][worn_data[vis_insp] == True]
    true_x, true_y = true_data[param], true_data[vis_insp]
    false_data = worn_data[[param, vis_insp]][worn_data[vis_insp] == False]
    false_x, false_y = false_data[param], false_data[vis_insp]
    
    return true_x, true_y, false_x, false_y
#%%
def img_param_vs_inspect(true_x, true_y, false_x, false_y, param, savefig = True):
    '''
    Generates a figure with x = param, y = True/False for visual inspection
    
    '''
    vis_insp = 'passed_visual_inspection'
    # Generate plot
    fig = plt.figure()
    plt.plot(true_x, true_y, marker = 'x', linestyle = 'None', color = 'green')
    plt.plot(false_x, false_y, marker = 'o', linestyle = 'None', color = 'red')
    plt.xlabel(param)
    plt.ylabel(vis_insp)
    plt.yticks([1.0, 0.0], ["True", "False"])
    plt.legend(['True', 'False'])
    plt.title('Influence of %s on %s' %(param, vis_insp))
    fig.show()
    if savefig:
        plt.savefig(param + '_vs_' + vis_insp +'.png')
    else:
        pass
