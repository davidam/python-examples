
import requests

fichero = open("namsorpass.txt", "r+")
contenido = fichero.readline().rstrip()

name = 'David'
surname = 'Arroyo'
url = 'https://v2.namsor.com/NamSorAPIv2/api2/json/gender/'
url = url + name + '/' + surname
payload = open("request.json")
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'X-API-KEY': contenido}
r = requests.get(url, data=payload, headers=headers)
print(r.json)
print(r.text)
print(payload)
