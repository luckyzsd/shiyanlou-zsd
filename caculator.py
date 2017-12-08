#!/usr/bin/env python3
import sys

def main():
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
    if len(sys.argv)!=2:
      print('Parameter Error')
      exit()
    
    salary=int(sys.argv[1])
    print('salary='+str(salary))
    taxsal=salary-insure-taxbase
    #print('taxsal='+str(taxsal))
    if taxsal<=Txl1:
      tax=taxsal*0.03-0
    elif taxsal<=Txl2 and taxsal>Txl1:
      #print('tax='+'{:.2f}'.format(taxsal*0.1))
      tax=taxsal*0.1-105
      #print('tax='+'{:.2f}'.format(tax))
    elif taxsal<=Txl3 and taxsal>Txl2:
      tax=taxsal*0.2-555
    elif taxsal<=Txl4 and taxsal>Txl3:
      tax=taxsal*0.25-1005
    elif taxsal<=Txl5 and taxsal>Txl4:
      tax=taxsal*0.3-2755
    elif taxsal<=Txl6 and taxsal>Txl5:
      tax=taxsal*0.35-5505
    else:
      tax=taxsal*0.45-13505
    print('tax='+'{:.2f}'.format(tax))
  except Exception as e:
    print("something wrong"+e)
    print("please input integer")

if __name__=='__main__':
  main()

