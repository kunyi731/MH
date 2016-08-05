import csv

from unicode_csv_reader import *

cr = UnicodeReader(open('MH4EQUIP_BODY.csv', "rb"), encoding="shift-JIS")

for i in range(2):
  for s in cr.next():
    print s.encode('utf-8')
  #print cr.next()
  #print cr.next()[0].encode('utf-8')
  #cr = csv.reader(open('MH4EQUIP_BODY.csv', "rb"))

#for row in cr:
#  print row
