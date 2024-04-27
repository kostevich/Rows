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
	
	def __init__(self, ID: int):

		# Форматирование даты.
		year, month, day = self.__Format(datetime.today())

		# Данные ряда.
		self.__Data = {
			"name": None,
			"color": None,
			"owner": None,
			"description": {
				"type": None
			},
			"metainfo": {
			"creation_date": f"{year}-{month}-{day}",
				"update_date": None
			},
			"data": {}
	}	
		# Получение ID ряда.
		self.ID = ID

		# Если файл JSON для ряда существует - чтение его.
		if os.path.exists(f"Data/{self.ID}.json"): self.__Data = ReadJSON(f"Data/{self.ID}.json")

		# Если нет - запись JSON.
		else: self.__Save()

	def __CheckUp(self, value: any, year: str, month: str, day: str) -> bool:

		# Значение по умолчанию.
		IsExists = False

		# Проверка: существует ли значение в ряде.
		if year in self.__Data["data"].keys():
			if month in self.__Data["data"][year].keys():
				if day in self.__Data["data"][year][month].keys(): IsExists = True

		return IsExists

	def __Format(self, datetime: datetime) -> str:
		"""Форматирует datetime в набор строковых величин.
		Year - строковое представление четырёхзначного число.
		Month - строковое представление двухзначного числа.
		Day - строковое представление двухзначного числа."""

		Year = datetime.strftime("%Y")
		Month = datetime.strftime("%m")
		Day = datetime.strftime("%d")
		
		return Year, Month, Day
	
	def __Standart(self, year: str, month: str, day: str) -> datetime:
		"""Форматирует строковое прредставление в datetime."""

		Datetime = datetime(int(year), int(month), int(day))
		
		return Datetime

	def __Save(self):

		# Сохранение файла json.
		WriteJSON(f"Data/{self.ID}.json", self.__Data)

	def Add(self, value: any, date: datetime):

		# Форматирование даты.
		year, month, day = self.__Format(date)

		# Если значение в ряду не существует.
		if not self.__CheckUp(value, year, month, day):
		
			# Запись значения в ряд.
			if year not in self.__Data["data"].keys(): self.__Data["data"][year] = dict()
			if month not in self.__Data["data"][year].keys(): self.__Data["data"][year][month] = dict()
			if day not in self.__Data["data"][year][month].keys(): self.__Data["data"][year][month][day] = value

			# Сохранение файла json.
			self.__Save()

	def Get(self, date: datetime) -> any:
		
		# Форматирование даты.
		year, month, day = self.__Format(date)

		# Получение значения словаря на выбранную дату.
		Value = self.__Data["data"][year][month][day] 
		
		return Value
	
	def Remove(self):

		# Удаление файла json.
		os.remove(f"Data/{self.ID}.json")
	
	def Replace(self, value: any, date: datetime):

		# Форматирование даты.
		year, month, day = self.__Format(date)

		# Если значение в ряду существует.
		if self.__CheckUp(value, year, month, day):

			# Замена значения в ряду.
			self.__Data["data"][year][month][day] = value

			# Сохранение файла json.
			self.__Save()

	def GetSegment(self, startdate: datetime, enddate: datetime)-> dict:

		# Словарь всех значений сегмента.
		Segment = dict()

		# Словарь всех значений словаря.
		AllValues = dict()

		# Форматирование данных в формат datetime: value.
		for years in self.__Data["data"]:
			for months in self.__Data["data"][years]:
					for days, values in self.__Data["data"][years][months].items():
						Keys = self.__Standart(years, months, days)
						AllValues[Keys]= values

		# Определение дат, находящихся в данном промежутке.
		for date, values in AllValues.items():
			if startdate <= date and enddate >= date:
				# Запись в словарь.
				Segment[date] = values
		
		return Segment
	











	
		
		



		

		
		

