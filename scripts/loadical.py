import os
from webuntis.models import Room
from webuntis.models import Event
import requests
from icalendar import Calendar

"""
Dieses Scipt führt man am besten über die Konsole aus.
    python manage.py runscript loadical
"""


class Icalevent:
    def __init__(self, dtstart, dtend, dtsummary):
        self.dtstart = dtstart
        self.dtend = dtend
        self.dtsummary = dtsummary


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
    print('Lese Datei')
    gcal = Calendar.from_ical(icsfile.read())

    time_last_change = None
    icallist = []
    writedb = False

    # Schreibe alle Werte in eine Liste -> schließe Datei
    print('Suche nach neuen Einträgen')
    for event in gcal.walk('vevent'):
        start = event.get('dtstart').dt
        summary = event.get('summary')
        end = event.get('dtend').dt
        icallist.append(Icalevent(start, end, summary))

    icsfile.close()

    # Überprüfe ob eine Änderung vorliegt
    for i in icallist:
        if searchevents(room, i.dtstart, i.dtend, i.dtsummary):
            # lösche Datenbank einträge und beende Überprüfung
            print('Neuer Eintrag gefunden')
            Event.objects.filter(room=room).delete()
            writedb = True
            break

    # Wenn eine Änderung ansteht ...
    if writedb:
        for i in icallist:
            time_last_change = eventsave(room, i.dtstart, i.dtend, i.dtsummary)
            # print("Folgender Eintrag wurde gespeichert:")
            # print(i)

        del icallist
        print('Neue Einträge wurden geschrieben')
        room.dtchanged = time_last_change
        room.save()
    else:
        print('Es gibt keine Neuigkeiten')


def searchevents(room, start, end, summary):
    query = Event.objects.filter(room=room,
                                 summary__exact=summary,
                                 dtstart__exact=start,
                                 dtend__exact=end)

    if not query:
        # print('Eintrag muss erstellt werden')
        return True
    else:
        # print('Eintrag existiert bereits')
        return False


def eventsave(room, start, end, summary):
    act = Event(dtstart=start, dtend=end, summary=summary, room=room)
    act.save()
    # print('neues Event wurde angelegt')
    return getattr(act, 'dtcreated')



