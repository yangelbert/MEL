import pandas as pd
import datetime as dt
from datetime import datetime
from datetime import timedelta
import random
from random import randint
import os

import attributes
import MEL_process as MP


#initialize total_case & generate case & activity table function

def initialize(n):
    global total_case, case_table, activity_table
    global SA_case_number, PR_case_number, PL_case_number, PU_case_number
    
    total_case = n
    SA_case_number = PR_case_number = PL_case_number = PU_case_number = 1
    
    case_table = pd.DataFrame(columns = [
        'CASE_ID',
        'REF_CASE_ID',
        'MATERIAL_ID',
        'CUSTOMER_ID',
        'SUPPLIER_ID'
    ])

    activity_table = pd.DataFrame(columns = [
        'CASE_ID',
        'ACTIVITY', 
        'SORT',
        'TIMESTAMP'
    ])
    
#dictionary function

def make_dict(activity_id, activity, duration, operate_day='everyday'):
    return {'activity_id':activity_id, 'activity':activity, 'duration':duration, 'operate_day':operate_day}

#random date and time functions

def rand_date(from_month,to_month,year,open_time=8,close_time=20):
    return datetime(year, randint(from_month,to_month),randint(1,28),randint(open_time,close_time),randint(1,59),randint(1,59))

def rand_time(from_time=0,to_time=0,unit='random'):
    if from_time == to_time: #not random
        if unit.lower() in set(('s','second','seconds'))   : return timedelta(seconds = from_time)
        elif unit.lower() in set(('m','minute','minutes')) : return timedelta(minutes = from_time)
        elif unit.lower() in set(('h','hour','hours'))     : return timedelta(hours = from_time)
        elif unit.lower() in set(('d','day','days'))       : return timedelta(days = from_time)
        else: return timedelta(days = randint(0,6), hours = randint(0,23), minutes = randint(0,59), seconds = randint(0,59))

    else: #random
        if unit.lower() in set(('s','second','seconds'))   : return timedelta(seconds = randint(from_time,to_time))
        elif unit.lower() in set(('m','minute','minutes')) : return timedelta(minutes = randint(from_time,to_time-1), seconds = randint(0,59))
        elif unit.lower() in set(('h','hour','hours'))     : return timedelta(hours = randint(from_time,to_time-1), minutes = randint(0,59), seconds = randint(0,59))
        elif unit.lower() in set(('d','day','days'))       : return timedelta(days = randint(from_time,to_time-1), hours = randint(0,23), minutes = randint(0,59), seconds = randint(0,59))
        else: return timedelta(days = randint(0,6), hours = randint(0,23), minutes = randint(0,59), seconds = randint(0,59))

def add_rand_time(time,from_time=0,to_time=0,unit='random',operate_day='everyday',open_time=8,close_time=20):
    if operate_day.lower() in set(('tomorrow','next day','working day')): #adjust operating day
        time += timedelta(days = 1)
        time = time.replace(hour = 8, minute = 0, second = 0)
        
    while operate_day in set(('monday','tuesday','wednesday','thursday','friday')):
        time += timedelta(days = 1)
        time = time.replace(hour = 8, minute = 0, second = 0)
        
        if time.strftime("%A").lower() == operate_day: break
        
    time += rand_time(from_time,to_time,unit) #add random time
    
    #adjust working time
    if (time.hour < open_time): time += timedelta(hours = open_time-time.hour)
    elif (time.hour >= close_time): time += timedelta(hours = 24-close_time+open_time)
    
    #adjust working day
    if time.isoweekday() in set([6,7]): time += timedelta(days = 8 - time.isoweekday())
        
    return time

#random variant number based on a given probability

def rand_var(probability):
    global total_case
    
    if probability > 1: deviation = 0.05
    else: deviation = 0.5
        
    probability /= 100
    
    return round(random.uniform((1-deviation)*probability*total_case, (1+deviation)*probability*total_case))

#new case & incident function    
   
def new_case(case_id, material, customer, supplier):
    global case_table
    
    case = {
        'CASE_ID'           :case_id,
        'MATERIAL_ID'       :material.id,
        'CUSTOMER_ID'       :customer.id,
        'SUPPLIER_ID'       :supplier.id
    }
    case_table = case_table.append(case, ignore_index=True)
    
