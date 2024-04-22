#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from Row import Row
from Manager import Manager
from datetime import datetime

row = Row(1)
manager = Manager()

YearNow = datetime.today().year
MonthNow = datetime.today().strftime("%m")
DayNow = datetime.today().strftime("%d")

row.Add(1459, YearNow, MonthNow, DayNow)