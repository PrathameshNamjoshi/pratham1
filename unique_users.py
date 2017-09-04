import xml.etree.cElementTree as ET
import pprint
import re
def get_user(element):
     if "uid" in element.attrib:
        return element.attrib["uid"]


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
       users.add(get_user(element))
       users.discard(None)
    return users
users = process_map('mumbai_sample.osm')
#pprint.pprint(users)
len(users)
