#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import WriteJSON, ReadJSON
from datetime import datetime
import os

#==========================================================================================#
# >>>>> РЯД <<<<< #
#==========================================================================================#
	
class Row():

	#==========================================================================================#
	# >>>>> КОНСТРУКТОР <<<<< #
	#==========================================================================================#
	
	def __init__(self, ID):

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
		self.ID = ID
		# self.ID = manager.GetFreeID()

		if os.path.exists(f"Data/{self.ID}.json"): self.__Data = ReadJSON(f"Data/{self.ID}.json")

		else: self.Save()

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
		# Проверка: есть ли значение в ряде.
		IsCreated = False

		if str(year) in self.__Data["data"].keys():
			if str(mounth) in self.__Data["data"][str(year)].keys():
				if str(day) in self.__Data["data"][str(year)][str(mounth)].keys(): IsCreated = True
		
		if IsCreated == False:

			# Запись значения в ряд.
			self.__Data["data"][str(year)] = dict()
			self.__Data["data"][str(year)][str(mounth)] = dict()
			self.__Data["data"][str(year)][str(mounth)][str(day)] = value

			# Сохранение файла json.
			self.Save()
		
		return IsCreated
	
	#==========================================================================================#
	# >>>>> СОХРАНЕНИЕ ДАННЫХ ФАЙЛА JSON <<<<< #
	#==========================================================================================#

	def Save(self):
		# Сохранение файла json.
		WriteJSON(f"Data/{self.ID}.json", self.__Data)
		
		

