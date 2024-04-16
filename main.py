#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from Row import Row
from Manager import Manager
from datetime import datetime

row = Row()
manager = Manager()

YearNow = datetime.today().year
MonthNow = datetime.today().strftime("%m")
DayNow = datetime.today().strftime("%d")

row.Create(manager)
row.Add(4, YearNow, MonthNow, DayNow)