from django.utils import timezone

from models import Skate
from OrgDash.models import AutoRecurringSkate
import datetime

def how_long_till_next_event(weeks=0, days=0, hours=0, minutes=0):
    delta = datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes)
    current_event_time = datetime.date.today()
    next_date = current_event_time + delta
    formatted = next_date.strftime('%Y-%m-%d %H:%M:%S')



    return("Next event will be" + formatted)



print(how_long_till_next_event(weeks=1))


'host','date', 'time', 'location', 'price', 'max_guests', 'recurring_event'
today=timezone.now()
all_recurring_events = AutoRecurringSkate.objects.filter(event__date__gte=today)
for event in all_recurring_events:
    next_date = event.next_skate_date()
    print(next_date)



def create_next_skate(AutoRecurringSkate, timedelta):
    current_skate = AutoRecurringSkate.event
    skate_data = {k: v for k, v in vars(current_skate).items()}
    skate_data['date'] += timedelta
    next_skate = Skate(**skate_data)
    # next_skate.save()




