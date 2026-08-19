import threading
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

import services.health_data as health_data
from models.DayEntity import *
from models.SleepQuality import SleepQuality
from services import health_database
from utils.input_utils import *

def read_xml_file():
    # xml_file = str(Path(__file__).parent) + "\\Meals_Workouts.xml"

    xml_file = str(Path(__file__).parent) + "\\Meals_Workouts_Sleep.xml"

    # print("xml_file = ", xml_file)

    # tree = ET.parse(r"C:\Data Files\Source\Repos\MCC\INFO 1501\Assignment 7\HealthWellness\services\Meals_Workouts.xml")
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # import meal data

    threads_meals = []
    threads_workouts = []
    threads_sleep = []

    sq = ["Very Poor", "Poor", "Fair", "Good", "Excellent"]

    for meal in root.findall("meal"):

        wk_date_str = meal.get("date")
        wk_date:date = datetime.strptime(wk_date_str, "%m/%d/%Y")

        desc = meal.find("description").text
        calories = meal.find("calories").text
        meal_type = meal.find("meal_type").text

        t = threading.Thread(target=health_database.add_meal, args=(wk_date, desc, meal_type, int(calories)))
        threads_meals.append(t)
        t.start()

    for t in threads_meals:
        t.join()


    for workout in root.findall("workout"):

        wk_date_str = workout.get("date")
        wk_date:date = datetime.strptime(wk_date_str, "%m/%d/%Y")

        desc = workout.find("description").text
        calories = workout.find("calories").text
        workout_type = workout.find("workout_type").text

        t = threading.Thread(target=health_database.add_workout, args=(wk_date, desc, workout_type, int(calories)))
        threads_meals.append(t)
        t.start()

    for t in threads_workouts:
            t.join()

    for sleep in root.findall("sleep"):
        wk_date_str = sleep.get("date")
        wk_date: date = datetime.strptime(wk_date_str, "%m/%d/%Y")

        start_time = sleep.find("start_time").text
        end_time = sleep.find("end_time").text
        sleep_quality = int(sleep.find("sleep_quality").text) - 1
        notes = sleep.find("notes").text

        t = threading.Thread(target=health_database.add_sleep_session,
                             args=(wk_date, start_time, end_time, sq[sleep_quality], notes))
        threads_sleep.append(t)
        t.start()

    for t in threads_workouts:
        t.join()
