from dublib.CLI.Terminalyzer import Command, Terminalyzer, NotEnoughParameters, ParametersTypes, ParsedCommandData
from dublib.Methods.System import Cls
from Source.Manager import Manager
from Source.Row import Row
from Graphics.Painter import Painter
from prettytable import PrettyTable
import readline
import shlex
import webbrowser

class Interpretator():
	def __init__(self) -> None:

		self.__manager = Manager()
		self.__painter = Painter()
		self.__AddCommands()

	def __AddCommands(self)-> list:

		CommandsList = list()

		Com = Command("exit", "Выход из скрипта.")
		CommandsList.append(Com)

		Com = Command("clear", "Очистка консоли.")
		CommandsList.append(Com)

		Com = Command("createrow", "Создание нового ряда.")
		Com.add_flag("w", "Заполнение данных для нового ряда.")
		CommandsList.append(Com)

		Com = Command("deleterow", "Удаление ряда.")
		Com.add_argument(ParametersTypes.Number, "ID ряда.", important=True)
		CommandsList.append(Com)

		Com = Command("listrows", "Вывод основных данных рядов в консоль.")
		CommandsList.append(Com)

		Com = Command("set", "Добавление данных для ряда.")
		Com.add_argument(ParametersTypes.Number, "ID ряда.", important=True)
		ComPos = Com.create_position(important=True)
		ComPos.add_key("name", "Имя ряда")
		ComPos.add_key("color", "Цвет ряда.")
		ComPos.add_key("description", "Описание ряда.")
		CommandsList.append(Com)

		Com = Command("add", "Добавление значения в ряд.")
		Com.add_argument(ParametersTypes.Number, "ID ряда", important = True)
		Com.add_key("day", ParametersTypes.Date, "Дата, для которой присваивается значение.", important = True)
		Com.add_key("value", ParametersTypes.All, "Значение.", important = True)
		CommandsList.append(Com)

		Com = Command("remove", "Удаление значения в ряду.")
		Com.add_argument(ParametersTypes.Number, "ID ряда", important = True)
		Com.add_key("day", ParametersTypes.Date, "Дата, для которой удаляется значение.", important = True)
		CommandsList.append(Com)

		Com = Command("build", "Построение таблицы.")
		Com.add_argument(ParametersTypes.Number, "ID ряда",  important = True)
		Com.add_key("sday", ParametersTypes.Date, "Дата, с которой начинается построение ряда",  important = True)
		Com.add_key("eday", ParametersTypes.Date, "Дата, которой заканчивается построение ряда",  important = True)
		CommandsList.append(Com)

		return CommandsList
	
	def __HandlerCommandLine(self, ParsedCommand: ParsedCommandData) -> None:
		if "exit" in ParsedCommand.name:
			exit(0)
		
		if "clear" in ParsedCommand.name:
			Cls()

		if "createrow" in ParsedCommand.name:
			ID = self.__manager.CreateRow()
			if ParsedCommand.check_flag("w") == True:
				row = self.__manager.GetRow(ID)
				data = row.GetTemplateExpressions("Templates/start.txt")				
		
		if "deleterow" in ParsedCommand.name:
			self.__manager.DeleteRow(ParsedCommand.arguments[0])

		if "listrows" in ParsedCommand.name:
			
			mytable = PrettyTable()
			mytable.border = False
			Data = {
					"ID": [],
					"Name": [],
					"Description": [],
					"Last_update": [],
			}

			for Id in self.__manager.GetRowsID():
				Data["ID"].append(self.__manager.GetRow(Id).ID)
				Data["Name"].append(self.__manager.GetRow(Id).name)
				Data["Description"].append(self.__manager.GetRow(Id).description)
				Data["Last_update"].append(self.__manager.GetRow(Id).update_date)
				
			for ColumnName in Data.keys():
				mytable.add_column(ColumnName, Data[ColumnName])

			print(mytable)

		if "set" in ParsedCommand.name:
			if "name" in ParsedCommand.keys: key = "name"
			if "description" in ParsedCommand.keys: key = "description"

			id = int(ParsedCommand.arguments[0])
			value = ParsedCommand.keys[key]
			row = self.__manager.GetRow(id)
			row.SetNameDescription(key, value)

		if "add" in ParsedCommand.name:
			id = int(ParsedCommand.arguments[0])
			day = ParsedCommand.keys["day"]
			value = ParsedCommand.keys["value"]
			typevalue = type(value).__name__
			if value.isdigit(): typevalue = "int"
			try:
				row = self.__manager.GetRow(id)
				Value = row.GetData(day)
				if Value:
					row.ReplaceData(typevalue, value, day)
				else:
					row.SetData(typevalue, value, day)
			except KeyError:
				print("Такого ряда не существует.")

		if "remove" in ParsedCommand.name:
			id = int(ParsedCommand.arguments[0])
			day = ParsedCommand.keys["day"]
			try:
				row = self.__manager.GetRow(id)
				row.RemoveData(day)
			except KeyError:
				print("Такого ряда не существует.")

		if "build" in ParsedCommand.name:
			id = int(ParsedCommand.arguments[0])
			row = self.__manager.GetRow(id)
			sday = ParsedCommand.keys["sday"]
			eday = ParsedCommand.keys["eday"]
			if self.__painter.DataSChart(row, sday, eday):
				webbrowser.open_new_tab(f'SimpleChart_{id}.html')

	def Run(self) -> None:
		while True:
			CommandLine = input("->")
			CommandLine = CommandLine.strip()
			CommandLine = shlex.split(CommandLine) if len(CommandLine) > 0 else [""]

			try:
				ParsedCommand = Terminalyzer(CommandLine).check_commands(self.__AddCommands())
				if ParsedCommand != None:
					self.__HandlerCommandLine(ParsedCommand)
				else:
					print("Команда не найдена.")

			except FileNotFoundError:
				print("Этот ряд был удалён.")
			
			except NotEnoughParameters:
				print("Недостаточно аргументов в команде.")