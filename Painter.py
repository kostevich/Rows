#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from Row import Row
from datetime import date

class Painter():
    def __init__(self):
        pass

    def DataSChart(self, CurrentRow: Row, startdate: date, enddate: date):

        id = CurrentRow.ID

        name = CurrentRow.name
        if name == None: name =""

        listdates = list()
        dates = CurrentRow.GetSegment(startdate, enddate).keys()
        for date in dates: listdates.append(date)
        

        listvalues = list()
        values = CurrentRow.GetSegment(startdate, enddate).values()
        for value in values: listvalues.append(value)

        return name, id, listdates, listvalues  


