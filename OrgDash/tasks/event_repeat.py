def duplicate_event():
    from OrgDash.models import Skate
    from django.utils import timezone
    from django.db.models import Q
    today= timezone.now().date()
    

    past_recurring_skates = Skate.objects.filter(Q(recurring_event=True) & Q(date__lt=today) & Q(already_duplicated=False))
    for skate in past_recurring_skates:
        skate_data = skate.get_next_skate_info()
        next_skate = Skate(**skate_data)
        next_skate.save()
        skate.already_duplicated = True
        skate.save()
    



