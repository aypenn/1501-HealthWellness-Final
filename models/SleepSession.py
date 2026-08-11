from datetime import datetime


class SleepSession:
    def __init__(self, start_time: datetime, end_time: datetime, quality: str, id:int = 0) -> None:
        self.__start_time = start_time
        self.__end_time = end_time
        self.__quality = quality
        self.__id = id

    def __str__(self) -> str:
        return "Id: " + str(self.__id) + " Quality: " + str(self.__quality) + " Start Time: " + str(self.__start_time) + " End Time: " + str(self.__end_time)