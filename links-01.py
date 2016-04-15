#!/usr/bin/python
import pprint 
import re
file =  open('/Users/ahmedsafwat/Downloads/interfaces-test.txt' , 'r')
Router_List=[]
for line in file:
	if 'show isis adj' in line:
		Router_name = re.split('>|@' , line)[1]
		Router_List.append(Router_name)
file2 = open ('/Users/ahmedsafwat/Downloads/interfaces-test.txt' , 'r')
for line1 in file2:
		for counter in range(len(Router_List)):
			if Router_List[counter] in line1:
				if 'show isis ad' not in line1:
					if 'exit' not in line1:
						Interface = line1.split()[0]
						Router_02 = line1.split()[1]
						print '"%s"       "%s"'  %(Interface , Router_02)
			counter += 1 
