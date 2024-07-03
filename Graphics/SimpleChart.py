#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

import pyecharts.options as opts
from pyecharts.charts import Line
from datetime import date

class SimpleChart():
    def __init__(self) -> None:

        self.CLine = Line()

    def DisplayChart(self, Name: str, ID: int, Dates: list[date], Values: list): 
    
        self.CLine.add_xaxis(xaxis_data = Dates)
        self.CLine.add_yaxis(series_name = Name, y_axis = Values, markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="Максимальное значение"),
                opts.MarkPointItem(type_="min", name="Минимальное значение"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="Среднее значение")]
        ),
    )
        self.CLine.set_global_opts(title_opts=opts.TitleOpts(title = Name))
        Status = True if self.CLine.render(f"SimpleChart_{ID}.html") else False

        return Status




