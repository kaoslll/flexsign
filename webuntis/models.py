from django.db import models

"""
Class Room
 alle Räume, welche abgesucht werden
"""

"""
Class Event
 alle Events, die zwischengespeichert werden.
"""


class Room(models.Model):
    name = models.CharField("Raumbezeichnung nach WebUntis", max_length=30, unique=True)
    url = models.URLField("Webuntis URL", max_length=300)
    dtchanged = models.DateTimeField("Letzte Änderung", null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    dtstart = models.DateTimeField("Startzeit")
    dtend = models.DateTimeField("Endzeit")
    summary = models.CharField("Kalendereintrag", max_length=250)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.summary





