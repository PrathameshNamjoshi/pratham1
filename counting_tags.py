import xml.etree.cElementTree as ET
import pprint
tags={}
def count_tags(sample_file):
    for event, elem in ET.iterparse(sample_file, events=("start",)):
        if elem.tag in tags.keys():
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
        #print tags
    return tags
tags = count_tags('mumbai_india.osm')
pprint.pprint(tags)