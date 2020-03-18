#!/usr/bin/env python
# -*- coding: utf-8 -*-
Z = float(input())
M = float(input())

T=Z+M

P1=Z/T
P2=M/T

P1*=100
P2*=100


print('Procenat žena u teretani je: {:5.2f}'.format(P1),'%',sep='')

print('Procenat muškaraca u teretani je: {:5.2f}'.format(P2),'%',sep='')
