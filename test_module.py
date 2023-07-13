import unittest
from time_calculator import add_time
from time_calculator import add_day
from time_calculator import add_date


def add_date(added_day):

    if added_day == 1:
        return '(next day)'
    elif added_day > 1:
        return f'({added_day} days later)'
    else:
        return ''

def add_day(added_day, current_day):
    day = current_day[0].upper() + current_day[1:].lower()
    week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    key_day = [i for i in week if week[i] == day][0]

    while added_day > 0:
        key_day += 1
        added_day -= 1
        if key_day == 7:
            key_day = 0
    return week.get(key_day)
    
def add_time(current_time, increment, days=False):

    time = current_time.split(" ")
    indicator = time[1]
    hour, minute = time[0].split(":")
    hour = int(hour)
    minute = int(minute)
    
    add_hour, add_minute = increment.split(":")
    add_hour = int(add_hour) * 60
    add_minute = int(add_minute) + add_hour

    increment_of_the_day = 0

    while add_minute > 0:
        add_minute -= 1
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 12:
                if indicator == "PM":
                    indicator = "AM"
                    increment_of_the_day +=1
                else:
                    indicator = "PM"
            if hour == 13:
                hour = 1

    
    if len(str(minute)) == 1:
        end_result = str(str(hour) + ":" + "0" + str(minute) + " " + indicator)
    else:
        end_result = str(str(hour) + ":" + str(minute) + " " + indicator)

    if days:
        day = add_day(increment_of_the_day ,days)
        end_result = end_result + f", {day.capitalize()}{add_date(increment_of_the_day)}"
    else:
        end_result = end_result + " " + add_date(increment_of_the_day)

    return end_result
