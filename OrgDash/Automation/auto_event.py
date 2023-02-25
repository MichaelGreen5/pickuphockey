from django.utils import timezone
import datetime

def how_long_till_next_event(weeks=0, days=0, hours=0, minutes=0):
    delta = datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes)
    current_event_time = datetime.date.today()
    next_date = current_event_time + delta
    formatted = next_date.strftime('%Y-%m-%d %H:%M:%S')



    return("Next event will be" + formatted)



print(how_long_till_next_event(weeks=1))



