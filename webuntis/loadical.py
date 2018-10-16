import requests

# https://www.oth-regensburg.de/typo3conf/ext/hsregensburg/Resources/Public/Images/oth-regensburg-logo.jpg

print('Beginning file download...')

url = 'https://www.oth-regensburg.de/typo3conf/ext/hsregensburg/Resources/Public/Images/oth-regensburg-logo.jpg'
r = requests.get(url)


with open('temp/logo.jpg', 'wb') as f:
    f.write(r.content)


print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)


if r.headers['content-type'] == 'image/jpeg':
    print('Download erfolgreich')






