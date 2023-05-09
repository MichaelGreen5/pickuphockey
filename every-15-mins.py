from OrgDash.models import Skate
from django.utils import timezone
from django.db.models import Q
from datetime import timedelta, datetime
# Auto sending rosters on event day at user requested time
from OrgDash.tasks.finalize_rosters_auto import auto_finalize_rosters, auto_make_teams
now_utc = datetime.utcnow()
todays_recurring_skates  = Skate.objects.filter(Q(recurring_event=True) & Q(date=now_utc.date()) & Q(auto_rosters_sent=False)).all()
for skate in todays_recurring_skates:
    skate_datetime = datetime.combine(skate.date, skate.time)
    action_time = skate_datetime - timedelta(hours=skate.finalize_event_hours_before)
    time_diff = action_time - now_utc
    if time_diff <= timedelta(minutes=15):
        auto_make_teams(skate)
        auto_finalize_rosters(skate)
        skate.auto_rosters_sent=True
        skate.save()