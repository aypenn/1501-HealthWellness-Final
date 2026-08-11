from datetime import datetime, date


class SleepSession:
    def __init__(self, session_date: date, start_time: datetime, end_time: datetime, sleepquality: str, notes:str = "", id:int = 0) -> None:
        self.__session_date = session_date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__sleepquality = sleepquality
        self.__id = id
        self.__notes = notes

    def add_sleep_session(self, sleepsession: SleepSession):
        self.__sleepsession = sleepsession

    # getters

    def id(self):
        return self.__id

    def start_time(self):
        return self.__start_time

    def end_time(self):
        return self.__end_time

    def quality(self):
        return self.__quality

    def notes(self):
        return self.__notes

    # setters

    def set_start_time(self, start_time: datetime):
        self.__start_time = start_time

    def set_end_time(self, end_time: datetime):
        self.__end_time = end_time

    def set_quality(self, quality: str):
        self.__quality = quality

    def set_notes(self, notes: str):
        self.__notes = notes




    def __str__(self) -> str:
        return "Id: " + str(self.__id) + " Quality: " + str(self.__quality) + " Start Time: " + str(self.__start_time) + " End Time: " + str(self.__end_time)