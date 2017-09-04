import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

def update_postcode(postcode):
    search = re.search(r'^\D*(\d{6}).*',postcode)
    search1 = re.search('^(4)(0)\d{4}$',postcode)
    if search1:
        return search.group(1)
    else :
        return '000000'
for i in tree.getiterator('tag'):
    k1 = i.get("k")
    if k1 == "addr:postcode":
        v1 = i.get("v")
        print  update_postcode(v1)
        
