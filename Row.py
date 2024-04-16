#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import WriteJSON
from datetime import datetime
import os

#==========================================================================================#
# >>>>> РЯД <<<<< #
#==========================================================================================#
	
class Row():

	#==========================================================================================#
	# >>>>> КОНСТРУКТОР <<<<< #
	#==========================================================================================#
	
	def __init__(self):
		pass

	#==========================================================================================#
	# >>>>> СОЗДАНИЕ РЯДА <<<<< #
	#==========================================================================================#
		
	def Create(self, manager):
		# Получение текущего года, месяца и дня.
		YearNow = datetime.today().year
		MonthNow = datetime.today().strftime("%m")
		DayNow = datetime.today().strftime("%d")

		# Данные ряда.
		self.__Data = {
			"name": None,
			"color": None,
			"owner": None,
			"description": {
				"type": None
			},
			"metainfo": {
			"creation_date": f"{YearNow}-{MonthNow}-{DayNow}",
				"update_date": None
			},
			"data": {}
	}	
		# Получение ID.
		self.ID = manager.GetFreeID()

		# Создание файла json.
		self.Save()

	#==========================================================================================#
	# >>>>> УДАЛЕНИЕ РЯДА <<<<< #
	#==========================================================================================#

	def Remove(self):
		# Удаление файла json.
		os.remove(f"Data/{self.ID}.json")

	#==========================================================================================#
	# >>>>> ДОБАВЛЕНИЕ ЗНАЧЕНИЯ В РЯД <<<<< #
	#==========================================================================================#

	def Add(self, value: any, year: int = None, mounth: int = None, day: int = None) -> bool:

		# Запись значения в ряд.
		self.__Data["data"][str(year)] = dict()
		self.__Data["data"][str(year)][str(mounth)] = dict()
		self.__Data["data"][str(year)][str(mounth)][str(day)] = value

		# Сохранение файла json.
		self.Save()

	#==========================================================================================#
	# >>>>> СОХРАНЕНИЕ ДАННЫХ ФАЙЛА JSON <<<<< #
	#==========================================================================================#

	def Save(self):
		# Сохранение файла json.
		WriteJSON(f"Data/{self.ID}.json", self.__Data)

		
		
