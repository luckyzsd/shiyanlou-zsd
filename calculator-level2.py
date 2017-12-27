#   *  utf-8  *

import sys
from collections import namedtuple

IncomeTaxItem=namedtuple('IncomeTaxItem',['start_point','tax_rate','quick_subtractor'])

INCOME_TAX_ST=3500

INCOME_TAX_TB=[
    IncomeTaxItem(80000,0.45,13505),
    IncomeTaxItem(55000,0.35,5505),
    IncomeTaxItem(35000,0.3,2755),
    IncomeTaxItem(9000,0.25,1005),
    IncomeTaxItem(4500,0.2,555),
    IncomeTaxItem(1500,0.1,105),
    IncomeTaxItem(0,0.03,0)
]

INSURANCE_RATE={
    'endowment':0.08,
    'medical':0.02,
    'unemployment':0.005,
    'injury':0,
    'maternity':0,
    'publicfund':0.06
}

def calc_income_tax(income):
  insurancemny=income*sum(INSURANCE_RATE.values())
  realincome=income-insurancemny
  taxableincome=realincome-INCOME_TAX_ST
  if taxableincome<0.0:
    return '0.00','{:.2f}'.format(realincome)
  for item in INCOME_TAX_TB:
    if taxableincome>item.start_point:
      tax=taxableincome*item.tax_rate-item.quick_subtractor
      return '{:.2f}'.format(tax),'{:.2f}'.format(realincome-tax)

def main():
    for item in sys.argv[1:]:
        id,incomestr=item.split(':')
        try:
            income=int(incomestr)
        except ValueError:
            print('Parameter Error')
        remain=calc_income_tax(income)
        print('{}:{}'.format(id,remain)


if __name__=='__main__':
    main()
