import os
import json

with open('backup_number.json', 'r') as openfile:
    backup_num_read = json.load(openfile)
while True:
  print(os.popen("echo {}".format(backup_num_read)).read())
  date = os.popen("date").read()
  num = list(backup_num_read) [-1]
  num = num + 1
  

backup_num = {num:date}

with open("backup_number.json", "w") as outfile:
  json.dump(backup_num, outfile)