def new_case_ref(case_id, ref_case_id, material, customer, supplier):
    global case_table
   
    case = {
        'CASE_ID'           :case_id,
        'REF_CASE_ID'       :ref_case_id,
        'MATERIAL_ID'       :material.id,
        'CUSTOMER_ID'       :customer.id,
        'SUPPLIER_ID'       :supplier.id
    }
    case_table = case_table.append(case, ignore_index=True)
    
def new_incident(case_id, activity, sort, timestamp):
    global activity_table
    
    incident = {
        'CASE_ID'           :case_id,
        'ACTIVITY'          :activity,
        'SORT'              :sort,
        'TIMESTAMP'         :timestamp
    }
    activity_table = activity_table.append(incident, ignore_index=True)
    
#case iteration function

#def iterate_case(iteration,activity_list,material,customer):
#    global activity_table
#    
#    case_number = 1
#    
#    for n in range(0,iteration):
#        sort = 1 #initialize current sort
#        timestamp = rand_date(1,5,2021) #initialize timestamp for each case
#        timestamp = add_rand_time(timestamp)
#        
#        for i in range(0,len(activity_list)):
#            normal_duration = activity_list[i]['duration'] #get normal duration
#            material_duration = material.exceptions.get(activity_list[i]['activity_id']) #get material exception duration
#            customer_duration = customer.exceptions.get(activity_list[i]['activity_id']) #get customer exception duration
#            
#            if not material_duration and not customer_duration: #add timestamp without exceptions
#                timestamp = add_rand_time(timestamp,normal_duration[0],normal_duration[1],normal_duration[2],activity_list[i]['operate_day'])
#            else: #add timestamp with exceptions
#                timestamp = add_rand_time(timestamp,0,0,'s',activity_list[i]['operate_day'])
#                if material_duration: timestamp = add_rand_time(timestamp,material_duration[0],material_duration[1],material_duration[2])
#                if customer_duration: timestamp = add_rand_time(timestamp,customer_duration[0],customer_duration[1],customer_duration[2])
#            
#            case_id = activity_list[i]['activity_id'][0:2] + '%04d'%case_number #initialize case_id from prefix & case_number
#            new_incident(case_id, activity_list[i]['activity'], i+1, timestamp)
#            
#        new_case(case_id, material, customer)
#        case_number += 1
    

def iterate_case(iteration, activity_list, material, customer, supplier):
    global activity_table, case_table
    global SA_case_number, PR_case_number, PL_case_number, PU_case_number
    
    for n in range(0,iteration):
        timestamp = rand_date(1,5,2021) #initialize timestamp for each case
        timestamp = add_rand_time(timestamp)
        
        case_id = activity_list[0]['activity_id'][0:2] + '-%04d'%SA_case_number #initialize case_id from prefix & case_number
        
        for i in range(0,len(activity_list)):
            if activity_list[i]['activity_id'] == 'SAPR':
                timestamp = MP.PR_run(timestamp, case_id, material, customer, supplier)
            else:    
                normal_duration = activity_list[i]['duration'] #get normal duration
                material_duration = material.exceptions.get(activity_list[i]['activity_id']) #get material exception duration
                customer_duration = customer.exceptions.get(activity_list[i]['activity_id']) #get customer exception duration
                supplier_duration = supplier.exceptions.get(activity_list[i]['activity_id']) #get customer exception duration
            
                if not material_duration and not customer_duration and not supplier_duration: #add timestamp without exceptions
                    timestamp = add_rand_time(timestamp,normal_duration[0],normal_duration[1],normal_duration[2],activity_list[i]['operate_day'])
                else: #add timestamp with exceptions
                    timestamp = add_rand_time(timestamp,0,0,'s',activity_list[i]['operate_day'])
                    if material_duration: timestamp = add_rand_time(timestamp,material_duration[0],material_duration[1],material_duration[2])
                    if customer_duration: timestamp = add_rand_time(timestamp,customer_duration[0],customer_duration[1],customer_duration[2])
                    if supplier_duration: timestamp = add_rand_time(timestamp,supplier_duration[0],supplier_duration[1],supplier_duration[2])
                
                new_incident(case_id, activity_list[i]['activity'], i+1, timestamp)
                   
        new_case(case_id, material, customer, supplier)
        SA_case_number += 1
        
        
