'''
	ip fuzzy search using prefix match
'''

import random
import pprint
import operator


query = '10.10.1.3'

def GenerateIP():
	ip = '10.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255))
	return ip

ips = [GenerateIP() for _ in xrange(100)] + ['10.10.1.3', '10.10.1.120','10.10.2.3', '10.10.2.10']

print ips

if query in ips:
	grp1 = {query: 1}

#10.*
grp4 = {}
anchar = query.index('.') + 1
for ip in ips:
	if ip[:anchar] == query[:anchar]:
		grp4[ip] = 4

#10.10.*
grp3 = {}
anchar = query.index('.', anchar) + 1
for ip in ips:
	if ip[:anchar] == query[:anchar]:
		grp3[ip] = 3

#10.10.1.*
grp2 = {}
anchar = query.index('.', anchar) + 1
for ip in ips:
	if ip[:anchar] == query[:anchar]:
		grp2[ip] = 2

#aggregation
result = {}
result.update(grp4)
result.update(grp3)
result.update(grp2)
result.update(grp1)

#sort
result = sorted(result.iteritems(), key=operator.itemgetter(1))
pprint.pprint(result)
