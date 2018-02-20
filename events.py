#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import json
from datetime import datetime
from datetime import timedelta
import time

events = {}

day = datetime(2018,2,19)
lastMon = day + timedelta(days=84)

while day <= lastMon:
    for count in range(0,4):
        dayStr = str(day.date())
        if day.weekday() == 0 and day > datetime(2018,2,19):
            events[dayStr] = [{'time': '1:40PM - 3:40PM','location': "MBCC 125"}]

        elif day.weekday() == 1:
            events[dayStr] = []
            if day >= datetime(2018,2,20):
                events[dayStr].append({'time': '12:50PM - 2:50PM','location': "MBCC 134"})
            if day >= datetime(2018,4,3):
                events[dayStr].append({'time': '2:00PM - 5:00PM','location': "MBCC 138"})
            events[dayStr].append({'time': '5:50PM - 7:50PM','location': "MBCC 136"})

        elif day.weekday() == 2:
            events[dayStr] = [{'time': '12:00PM - 3:40PM','location': "MBCC 136"}]

        elif day.weekday() == 3:
            events[dayStr] = []
            if day > datetime(2018,2,22):
                events[dayStr].append({'time': '12:50PM - 2:50PM','location': "MBCC 134"})
            if day.weekday() == datetime(2018,3,8):
                events[dayStr].append({'time': '2:50PM - 5:50PM','location': "MBCC 138"})
            elif day <= datetime(2018,3,22):
                events[dayStr].append({'time': '2:50PM - 5:50PM','location': "MBCC 137"})
            events[dayStr].append({'time': '5:50PM - 7:50PM','location': "MBCC 125"})
        day += timedelta(days=1)

    day += timedelta(days=3)

print(json.dumps(events))
