import random
from random import randint

import MEL_function as MF
import attributes


#Sales Order 
    
def run():
    
    SA1  = MF.make_dict('SA1','Receive customer order request (ERP based)', [0,0,'second'], 'working day')
    SA2  = MF.make_dict('SA2','Receive customer order request (PDF file)', [12,24,'hour'])
    SA3  = MF.make_dict('SA3','Create customer order request', [4,6,'hour'])
    SA4a = MF.make_dict('SA4a','Review customer order request', [0,8,'hour'])
    SA4b = MF.make_dict('SA4b','Review customer order request', [0,0,'second'], 'working day')
    SA5  = MF.make_dict('SA5','Resolve capacity problems', [2,36,'hour'])
    SA6  = MF.make_dict('SA6','Create customer order', [2,8,'hour'])
    SA7  = MF.make_dict('SA7','Check customer order items', [0,0,'second'], 'working day')
    SA8  = MF.make_dict('SA8','Send revision request', [2,4,'hour'])
    SA9  = MF.make_dict('SA9','Change customer order', [2,48,'hour']) 
    SAPR = MF.make_dict('SAPR','Create Production Order', [0,0,'second']) #-> PR
    SA10 = MF.make_dict('SA10','Ship finished goods to headquarter', [4,48,'hour']) 
    SA11 = MF.make_dict('SA11','Receive finished goods', [1,2,'day'])
    SA12 = MF.make_dict('SA12','Ship finished goods to customer', [1,7,'day'], 'monday')
    SA13 = MF.make_dict('SA13','Create invoice', [0,4,'hour'])
    SA14 = MF.make_dict('SA14','Clear invoice', [30,90,'day'])

    #M1 & M2
   
    variant1 = MF.rand_var(15.2 * 2)
    MF.iterate_case(variant1, [SA2,SA3,SA4b,SA6,SA7,SAPR,SA10,SA11,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant2 = MF.rand_var(12.8 * 2)
    MF.iterate_case(variant2, [SA1,SA4a,SA5,SA6,SA7,SAPR,SA10,SA11,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant3 = MF.rand_var(11.4 * 2)
    MF.iterate_case(variant3, [SA2,SA3,SA4b,SA5,SA6,SA7,SAPR,SA10,SA11,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant4 = MF.rand_var(10.4 * 2)
    MF.iterate_case(variant4, [SA1,SA4a,SA6,SA7,SAPR,SA10,SA11,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant5 = MF.rand_var(8.2 * 2)
    MF.iterate_case(variant5, [SA1,SA4a,SA6,SA7,SAPR,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant6 = MF.rand_var(7.4 * 2)
    MF.iterate_case(variant6, [SA2,SA3,SA4b,SA5,SA6,SA7,SAPR,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant7 = MF.rand_var(7.2 * 2)
    MF.iterate_case(variant7, [SA1,SA4a,SA5,SA6,SA7,SAPR,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant8 = MF.rand_var(7 * 2)
    MF.iterate_case(variant8, [SA2,SA3,SA4b,SA6,SA7,SAPR,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant9 = MF.rand_var(5.4 * 2)
    MF.iterate_case(variant9, [SA1,SA4a,SA6,SA7,SA8,SA9,SAPR,SA10,SA11,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant10 = MF.rand_var(4.8 * 2)
    MF.iterate_case(variant10, [SA2,SA3,SA4b,SA6,SA7,SA8,SA9,SAPR,SA10,SA11,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant11 = MF.rand_var(4.4 * 2)
    MF.iterate_case(variant11, [SA2,SA3,SA4b,SA5,SA6,SA7,SA8,SA9,SAPR,SA10,SA11,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant12 = MF.rand_var(3.4 * 2)
    MF.iterate_case(variant12, [SA1,SA4a,SA5,SA6,SA7,SA8,SA9,SAPR,SA10,SA11,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant13 = MF.rand_var(0.8 * 2)
    MF.iterate_case(variant13, [SA1,SA4a,SA5,SA6,SA7,SA8,SA9,SAPR,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant14 = MF.rand_var(0.6 * 2)
    MF.iterate_case(variant14, [SA1,SA4a,SA6,SA7,SA8,SA9,SAPR,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant15 = MF.rand_var(0.6 * 2)
    MF.iterate_case(variant15, [SA2,SA3,SA4b,SA5,SA6,SA7,SA8,SA9,SAPR,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant16 = MF.rand_var(0.4 * 2)
    MF.iterate_case(variant16, [SA2,SA3,SA4b,SA6,SA7,SA8,SA9,SAPR,SA12,SA13,SA14], random.choice([attributes.M1, attributes.M2]), random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    #M3

    variant6 = MF.rand_var(80)
    MF.iterate_case(variant6, [SA2,SA3,SA4b,SA5,SA6,SA7,SAPR,SA12,SA13,SA14], attributes.M3, random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant7 = MF.rand_var(60)
    MF.iterate_case(variant7, [SA1,SA4a,SA5,SA6,SA7,SAPR,SA12,SA13,SA14], attributes.M3, random.choice([attributes.C1, attributes.C2, attributes.C3, attributes.C4]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    #M4

    variant6 = MF.rand_var(60)
    MF.iterate_case(variant6, [SA2,SA3,SA4b,SA5,SA6,SA7,SAPR,SA12,SA13,SA14], attributes.M4, random.choice([attributes.C1, attributes.C2, attributes.C3]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    variant7 = MF.rand_var(80)
    MF.iterate_case(variant7, [SA1,SA4a,SA5,SA6,SA7,SAPR,SA12,SA13,SA14], attributes.M4, random.choice([attributes.C1, attributes.C2, attributes.C3]), random.choice([attributes.S1, attributes.S2, attributes.S3, attributes.S4]))

    
#Production Order

def PR_run(timestamp, ref_case_id, material, customer, supplier): 
    
    PR1  = MF.make_dict('PR1', 'Planned Production Order created', [1,60,'second'])
    PR2  = MF.make_dict('PR2', 'Retrieve stock list', [0,3,'hour'], 'working day')
    PR3  = MF.make_dict('PR3', 'Create current stock analysis', [30,60,'minute']) 
    PRPL = MF.make_dict('PRPL','Create Production Planning', [0,0,'second']) #->PL
    PR4  = MF.make_dict('PR4', 'Order raw material', [30,120,'minute']) 
    PRPU = MF.make_dict('PRPU','Create Purchase Order', [0,0,'second']) #->PU
    PR5  = MF.make_dict('PR5', 'Produce final goods', [4,4,'day'])
    PR6  = MF.make_dict('PR6', 'Record final goods receipt', [5,9,'day'])
    PR7  = MF.make_dict('PR7', 'Check quality of final goods', [4,6,'hour'])

    n = randint(1,100)
    if n < 60 : activity_list = [PR1,PR2,PR3,PRPL,PR4,PRPU,PR5,PR6,PR7]
    else      : activity_list = [PR1,PR2,PRPL,PR4,PRPU,PR5,PR6,PR7]
    
    timestamp = MF.PR_create_case(timestamp, ref_case_id, activity_list, material, customer, supplier)
    
    return timestamp
    
    #variant1 = MF.rand_var(60)
    #MF.iterate_case(variant1, [PR1,PR2,PR3,PR4,PR5,PR6,PR7], attributes.M1, attributes.C1)

    #variant2 = MF.rand_var(40)

    
#Production planning

def PL_run(timestamp, ref_case_id, material, customer, supplier):
    
    PL1 = MF.make_dict('PL1', 'Schedule production plan', [2,3,'hour'])
    PL2 = MF.make_dict('PL2', 'Update planned production orders', [30,60,'minute'])
    PL3 = MF.make_dict('PL3', 'Create leveling plan', [0,12,'hour'], 'tuesday')
    PL4 = MF.make_dict('PL4', 'Create production order', [0,2,'day'])

    activity_list = [PL1,PL2,PL3,PL4]
    
    timestamp = MF.PL_create_case(timestamp, ref_case_id, activity_list, material, customer, supplier)
    
    return timestamp
    
    #variant1 = MF.rand_var(100)
    #MF.iterate_case(variant1, [PL1,PL2,PL3,PL4], attributes.M1, attributes.C1)

    
#Purchase Order    
    
def PU_run(timestamp, ref_case_id, material, customer, supplier):
    
    PU1  = MF.make_dict('PU1', 'Receive missing raw material notification', [2,8,'hour']) 
    PU2  = MF.make_dict('PU2', 'Check customer preference', [5,10,'second'])
    PU3  = MF.make_dict('PU3', 'Search Suitable vendor', [1,5,'day'])
    PU4  = MF.make_dict('PU4', 'Request quote', [1,2,'day'])
    PU5  = MF.make_dict('PU5', 'Create purchase order', [1,1,'day'])
    PU6  = MF.make_dict('PU6', 'Release purchase order', [0,0,'second'])
    PU7  = MF.make_dict('PU7', 'Send purchase order', [0,0,'minute'], 'working day')
    PU8a = MF.make_dict('PU8a', 'Record goods receipt at headquarter', [7,56,'day'])
    PU8b = MF.make_dict('PU8b', 'Record goods receipt at headquarter', [21,42,'day'])
    PU9  = MF.make_dict('PU9', 'Check quality', [1,3,'day'])
    PU10 = MF.make_dict('PU10', 'Create complaint', [1,3,'day'])
    PU11 = MF.make_dict('PU11', 'Send back raw material', [1,3,'day'])
    PU12 = MF.make_dict('PU12', 'Ship raw materials to plant', [1,4,'day'])
    PU13 = MF.make_dict('PU13', 'Receive raw materials at plant', [2,2,'day'])

    n = randint(1,100)
    if n < 40   : activity_list = [PU1,PU2,PU4,PU5,PU6,PU7,PU8a,PU9,PU12,PU13]
    elif n < 65 : activity_list = [PU1,PU2,PU3,PU4,PU5,PU6,PU7,PU8a,PU9,PU12,PU13]   
    elif n < 85 : activity_list = [PU1,PU2,PU4,PU5,PU6,PU7,PU8a,PU9,PU10,PU11,PU8b,PU9,PU12,PU13]
    elif n < 95 : activity_list = [PU1,PU2,PU3,PU4,PU5,PU6,PU7,PU8a,PU9,PU10,PU11,PU8b,PU9,PU12,PU13]
    elif n < 98 : activity_list = [PU1,PU2,PU4,PU5,PU6,PU7,PU8a,PU9,PU10,PU11,PU8b,PU9,PU10,PU11,PU8b,PU9,PU12,PU13]
    else        : activity_list = [PU1,PU2,PU3,PU4,PU5,PU6,PU7,PU8a,PU9,PU10,PU11,PU8b,PU9,PU10,PU11,PU8b,PU9,PU12,PU13]
    
    timestamp = MF.PU_create_case(timestamp, ref_case_id, activity_list, material, customer, supplier)
    
    return timestamp

    #variant1 = MF.rand_var(40)
    #MF.iterate_case(variant1, [PU1,PU2,PU4,PU5,PU6,PU7,PU8a,PU9,PU12,PU13], attributes.M1, attributes.S1)

    #variant1 = MF.rand_var(25)
    #MF.iterate_case(variant1, [PU1,PU2,PU3,PU4,PU5,PU6,PU7,PU8a,PU9,PU12,PU13], attributes.M1, attributes.S1)

    #variant2 = MF.rand_var(20)
    #MF.iterate_case(variant2, [PU1,PU2,PU4,PU5,PU6,PU7,PU8a,PU9,PU10,PU11,PU8b,PU9,PU12,PU13], attributes.M1, attributes.S1)

    #variant2 = MF.rand_var(10)
    #MF.iterate_case(variant2, [PU1,PU2,PU3,PU4,PU5,PU6,PU7,PU8a,PU9,PU10,PU11,PU8b,PU9,PU12,PU13], attributes.M1, attributes.S1)

    #variant1 = MF.rand_var(3)
    #MF.iterate_case(variant1, [PU1,PU2,PU4,PU5,PU6,PU7,PU8a,PU9,PU10,PU11,PU8b,PU9,PU10,PU11,PU8b,PU9,PU12,PU13], attributes.M1, attributes.S1)

    #variant2 = MF.rand_var(2)
    #MF.iterate_case(variant2, [PU1,PU2,PU3,PU4,PU5,PU6,PU7,PU8a,PU9,PU10,PU11,PU8b,PU9,PU10,PU11,PU8b,PU9,PU12,PU13], attributes.M1, attributes.S1)
    
    
