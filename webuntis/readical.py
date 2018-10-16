from icalendar import Calendar


filename = 'S042.ics'

icsfile = open('temp/' + filename, 'rb')
gcal = Calendar.from_ical(icsfile.read())

for event in gcal.walk('vevent'):
    start = event.get('dtstart')
    summary = event.get('summary')
    end = event.get('dtend')
    timestamp = event.get('dtstamp')

    print(start.dt)
    print(summary)
    print(end.dt)
    print(timestamp.dt)
    print(' ')


icsfile.close()










