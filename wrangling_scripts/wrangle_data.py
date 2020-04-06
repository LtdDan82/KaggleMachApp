import pandas as pd
import plotly.graph_objs as go

from mylib.import_data import get_alldata
from mylib.param_inspection import clean_data_for_param_vs_inspection
from mylib.param_inspection import param_vs_inspection
from mylib.param_inspection import img_param_vs_inspect

# Load all datasets
alldata = get_alldata()
# Get the general_data from all the experiments
general_data = alldata['train.csv']

#Clean the data
#print(clean_data_for_param_vs_inspection.__doc__)
df = clean_data_for_param_vs_inspection(general_data)

param_dict = {}
for p in ['feedrate', 'clamp_pressure']:
    true_x, true_y, false_x, false_y = param_vs_inspection(df,
                                                           param = p)
    # Save the x/y values in the param_dict
    param_dict[p] = [true_x, true_y, false_x, false_y]


feedrate_vals = param_dict['feedrate']
feedrate_x1 = feedrate_vals[0]
feedrate_y1 = list(map(int, feedrate_vals[1]))
feedrate_x2 = feedrate_vals[2]
feedrate_y2 = list(map(int, feedrate_vals[3]))


clamp_vals = param_dict['clamp_pressure']


def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots the True/False visual inspections as function of the feedrate
    # as a line chart
    
    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = (feedrate_x1),
      y = (feedrate_y1),
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'Feedrate_True',
                xaxis = dict(title = 'feedrate'),
                yaxis = dict(title = 'passed_inspection'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    graph_two = []

    graph_two.append(
      go.Scatter(
      x = (feedrate_x2),
      y = (feedrate_y2),
      mode = 'lines'
      )
    )

    layout_two = dict(title = 'Feedrate_False',
                xaxis = dict(title = 'feedrate',),
                yaxis = dict(title = 'passed_inspection'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = [5, 4, 3, 2, 1, 0],
      y = [0, 2, 4, 6, 8, 10],
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Chart Three',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    
    graph_four.append(
      go.Scatter(
      x = [20, 40, 60, 80],
      y = [10, 20, 30, 40],
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Chart Four',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    #figures.append(dict(data=graph_three, layout=layout_three))
    #figures.append(dict(data=graph_four, layout=layout_four))

    return figures