# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:36:21 2018

@author: David
"""

from difflib import SequenceMatcher
from urllib.request import urlopen
from xml.etree.ElementTree import parse

namelist=['Dipesh','Abdul','Ram','Choi','Dave','abd']
namelist1=[]
dict1={}

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
    
def buildnamelist():
    u = urlopen('https://scsanctions.un.org/resources/xml/en/consolidated.xml')
    doc = parse(u)
    #print(doc)
    for item in doc.iterfind('INDIVIDUALS/INDIVIDUAL'):
        #print(item)
        first_name=item.findtext('FIRST_NAME')
        namelist1.append(first_name)
        last_name=item.findtext('SECOND_NAME')
        namelist1.append(last_name)
        dataid=item.findtext('DATAID')
        dict1[first_name]=dataid
        dict1[last_name]=dataid
        
    print(namelist1)
        
        #print(name)

        
    
def listnames(b):
    newlist=[]
    print(type(namelist1))
    namelist2= [x for x in namelist1 if x is not None]
    for name in namelist2:
        
        #print(name)
        result=similar(name.lower(),b.lower())
        #print(result)
        #print(type((name,result)))
        if result >= 0.75:
            #print((name,result))
            
            
            newlist.append(tuple((name,result,dict1[name])))
            
        #print(newlist)
    
    return newlist
    
def shownames(a):
    buildnamelist()
    names = listnames(a)
    print(names)
    for i in names:
        #print("name {1} is {2} percent match".format(i[0],float(i[1])*100))
        print(i[0]+ " matches " + str(i[1] *100) + " percent " +" dataid id is " + i[2])
    
