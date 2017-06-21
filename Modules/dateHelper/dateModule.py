import time,datetime


def getWeekName(weekday):
    weeknames = {
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Firday",
        "6": "Saturday",
        "0": "Sunday",
    }
    return weeknames.get(weekday)


def getDayOfWeek(dateStr):
    tempDate = time.strptime(dateStr, "%Y-%m-%d")
    return getWeekName(time.strftime("%w", tempDate))