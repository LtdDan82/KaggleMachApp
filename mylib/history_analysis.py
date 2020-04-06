# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:53:20 2020

@author: LtdDan82
@github: https://github.com/LtdDan82

OLD STUFF

"""

#%%
# get the general data info
def get_data_wear(general_data, data, condition):
    # Input
    # general data = overview of general data per experiment (0 -17)
    # data = dataframe from experiment
    # condition = 'worn' / 'unworn' after expierment
    
    # Output
    # condition_data = dict of experiment dataframes where condition is fullfilled
    # data_true = experiment dataframe with condition true with experiment data
    
    data_true = general_data[general_data['tool_condition'] == condition]
    filenumber = data_true['No']
    
    condition_data = {my_key: data[my_key] for my_key in filenumber}
    
    return condition_data, data_true

''' Mögliche Fragestellungen: 
    1. Gibt es Datensätze mit un- bzw. verschlissenem Werkzeug,  welche identische 
    Versuchsbedingungen (feedrate, clamp_pressure) aufweisen und 
    einmal der Fertigungsprozess erfolgreich war und einmal nicht ?
    (Sichtprüfung ausgeschlossen, da keine Versuchsbedingung)
    
    2. Wie Verhalten sich die Parameter zueinander bei diesen beiden Datensätzen ?
       Gibt es Auffälligkeiten ?
'''

def get_identicals(data_true, data):
    # Input
    # data_true = experiment dataframe with condition true with experiment data
    # data = dict of dataframes from the experiment
    
    # Output
    # duplicate_info = experimental parameters for duplicates
    # duplicate_dict = dict with the measurement values as dataframe 
    #                   of the duplicates
    
    
    dupl = data_true.duplicated(subset = ['feedrate', 'clamp_pressure'],
                                keep = False)
    
    duplicate_info = data_true[dupl]
    filenumber = duplicate_info['No']
    
    duplicate_dict = {my_key: data[my_key] for my_key in filenumber}
    duplicate_dict['mach_no'] = duplicate_dict.pop(7)
    duplicate_dict['mach_yes'] = duplicate_dict.pop(8)
        
    return duplicate_info, duplicate_dict



