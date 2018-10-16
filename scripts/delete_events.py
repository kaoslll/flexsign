from webuntis.models import Event

"""
Dieses Scipt führt man am besten über die Konsole aus.
    python manage.py runscript delete_events
"""


def run():
    Event.objects.all().delete()
    print('Alle Events wurden gelöscht')



