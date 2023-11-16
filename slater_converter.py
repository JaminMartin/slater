#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:27:56 2022

@author: jamin
"""

'''
Convert E_k, F_k and F^k Slater parameters between each other, just enter given parameters and the conversion
index, e.g. if you are starting with F^k, conv = 2 
'''
class slater:
  def __init__(self,u1,u2,u3,conv):
      
      if conv == 0:
          self.E1 = u1
          self.E2 = u2
          self.E3 = u3
          
          self.F_2 = (self.E1 + 143 * self.E2 + 11 * self.E3)/42
          self.F_4 = (self.E1 - 130 * self.E2 + 4 * self.E3)/77
          self.F_6 = (self.E1 + 35 * self.E2 - 7 * self.E3)/462
          
          self.F2 = 225 * self.F_2
          self.F4 = 1089 * self.F_4
          self.F6 = (184041/25) * self.F_6
          
      elif conv == 1:
          self.F_2 = u1
          self.F_4 = u2 
          self.F_6 = u3
          self.E1 = (70 * self.F_2 + 231 * self.F_4 + 2002 * self.F_6)/9
          self.E2 = (self.F_2 - 3 * self.F_4 + 7 * self.F_6)/9
          self.E3 = (5 * self.F_2 + 6 * self.F_4  - 91 * self.F_6)/3
          self.F2 = 225 * self.F_2
          self.F4 = 1089 * self.F_4
          self.F6 = (184041/25) * self.F_6
      elif conv == 2:
          self.F2 = u1
          self.F4 = u2
          self.F6 = u3
          self.F_2 = self.F2 / 225 
          self.F_4 = self.F4 / 1089
          self.F_6 = self.F6 /( 184041/25)
          self.E1 = (70 * self.F_2 + 231 * self.F_4 + 2002 * self.F_6)/9
          self.E2 = (self.F_2 - 3 * self.F_4 + 7 * self.F_6)/9
          self.E3 = (5 * self.F_2 + 6 * self.F_4  - 91 * self.F_6)/3
      else:
          print('Error! invalid conversion index, 1 = E_k, 2 = F_k, 3, F^K')

if __name__ == "__main__":
	'example'
	'start with F^K parameters'
	A  = slater(5434.4,24.62 , 525.05, 0)

	'print E_k params'
	print('E_k:')
	print(A.E1,A.E2,A.E3)

	'print F_k params'
	print('F_k:')
	print(A.F_2,A.F_4,A.F_6)

	'print Fk params'
	print('Fk:')
	print(A.F2,A.F4,A.F6)
