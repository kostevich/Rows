#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from Source.Row import Row
import os

class Manager():
    
    def __init__(self) -> None:

        # Словарь рядов.
        self.__Rows = dict()

        # Получение словаря рядов.
        self.__InitializeRows()

    def __InitializeRows(self) -> None:
        """Инициализирует объектные представления существующих рядов."""

        # Получение списка файлов json.
        RowsID = self.GetRowsID()

        # Запись словаря значениями ID.
        for ID in RowsID:
            self.__Rows[ID] = Row(ID)

    def __GetFiles(self) -> list[str]:

        # Получение списка файлов в директории.
        Files = os.listdir("Data")
        # Фильтрация только файлов формата JSON.
        Files = list(filter(lambda List: List.endswith(".json"), Files))
        Files.sort()

        return Files
    
    def __GetFreeID(self) -> int:

        # Получение списка ID.
        RowsID = self.GetRowsID()

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

    def CreateRow(self) -> int:

        # Получение свободного ID.
        ID = self.__GetFreeID()

        # Запись ID.
        self.__Rows[ID] = Row(ID)

        return ID
    
    def DeleteRow(self, ID: int) -> None:

		# Сохранение ID файла, который требуется удалить.
        self.ID = ID

        # Удаление файла json.
        os.remove(f"Data/{self.ID}.json")
    
    def GetRow(self, ID) -> Row:
        return self.__Rows[ID]

    def GetRowsID(self) -> list[int]:

        # Получение списка файлов json.
        Files = self.__GetFiles()

        # Список ID.
        RowsID = list()

        # Для каждого файла получить ID.
        for File in Files: RowsID.append(int(File.replace(".json", "")))

        return RowsID