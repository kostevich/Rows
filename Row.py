#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods.JSON import WriteJSON, ReadJSON
from collections import OrderedDict
from datetime import date
import os

class Row():

	@property
	def name(self):
		return self.GetSettings("name")
	
	@property
	def color(self):
		return self.GetSettings("color")
		
	@property
	def creation_date(self):
		return self.GetSettings("metainfo/creation_date")
	
	@property
	def update_date(self):
		return self.GetSettings("metainfo/update_date")
	
	def __init__(self, ID: int):

		# Форматирование даты.
		year, month, day = self.__Format(date.today())

		# Данные ряда.
		self.__Data = {
			"name": None,
			"color": None,
			"description": {},
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

	def __CheckUp(self, year: str, month: str, day: str) -> bool:

		# Значение по умолчанию.
		IsExists = False

		# Проверка: существует ли значение в ряде.
		if year in self.__Data["data"].keys():
			if month in self.__Data["data"][year].keys():
				if day in self.__Data["data"][year][month].keys(): IsExists = True

		return IsExists

	def __Format(self, date: date) -> str:
		"""Форматирует datetime в набор строковых величин.
		Year - строковое представление четырёхзначного число.
		Month - строковое представление двухзначного числа.
		Day - строковое представление двухзначного числа."""

		Year = date.strftime("%Y")
		Month = date.strftime("%m")
		Day = date.strftime("%d")
		
		return Year, Month, Day
	
	def __Standart(self, year: str, month: str, day: str) -> date:
		"""Форматирует строковое прредставление в date."""

		Date = date(int(year), int(month), int(day))
		
		return Date

	def __Save(self):

		# Сохранение файла json.
		WriteJSON(f"Data/{self.ID}.json", self.__Data)

	def SetData(self, type: str, value: any, date: date):

		# Форматирование даты.
		year, month, day = self.__Format(date)

		# Если значение в ряду не существует.
		if not self.__CheckUp(year, month, day):
		
			# Запись значения в ряд.
			if year not in self.__Data["data"].keys(): self.__Data["data"][year] = dict()
			if month not in self.__Data["data"][year].keys(): self.__Data["data"][year][month] = dict()
			if day not in self.__Data["data"][year][month].keys():
				if type == "str":
					self.__Data["data"][year][month][day] = dict([("type",f"{type}"), ("value",f"{value}")])
				if type == "int":
					self.__Data["data"][year][month][day] = dict([("type",f"{type}"), ("value", value)])

			# Сохранение файла json.
			self.__Save()

	def GetData(self, date: date) -> any:
		
		# Форматирование даты.
		year, month, day = self.__Format(date)

		# Получение значения словаря на выбранную дату.
		try:
			Value = self.__Data["data"][year][month][day]["value"] 
		except KeyError:
			Value = ""
		
		return Value
	
	def RemoveData(self, date: date):
			
		# Форматирование даты.
		year, month, day = self.__Format(date)
		print(self.__Data)

		# Если значение в ряду не существует.
		if self.__CheckUp(year, month, day):
		
			# Запись значения в ряд.
			if year not in self.__Data["data"].keys(): self.__Data["data"][year] = dict()
			print(self.__Data)
			if month not in self.__Data["data"][year].keys(): self.__Data["data"][year][month] = dict()
			print(self.__Data)
			if day in self.__Data["data"][year][month].keys(): del self.__Data["data"][year][month][day]
			print(self.__Data)

			# Сохранение файла json.
			self.__Save()
	
	def ReplaceData(self, type: str, value: any, date: date):

		# Форматирование даты.
		year, month, day = self.__Format(date)
		
		# Если значение в ряду существует.
		if self.__CheckUp(year, month, day):
			input(type)
			# Замена значения в ряду.
			if type == "str":
				self.__Data["data"][year][month][day] = dict([("type",f"{type}"), ("value",f"{value}")])
			if type == "int":
				self.__Data["data"][year][month][day] = dict([("type",f"{type}"), ("value", value)])

			# Сохранение файла json.
			self.__Save()

	def GetSegment(self, startdate: date, enddate: date)-> dict:

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
		for datekey, values in AllValues.items():
			if startdate <= datekey and enddate >= datekey:
				# Запись в словарь.
				Segment[datekey] = values

		OrderedSegment = OrderedDict(sorted(Segment.items()))
		
		return OrderedSegment
	
	def SetNameColor(self, key: str, value: str):
		self.__Data[key] = value

		# Сохранение файла json.
		self.__Save()

	def SetDescription(self, key: str, value: str):
		self.__Data["description"][key] = value

		# Сохранение файла json.
		self.__Save()

	def SetMetaInfo(self, key: str):

		year, month, day = self.__Format(date.today())

		self.__Data["metainfo"][key] = str(f"{year}-{month}-{day}")

		# Сохранение файла json.
		self.__Save()

	def GetSettings(self, path: str) -> str:
		
		Count = path.count("/")

		if Count == 0: Value = self.__Data[path]
		if Count == 1:
			Value1, Value2 = path.split("/")
			Value = self.__Data[Value1][Value2]

		return Value
