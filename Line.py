#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

import pyecharts.options as opts
from pyecharts.charts import Line

class SimpleChart():
    def __init__(self):

        self.CLine = Line()

        self.xvalues = ["27 апреля 2024", "28 апреля 2024", "29 апреля 2024", "30 апреля 2024"]
        self.yvalues = [1800, 2000, 1900, 1400]
        self.legend = "Количество выпитой воды"

    def LayoutChart(self):

        self.CLine.add_xaxis(xaxis_data = self.xvalues)
        self.CLine.add_yaxis(series_name = self.legend, y_axis = self.yvalues, markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="Максимальное значение"),
                opts.MarkPointItem(type_="min", name="Минимальное значение"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="Среднее значение")]
        ),
    )

    def DisplayChart(self):
        
        self.LayoutChart()
        self.CLine.set_global_opts(title_opts=opts.TitleOpts(title="Вода", subtitle=""))
        self.CLine.render("Row.html")

SimpleChart().DisplayChart()

