#!/usr/bin/python
import pprint 
import re
file =  open('/Users/ahmedsafwat/Downloads/interfaces-test.txt' , 'r')
Router_dic = {}
Router_List = []
for line in file:
		if 'show isis adj' in line:
			Router_dic['Router-01'] = re.split('>|@' , line)[1]
			Rout_name = re.split('>|@' , line)[1]
			Router_List.append(Rout_name)
		if 'Up' in line:
			Router_dic['Interface-01'] = line.split()[0] 
			Router_dic['Router_02'] = line.split()[1]
file2 = open ('/Users/ahmedsafwat/Downloads/interfaces-test.txt' , 'r')
for line1 in file2:
            #    for counter in range(len(Router_List)):
                        if Router_dic['Router-01'] in line1 and 'show isis adj' not in line1 and 'exit' not in line1:
                              Router_dic['Interface-02'] = line1.split()[0]
                              print "%s"  %Router_dic 
