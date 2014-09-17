#!/usr/bin/python
from datetime import datetime, timedelta
from subprocess import call
import errno
import os.path
import ConfigParser
import shutil


def getMonthDateString(m, y):
    s = str(y)
    if m < 10:
        s = s + '0' + str(m)
    else:
        s = s + str(m)
    return s;

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
DATA_DIR_YEARLY = "datay"
DATA_DIR_MONTHLY = "datam"
DATA_DIR_WEEKLY = "dataw"
DATA_DIR_DAILY = "data"
mkdir_p(DATA_DIR_DAILY)
mkdir_p(DATA_DIR_MONTHLY)
mkdir_p(DATA_DIR_WEEKLY)
mkdir_p(DATA_DIR_YEARLY)
now = datetime.now()

sunday = now - timedelta(days=now.weekday()) + timedelta(days=6)
# Weekly
print "Download weekly reports"
for i in range(1, 27):
    sunday = sunday + timedelta(weeks=-1)
    fdate =  getDayDateString(sunday.day, sunday.month,  sunday.year )
    fname = 'S_W_' + VENDOR_ID + '_' + fdate + '.txt.gz'
    fpath = DATA_DIR_WEEKLY+'/'+fname
    if os.path.isfile(fpath):
        print fpath+' already downloaded'
    else:
        print  'java Autoingestion autoingestion.properties ' + VENDOR_ID+ ' Sales Weekly Summary '+fdate
        call(["java", "Autoingestion", "autoingestion.properties", VENDOR_ID, "Sales", "Weekly", "Summary", fdate])
        if os.path.isfile(fname):
            shutil.move(fname, fpath)


# Monthly
print "Download monthly reports"
month = now.month
year = now.year
for i in range(1, 13):
    month = month-1;
    if (month<=0):
        month = 12
        year = year-1
    fdate =  getMonthDateString(month,  year )
    fname = 'S_M_' + VENDOR_ID + '_' + fdate + '.txt.gz'
    fpath = DATA_DIR_MONTHLY+'/'+fname
    if os.path.isfile(fpath):
        print fpath+' already downloaded'
    else:
        print  'java Autoingestion autoingestion.properties ' + VENDOR_ID+ ' Sales Monthly Summary '+fdate
        call(["java", "Autoingestion", "autoingestion.properties", VENDOR_ID, "Sales", "Monthly", "Summary", fdate])
        if os.path.isfile(fname):
            shutil.move(fname, fpath)

# Yearly
print "Download yearly reports"
year = now.year
while (year>2010):
    year = year - 1
    fname = 'S_Y_' + VENDOR_ID + '_' + str(year) + '.txt.gz'
    fpath = DATA_DIR_YEARLY+'/'+fname
    if os.path.isfile(fpath):
        print fpath+' already downloaded'
    else:
        print  'java Autoingestion autoingestion.properties ' + VENDOR_ID+ ' Sales Yearly Summary '+str(year)
        call(["java", "Autoingestion", "autoingestion.properties", VENDOR_ID, "Sales", "Yearly", "Summary", str(year)])
        if os.path.isfile(fname):
            shutil.move(fname, fpath)

# Daily
print "Download daily reports"
for i in range(1, 30):
    d=now-timedelta(days=i)
    fdate =  getDayDateString(d.day, d.month,  d.year )
    fname = 'S_D_' + VENDOR_ID + '_' + fdate + '.txt.gz'
    fpath = DATA_DIR_DAILY+'/'+fname
    if os.path.isfile(fpath):
        print fpath+' already downloaded'
    else:
        print  'java Autoingestion autoingestion.properties ' + VENDOR_ID+ ' Sales Daily Summary '+fdate
        call(["java", "Autoingestion", "autoingestion.properties", VENDOR_ID, "Sales", "Daily", "Summary", fdate])
    if os.path.isfile(fname):
            shutil.move(fname, fpath)

