#!/usr/bin/env python3

import re, operator, csv
import collections

err = {}
usr_info = {}
usr_err = {}
usr_list = []

f = open('syslog.log')
lines = f.readlines()
f.close()

for line in lines:
  match = re.search(r'ticky: ([\w]*) ([\w\d\[\]#\' ]*) \(([\w.]*)', line)
  if match != None:
       #print(match.group(1))
      if match.group(1) == 'ERROR':
         #print (match.group(2))
         err[match.group(2)] = err.get(match.group(2), 0) + 1
         usr_err[match.group(3)] = usr_err.get(match.group(3), 0) + 1
      if match.group(1) == 'INFO':
         #print (line)
         usr_info[match.group(3)] = usr_info.get(match.group(3), 0) + 1
#print(str(err) + '\n' + str(usr_info) + '\n' + str(usr_err))
#err = dict(sorted(err.items(), key=lambda item: item[1], reverse=True))
#err = dict(sorted(err.items(), key=operator.itemgetter(1), reverse=True))
#err = dict(sorted(err, key=err.get, reverse=True))
temp = sorted(err.items(), key=lambda item: item[1], reverse=True)
err = collections.OrderedDict(temp)
print(str(err) + '\n' + str(usr_info) + '\n' + str(usr_err))
usr_list = [x for x in usr_info.keys() if x not in usr_list]
usr_list.extend([x for x in usr_err.keys() if x not in usr_list])
usr_list.sort()
#print(usr_list)

with open('error_message.csv', 'w') as output:
    cw = csv.writer(output)
    cw.writerow(['Error', 'Count'])
    for k in err.keys():
      cw.writerow([k, err[k]])

with open('user_statistics.csv', 'w') as output:
    cw = csv.writer(output)
    cw.writerow(['Username', 'INFO', 'ERROR'])
    for k in usr_list:
      cw.writerow([k, usr_info.get(k,0), usr_err.get(k,0)])