def PR_create_case(timestamp, ref_case_id, activity_list, material, customer, supplier):
    global activity_table, case_table
    global SA_case_number, PR_case_number, PL_case_number, PU_case_number
        
    case_id = activity_list[0]['activity_id'][0:2] + '-%04d'%PR_case_number #case_id from prefix & case_number
    
    for i in range(0,len(activity_list)):
        if activity_list[i]['activity_id'] == 'PRPL':
            timestamp = MP.PL_run(timestamp, case_id, material, customer, supplier)
        elif activity_list[i]['activity_id'] == 'PRPU':
            timestamp = MP.PU_run(timestamp, case_id, material, customer, supplier)
        else:
            normal_duration = activity_list[i]['duration'] #get normal duration
            material_duration = material.exceptions.get(activity_list[i]['activity_id']) #get material exception duration
            customer_duration = customer.exceptions.get(activity_list[i]['activity_id']) #get customer exception duration
            supplier_duration = supplier.exceptions.get(activity_list[i]['activity_id']) #get customer exception duration
            
            if not material_duration and not customer_duration and not supplier_duration: #add timestamp without exceptions
                timestamp = add_rand_time(timestamp,normal_duration[0],normal_duration[1],normal_duration[2],activity_list[i]['operate_day'])
            else: #add timestamp with exceptions
                timestamp = add_rand_time(timestamp,0,0,'s',activity_list[i]['operate_day'])
                if material_duration: timestamp = add_rand_time(timestamp,material_duration[0],material_duration[1],material_duration[2])
                if customer_duration: timestamp = add_rand_time(timestamp,customer_duration[0],customer_duration[1],customer_duration[2])
                if supplier_duration: timestamp = add_rand_time(timestamp,supplier_duration[0],supplier_duration[1],supplier_duration[2])
            
            new_incident(case_id, activity_list[i]['activity'], i+1, timestamp)
            
    new_case_ref(case_id, ref_case_id, material, customer, supplier)
    PR_case_number += 1
    
    return timestamp


def PL_create_case(timestamp, ref_case_id, activity_list, material, customer, supplier):
    global activity_table, case_table
    global SA_case_number, PR_case_number, PL_case_number, PU_case_number
    
    case_id = activity_list[0]['activity_id'][0:2] + '-%04d'%PL_case_number #case_id from prefix & case_number
    
    for i in range(0,len(activity_list)):
        normal_duration = activity_list[i]['duration'] #get normal duration
        material_duration = material.exceptions.get(activity_list[i]['activity_id']) #get material exception duration
        customer_duration = customer.exceptions.get(activity_list[i]['activity_id']) #get customer exception duration
        supplier_duration = supplier.exceptions.get(activity_list[i]['activity_id']) #get customer exception duration
            
        if not material_duration and not customer_duration and not supplier_duration: #add timestamp without exceptions
            timestamp = add_rand_time(timestamp,normal_duration[0],normal_duration[1],normal_duration[2],activity_list[i]['operate_day'])
        else: #add timestamp with exceptions
            timestamp = add_rand_time(timestamp,0,0,'s',activity_list[i]['operate_day'])
            if material_duration: timestamp = add_rand_time(timestamp,material_duration[0],material_duration[1],material_duration[2])
            if customer_duration: timestamp = add_rand_time(timestamp,customer_duration[0],customer_duration[1],customer_duration[2])
            if supplier_duration: timestamp = add_rand_time(timestamp,supplier_duration[0],supplier_duration[1],supplier_duration[2])
            
        new_incident(case_id, activity_list[i]['activity'], i+1, timestamp)
            
    new_case_ref(case_id, ref_case_id, material, customer, supplier)
    PL_case_number += 1
    
    return timestamp

def PU_create_case(timestamp, ref_case_id, activity_list, material, customer, supplier):
    global activity_table, case_table
    global SA_case_number, PR_case_number, PL_case_number, PU_case_number
        
    case_id = activity_list[0]['activity_id'][0:2] + '-%04d'%PU_case_number #case_id from prefix & case_number
        
    for i in range(0,len(activity_list)):
        normal_duration = activity_list[i]['duration'] #get normal duration
        material_duration = material.exceptions.get(activity_list[i]['activity_id']) #get material exception duration
        customer_duration = customer.exceptions.get(activity_list[i]['activity_id']) #get customer exception duration
        supplier_duration = supplier.exceptions.get(activity_list[i]['activity_id']) #get customer exception duration
            
        if not material_duration and not customer_duration and not supplier_duration: #add timestamp without exceptions
            timestamp = add_rand_time(timestamp,normal_duration[0],normal_duration[1],normal_duration[2],activity_list[i]['operate_day'])
        else: #add timestamp with exceptions
            timestamp = add_rand_time(timestamp,0,0,'s',activity_list[i]['operate_day'])
            if material_duration: timestamp = add_rand_time(timestamp,material_duration[0],material_duration[1],material_duration[2])
            if customer_duration: timestamp = add_rand_time(timestamp,customer_duration[0],customer_duration[1],customer_duration[2])
            if supplier_duration: timestamp = add_rand_time(timestamp,supplier_duration[0],supplier_duration[1],supplier_duration[2])
            
        new_incident(case_id, activity_list[i]['activity'], i+1, timestamp)
            
    new_case_ref(case_id, ref_case_id, material, customer, supplier)
    PU_case_number += 1
    
    return timestamp


