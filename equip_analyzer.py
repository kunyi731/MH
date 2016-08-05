from mh_equip import *
import csv
from glob import *

from unicode_csv_reader import *

cr = UnicodeReader(open('MH4EQUIP_BODY.csv', "rb"), encoding="shift-JIS")

#for row in cr:
#  print Equip(row)
 
# Analyze equipment data
db = EquipDb()
for f in glob('MH4EQUIP_*.csv'):
  db.load_file(f)
print db

print db.count_slots()
