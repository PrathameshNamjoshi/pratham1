import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "mumbai_india.osm"
tree = ET.parse(OSMFILE)
root = tree.getroot()

postal_type_re = re.compile('^(4)(0)\d{4}$')

def audit_postal_code(postal_types,postal_value):
    m = postal_type_re.search(postal_value)
    if m:
        postal_type=m.group()
        postal_types[postal_type].add(postal_value)

def is_postal_code(elem):
    return (elem.attrib['k'] == "addr:postcode")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    postal_types=defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag in["node", "way", "relation"] :
            for tag in elem.iter("tag"):
                if is_postal_code(tag):
                    audit_postal_code(postal_types,tag.attrib['v'])
    osm_file.close()
    return postal_types


#audit(SAMPLE_FILE)
audit(OSMFILE)
pprint.pprint(dict(audit(OSMFILE)))