#sort case_id by timestamp

def resort(activity_table):
    activity_table = activity_table.sort_values(by=['TIMESTAMP'], ignore_index=True) #sort table by timestamp
    
    total_incident = activity_table.shape[0]

    unsorted_case = activity_table.loc[:,'CASE_ID'].values.tolist()
    unsorted_number = ['%04d'%int(i.split('-')[1]) for i in unsorted_case]
    
    sorted_number = [0] 

    for i in range(0,total_incident): #sort case_id by timestamp
        if not unsorted_number[i] in sorted_number:
            sorted_number.append(unsorted_number[i])
    
    return activity_table, sorted_number

def rearrange(case_table, activity_table, case_number, sorted_number, ref_sorted_number): 
    total_incident = activity_table.shape[0]
    
    for i in range(0,total_incident): #adjust case_id based on timestamp    
        activity_table.loc[i,'CASE_ID'] = activity_table.loc[i,'CASE_ID'][0:2] + '-%04d'  %sorted_number.index(activity_table.loc[i,'CASE_ID'][3:7])
    
    for i in range(0,case_number-1): #adjust case_id based on timestamp
        case_table.loc[i,'CASE_ID'] = case_table.loc[i,'CASE_ID'][0:2] + '-%04d'      %sorted_number.index(case_table.loc[i,'CASE_ID'][3:7])
        if type(case_table.loc[i,'REF_CASE_ID']) == str: case_table.loc[i,'REF_CASE_ID'] = case_table.loc[i,'REF_CASE_ID'][0:2] + '-%04d'  %ref_sorted_number.index(case_table.loc[i,'REF_CASE_ID'][3:7])
    
    activity_table = activity_table.sort_values(by=['CASE_ID','SORT'], ignore_index=True)
    case_table = case_table.sort_values(by=['CASE_ID'], ignore_index=True)
    
    return case_table, activity_table

def resort_rearrange():
    global SA_case_number, PR_case_number, PL_case_number, PU_case_number
    global SA_activity_table, PR_activity_table, PL_activity_table, PU_activity_table
    global SA_case_table, PR_case_table, PL_case_table, PU_case_table
    
    SA_activity_table, SA_sorted_number = resort(SA_activity_table) 
    PR_activity_table, PR_sorted_number = resort(PR_activity_table)
    PL_activity_table, PL_sorted_number = resort(PL_activity_table)
    PU_activity_table, PU_sorted_number = resort(PU_activity_table)
    
    SA_case_table, SA_activity_table = rearrange(SA_case_table, SA_activity_table, SA_case_number, SA_sorted_number, SA_sorted_number)
    PR_case_table, PR_activity_table = rearrange(PR_case_table, PR_activity_table, PR_case_number, PR_sorted_number, SA_sorted_number)
    PL_case_table, PL_activity_table = rearrange(PL_case_table, PL_activity_table, PL_case_number, PL_sorted_number, PR_sorted_number)
    PU_case_table, PU_activity_table = rearrange(PU_case_table, PU_activity_table, PU_case_number, PU_sorted_number, PR_sorted_number)
    

#split, rearrange, and export tables as csv

