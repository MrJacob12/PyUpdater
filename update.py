import requests
from zipfile import ZipFile
import os

url = ''
r = requests.get(url, allow_redirects=True)
print(r.headers.get('content-type'))

if r.headers.get('content-type') == "application/zip":
    try:
        print('Downloading ...')
        open('update.zip','wb').write(r.content)
        with ZipFile('update.zip', 'r') as zipObj:
            zipObj.extractall()
    except:
        print('Something went wrong, try again later.')


os.remove('update.zip')