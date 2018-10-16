import requests
import os

address = 'https://kephiso.webuntis.com/WebUntis/Ical.do?elemType=4&elemId=200&rpt_sd=2018-10-15'
file = 'S042.ics'


def downloadical(url, filename):
    print('Beginning file download...')
    cookie = {'schoolname': '_b3RoLXJlZ2Vuc2J1cmc='}
    r = requests.get(url, cookies=cookie)

    with open('temp/' + filename, 'wb') as f:
        f.write(r.content)

    if r.headers['content-type'] == 'image/jpeg':
        print('Download erfolgreich')


def deletefile(filename):
    try:
        os.remove('temp/' + filename)
        print("File removed")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


downloadical(address, file)
# deletefile(file)



