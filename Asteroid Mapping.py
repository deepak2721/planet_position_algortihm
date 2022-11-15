
import numpy
import requests

api_url = "https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=8Ser8hk2aPrIsmyIgqgpJDInI9WIBr8xfiUbkbsl"

api_url2 = "https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=8Ser8hk2aPrIsmyIgqgpJDInI9WIBr8xfiUbkbsl"

r = requests.get(api_url2)
data = r.json()

print((data))
