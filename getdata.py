#!/usr/bin/python
from datetime import datetime, timedelta
from subprocess import call
import errno
import os.path
import ConfigParser
import shutil



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
  

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise
        
        
# ------------------------- Main
config = ConfigParser.RawConfigParser()
config.read('config.ini')
VENDOR_ID = config.get('vendor', 'vendorid')

mkdir_p("data")
now = datetime.now()

# Daily
for i in range(1, 26):
    d=now-timedelta(days=i)
    fdate =  getDayDateString(d.day, d.month,  d.year )
    fname = 'S_D_' + VENDOR_ID + '_' + fdate + '.txt.gz'
    fpath = 'data/'+fname
    if os.path.isfile(fpath):
        print fpath+' already downloaded'
    else:
        print  'java Autoingestion autoingestion.properties ' + VENDOR_ID+ ' Sales Daily Summary '+fdate
        call(["java", "Autoingestion", "autoingestion.properties", VENDOR_ID, "Sales", "Daily", "Summary", fdate])
        shutil.move(fname, fpath)

