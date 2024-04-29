#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

import pyecharts.options as opts
from pyecharts.charts import Line

class SimpleChart():
    def __init__(self):

        self.xsignature = None
        self.ysignature = None
        self.xvalues = None
        self.yvalues = None
        self.legent = None
        self.CLine = Line()

    def LayoutChart(self):

        self.CLine.add_xaxis(xaxis_data = self.xvalues)

    def DisplayChart(self):
        
        self.LayoutChart()
        self.CLine.render("Row.html")

SimpleChart().DisplayChart()