def export_table():
    global case_table, activity_table
    global SA_activity_table, PR_activity_table, PL_activity_table, PU_activity_table
    global SA_case_table, PR_case_table, PL_case_table, PU_case_table
    global SA_case_number, PR_case_number, PL_case_number, PU_case_number
    
    #split main activity_table based on the processes
    
    SA_activity_table = pd.DataFrame(columns = ['CASE_ID','ACTIVITY','SORT','TIMESTAMP'])
    SA_case_table = pd.DataFrame(columns = ['CASE_ID','REF_CASE_ID','MATERIAL_ID','CUSTOMER_ID','SUPPLIER_ID'])
    
    PR_activity_table = pd.DataFrame(columns = ['CASE_ID','ACTIVITY','SORT','TIMESTAMP'])
    PR_case_table = pd.DataFrame(columns = ['CASE_ID','REF_CASE_ID','MATERIAL_ID','CUSTOMER_ID','SUPPLIER_ID'])

    PL_activity_table = pd.DataFrame(columns = ['CASE_ID','ACTIVITY','SORT','TIMESTAMP'])
    PL_case_table = pd.DataFrame(columns = ['CASE_ID','REF_CASE_ID','MATERIAL_ID','CUSTOMER_ID','SUPPLIER_ID'])
    
    PU_activity_table = pd.DataFrame(columns = ['CASE_ID','ACTIVITY','SORT','TIMESTAMP'])
    PU_case_table = pd.DataFrame(columns = ['CASE_ID','REF_CASE_ID','MATERIAL_ID','CUSTOMER_ID','SUPPLIER_ID'])

    for i in range(0,activity_table.shape[0]):
        if activity_table.loc[i,'CASE_ID'][0:2] == 'SA':
            SA_activity_table = SA_activity_table.append(activity_table.loc[i], ignore_index=True)
        elif activity_table.loc[i,'CASE_ID'][0:2] == 'PR':
            PR_activity_table = PR_activity_table.append(activity_table.loc[i], ignore_index=True)
        elif activity_table.loc[i,'CASE_ID'][0:2] == 'PL':
            PL_activity_table = PL_activity_table.append(activity_table.loc[i], ignore_index=True)
        elif activity_table.loc[i,'CASE_ID'][0:2] == 'PU':
            PU_activity_table = PU_activity_table.append(activity_table.loc[i], ignore_index=True)
        
    for i in range(0,case_table.shape[0]):
        if case_table.loc[i,'CASE_ID'][0:2] == 'SA':
            SA_case_table = SA_case_table.append(case_table.loc[i], ignore_index=True)
        elif case_table.loc[i,'CASE_ID'][0:2] == 'PR':
            PR_case_table = PR_case_table.append(case_table.loc[i], ignore_index=True)
        elif case_table.loc[i,'CASE_ID'][0:2] == 'PL':
            PL_case_table = PL_case_table.append(case_table.loc[i], ignore_index=True)
        elif case_table.loc[i,'CASE_ID'][0:2] == 'PU':
            PU_case_table = PU_case_table.append(case_table.loc[i], ignore_index=True)
    
    #rearrange table by timestamp
    
    resort_rearrange()
    
    #export table as csv
    
    SA_activity_table = SA_activity_table.reset_index(drop=True)
    SA_activity_table.to_csv(os.getcwd()+"/"+"output"+"/"+"SA_ACTIVITY_TABLE_test.csv", index=False)

    SA_case_table = SA_case_table.reset_index(drop=True)
    SA_case_table.to_csv(os.getcwd()+"/"+"output"+"/"+"SA_CASE_TABLE_test.csv", index=False)
    
    PR_activity_table = PR_activity_table.reset_index(drop=True)
    PR_activity_table.to_csv(os.getcwd()+"/"+"output"+"/"+"PR_ACTIVITY_TABLE_test.csv", index=False)

    PR_case_table = PR_case_table.reset_index(drop=True)
    PR_case_table.to_csv(os.getcwd()+"/"+"output"+"/"+"PR_CASE_TABLE_test.csv", index=False)
    
    PL_activity_table = PL_activity_table.reset_index(drop=True)
    PL_activity_table.to_csv(os.getcwd()+"/"+"output"+"/"+"PL_ACTIVITY_TABLE_test.csv", index=False)

    PL_case_table = PL_case_table.reset_index(drop=True)
    PL_case_table.to_csv(os.getcwd()+"/"+"output"+"/"+"PL_CASE_TABLE_test.csv", index=False)
    
    PU_activity_table = PU_activity_table.reset_index(drop=True)
    PU_activity_table.to_csv(os.getcwd()+"/"+"output"+"/"+"PU_ACTIVITY_TABLE_test.csv", index=False)

    PU_case_table = PU_case_table.reset_index(drop=True)
    PU_case_table.to_csv(os.getcwd()+"/"+"output"+"/"+"PU_CASE_TABLE_test.csv", index=False)