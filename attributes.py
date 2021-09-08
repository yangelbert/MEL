#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#SA1  = make_dict('SA1','Receive customer order request (ERP based)', [0,0,'second'], 'working day')
#SA2  = make_dict('SA2','Receive customer order request (PDF file)', [12,24,'hour'])
#SA3  = make_dict('SA3','Create customer order request', [4,6,'hour'])
#SA4a = make_dict('SA4a','Review customer order request', [0,8,'hour'])
#SA4b = make_dict('SA4b','Review customer order request', [0,0,'second'], 'working day')
#SA5  = make_dict('SA5','Resolve capacity problems', [2,36,'hour'])
#SA6  = make_dict('SA6','Create customer order', [2,8,'hour'])
#SA7  = make_dict('SA7','Check customer order items', [0,0,'second'], 'working day')
#SA8  = make_dict('SA8','Send revision request', [2,4,'hour'])
#SA9  = make_dict('SA9','Change customer order', [2,48,'hour']) #-> PR
#SA10 = make_dict('SA10','Ship finished goods to headquarter', [4,48,'hour'])
#SA11 = make_dict('SA11','Receive finished goods', [1,2,'day'])
#SA12 = make_dict('SA12','Ship finished goods to customer', [1,7,'day'], 'monday')
#SA13 = make_dict('SA13','Create invoice', [0,4,'hour'])
#SA14 = make_dict('SA14','Clear invoice', [30,90,'day'])

def initialize():
    
    global C1,C2,C3,C4
    global M1,M2,M3,M4
    global S1,S2,S3,S4
    
    class attribute:

        def __init__(self, id, exceptions):
            self.id = id
            self.exceptions = exceptions

    C1  = attribute('C1', {'SA5':[1,2,'day'], 'SA14':[3,10,'day']}) #München
    C2  = attribute('C2', {'SA5':[1,2,'day'], 'SA14':[60,90,'day']}) #München
    C3  = attribute('C3', {'SA14':[10,20,'day']}) #Pforzheim
    C4  = attribute('C4', {'SA14':[30,60,'day']}) #Pforzheim

    M1  = attribute('M1', {}) #battery
    M2  = attribute('M2', {}) #battery
    M3  = attribute('M3', {'SA12':[1,2,'day']}) #cable
    M4  = attribute('M4', {'SA12':[1,2,'day']}) #cable
    
    S1  = attribute('S1', {}) #
    S2  = attribute('S2', {}) #
    S3  = attribute('S3', {'PU8a':[5,10,'day'], 'PU8b':[5,10,'day']}) #Budapest
    S4  = attribute('S4', {'PU8a':[40,56,'day'], 'PU8b':[30,42,'day']}) #Ankara, Türkei



