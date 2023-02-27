import requests

request = requests.get('https://ident.me')
ip_publica = request.text
print(ip_publica)


import public_ip as ip

ip_publica_2 = ip.get()
print(ip_publica_2)
