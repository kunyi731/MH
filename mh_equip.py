import csv
from unicode_csv_reader import *


class Equip:
  
  # Given a parsed csv str array, init object
  # Name / Sex / Type / Rare / Slots / TimeGetAtBar / TimeGetAtVil / InitDef / FinalDef / FireRes / WaterRes / ThunRes / IceRes / DrgRes / 
  #  Skill(1-5)+Pts / Material(1-4)+Cnt
  def __init__(self, csv_str):
    self.name = csv_str[0]
    self.sex = csv_str[1]
    self.type = csv_str[2]
    self.rarity = csv_str[3]
    self.slots = csv_str[4]
    self.skill = dict(zip(csv_str[14:24:2], csv_str[15:25:2]))
    self.skill = dict((k, v) for k, v in self.skill.iteritems() if k)

  # Print
  def __str__(self):
    s = "Equip name %s\n" % self.name
    s += "Equip slots %s\n" % self.slots
    i = 0
    for skill in self.skill.keys():
      s += "  Skill %d: %s + %s\n" % (i, skill, self.skill[skill])
      i += 1
    return s.encode('utf-8')


# Equipment database
class EquipDb:
  def __init__(self):
    self.db = []

  def load(self, csv_str):
    self.db.append(Equip(csv_str))

  def load_file(self, fname):
    cr = UnicodeReader(open(fname, "rb"), encoding="shift-JIS")
    row_cnt = 0
    for row in cr:
      if row_cnt > 0:
        self.load(row)
      row_cnt += 1

  def count_slots(self):
    d = {}
    for i in range(4):
      d[i] = 0
    for e in self.db:
      if (int(e.rarity) >= 5):
        d[int(e.slots)] += 1
    return d

  def __str__(self):
    s = "Equip database: %d equipments\n" % len(self.db)
    return s
