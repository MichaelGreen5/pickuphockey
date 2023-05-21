import os
import django
# from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickupsports.settings')



# Initialize Django settings
django.setup()




#checks if any events are ready for rosters to be sent. Then sends them
from OrgDash.models import Skate
# from django.utils import timezone
from django.db.models import Q
from datetime import timedelta, datetime
# Auto sending rosters on event day at user requested time
from OrgDash.tasks.finalize_rosters_auto import auto_finalize_rosters, auto_make_teams
now_utc = datetime.utcnow()
etime = now_utc - timedelta(hours=4)
todays_recurring_skates  = Skate.objects.filter(Q(recurring_event=True) & Q(date=now_utc.date()) & Q(auto_rosters_sent=False)).all()
for skate in todays_recurring_skates:
    skate_datetime = datetime.combine(skate.date, skate.time)
    action_time = skate_datetime - timedelta(hours=skate.finalize_event_hours_before)
    time_diff = action_time - etime
    if time_diff <= timedelta(minutes=15):
        print('its time')
        auto_make_teams(skate)
        auto_finalize_rosters(skate)
        skate.auto_rosters_sent=True
        skate.save()