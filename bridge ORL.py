i# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:53:59 2020

@author: WCHC3A
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import datetime
#from fuzzywuzzy import fuzz 
#from fuzzywuzzy import process    
bridge12=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\12_Dec_2019_Bridge_Specimen_Compliance.xlsx",sheet_name='Raw Data')
#bridge12orl=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\12_Dec_2019_Bridge_Specimen_Compliance_orl.xlsx",sheet_name='Raw Data')
bridge11=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\11_Nov_2019_Bridge_Specimen_Compliance1.xlsx",sheet_name='Raw Data')
bridge10=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\10_Oct_2019_Bridge_Specimen_Compliance.xlsx",sheet_name='Raw Data')
bridge9=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\09_Sep_2019_Bridge_Specimen_Compliance.xlsx",sheet_name='Raw Data')
bridge8=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\08_Aug_2019_Bridge_Specimen_Compliance.xlsx",sheet_name='Raw Data')
bridge7=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\07_Jul_2019_Bridge_Specimen_Compliance.xlsx",sheet_name='Raw Data')
#bridge6=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\06_Jun_2019_Bridge_Specimen_Compliance.xlsx",sheet_name='Raw Data')
bridge712 =bridge7.append([bridge8,bridge9,bridge10,bridge11,bridge12])
bridge712['TEST_UPPER'] =bridge712['Test'].str.upper()
bridge712orl=bridge712[bridge712['Facility ']=='FH Orlando']
bridge712orl['PtOrderLoc']=bridge712orl['Nurse Unit'].str.slice(4, 9)
bridge712orl['PtOrderLoc'].str.strip()
#bridge712["Collection date/time"]=pd.to_datetime(bridge712["Collection date/time"])
#bridge712["Collection date/time new"]=bridge712["Collection date/time"].dt.strftime('%m/%d/%Y')
bridge712orlunit=bridge712orl[['PtOrderLoc']]
bridge712orlunitdis=bridge712orlunit.drop_duplicates()
bridge712orlfin=bridge712orl[["FIN"]]
bridge712orlgrofin=bridge712orlfin.drop_duplicates()
#12 only#
bridge12orl=bridge12[bridge12['Facility ']=='FH Orlando']
bridge12orl['PtOrderLoc']=bridge12orl['Nurse Unit'].str.slice(4, 9)
bridge12orl['PtOrderLoc'].str.strip()
bridge12orl["Collection date/time"]=pd.to_datetime(bridge12orl["Collection date/time"])
bridge12orl['Day'] = bridge12orl["Collection date/time"].dt.day
#bridge12orl["Collection date/time new"]=bridge12orl["Collection date/time"].dt.strftime('%m/%d/%Y') 
bridge12orlfin=bridge12orl[["FIN"]]
bridge12orlgrofin=bridge12orlfin.drop_duplicates()
bridge12orlgrofin.to_csv(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\b12.csv")

#11only#
bridge11orl=bridge11[bridge11['Facility ']=='FH Orlando']
bridge11orl['PtOrderLoc']=bridge11orl['Nurse Unit'].str.slice(4, 9)
bridge11orl['PtOrderLoc'].str.strip()
bridge11orl["Collection date/time"]=pd.to_datetime(bridge11orl["Collection date/time"])
bridge11orl['Day'] = bridge11orl["Collection date/time"].dt.day
#bridge12orl["Collection date/time new"]=bridge12orl["Collection date/time"].dt.strftime('%m/%d/%Y') 
bridge11orlfin=bridge11orl[["FIN"]]
bridge11orlgrofin=bridge11orlfin.drop_duplicates()
bridge11orlgrofin.to_csv(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\b11.csv")
#10
bridge10orl=bridge10[bridge10['Facility ']=='FH Orlando']
bridge10orl['PtOrderLoc']=bridge10orl['Nurse Unit'].str.slice(4, 9)
bridge10orl['PtOrderLoc'].str.strip()
bridge10orl["Collection date/time"]=pd.to_datetime(bridge10orl["Collection date/time"])
bridge10orl['Day'] = bridge10orl["Collection date/time"].dt.day
#bridge12orl["Collection date/time new"]=bridge12orl["Collection date/time"].dt.strftime('%m/%d/%Y') 
bridge10orlfin=bridge10orl[["FIN"]]
bridge10orlgrofin=bridge10orlfin.drop_duplicates()
bridge10orlgrofin.to_csv(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\b10.csv")
#9
bridge9orl=bridge9[bridge9['Facility ']=='FH Orlando']
bridge9orl['PtOrderLoc']=bridge9orl['Nurse Unit'].str.slice(4, 9)
bridge9orl['PtOrderLoc'].str.strip()
bridge9orl["Collection date/time"]=pd.to_datetime(bridge9orl["Collection date/time"])
bridge9orl['Day'] = bridge9orl["Collection date/time"].dt.day
#bridge12orl["Collection date/time new"]=bridge12orl["Collection date/time"].dt.strftime('%m/%d/%Y') 
bridge9orlfin=bridge9orl[["FIN"]]
bridge9orlgrofin=bridge9orlfin.drop_duplicates()
bridge9orlgrofin.to_csv(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\b9.csv")
#8
bridge8orl=bridge8[bridge8['Facility ']=='FH Orlando']
bridge8orl['PtOrderLoc']=bridge8orl['Nurse Unit'].str.slice(4, 9)
bridge8orl['PtOrderLoc'].str.strip()
bridge8orl["Collection date/time"]=pd.to_datetime(bridge8orl["Collection date/time"])
bridge8orl['Day'] = bridge8orl["Collection date/time"].dt.day
#bridge12orl["Collection date/time new"]=bridge12orl["Collection date/time"].dt.strftime('%m/%d/%Y') 
bridge8orlfin=bridge8orl[["FIN"]]
bridge8orlgrofin=bridge8orlfin.drop_duplicates()
bridge8orlgrofin.to_csv(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\b8.csv")
#7
bridge7orl=bridge7[bridge7['Facility ']=='FH Orlando']
bridge7orl['PtOrderLoc']=bridge7orl['Nurse Unit'].str.slice(4, 9)
bridge7orl['PtOrderLoc'].str.strip()
bridge7orl["Collection date/time"]=pd.to_datetime(bridge7orl["Collection date/time"])
bridge7orl['Day'] = bridge7orl["Collection date/time"].dt.day
#bridge12orl["Collection date/time new"]=bridge12orl["Collection date/time"].dt.strftime('%m/%d/%Y') 
bridge7orlfin=bridge7orl[["FIN"]]
bridge7orlgrofin=bridge7orlfin.drop_duplicates()
bridge7orlgrofin.to_csv(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\b7.csv")


lis121=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1219.xls",sheet_name='Sheet1')
lis122=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1219.xls",sheet_name='Sheet2', header=None)
lis123=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1219.xls",sheet_name='Sheet3', header=None)
lis124=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1219.xls",sheet_name='Sheet4', header=None)
lis125=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1219.xls",sheet_name='Sheet5', header=None)
lis126=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1219.xls",sheet_name='Sheet6', header=None)
lis122.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis123.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis124.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis125.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis126.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']

lis111=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1119.xls",sheet_name='Sheet1')
lis112=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1119.xls",sheet_name='Sheet2', header=None)
lis113=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1119.xls",sheet_name='Sheet3', header=None)
lis114=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1119.xls",sheet_name='Sheet4', header=None)
lis115=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1119.xls",sheet_name='Sheet5', header=None)
lis112.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis113.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis114.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis115.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']


lis101=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1019.xls",sheet_name='Sheet1')
lis102=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1019.xls",sheet_name='Sheet2', header=None)
lis103=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1019.xls",sheet_name='Sheet3', header=None)
lis104=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1019.xls",sheet_name='Sheet4', header=None)
lis105=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1019.xls",sheet_name='Sheet5', header=None)
lis106=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_1019.xls",sheet_name='Sheet6', header=None)
lis102.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis103.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis104.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis105.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis106.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']

lis91=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0919.xls",sheet_name='Sheet1')
lis92=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0919.xls",sheet_name='Sheet2', header=None)
lis93=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0919.xls",sheet_name='Sheet3', header=None)
lis94=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0919.xls",sheet_name='Sheet4', header=None)
lis95=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0919.xls",sheet_name='Sheet5', header=None)
lis96=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0919.xls",sheet_name='Sheet6', header=None)
lis92.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis93.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis94.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis95.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis96.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']

lis81=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0819.xls",sheet_name='Sheet1')
lis82=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0819.xls",sheet_name='Sheet2', header=None)
lis83=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0819.xls",sheet_name='Sheet3', header=None)
lis84=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0819.xls",sheet_name='Sheet4', header=None)
lis85=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0819.xls",sheet_name='Sheet5', header=None)
lis86=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0819.xls",sheet_name='Sheet6', header=None)
lis82.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis83.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis84.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis85.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis86.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']

lis71=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0719.xls",sheet_name='Sheet1')
lis72=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0719.xls",sheet_name='Sheet2', header=None)
lis73=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0719.xls",sheet_name='Sheet3', header=None)
lis74=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0719.xls",sheet_name='Sheet4', header=None)
lis75=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0719.xls",sheet_name='Sheet5', header=None)
lis76=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\Bridge_collect_0719.xls",sheet_name='Sheet6', header=None)
lis72.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis73.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis74.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis75.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']
lis76.columns = ['Acc','mrn','PtOrdAccount','PtOrderLoc','collected', 'BatTstCode','LabDept','recieved','can','PHLEB','opid']


lis12=lis121.append([lis122,lis123,lis124,lis125,lis126])
lis11 =lis111.append([lis112,lis113,lis114,lis115])
lis10 =lis101.append([lis102,lis103,lis104,lis105,lis106])
lis9 =lis91.append([lis92,lis93,lis94,lis95,lis96])
lis8 =lis81.append([lis82,lis83,lis84,lis85,lis86])
lis7 =lis71.append([lis72,lis73,lis74,lis75,lis76])

lis12['PHLEB'].fillna("NO PHLEB", inplace=True)
lis11['PHLEB'].fillna("NO PHLEB", inplace=True)
lis10['PHLEB'].fillna("NO PHLEB", inplace=True)
lis9['PHLEB'].fillna("NO PHLEB", inplace=True)
lis8['PHLEB'].fillna("NO PHLEB", inplace=True)
lis7['PHLEB'].fillna("NO PHLEB", inplace=True)

lis12['BatTstCode'].fillna("NA", inplace=True)
lis11['BatTstCode'].fillna("NA", inplace=True)
lis10['BatTstCode'].fillna("NA", inplace=True)
lis9['BatTstCode'].fillna("NA", inplace=True)
lis8['BatTstCode'].fillna("NA", inplace=True)
lis7['BatTstCode'].fillna("NA", inplace=True)














lis12["collected"]=pd.to_datetime(lis12["collected"])
lis12['Day'] = lis12["collected"].dt.day
lis11["collected"]=pd.to_datetime(lis11["collected"])
lis11['Day'] = lis11["collected"].dt.day
lis10["collected"]=pd.to_datetime(lis10["collected"])
lis10['Day'] = lis10["collected"].dt.day
lis9["collected"]=pd.to_datetime(lis9["collected"])
lis9['Day'] = lis9["collected"].dt.day
lis8["collected"]=pd.to_datetime(lis8["collected"])
lis8['Day'] = lis8["collected"].dt.day
lis7["collected"]=pd.to_datetime(lis7["collected"])
lis7['Day'] = lis7["collected"].dt.day

lis12dayphleb=lis12.groupby(["Day","PHLEB"])["PtOrdAccount"].agg("count").reset_index()
#lis12dayphleb.to_csv(r"H:\Qa\QA_SHARED\vicky chen\data\bridge\lis12dayphleb.csv")
lis11dayphleb=lis11.groupby(["Day","PHLEB"])["PtOrdAccount"].agg("count").reset_index()
#lis11dayphleb.to_csv(r"H:\Qa\QA_SHARED\vicky chen\data\bridge\lis11dayphleb.csv")
lis10dayphleb=lis10.groupby(["Day","PHLEB"])["PtOrdAccount"].agg("count").reset_index()
#lis10dayphleb.to_csv(r"H:\Qa\QA_SHARED\vicky chen\data\bridge\lis10dayphleb.csv")
lis9dayphleb=lis9.groupby(["Day","PHLEB"])["PtOrdAccount"].agg("count").reset_index()
#lis9dayphleb.to_csv(r"H:\Qa\QA_SHARED\vicky chen\data\bridge\lis9dayphleb.csv")
lis8dayphleb=lis8.groupby(["Day","PHLEB"])["PtOrdAccount"].agg("count").reset_index()
#lis8dayphleb.to_csv(r"H:\Qa\QA_SHARED\vicky chen\data\bridge\lis8dayphleb.csv")
lis7dayphleb=lis7.groupby(["Day","PHLEB"])["PtOrdAccount"].agg("count").reset_index()
#lis7dayphleb.to_csv(r"H:\Qa\QA_SHARED\vicky chen\data\bridge\lis7dayphleb.csv")














lis712=lis12.append([lis11,lis10,lis9,lis8,lis7])
lis712["PtOrdAccount"].astype(int)
lis712["FIN"]=lis712["PtOrdAccount"]

lis712fin=lis712[["PtOrdAccount","FIN"]]
lis712gro=lis712fin.drop_duplicates()

lis712loc=lis712[['PtOrderLoc']]
lis712locdis=lis712loc.drop_duplicates()
lis712test=lis712[['BatTstCode']]
lis712testdis=lis712test.drop_duplicates()
#every month

lis12["PtOrdAccount"].astype(int)
lis11["PtOrdAccount"].astype(int)
lis10["PtOrdAccount"].astype(int)
lis9["PtOrdAccount"].astype(int)
lis8["PtOrdAccount"].astype(int)
lis7["PtOrdAccount"].astype(int)

lis12["FIN"]=lis12["PtOrdAccount"]
lis11["FIN"]=lis11["PtOrdAccount"]
lis10["FIN"]=lis10["PtOrdAccount"]
lis9["FIN"]=lis9["PtOrdAccount"]
lis8["FIN"]=lis8["PtOrdAccount"]
lis7["FIN"]=lis7["PtOrdAccount"]

lis12fin=lis12[["PtOrdAccount","FIN"]]
lis12gro=lis12fin.drop_duplicates()
lis11fin=lis11[["PtOrdAccount","FIN"]]
lis11gro=lis11fin.drop_duplicates()
lis10fin=lis10[["PtOrdAccount","FIN"]]
lis10gro=lis10fin.drop_duplicates()
lis9fin=lis9[["PtOrdAccount","FIN"]]
lis9gro=lis9fin.drop_duplicates()
lis8fin=lis8[["PtOrdAccount","FIN"]]
lis8gro=lis8fin.drop_duplicates()
lis7fin=lis7[["PtOrdAccount","FIN"]]
lis7gro=lis7fin.drop_duplicates()



##nurse unit compare
#matchloc=pd.merge(lis712locdis,bridge712unitdis,on="Nurse Unit",how="inner")
#allloc=pd.merge(lis712locdis,bridge712unitdis,on="Nurse Unit",how="outer")
#locbri=allloc[allloc["PtOrderLoc"].isnull()]
#loclis=allloc[allloc["Nurse Unit"].isnull()]

#bridge712unitdis.to_csv(r"H:\Qa\QA_SHARED\vicky chen\data\bridge712unitdis.csv")
#lis712locdis.to_csv(r"H:\Qa\QA_SHARED\vicky chen\data\lis712locdis.csv")

#lis12test.to_csv(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\LIS Reports\lis12test.csv")
#lis129099=lis12[lis12["PHLEB"]==9099]
#lis12gro=lis12.groupby(["PtOrdAccount"])["PtOrderLoc"].agg('count').reset_index()




#lis11gro=lis11.groupby(["PtOrdAccount"])["PtOrderLoc"].agg('count').reset_index()





#lis12["Collection date/time new"]=lis12["collected"].dt.strftime('%m/%d/%Y')
#bridge12["key"]=bridge12["FIN"].astype(str)+"-"+bridge12["Nurse Unit"].astype(str)+"-"+bridge12["Collection date/time new"].astype(str)
#lis12["key"]=lis12["PtOrdAccount"].astype(str)+"-"+lis12["PtOrderLoc"].astype(str)+"-"+lis12["Collection date/time new"].astype(str)
#bridge12["key"]=bridge12["FIN"].astype(str)+"-"+bridge12["Collection date/time new"].astype(str)
#lis12["key"]=lis12["PtOrdAccount"].astype(str)+"-"+lis12["Collection date/time new"].astype(str)

#bl12=pd.merge(lis12gro,bridge12orlgrofin,on="FIN",how="outer")
bl12in=pd.merge(lis12gro,bridge12orlgrofin,on="FIN",how="inner")
#bl11=pd.merge(lis11gro,bridge11orlgrofin,on="FIN",how="outer")
bl11in=pd.merge(lis11gro,bridge11orlgrofin,on="FIN",how="inner")
bl10in=pd.merge(lis10gro,bridge10orlgrofin,on="FIN",how="inner")
bl9in=pd.merge(lis9gro,bridge9orlgrofin,on="FIN",how="inner")
bl8in=pd.merge(lis8gro,bridge8orlgrofin,on="FIN",how="inner")
bl7in=pd.merge(lis7gro,bridge7orlgrofin,on="FIN",how="inner")
bl712in=pd.merge(lis712gro,bridge712orlgrofin,on="FIN",how="inner")


option712=bl712in["FIN"]
bl712inlis=lis712[lis712["FIN"].isin(option712)]
bl712inlisgro=bl712inlis.groupby(["PHLEB"])["FIN"].nunique().reset_index()
#all month


option12=bl12in["FIN"]
bl12inlis=lis12[lis12["FIN"].isin(option12)]
bl12inlisgro=bl12inlis.groupby(["PHLEB"])["FIN"].nunique().reset_index()

option11=bl11in["FIN"]
bl11inlis=lis11[lis11["FIN"].isin(option11)]
bl11inlisgro=bl11inlis.groupby(["PHLEB"])["FIN"].nunique().reset_index()

option10=bl10in["FIN"]
bl10inlis=lis10[lis10["FIN"].isin(option10)]
bl10inlisgro=bl10inlis.groupby(["PHLEB"])["FIN"].nunique().reset_index()

option9=bl9in["FIN"]
bl9inlis=lis9[lis9["FIN"].isin(option9)]
bl9inlisgro=bl9inlis.groupby(["PHLEB"])["FIN"].nunique().reset_index()

option8=bl8in["FIN"]
bl8inlis=lis8[lis8["FIN"].isin(option8)]
bl8inlisgro=bl8inlis.groupby(["PHLEB"])["FIN"].nunique().reset_index()

option7=bl7in["FIN"]
bl7inlis=lis7[lis7["FIN"].isin(option7)]
bl7inlisgro=bl7inlis.groupby(["PHLEB"])["FIN"].nunique().reset_index()


#bridge12orl["key"]=bridge12orl["FIN"].astype(str)+"-"+bridge12orl["Day"].astype(str)+"-"+bridge12orl['PtOrderLoc'].astype(str)
#bridge12orl["key"].astype(str)
#lis12["key"]=lis12["PtOrdAccount"].astype(str)+"-"+lis12["Day"].astype(str)+"-"+lis12["PtOrderLoc"].astype(str)
#lis12["key"].astype(str)
#lis129099=lis12[lis12['PHLEB']==9099]
#lis129099["key"]=lis129099["PtOrdAccount"].astype(str)+"-"+lis129099["Day"].astype(str)+"-"+lis129099["PtOrderLoc"].astype(str)
#lis129099["key"].astype(str)
#bl12lis9099=pd.merge(lis129099[["key"]],bridge12orl[["key"]],on="key",how="inner")
#bl12lis=pd.merge(lis12[["key"]],bridge12orl[["key"]],on="key",how="inner")






#testfuzzy=pd.read_excel(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\test fuzzy.xlsx",sheet_name='match')
#option=bl12in["FIN"]
#bridge12in=bridge12[bridge12["FIN"].isin(option)]
#lis12["FIN"]=lis12["PtOrdAccount"]
#lis12["Code"]=lis12["BatTstCode"]
#lis12["Nurse Unit"]=lis12["PtOrderLoc"]
#lis12in=lis12[lis12["FIN"].isin(option)]

#bridge12infuzzy=pd.merge(bridge12in,testfuzzy,on="TEST_UPPER",how="left")

#bridge12infuzzy["key"]=bridge12infuzzy["FIN"].astype(str)+"-"+bridge12infuzzy["Code"].astype(str)
#lis12in["key"]=lis12in["PtOrdAccount"].astype(str)+"-"+lis12in["Code"].astype(str)
#bridge12infuzzy["Collection date/time new"].astype(str)
#lis12in["Collection date/time new"].astype(str)





#match=pd.merge(lis12in[["FIN","Code","Nurse Unit","PtOrderLoc","collected"]],bridge12infuzzy[["FIN","Code","Nurse Unit","TEST_UPPER","Collection date/time"]],on=['FIN', 'Code'],how="inner")

#match.to_csv(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\match.csv")





#####test###
#bridge612 =bridge6.append([bridge7,bridge8,bridge9,bridge10,bridge11,bridge12])
#bridge612['Nurse Unit']=bridge12['Nurse Unit'].str.slice(4, 9)
#bridge612drop=bridge612.drop(columns=['Facility ',
# 'Nurse Unit',
# 'FIN',
# 'Wristband scanned?',
# 'Scanned to confirm?',
# 'Collection date/time',
# 'Collector OPID',
# 'Collector last name',
# 'Collector first name',
# 'Manual confirm reason',
# 'Reason for Manual Confirmation'])
#bridge612test=bridge612drop.drop_duplicates()
#bridge612test['TEST_UPPER'] =bridge612test['Test'].str.upper()
#bridge612test.to_csv(r"H:\Qa\QA_SHARED\LAB UTILIZATION\Lab Utilization\Bridge Compliance\Bridge Reports\bridgetest.csv")
####test
#lis712drop=lis712.drop(columns=['Acc',
# 'mrn',
# 'PtOrdAccount',
# 'PtOrderLoc',
# 'collected',
# 'LabDept',
# 'recieved',
# 'can',
# 'PHLEB',
# 'opid'])
#lis712test=lis712drop.drop_duplicates()


#list= ["E","S","P","C","W","D","N","6"]
#A=bridge712[bridge712["Nurse Unit"].isin(list)]