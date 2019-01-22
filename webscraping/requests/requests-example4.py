import requests

r1 = requests.get('https://api.github.com/events')
print("############## r1 = requests.get('https://api.github.com/events')")
print(r1.text)
r2 = requests.post('https://httpbin.org/post', data = {'key':'value'})
print("############## r2 = requests.post('https://httpbin.org/post', data = {'key':'value'})")
print(r2.text)

r3 = requests.put('https://httpbin.org/put', data = {'key':'value'})
print("############## r3 = requests.put('https://httpbin.org/put', data = {'key':'value'})")
print(r3.text)

r4 = requests.delete('https://httpbin.org/delete')
print("############### r4 = requests.delete('https://httpbin.org/delete')")
print(r4.text)


r5 = requests.head('https://httpbin.org/get')
print("############### r5 = requests.head('https://httpbin.org/get')")
print(r5.text)

r6 = requests.options('https://httpbin.org/get')
print("############### r6 = requests.options('https://httpbin.org/get')")
print(r6.text)
