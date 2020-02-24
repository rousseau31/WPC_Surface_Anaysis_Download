"""
Python 3
Created on January 25, 2020

@author: Nicholas Rousseau
https://github.com/rousseau31
https://www.linkedin.com/in/nicholas-rousseau/

"""

#imports
import os
import urllib.request
from datetime import date, timedelta



def Time_MOD(Hour):
    if int(Hour) < 10:
        return '0'+ str(Hour)
    else:
        return str(Hour)

def Pull_WPC_Sf(start_year, start_month, start_day, end_year, end_month, end_day):
            
                    
    #start_date = date(2018,12,28)
    #end_date = date(2019,1,5) 
    
    start_date = date(start_year,start_month,start_day)
    end_date = date(end_year,end_month,end_day) 
    
    delta = end_date - start_date       # as timedelta
    
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        print(day)
        
        createFolder('./WPC_Surface_Anaysis/'+ str(day))
    
        Year, Month, Day = str(day).split('-')
        for Hour in range(0,24,+3):
    
            Year = str(Year)    
            Month = str(Month)
            Day = str(Day)
            Hour = str(Hour)
            
            #time.sleep(20) 
            
            FileNameDate = Year + (Month) + (Day) + (Hour) + 'WPC_SA'
            print('https://www.wpc.ncep.noaa.gov/archives/sfc/'+ Year + '/lrgnamsfc'+ Year + (Month) + (Day) + Time_MOD(Hour) +'.gif')
            try:
                urllib.request.urlretrieve('https://www.wpc.ncep.noaa.gov/archives/sfc/'+ Year + '/lrgnamsfc'+ Year + (Month) + (Day) + Time_MOD(Hour) +'.gif',  'WPC_Surface_Anaysis/'+ str(day) +'/' + FileNameDate + 'WPC_Surf' + '.png')
                print(":)")
            except: 
                print('Nope')
   
def createFolder(directory):
    try:
        if not os.path.exists(directory):
                    os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
createFolder('./WPC_Surface_Anaysis/')






#Dates of study start(year,month,day) - end(year,month,day)

##2018/2/6","2018/2/7"

Pull_WPC_Sf(2018,12,28,2019,1,5)
print('Done')