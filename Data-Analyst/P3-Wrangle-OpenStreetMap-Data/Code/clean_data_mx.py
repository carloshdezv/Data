#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
from collections import defaultdict
#Set encoding to UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Update street names mapping

expected = ["Avenida", "Andador", "Boulevard", "Calle", "Calzada", "Cerrada", "Circuito", "Callejón", 
            "Camino", "Carretera", "Glorieta","Plaza","Privada","Prolongación","Retorno","CP "]

mapping = { "Av ": "Avenida ",
            "Av. ": "Avenida ",            
            "Blvd ": "Boulevard ",
            "Blvd. ": "Boulevard ",
            "Calz ": "Calzada ",
            "Calz. ": "Calzada ",
            "Cda ": "Cerrada ",
            "Cda. ": "Cerrada ",
            "Carr ": "Carretera ",
            "Carr. ": "Carretera ",
            "Prol ": "Prolongación ",
            "Prol. ": "Prolongación ",
            "Ret ": "Retorno ",
            "Ret. ": "Retorno "
            }

#Regex to replace abbreviations from stack overflow: http://stackoverflow.com/questions/2400504/easiest-way-to-replace-a-string-using-a-dictionary-of-replacements

street_type_re = re.compile(r'\b(' + '|'.join(mapping.keys()) + r')\b')

#Update street names function

def update_name(name, mapping):

    m = street_type_re.search(name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            name=street_type_re.sub(lambda x: mapping[x.group()], name)
    return name

#Transforming the shape of the data

#regex to search tags
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

#Elements for created array
CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

#Shape elements

def shape_element(element):
    node = {}
    address = {}
    node_refs=[]

    if element.tag == "node" or element.tag == "way":
        node['id'] = element.attrib['id']
        node['type'] = element.tag

        for k in element.attrib.keys():
            #Store values in created array
            if k in CREATED:
                node['created']={
                                "changeset": None,
                                "user": None,
                                "version": None,
                                "uid": None,
                                "timestamp": None
                                }
                for l in CREATED:
                    node['created'][l]=element.attrib[l]
            #Store values for lattitue and longitude
            elif k in ['lat', 'lon']:
                node['pos']=[]
                for l in ['lat', 'lon']:
                    node['pos'].append(float(element.attrib[l]))
            else:
                node[k]=element.attrib[k]

        
        for tag in element.iter('tag'):            
            #Get tags different to addr:
            if tag.attrib['k'][:5]!='addr:':
                node[tag.attrib['k']] = tag.attrib['v']
            elif re.search(problemchars, tag.attrib['k']):
                break  
            elif re.search(lower, tag.attrib['k']):
                break
            # Get address tags 
            elif re.search(lower_colon, tag.attrib['k']):
                #Update street name                     
                if tag.attrib['k'][5:] == "street": 
                    value = tag.attrib['v']                    
                    address["street"] = update_name(value, mapping)
                else:
                    address[tag.attrib['k'][5:]]=tag.attrib['v']                
                node['address'] = address
            #Get remaining tags                
            elif re.search(lower_colon, tag.attrib['k']):
                node[tag.attrib['k']] = tag.attrib['v']
        #Gets all node refs        
        if element.tag == "way": 
            node['node_refs']=[]
            for tag in element.iter("nd"):            
                node_refs.append(tag.get("ref"))
            node['node_refs']=node_refs
                   
        return node
    else:
        return None

#Write to json file

def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el,ensure_ascii=False) + "\n") #Force encoding to Unicode
    return data

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
            
    data = process_map("/Users/CarlosA/Downloads/mexico-city_mexico.osm", False)

if __name__ == "__main__":
    test()
