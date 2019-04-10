import requests
import json
a = input("Enter Mobile Number:")
c = input("Enter Country Code example IN , US :")
r = requests.get("http://apilayer.net/api/validate?access_key=34d427a1b1e25ce506f095860b7cfa68&number="+a+"&country_code="+c+"&format=1")
x = json.load(r.text)
b = x.get("location")
print ("Your Number Location is:" +b)
