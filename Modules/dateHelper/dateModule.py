import datetime


def getWeekName(weekday):
    weeknames = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Firday",
        6: "Saturday",
        7: "Sunday",
    }
    return weeknames.get(weekday)


def getDayOfWeek(year, month, day):
    tempDate = datetime.date(year, month, day)
    return getWeekName(tempDate.weekday() + 1)