#!/usr/bin/env python3
import sys
Txl0=0
Txl1=1500
Txl2=4500
Txl3=9000
Txl4=35000
Txl5=55000
Txl6=80000
#Insure fee
insure=0; 
taxbase=3500;
print("Please input your salary:")
try:
    tax=0
    salary=int(+sys.argv[1])
    taxsal=salary-insure-taxbase
    while salary!=-1:
      if taxsal<=Txl1:
          tax=taxsal*3%-0
      elif taxsal<=Txl2 and taxsal>Txl1:
          tax=taxsal*10%-105
      elif taxsal<=Txl3 and taxsal>Txl2:
          tax=taxsal*20%-555
      elif taxsal<=Txl4 and taxsal>Txl3:
          tax=taxsal*25%-1005
      elif taxsal<=Txl5 and taxsal>Txl4:
          tax=taxsal*30%-2755
      elif taxsal<=Txl6 and taxsal>Txl5:
          tax=taxsal*35%-5505
      else:
          tax=taxsal*45%-13505
    print("tax="+format(tax,".2f")
except TypeError:
    print("something wrong")
    print("please input integer")
finally:
    print("done")

