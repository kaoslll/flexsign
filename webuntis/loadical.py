import requests
import os

address = 'https://www.oth-regensburg.de/typo3conf/ext/hsregensburg/Resources/Public/Images/oth-regensburg-logo.jpg'
file = 'logo.jpg'


def downloadical(url, filename):
    print('Beginning file download...')

    r = requests.get(url)

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



