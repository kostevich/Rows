#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from Source.Row import Row
from datetime import date
from Graphics.SimpleChart import SimpleChart

class Painter():
    def __init__(self) -> None:
        self.__simplechart = SimpleChart()

    def DataSChart(self, CurrentRow: Row, startdate: date, enddate: date) -> bool:

        Name = CurrentRow.name or ""

        ListDates = list()
        dates = CurrentRow.GetSegment(startdate, enddate).keys()
        for date in dates: ListDates.append(date)
        
        ListValues = list()
        values = CurrentRow.GetSegment(startdate, enddate).values()
        for value in values: ListValues.append(value["value"])

        isSuccess = True if self.__simplechart.DisplayChart(Name, CurrentRow.ID, ListDates, ListValues) else False

        return isSuccess


