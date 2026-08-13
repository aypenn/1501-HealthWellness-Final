from enum import Enum

class SleepQuality(Enum):
    Very_Poor = "Very Poor"
    Poor = "Poor"
    Fair = "Fair"
    Good = "Good"
    Excellent = "Excellent"

    def __str__(self):
        return str(self.value)