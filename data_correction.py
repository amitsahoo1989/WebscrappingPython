from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen
import csv,time 
    

def getdetails(URL):
    req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    
    table = soup.find('table',attrs={"class":"weatherhistory_results"})
    to_add=[]
    try:
        min_temp = table.find('tr',attrs={"class":"weatherhistory_results_datavalue temp_mn"})
        if('class="nullvalue">No data.' in str(min_temp)):
            ##print("No data")
            to_add.append('')
        else:
            min_temp=min_temp.find('span',attrs={"class":"value"})
            min_temp=(str(min_temp.contents).strip("['']"))
            to_add.append(min_temp)
            ##print(to_add)
        
        mean_temp = table.find('tr',attrs={"class":"weatherhistory_results_datavalue temp"})
        if('class="nullvalue">No data.' in str(mean_temp)):
            ##print("No data")
            to_add.append('')
        else:
            mean_temp=mean_temp.find('span',attrs={"class":"value"})
            mean_temp=(str(mean_temp.contents).strip("['']"))
            to_add.append(mean_temp)
            ##print(to_add)
    
        max_temp = table.find('tr',attrs={"class":"weatherhistory_results_datavalue temp_mx"})
        if('class="nullvalue">No data.' in str(max_temp)):
            ##print("No data")
            to_add.append('')
        else:
            max_temp = max_temp.find('span',attrs={"class":"value"})
            max_temp=(str(max_temp.contents).strip("['']"))
            to_add.append(max_temp)
            ##print(to_add)
    
        sea_lvl_pres = table.find('tr',attrs={"class":"weatherhistory_results_datavalue slp"})
        if('class="nullvalue">No data.' in str(sea_lvl_pres)):
            ##print("No data")
            to_add.append('')
        else:
            sea_lvl_pres=sea_lvl_pres.find('span',attrs={"class":"value"})
            sea_lvl_pres=(str(sea_lvl_pres.contents).strip("['']"))
            to_add.append(sea_lvl_pres)
            ##print(to_add)
        
    
        dew_pnt = table.find('tr',attrs={"class":"weatherhistory_results_datavalue dewp"})
        if ('class="nullvalue">No data.' in str(dew_pnt)):
            ##print('No data')
            to_add.append('')
        else:
            dew_pnt= dew_pnt.find('span',attrs={"class":"value"})
            dew_pnt=(str(dew_pnt.contents).strip("['']"))
            to_add.append(dew_pnt)
            #print(to_add)
        
        prcp = table.find('tr',attrs={"class":"weatherhistory_results_datavalue prcp"})
        if ('class="nullvalue">No data.' in str(prcp)):
            ##print('No data')
            to_add.append('')
    
        else:
            prcp= prcp.find('span',attrs={"class":"value"})
            prcp=(str(prcp.contents).strip("['']"))
            to_add.append(prcp)
            #print(to_add)
        
        visib = table.find('tr',attrs={"class":"weatherhistory_results_datavalue visib"})
        if ('class="nullvalue">No data.' in str(visib)):
            ##print('No data')
            to_add.append('')
        else:
            visib= visib.find('span',attrs={"class":"value"})
            visib=(str(visib.contents).strip("['']"))
            to_add.append(visib)
            #print(to_add)
                
        wdsp = table.find('tr',attrs={"class":"weatherhistory_results_datavalue wdsp"})
        if ('class="nullvalue">No data.' in str(wdsp)):
            #print('No data')
            to_add.append('')
        else:
            wdsp= wdsp.find('span',attrs={"class":"value"})
            wdsp=(str(wdsp.contents).strip("['']"))
            to_add.append(wdsp)
            #print(to_add)
        
        mxspd = table.find('tr',attrs={"class":"weatherhistory_results_datavalue mxspd"})
        if ('class="nullvalue">No data.' in str(mxspd)):
            #print('No data')
            to_add.append('')
        else:
            mxspd= mxspd.find('span',attrs={"class":"value"})
            mxspd=(str(mxspd.contents).strip("['']"))
            to_add.append(mxspd)
            #print(to_add)
        gust = table.find('tr',attrs={"class":"weatherhistory_results_datavalue gust"})
        if ('class="nullvalue">No data.' in str(gust)):
            #print('No data')
            to_add.append('')
        else:
            gust= gust.find('span',attrs={"class":"value"})
            gust=(str(gust.contents).strip("['']"))
            to_add.append(gust)
        
        metro_values=to_add
        
    except:
        metro_values=['', '', '', '', '', '', '', '', '', '']
    
    return metro_values

path=r'C:\Users\toshiba\Desktop\fire forest\data_per_day\Day1\Day1.csv'

my_dict={}
with open(path,'r') as file:
    reader=csv.DictReader(file)
    counter=1
    for i in reader:
        if (i['Remarks'] !=''):
            print(counter)
            if (counter%15==0):
                time.sleep(60)
            metro_values=getdetails(i['URL'])
            metro_values.insert(0,i['URL'])
            metro_values.insert(1,'')
            #print(metro_values)
            my_dict.update({i['URL']:metro_values})
            counter=counter+1
            

import pandas as pd
df=pd.read_csv(path)
print(df.columns)

for k in my_dict.keys():
    #print(k)
    for i,j in enumerate(df['URL']):
        if (j==k):
            #print(my_dict[k])
            
            #print(df.iloc[i])
            #print(my_dict[k])
            df.iloc[i]=my_dict[k]
            #print(df.iloc[i])
            
df.to_csv (r'C:\Users\toshiba\Desktop\fire forest\Images\day1_correction.csv', index = False, header=True)   
    