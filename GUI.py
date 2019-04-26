import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb


UL_Main_Data= pd.read_csv('324_UL.csv')
LD_Main_Data = pd.read_csv('324_LD.csv')

# Next couple lines imports the data from the files and names the columns of the dataframe
UL_Main_Data.columns = ['Pro','UL','Dock','Ship','Pcs','Wgt','ULTrlr','ULDoor',
                        'UnloadTS','UnLoadDOW','LoadInterval','Org',
                        'UnloadDate','UnloadTime']

LD_Main_Data.columns = ['Pro','L','Dock','Ship','Pcs','Wgt','LdTrlr','LdDoor',
                        'LoadTS','LoadDOW','LoadIntberval','Dest','LoadTo',
                        'LoadToParent','LoadDate','LoadTime']

#The line below deletes the UL and Org column since it is not needed when analyzing UL
UL_Data1 = UL_Main_Data.drop(['UL','Org'], axis = 1)
UL_Data1 = UL_Main_Data.columns = ['Pro','UL','Dock','Ship','Pcs','Wgt',
                                   'ULTrlr','ULDoor','UnloadTS','UnLoadDOW',
                                   'LoadInterval','Org','UnloadDate',
                                   'UnloadTime']

#Finding Wgt congestion per door per day
Wgt_cong_UL_data = UL_Data1.drop(['Dock','Ship','Pcs','ULTrlr','UnloadTS',
                                  'UnLoadDOW','LoadInterval'], axis = 1)
Wgt_cong_UL_data


#Sort df by date
Wgt_cong_UL_data.sort_values(by = ['UnloadDate','UnloadTime'], inplace = True)
Wgt_cong_UL_data = Wgt_cong_UL_data.reset_index(drop = True)
Wgt_cong_UL_data

i = 0
#j = 0 #i and j will be used as counters for the if loop

#len(Wgt_cong_UL_data)  #Get the number of rows in the df
Wgt_cong_ULDate = Wgt_cong_UL_data['UnloadDate'] #Create new df with only dates
Wgt_cong_ULDate = Wgt_cong_ULDate.drop_duplicates() #remove duplicate dates
Wgt_cong_ULDate = Wgt_cong_ULDate.reset_index(drop = True)
print(Wgt_cong_ULDate)

Wgt_Date_UL_df = Wgt_cong_UL_data.filter(['Wgt','ULDoor','UnloadDate'], 
                                         axis = 1) #create new df using columns from old one
#print(Wgt_Date_UL_df)


UL_Wgt_Date_Door_Table = Wgt_Date_UL_df.pivot_table(index = 'UnloadDate', 
                                                    columns = 'ULDoor', 
                                                    aggfunc = sum, 
                                                    fill_value = 0)
UL_Wgt_Date_Door_Table

UL_Wgt_Date_Door_Table.loc[Wgt_cong_ULDate[i]]