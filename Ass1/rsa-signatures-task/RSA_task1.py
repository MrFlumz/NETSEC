
import requests
url = "http://127.0.0.1:5000/"


while True:
    print(2)


s = requests.Session()
resp1 = s.get(url)
#print(resp1.headers)
auth = resp1.cookies.get('grade')

print('auth: '+str(auth))