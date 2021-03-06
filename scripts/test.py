from webuntis.models import Room
from webuntis.models import Event
from django.utils import timezone


def run():

    roomsel = Room.objects.get(name__contains='S042')
    monday = Event.objects.filter(room=roomsel,
                                  dtstart__day=get_day_of_actual_monday()+0)
    thuesday = Event.objects.filter(room=roomsel,
                                    dtstart__day=get_day_of_actual_monday()+1)
    wednesday = Event.objects.filter(room=roomsel,
                                     dtstart__day=get_day_of_actual_monday()+2)
    thursday = Event.objects.filter(room=roomsel,
                                    dtstart__day=get_day_of_actual_monday()+3)
    friday = Event.objects.filter(room=roomsel,
                                  dtstart__day=get_day_of_actual_monday()+4)

    print(monday[0])
    print(monday[0].dtstart)
    print(monday[0].dtend)

    # print(timezone.template_localtime(monday[0].dtstart, use_tz='Europe/Berlin'))



def get_day_of_actual_monday():
    date = timezone.now() - timezone.timedelta(timezone.now().isoweekday() % 7) + timezone.timedelta(1)
    return date.day

