from huey.contrib.djhuey import task
from pickuphockey.models import Skate
from huey import RedisHuey
from huey import crontab


huey = RedisHuey()


@task()
def bingbong():
    print('bingbong')


bingbong.schedule(delay=5)


@task()
def create_next_skate(skate_obj):
    skate_data = skate_obj.get_next_skate_info()
    next_skate = Skate(**skate_data)
    next_skate.save()


skates=Skate.objects.all()
for skate in skates:
    if skate.recurring_event:
        create_next_skate(skate)
    









