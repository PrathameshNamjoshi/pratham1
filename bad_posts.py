import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

import xml.etree.ElementTree as ET
import re

tree = ET.parse(OSMFILE)
root = tree.getroot()

counttotal = 0
count = 0
wp = []
regex = re.compile('^(4)(0)\d{4}$')
for i in tree.getiterator('tag'):
    k1 = i.get("k")
    if k1 == "addr:postcode":
        v1 = i.get("v")
        m1 = regex.match(v1)
        if not m1:
            counttotal = counttotal +1
            if len(v1) <> 6:
                v1 = v1.replace(" ","")
                m2 = regex.match(v1)
                if not m2:
                    wp.append(v1)
                    count = count +1
            elif len(v1) == 6:
                wp.append(v1)
                count = count +1

print wp
print count
