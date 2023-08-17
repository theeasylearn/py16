# Write a programe to find kb and mb , gb outof given bytes 
class Kb:
     def __init__(self,byte):
          self.byte = byte 
     def get_kb(self):
          kb = self.byte / 1000
          print("Total Kb are ",kb)
          return kb

class Mb(Kb):
     def __init__(self, byte):
          Kb.__init__(self, byte)

     def get_mb(self):
          kb = Kb.get_kb(self)
          mb = kb / 1000
          print("Total Mb are ",mb)

byte = int(input("Enter total bytes "))

k1 = Kb(byte)
m1 = Mb(byte)

k1.get_kb()
m1.get_mb()