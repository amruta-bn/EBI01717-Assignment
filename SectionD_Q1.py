import re
import xml.etree.ElementTree as ET
from collections import defaultdict

xmlfile="InputSectionD.Q1.xml"
tree = ET.parse(xmlfile)
root = tree.getroot()


d1 = defaultdict(list)
uniqueName=[]


for arc in root.findall('Article'):
	at=arc.find('ArticleTitle').text
	for aut in arc.findall('AuthorList/Author'):
		fn=aut.find('ForeName').text
		ln=aut.find('LastName').text
		name=ln+","+fn
		temp=at.split("Title")
		order=temp[-1]
		d1[order].append(name)
		if name not in uniqueName:
			uniqueName.append(name)
			

headers = sorted(uniqueName)
print(d1)
