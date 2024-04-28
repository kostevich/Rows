#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from Row import Row
import os

class Manager():
    
    def __init__(self):

        # Словарь рядов.
        self.__Rows = dict()

        # Получение словаря рядов.
        self.__GetDictRows()

    def __GetDictRows(self):
        """ Запись словаря, где ключ - ID; значение - объект Rows."""

        # Получение списка файлов json.
        RowsID = self.__GetRowsID()

        # Запись словаря значениями ID.
        for ID in RowsID:
            self.__Rows[ID] = Row(ID)

    def __GetFiles(self) -> list[str]:

        # Получение списка файлов в директории.
        Files = os.listdir("Data")
        # Фильтрация только файлов формата JSON.
        Files = list(filter(lambda List: List.endswith(".json"), Files))

        return Files

    def __GetRowsID(self) -> list[int]:

        # Получение списка файлов json.
        Files = self.__GetFiles()

        # Список ID.
        RowsID = list()

        # Для каждого файла получить ID.
        for File in Files: RowsID.append(int(File.replace(".json", "")))

        return RowsID

    def CreateRow(self):

        # Получение свободного ID.
        ID = self.__GetFreeID()

        # Запись ID.
        self.__Rows[ID] = Row(ID)

    def __GetFreeID(self):

        # Получение списка ID.
        RowsID = self.__GetRowsID()

        # Получение списка файлов json.
        Files = self.__GetFiles()

        # Если файлы существуют.
        if Files != []:

            # ID нового ряда.
            ID = None 

            # Для каждого числа до максимального ID.
            for Index in range(1, max(RowsID) + 1):

                # Если число не используется в качестве ID.
                if Index not in RowsID:
                    # Присвоение ID.
                    ID = Index
                    # Остановка цикла.
                    break

            # Если свободный ID не определён, назначить новый инкрементом.
            if not ID: ID = max(RowsID) + 1

        else: ID = 1

        return ID
    
    def RemoveRow(self, ID):

		# Сохранение ID файла, который требуется удалить.
        self.ID = ID

        # Удаление файла json.
        os.remove(f"Data/{self.ID}.json")
 
