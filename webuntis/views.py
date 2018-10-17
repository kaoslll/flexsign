from django.shortcuts import render
from .models import Room


# Create your views here.
def test(request):
    rooms = Room.objects.filter(name__contains='S042')
    return render(request, 'webuntis/test.html', {'rooms': rooms})


def cal(request):
    return render(request, 'webuntis/cal.html', {})
