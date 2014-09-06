#!/usr/bin/python
VENDOR_ID = 85202719

def getDayDateString(d, m, y):
  s = str(y)
  if m < 10:
    s = s + '0' + str(m)
  else:
    s = s + str(m)
  if d < 10:
    s = s + '0' + str(d)
  else:
    s = s + str(d)
  return s;
  

from datetime import datetime, date, timedelta

now = datetime.now()

mm = now.month
dd = now.day
yyyy = now.year

# Daily
for i in range(1, 26):
  d=now-timedelta(days=i)
  print getDayDateString(d.day, d.month,  d.year )
#java Autoingestion props.properties 85202719 Sales Daily Summary 20140903
#java Autoingestion props.properties 85202719 Sales Wekely Opt-In 20140902

