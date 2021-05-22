import requests

e="https://api.zippopotam.us/"
c=str(input("Enter your country:")).upper()
p = input("Enter your Pincode:")

response = requests.get(e+c+'/'+p)
#print(response)

info =response.json()
#print(info)
#print(info['places'][0])#['state'])
country=info['country']
#print(c)
state=info['places'][0]['state']
#print(s)
pin=info['places'][0]['place name']
print("Country:",country,"\nPlace Name:",pin,"\nState:",state)
