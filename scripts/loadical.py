import os
from webuntis.models import Room
from webuntis.models import Event
import requests
from icalendar import Calendar

"""
Dieses Scipt führt man am besten über die Konsole aus.
    python manage.py runscript loadical
"""


def run():
    myroom = 'S042'
    print('Suche Raum ' + myroom + ' in der Datenbank.')

    r1 = Room.objects.get(name__contains=myroom)

    if r1 is not None:
        print('Raum ' + myroom + ' gefunden!')
        address = getattr(r1, 'url')
        myfile = getattr(r1, 'name') + '.ics'
        print('URL: ' + address)
        print('Erzeuge Cache Datei: ' + myfile)
        downloadical(address, myfile)
        readical(myfile, r1)
        deletefile(myfile)

    else:
        print('Raum nicht gefunden.')
        print('Abbruch!')


def downloadical(url, filename):
    print('Beginning file download...')
    cookie = {'schoolname': '_b3RoLXJlZ2Vuc2J1cmc='}
    r = requests.get(url, cookies=cookie)

    temp_dir = os.path.dirname(os.path.dirname(__file__))
    temp_dir = os.path.join(temp_dir, "webuntis", "temp")
    file_path = os.path.join(temp_dir, filename)

    with open(file_path, 'wb') as f:
        f.write(r.content)

    print(file_path + ' wurde erfolgreich geschrieben')
    print(' ')


def deletefile(filename):
    temp_dir = os.path.dirname(os.path.dirname(__file__))
    temp_dir = os.path.join(temp_dir, "webuntis", "temp")
    file_path = os.path.join(temp_dir, filename)

    try:
        os.remove(file_path)
        print("Cache Datei " + filename + " wurde erfolgreich gelöscht.")
        print(' ')
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def readical(filename, room):
    temp_dir = os.path.dirname(os.path.dirname(__file__))
    temp_dir = os.path.join(temp_dir, "webuntis", "temp")
    file_path = os.path.join(temp_dir, filename)

    icsfile = open(file_path, 'rb')
    gcal = Calendar.from_ical(icsfile.read())

    for event in gcal.walk('vevent'):
        start = event.get('dtstart').dt
        summary = event.get('summary')
        end = event.get('dtend').dt
        # timestamp = event.get('dtstamp').dt

        print(start)
        print(summary)
        print(end)
        # print(timestamp)
        # print(' ')
        eventexist = searchevents(room, start, end, summary)
        if eventexist:
            eventsave(room, start, end, summary)

        print(' ')

    icsfile.close()


def searchevents(room, start, end, summary):
    query = Event.objects.filter(room=room,
                                 summary__exact=summary,
                                 dtstart__exact=start,
                                 dtend__exact=end)

    if not query:
        print('Eintrag muss erstellt werden')
        return True
    else:
        print('Eintrag existiert bereits')
        return False


def eventsave(room, start, end, summary):
    act = Event(dtstart=start, dtend=end, summary=summary, room=room)
    act.save()
    print('neues Event wurde angelegt')



