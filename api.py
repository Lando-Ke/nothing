from xml.dom import minidom
import json
from pprint import pprint

f = open('pets.txt', 'r')



pets = json.loads(f.read())
f.close()

pprint(pets)