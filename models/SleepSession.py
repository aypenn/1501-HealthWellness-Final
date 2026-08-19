from datetime import datetime, date

from services import health_database


class SleepSession:
    def __init__(self, session_date: date, start_time:str, end_time: str, sleepquality: str, notes:str = "", id:int = 0) -> None:
        self.__session_date = session_date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__sleepquality = sleepquality
        self.__notes = notes
        self.__id = id

    def add_sleep_session(self):
        return health_database.add_sleep_session(self.session_date(), self.start_time(), self.end_time(), self.sleep_quality(), self.notes())

    # getters

    def id(self):
        return self.__id

    def session_date(self):
        return self.__session_date

    def sleep_quality(self):
        return self.__sleepquality

    def start_time(self):
        return self.__start_time

    def end_time(self):
        return self.__end_time

    def quality(self):
        return self.__quality

    def session_date(self):
        return self.__session_date

    def notes(self):
        return self.__notes

    # setters

    def set_start_time(self, start_time: datetime):
        self.__start_time = start_time

    def set_end_time(self, end_time: datetime):
        self.__end_time = end_time

    def set_quality(self, quality: str):
        print("in set_quality: " + str(quality))
        self.__sleepquality = quality

    def set_notes(self, notes: str):
        self.__notes = notes

    def __str__(self) -> str:
        return "Id: " + str(self.__id) + " Quality: " + str(self.__sleepquality) + " Start Time: " + str(self.__start_time) + " End Time: " + str(self.__end_time)