#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

import pyecharts.options as opts
from pyecharts.charts import Line
from Painter import Painter
from datetime import date
from Row import Row

class SimpleChart():
    def __init__(self):

        self.CLine = Line()

        self.id = id
        self.name = ""
        self.xvalues = [1, 2, 3]
        self.yvalues = [2, 4, 5]

    def LayoutChart(self):

        self.CLine.add_xaxis(xaxis_data = self.xvalues)
        self.CLine.add_yaxis(series_name = self.name, y_axis = self.yvalues, markpoint_opts=opts.MarkPointOpts(
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
        p = Painter()
        self.name, self.id, self.xvalues, self.yvalues = Painter().DataSChart(CurrentRow=Row(1), startdate = date(2024, 4, 2), enddate=date(2024, 6, 2))
        self.LayoutChart()
        self.CLine.set_global_opts(title_opts=opts.TitleOpts(title = self.name))
        self.CLine.render(f"SimpleChart_{self.id}.html")

SimpleChart().DisplayChart()



