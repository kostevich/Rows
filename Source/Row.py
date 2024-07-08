#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods.JSON import WriteJSON, ReadJSON
from collections import OrderedDict
from datetime import datetime
import os

class Row():

	@property
	def name(self) -> str:
		return self.GetSettings("name")
		
	@property
	def creation_date(self)-> str:
		return self.GetSettings("metainfo/creation_date")
	
	@property
	def update_date(self)-> str:
		return self.GetSettings("metainfo/update_date")
	
	@property
	def description(self) -> str:
		return self.GetSettings("description")
	
	def __init__(self, ID: int) -> None:

		# Форматирование даты.
		year, month, day = self.__FormatDate(datetime.now())

		# Данные ряда.
		self.__Data = {
			"name": None,
			"description": None,
			"metainfo": {
			"creation_date": f"{year}-{month}-{day}",
				"update_date": None,
			},
			"data": {}
	}	
		# Получение ID ряда.
		self.ID = ID

		# Если файл JSON для ряда существует - чтение его.
		if os.path.exists(f"Data/{self.ID}.json"): self.__Data = ReadJSON(f"Data/{self.ID}.json")

		# Если нет - запись JSON.
		else: self.__Save(False)

	def __CheckUp(self, year: str, month: str, day: str) -> bool:

		# Значение по умолчанию.
		IsExists = False

		# Проверка: существует ли значение в ряде.
		if year in self.__Data["data"].keys():
			if month in self.__Data["data"][year].keys():
				if day in self.__Data["data"][year][month].keys(): IsExists = True

		return IsExists

	def __FormatDate(self, date: datetime) -> str:
		"""Форматирует datetime в набор строковых величин.
		Year - строковое представление четырёхзначного число.
		Month - строковое представление двухзначного числа.
		Day - строковое представление двухзначного числа."""

		Year = date.strftime("%Y")
		Month = date.strftime("%m")
		Day = date.strftime("%d")
		
		return Year, Month, Day
	
	def __FormatTime(self, time: datetime) -> str:

		Hour = time.strftime("%H")   
		Minutes = time.strftime("%M")
		Seconds = time.strftime("%S")
		
		return Hour, Minutes, Seconds
	
	def __Standart(self, year: str, month: str, day: str) -> datetime:
		"""Форматирует строковое прредставление в date."""

		Date = datetime(int(year), int(month), int(day))
		
		return Date

	def __Save(self, update: bool = True) -> None:
		if update == True: 

			year, month, day = self.__FormatDate(datetime.now())
			hour, minutes, seconds = self.__FormatTime(datetime.now())
			self.__Data["metainfo"]["update_date"] = (f"{year}-{month}-{day} {hour}:{minutes}:{seconds}")

		# Сохранение файла json.
		WriteJSON(f"Data/{self.ID}.json", self.__Data)

	def SetData(self, type: str, value: any, date: datetime)-> None:

		# Форматирование даты.
		year, month, day = self.__FormatDate(date)

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

	def GetData(self, date: datetime) -> any:
		
		# Форматирование даты.
		year, month, day = self.__FormatDate(date)

		# Получение значения словаря на выбранную дату.
		try:
			Value = self.__Data["data"][year][month][day]["value"] 
		except KeyError:
			Value = ""
		
		return Value
	
	def RemoveData(self, date: datetime)-> None:
			
		# Форматирование даты.
		year, month, day = self.__Format(date)

		# Если значение в ряду существует.
		if self.__CheckUp(year, month, day)== True:
			if day not in self.__Data["data"][year][month][day].keys(): del self.__Data["data"][year][month][day]

			if not self.__Data["data"][year][month]: del self.__Data["data"][year][month]

			if not self.__Data["data"][year]: del self.__Data["data"][year]
			
			# Сохранение файла json.
			self.__Save()
	
		else: print("Такой даты не существует")

	def ReplaceData(self, type: str, value: any, date: datetime)-> None:

		# Форматирование даты.
		year, month, day = self.__FormatDate(date)
		
		# Если значение в ряду существует.
		if self.__CheckUp(year, month, day):

			# Замена значения в ряду.
			if type == "str":
				self.__Data["data"][year][month][day] = dict([("type",f"{type}"), ("value",f"{value}")])
			if type == "int":
				self.__Data["data"][year][month][day] = dict([("type",f"{type}"), ("value", value)])

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
		for datekey, values in AllValues.items():
			if startdate <= datekey and enddate >= datekey:
				# Запись в словарь.
				Segment[datekey] = values

		OrderedSegment = OrderedDict(sorted(Segment.items()))
		
		return OrderedSegment
	
	def SetNameDescription(self, key: str, value: str)-> None:
		self.__Data[key] = value

		# Сохранение файла json.
		self.__Save()

	def SetMetaInfo(self, key: str)-> None:

		year, month, day = self.__Format(datetime.now())

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



