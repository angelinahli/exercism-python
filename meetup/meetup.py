from calendar import day_name, monthcalendar
from datetime import date

class MeetupDayException(Exception):
    pass

def meetup_day(year, month, weekday, day_pos):
    """
    year and month are ints
    weekday amd day_pos are strings
    """

    # reference calendar
    month_cal_array = monthcalendar(year, month)

    # grab all matching weekdays in month
    wkday_index = list(day_name).index(weekday)
    weekdays_in_month = [week[wkday_index] for week in month_cal_array if week[wkday_index] != 0]

    if day_pos == 'teenth':
        teenth_days = range(13,20)
        day = filter(lambda day: day in teenth_days, weekdays_in_month)[0]

    else:
        # convert day_pos into an index of weekdays_in_month
        day_pos = day_pos[0]
        pos_index = int(day_pos)-1 if day_pos.isdigit() else -1

        if len(weekdays_in_month) < pos_index+1:
            raise MeetupDayException
        else:
            day = weekdays_in_month[pos_index]

    return date(year, month, day)

