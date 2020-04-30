import requests
import numpy

r = requests.get('https://xkcd.com/353/')

print(r) #Gives us a 200 response, which means everything is okay1

print(help(r)) #Gives us some information on methods and attributes of r

print(r.text)