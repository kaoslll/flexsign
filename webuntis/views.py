from django.shortcuts import render
from .models import Room
from .models import Event
from django.utils import timezone


# Create your views here.
def test(request):
    rooms = Room.objects.filter(name__contains='S042')
    return render(request, 'webuntis/test.html', {'rooms': rooms})


def cal(request):
    roomsel = Room.objects.get(name__contains='S042')
    monday = Event.objects.filter(room=roomsel,
                                  dtstart__day=get_day_of_actual_monday()+0)
    return render(request, 'webuntis/caltest.html', {'roomsel': roomsel, 'monday': monday})




def get_day_of_actual_monday():
    date = timezone.now() - timezone.timedelta(timezone.now().isoweekday() % 7) + timezone.timedelta(1)
    return date.day

