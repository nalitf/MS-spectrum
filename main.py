import pandas as pd
import matplotlib.pyplot as plt

#**********************************
# Please set appropriate values in this section.
#
# FILEPATH
FILE_PATH = ("C:/Users/Sana/hogehoge/maldidata.txt")
#
# TITLE
DATATITLE = ("sample-maldi")
#
# Range of x and y axis
MIN_X = 500
MAX_X = 1000
MIN_Y = 0
MAX_Y = 100
#
# x and y label
LABEL_X = ("Mass $\it{m/z}$")
LABEL_Y = ("% intensity")
#
#SIZE OF GRAPH
GRAPH_DPI = 300
GRAPH_WIDTH = 2000
GRAPH_HEIGHT = 1500
#STYLE OF LINE
LINE_WIDTH = 0.7
LINE_COLOR = 'k'
LINE_STYLE = 'solid'
#
#STYLE OF PLOTTING
# If you set the number "1", the graph will be plotted in continuous line.
# If you set the number "2", the graph will be plotted in assembly of vertical lines.
# Plotting lots of vertical lines take lots of time. If you would like to plot wide range, the choice "1" is recommended; as "1" and "2" style show little difference in wide range plotting.
# On the other hand, if you would like to plot too narrow range, the choice "2" is reccomended.
PLOTTING_STYLE = 1
#
#number of header row to skip (the data should not have header information and name of columns)
SKIP_ROW = 2
#
#**********************************

maldidata = pd.read_table(FILE_PATH, header=None, names=['mass', 'intensity'], skiprows=SKIP_ROW)
intensity_max=max(maldidata['intensity'])
num_xmin=min(maldidata.sort_values(by='mass').query('mass>=@MIN_X').index)
num_xmax=max(maldidata.sort_values(by='mass').query('mass<=@MAX_X').index)
#print(num_xmin)
#print(num_xmax)
#print(maldidata['mass'][num_xmin:num_xmax])

plt.figure(dpi=GRAPH_DPI,figsize=(GRAPH_WIDTH/GRAPH_DPI,GRAPH_HEIGHT/GRAPH_DPI))
plt.xlim(MIN_X,MAX_X)
plt.ylim(MIN_Y,MAX_Y)
plt.xlabel(LABEL_X)
plt.ylabel(LABEL_Y)
#plt.legend()
#plt.show()
if PLOTTING_STYLE == 1:
    plt.plot(maldidata['mass'][num_xmin:num_xmax],(maldidata['intensity'][num_xmin:num_xmax]/intensity_max)*100 ,color=LINE_COLOR,linewidth=LINE_WIDTH,linestyle=LINE_STYLE)
elif PLOTTING_STYLE == 2:
    plt.bar(x=maldidata['mass'][num_xmin:num_xmax], height=((maldidata['intensity'][num_xmin:num_xmax]/intensity_max)*100), color=LINE_COLOR,width=LINE_WIDTH)
plt.savefig(DATATITLE+'.png')