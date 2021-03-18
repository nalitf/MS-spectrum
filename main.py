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
LABEL_X = ("m/z")
LABEL_Y = ("% intensity")
#
#SIZE OF GRAPH
GRAPH_DPI = 300
GRAPH_WIDTH = 2000
GRAPH_HEIGHT = 1500
#STYLE OF LINE
LINE_WIDTH = 0.5
LINE_COLOR = 'k'
LINE_STYLE = 'solid'
#
#number of header row to skip (the data should not have header information and name of columns)
SKIP_ROW = 2
#
#**********************************

maldidata = pd.read_table(FILE_PATH, header=None, names=['mass', 'intensity'], skiprows=SKIP_ROW)
intensity_max=max(maldidata['intensity'])
#print(maldidata)
plotting=maldidata.query('mass >= @MIN_X and mass <= @MAX_X')
#print(plotting)
#to make program lighter, only data in the range of graph will be plot.

#plt.plot(plotting['mass'],(plotting['intensity']/intensity_max)*100 ,color=LINE_COLOR,linewidth=LINE_WIDTH,linestyle=LINE_STYLE)
#this line shows just a line plotting.

plt.figure(dpi=GRAPH_DPI,figsize=(GRAPH_WIDTH/GRAPH_DPI,GRAPH_HEIGHT/GRAPH_DPI))
plt.xlim(MIN_X,MAX_X)
plt.ylim(MIN_Y,MAX_Y)
plt.xlabel(LABEL_X)
plt.ylabel(LABEL_Y)
plt.bar(x=plotting['mass'], height=((plotting['intensity']/intensity_max)*100), color=LINE_COLOR,width=LINE_WIDTH)
#plt.legend()
#plt.show()
plt.savefig(DATATITLE+'.png')