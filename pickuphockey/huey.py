from huey import RedisHuey
from huey import crontab
from pickuphockey.models import Skate

huey = RedisHuey()



@huey.periodic_task(crontab(hour="23", minute="4"))
def run_next_skate():
    skates=Skate.objects.all()
    # create_next_skate(skates)

run_next_skate()