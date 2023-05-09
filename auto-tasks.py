import os
import django
# from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickupsports.settings')



# Initialize Django settings
django.setup()

#Duplicating recurring events
from OrgDash.tasks.event_repeat import duplicate_event
duplicate_event()

# Auto sending invites on user requested date
from OrgDash.models import Skate
from django.utils import timezone
from django.db.models import Q
from OrgDash.tasks.send_invites_auto import auto_send_invites

today= timezone.now().date()
from datetime import timedelta
future_recurring_skates = Skate.objects.filter(Q(recurring_event=True) & Q(date__gte=today) & Q(auto_invites_sent=False)).all()
for skate in future_recurring_skates:
    send_invite_date = skate.date - timedelta(days = skate.send_invite_days_before)
    if send_invite_date == today:
        auto_send_invites(skate)
        skate.auto_invites_sent = True
        skate.save()

