import requests
from requests.auth import HTTPBasicAuth

username = 'carletonuniversity_namakamalesh_lavesh'
password = 'l7bI01rHdw4bN4pCHk3K'
url = "https://api.meteomatics.com/2025-08-07T00:00:00Z/t_2m:C/52.520551,13.461804/html"

response = requests.get(url,auth=HTTPBasicAuth(username,password))

print(response.text)

