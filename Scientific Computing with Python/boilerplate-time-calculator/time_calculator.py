def add_time(start_time, duration, start_day=None):
    start_hour, start_minute_period = start_time.split(':')
    start_minute, period = start_minute_period.split()
    start_hour, start_minute = int(start_hour), int(start_minute)

    duration_hour, duration_minute = map(int, duration.split(':'))

    if period == 'PM' and start_hour != 12:
        start_hour += 12

    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute

    if end_minute >= 60:
        end_minute -= 60
        end_hour += 1

    days_later = end_hour // 24
    end_hour %= 24

    if end_hour > 12:
        end_hour -= 12
        period = 'PM'
    elif end_hour == 12:
        period = 'PM'
    else:
        period = 'AM'

    days_of_week = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]

    if start_day:
        start_day_index = days_of_week.index(start_day.lower().capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        day_output = f", {new_day}"
    else:
        day_output = ""

    if (end_hour == 0):
        end_hour = 12
    
    if days_later == 0:
        result = f"{end_hour}:{str(end_minute).zfill(2)} {period}{day_output}"
    elif days_later == 1:
        result = f"{end_hour}:{str(end_minute).zfill(2)} {period}{day_output} (next day)"
    else:
        result = f"{end_hour}:{str(end_minute).zfill(2)} {period}{day_output} ({days_later} days later)"

    return result