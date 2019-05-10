#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

import pandas as pd
import tkinter
from tkinter import ttk

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
LOCATIONS = ['Indianapolis = 324', 'Nashville = 422']
LOCATION_DIC = {
    "Indianapolis = 324": 324,
    "Nashville = 422": 422
}


class LocMonND:

    def __init__(self, master):

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header,
                  text='YRC Freight: An Application for Optmizing Dock Layout at YRC Distribution Centers ').grid(row=0,
                                                                                                                  column=0)
        ttk.Label(self.frame_header, wraplength=300, text=(
            "This is an application that was built using the front end and back end code using the Python. Buit in Spyder, this applicaton can be downloaded on GitHUb. Using the URL (https://github.com/AlesiaStewart/Spring2019_SD.git) "

            " By: Esteban Gamboa, Mazen Khoja, Abdulaziz Shalaby, Alesia Stewart")).grid(row=0, column=1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text='Month:').grid(row=2, column=1, padx=3, sticky='sw')
        ttk.Label(self.frame_content, text='Location:').grid(row=1, column=1, padx=3, sticky='sw')

        ttk.Label(self.frame_content, text='Number of Doors:').grid(row=3, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text = "Current Layout Cost").grid(row =3, column=10, padx=3, sticky='sw')
        ttk.Label(self.frame_content, text='New Layout Cost : ').grid(row=4, column=10, padx=4, sticky='sw')
        ttk.Label(self.frame_content, text ='New Layout Table').grid(row=5, column=10,padx=4,sticky='sw')
        self.location_var = tkinter.StringVar(master)
        self.location_var.set(LOCATIONS[0])
        self.location_dropdown = tkinter.OptionMenu(self.frame_content, self.location_var, *LOCATIONS)
        self.location_dropdown.grid(row=1, column=3)

        self.months_var = tkinter.StringVar(master)
        self.months_var.set(MONTHS[0])
        self.month_dropdown = tkinter.OptionMenu(self.frame_content, self.months_var, *MONTHS)
        self.month_dropdown.grid(row=2, column=3)

        self.entry_nodoors = ttk.Entry(self.frame_content, width=10)
        self.entry_newlayoutcost = ttk.Entry(self.frame_content, width=10)
        self.entry_pl = ttk.Entry(self.frame_content, width=10)
        self.entry_newlayout = ttk.Entry(self.frame_content, width = 10)

        self.entry_nodoors.grid(row=3, column=3, padx=5)
        self.entry_newlayoutcost.grid(row=3, column=11, padx=5)
        self.entry_pl.grid(row=4, column=11, padx=5)
        self.entry_newlayout.grid(row=5, column = 11, padx =5)

        ttk.Button(self.frame_content, text='Submit', command=self.submit).grid(row=4, column=0, padx=5, pady=5, sticky='e')

    def submit(self):

        print('Location: {}'.format(self.location_var.get()))
        print('Month: {}'.format(self.months_var.get()))
        print('Number of Doors in Dock : {}'.format(self.entry_nodoors.get()))
        print("Selected Location: ", self.location_var.get())
        print("Selected Month: ", self.months_var.get())
        print('Total Time Cost Equation with forklift interference:', )
        self.entry_newlayoutcost.insert(0, self.timecost())
       # self.entry_pl.insert(0, self.entry_pl.get())
        print('Pairwise Layout: {}')
        ##self.clear(self)

    def timecost(self, LOCATION_DIC = 324):
        NumOfDoor = self.entry_nodoors.get()
        try:
            val = int(NumOfDoor)
        except ValueError:
            print("No.. input string is not an Integer. It's a string")
            # tkinter.messagebox.showinfo("ERROR", "input for number of doors must be an integer")
            return "ERROR: Invalid number of doors"
        DoorsWide = 11
        DoorWidth = 12
        DoorSpace = 2
        DockWidth = DoorsWide * DoorWidth + DoorSpace * (DoorsWide + 1)
        Y = 10  # the space from the door to the lane dedicated for forklift travel
        ##print(DockWidth)

        AllDoors = range(1, int(NumOfDoor) + 1)
        ##print(AllDoors)

        NumDoorNoWide = (int(NumOfDoor) - (DoorsWide * 2))
        ##print(NumDoorNoWide)

        Half = NumDoorNoWide / 2
        ##print(Half)

        SideDoors1 = range(1, DoorsWide + 1)
        ##print(SideDoors1)
        SideDoors2 = range(int(NumOfDoor) + 1 - DoorsWide, int(NumOfDoor) + 1)
        #print(SideDoors2)
        SideDoors = []
        for elem in SideDoors1:
            SideDoors.append(elem)
        for elem in SideDoors2:
            SideDoors.append(elem)
        print(SideDoors)

        Doors = [e for e in AllDoors if e not in SideDoors]
        #print(Doors)

        OddDoors = [num for num in Doors if num % 2 == 1]
        #print(OddDoors)

        EvenDoors = [num for num in Doors if num % 2 == 0]
        print(EvenDoors)

        address_LD = '324_LD.csv'
        address_UL = '324_UL.csv'

        # Next couple lines imports the data from the files and names the columns of the dataframe
        UL_Main_Data = pd.read_csv(address_UL)
        UL_Main_Data.columns = ['Pro', 'UL', 'Dock', 'Ship', 'Pcs', 'Wgt', 'ULTrlr', 'ULDoor', 'UnloadTS', 'UnLoadDOW',
                                'LoadInterval', 'Org', 'UnloadDate', 'UnloadTime']

        LD_Main_Data = pd.read_csv(address_LD)
        LD_Main_Data.columns = ['Pro', 'L', 'Dock', 'Ship', 'Pcs', 'Wgt', 'LdTrlr', 'LdDoor', 'LoadTS', 'LoadDOW',
                                'LoadInterval', 'Dest', 'LoadTo', 'LoadToParent', 'LoadDate', 'LoadTime']

        ULData = UL_Main_Data[pd.to_numeric(UL_Main_Data['ULDoor'], errors='coerce').notnull()]
        # ULDoorAndPro = ULData.drop(['UL','Org','Dock','Ship','Pcs','Wgt','ULTrlr','UnloadTS','UnLoadDOW','LoadInterval','UnloadDate','UnloadTime'], axis = 1)
        ULDoorAndPro = ULData.drop(
            ['UL', 'Org', 'Dock', 'Ship', 'ULTrlr', 'UnloadTS', 'UnLoadDOW', 'LoadInterval', 'UnloadDate',
             'UnloadTime'], axis=1)

        # print(ULDoorAndPro)

        LDdata = LD_Main_Data[pd.to_numeric(LD_Main_Data['LdDoor'], errors='coerce').notnull()]
        # LDdoorAndPro = LDdata.drop(['L','Dock','Ship','Pcs','Wgt','LdTrlr','LoadTS','LoadDOW','LoadInterval','Dest', 'LoadToParent', 'LoadTo', 'LoadDate','LoadTime'], axis = 1)
        LDdoorAndPro = LDdata.drop(
            ['L', 'Dock', 'Ship', 'LdTrlr', 'LoadTS', 'LoadDOW', 'LoadInterval', 'Dest', 'LoadToParent', 'LoadDate',
             'LoadTime'], axis=1)

        # print(LDdoorAndPro)

        # LDdoorNum = LD_Main_Data['LdDoor'] # Gets Load door numbers
        # DoorNumFull = pd.concat([ULDoorNum, LDdoorNum]) # Combines both to get full list of doors being used to unload and load
        Df_ULandLD = ULDoorAndPro.Pro.isin(LDdoorAndPro.Pro)  # Checks if all the Pros that come in leave at some point

        ULDoorAndPro['UL_to_LD'] = Df_ULandLD  # Add the row of Booleans to the original df
        # print(ULDoorAndPro)
        ULDoorAndPro = ULDoorAndPro.reset_index(drop=True)
        ULDoorAndPro_True = ULDoorAndPro[ULDoorAndPro.UL_to_LD]  # Only get the true values
        ULDoorAndPro_True = ULDoorAndPro_True.reset_index(drop=True)
        ULemptyCount = pd.DataFrame(index=ULDoorAndPro.index.values,
                                    columns=['Count'])  # Create empty dataframe with index from ULDoorAndPro_True
        ULemptyCount = ULemptyCount.fillna(0)

        for a in range(len(ULemptyCount)):
            if a == 0:
                ULemptyCount.iloc[a] = 1
            else:
                if ULDoorAndPro.loc[a - 1, 'Pro'] == ULDoorAndPro.loc[a, 'Pro']:
                    ULemptyCount.iloc[a] = 1 + ULemptyCount.iloc[a - 1]
                else:
                    ULemptyCount.iloc[a] = 1
        # print(ULemptyCount)
        ULDoorAndPro['Count'] = ULemptyCount
        # print(ULDoorAndPro)

        Df_LDandUL = LDdoorAndPro.Pro.isin(ULDoorAndPro_True.Pro)
        LDdoorAndPro['LD_to_UL'] = Df_LDandUL
        LDdoorAndPro = LDdoorAndPro.reset_index(drop=True)
        LDdoorAndPro_True = LDdoorAndPro[LDdoorAndPro.LD_to_UL]
        LDdoorAndPro_True = LDdoorAndPro_True.reset_index(drop=True)
        LDemptyCount = pd.DataFrame(index=LDdoorAndPro.index.values,
                                    columns=['Count'])  # Create empty dataframe with index from LDdoorAndPro_True
        LDemptyCount = LDemptyCount.fillna(0)
        for a in range(len(LDemptyCount)):
            if a == 0:
                LDemptyCount.iloc[a] = 1
            else:
                if LDdoorAndPro.loc[a - 1, 'Pro'] == LDdoorAndPro.loc[a, 'Pro']:
                    LDemptyCount.iloc[a] = 1 + LDemptyCount.iloc[a - 1]
                else:
                    LDemptyCount.iloc[a] = 1
        LDdoorAndPro['Count'] = LDemptyCount
        # print(LDemptyCount)
        # print(LDdoorAndPro)

        # FromTo_v1 = pd.merge(ULDoorAndPro_True,LDdoorAndPro_True[['Pro','LdDoor']],on = 'Pro', how = 'inner')
        # FromTo = FromTo_v1.drop_duplicates(subset=['Pro','ULDoor','LdDoor'], keep = 'first')
        # ULDoorAndPro_True['LdDoor'] = LDdoorAndPro.LdDoor
        # FromTo = ULDoorAndPro_True
        # FromTo = FromTo.drop(['UL_to_LD'])
        # print(FromTo_v1)
        FromTo = pd.merge(ULDoorAndPro, LDdoorAndPro, on=['Pro', 'Count'])  # Shortcut to above stuff
        print(FromTo)
        # FromTo = FromTo.drop(['UL_to_LD', 'Count','LD_to_UL'])

        distance = pd.DataFrame(index=FromTo.index.values, columns=['Distance'])
        distance = distance.fillna(0)

        for b in range(len(FromTo)):
            # print(type(FromTo.loc[b,'ULDoor']))
            if int(FromTo.loc[b, 'ULDoor']) in EvenDoors and int(FromTo.loc[b, 'LdDoor']) in EvenDoors:
                x = abs(EvenDoors.index(int(FromTo.loc[b, 'ULDoor'])) - EvenDoors.index(int(FromTo.loc[b, 'LdDoor'])))
                if x < 1:
                    distance.loc[b] = 0
                else:
                    distance.loc[b] = DoorWidth * x + DoorSpace * x + 2 * Y
            elif int(FromTo.loc[b, 'ULDoor']) in OddDoors and int(FromTo.loc[b, 'LdDoor']) in OddDoors:
                x = abs(OddDoors.index(int(FromTo.loc[b, 'ULDoor'])) - OddDoors.index(int(FromTo.loc[b, 'LdDoor'])))
                if x < 1:
                    distance.loc[b] = 0
                else:
                    distance.loc[b] = DoorWidth * x + DoorSpace * x + 2 * Y
            elif int(FromTo.loc[b, 'ULDoor']) in SideDoors and int(FromTo.loc[b, 'LdDoor']) in SideDoors:
                distance.loc[b] = None
            else:
                if int(FromTo.loc[b, 'ULDoor']) in OddDoors and int(FromTo.loc[b, 'LdDoor']) in EvenDoors:
                    x = abs(
                        OddDoors.index(int(FromTo.loc[b, 'ULDoor'])) - EvenDoors.index(int(FromTo.loc[b, 'LdDoor'])))
                    distance.loc[b] = DoorWidth * x + DoorSpace * x + 2 * Y + DockWidth
                elif int(FromTo.loc[b, 'ULDoor']) in EvenDoors and int(FromTo.loc[b, 'LdDoor']) in OddDoors:
                    x = abs(
                        EvenDoors.index(int(FromTo.loc[b, 'ULDoor'])) - OddDoors.index(int(FromTo.loc[b, 'LdDoor'])))
                    distance.loc[b] = DoorWidth * x + DoorSpace * x + 2 * Y + DockWidth

            ## x = max(x1, x2)

        print(distance)

        FromTo['Distance'] = distance * 2
        speed = 26000  # (feet per hour | Avg speed of a forklift

        WgtPerPiece = FromTo['Wgt_y'] / FromTo['Pcs_y']
        h = WgtPerPiece.mean()
        print(h)

        c = FromTo['c_ij'] = FromTo['Distance'] / (
                h * speed)  # Cost in man hours to move a pound of freight from door i to door j

        # FromTo now contains c_ij and f_ij. To get sum_i (sum_j(c_ij*f_ij)), add up the columns fo these sections
        labor_cost_travel_df = FromTo['c_ij'] * FromTo['Wgt_y']
        return labor_cost_travel_df.sum()

    def timecost1(self, LOCATION_DIC = 422):
        NumOfDoor = self.entry_nodoors.get()
        try:
            val = int(NumOfDoor)
        except ValueError:
            print("No.. input string is not an Integer. It's a string")
            # tkinter.messagebox.showinfo("ERROR", "input for number of doors must be an integer")
            return "ERROR: Invalid number of doors"
        DoorsWide = 11
        DoorWidth = 12
        DoorSpace = 2
        DockWidth = DoorsWide * DoorWidth + DoorSpace * (DoorsWide + 1)
        Y = 10  # the space from the door to the lane dedicated for forklift travel
        ##print(DockWidth)

        AllDoors = range(1, int(NumOfDoor) + 1)
        ##print(AllDoors)

        NumDoorNoWide = (int(NumOfDoor) - (DoorsWide * 2))
        ##print(NumDoorNoWide)

        Half = NumDoorNoWide / 2
        ##print(Half)

        SideDoors1 = range(1, DoorsWide + 1)
        ##print(SideDoors1)
        SideDoors2 = range(int(NumOfDoor) + 1 - DoorsWide, int(NumOfDoor) + 1)
        # print(SideDoors2)
        SideDoors = []
        for elem in SideDoors1:
            SideDoors.append(elem)
        for elem in SideDoors2:
            SideDoors.append(elem)
        print(SideDoors)

        Doors = [e for e in AllDoors if e not in SideDoors]
        # print(Doors)

        OddDoors = [num for num in Doors if num % 2 == 1]
        # print(OddDoors)

        EvenDoors = [num for num in Doors if num % 2 == 0]
        print(EvenDoors)

        address_LD = '422 LoadData.csv'
        address_UL = '422 Unload.csv'
        # Next couple lines imports the data from the files and names the columns of the dataframe
        UL_Main_Data = pd.read_csv(address_UL)
        UL_Main_Data.columns = ['Pro', 'UL', 'Dock', 'Ship', 'Pcs', 'Wgt', 'ULTrlr', 'ULDoor', 'UnloadTS', 'UnLoadDOW',
                                'LoadInterval', 'Org']

        LD_Main_Data = pd.read_csv(address_LD)
        LD_Main_Data.columns = ['Pro', 'L', 'Dock', 'Ship', 'Pcs', 'Wgt', 'LdTrlr', 'LdDoor', 'LoadTS', 'LoadDOW',
                                'LoadInterval', 'Dest', 'LoadTo', 'LoadToParent']

        ULData = UL_Main_Data[pd.to_numeric(UL_Main_Data['ULDoor'], errors='coerce').notnull()]
        ULDoorAndPro = ULData.drop(['UL', 'Org', 'Dock', 'Ship', 'ULTrlr', 'UnloadTS', 'UnLoadDOW', 'LoadInterval'],
                                   axis=1)

        LDdata = LD_Main_Data[pd.to_numeric(LD_Main_Data['LdDoor'], errors='coerce').notnull()]
        LDdoorAndPro = LDdata.drop(
            ['L', 'Dock', 'Ship', 'LdTrlr', 'LoadTS', 'LoadDOW', 'LoadInterval', 'Dest', 'LoadToParent'],
            axis=1)
        # print(ULDoorAndPro)

        LDdata = LD_Main_Data[pd.to_numeric(LD_Main_Data['LdDoor'], errors='coerce').notnull()]
        # LDdoorAndPro = LDdata.drop(['L','Dock','Ship','Pcs','Wgt','LdTrlr','LoadTS','LoadDOW','LoadInterval','Dest', 'LoadToParent', 'LoadTo', 'LoadDate','LoadTime'], axis = 1)
        LDdoorAndPro = LDdata.drop(
            ['L', 'Dock', 'Ship', 'LdTrlr', 'LoadTS', 'LoadDOW', 'LoadInterval', 'Dest', 'LoadToParent', 'LoadDate',
             'LoadTime'], axis=1)

        # print(LDdoorAndPro)

        # LDdoorNum = LD_Main_Data['LdDoor'] # Gets Load door numbers
        # DoorNumFull = pd.concat([ULDoorNum, LDdoorNum]) # Combines both to get full list of doors being used to unload and load
        Df_ULandLD = ULDoorAndPro.Pro.isin(LDdoorAndPro.Pro)  # Checks if all the Pros that come in leave at some point

        ULDoorAndPro['UL_to_LD'] = Df_ULandLD  # Add the row of Booleans to the original df
        # print(ULDoorAndPro)
        ULDoorAndPro = ULDoorAndPro.reset_index(drop=True)
        ULDoorAndPro_True = ULDoorAndPro[ULDoorAndPro.UL_to_LD]  # Only get the true values
        ULDoorAndPro_True = ULDoorAndPro_True.reset_index(drop=True)
        ULemptyCount = pd.DataFrame(index=ULDoorAndPro.index.values,
                                    columns=['Count'])  # Create empty dataframe with index from ULDoorAndPro_True
        ULemptyCount = ULemptyCount.fillna(0)

        for a in range(len(ULemptyCount)):
            if a == 0:
                ULemptyCount.iloc[a] = 1
            else:
                if ULDoorAndPro.loc[a - 1, 'Pro'] == ULDoorAndPro.loc[a, 'Pro']:
                    ULemptyCount.iloc[a] = 1 + ULemptyCount.iloc[a - 1]
                else:
                    ULemptyCount.iloc[a] = 1
        # print(ULemptyCount)
        ULDoorAndPro['Count'] = ULemptyCount
        # print(ULDoorAndPro)

        Df_LDandUL = LDdoorAndPro.Pro.isin(ULDoorAndPro_True.Pro)
        LDdoorAndPro['LD_to_UL'] = Df_LDandUL
        LDdoorAndPro = LDdoorAndPro.reset_index(drop=True)
        LDdoorAndPro_True = LDdoorAndPro[LDdoorAndPro.LD_to_UL]
        LDdoorAndPro_True = LDdoorAndPro_True.reset_index(drop=True)
        LDemptyCount = pd.DataFrame(index=LDdoorAndPro.index.values,
                                    columns=['Count'])  # Create empty dataframe with index from LDdoorAndPro_True
        LDemptyCount = LDemptyCount.fillna(0)
        for a in range(len(LDemptyCount)):
            if a == 0:
                LDemptyCount.iloc[a] = 1
            else:
                if LDdoorAndPro.loc[a - 1, 'Pro'] == LDdoorAndPro.loc[a, 'Pro']:
                    LDemptyCount.iloc[a] = 1 + LDemptyCount.iloc[a - 1]
                else:
                    LDemptyCount.iloc[a] = 1
        LDdoorAndPro['Count'] = LDemptyCount
        # print(LDemptyCount)
        # print(LDdoorAndPro)

        # FromTo_v1 = pd.merge(ULDoorAndPro_True,LDdoorAndPro_True[['Pro','LdDoor']],on = 'Pro', how = 'inner')
        # FromTo = FromTo_v1.drop_duplicates(subset=['Pro','ULDoor','LdDoor'], keep = 'first')
        # ULDoorAndPro_True['LdDoor'] = LDdoorAndPro.LdDoor
        # FromTo = ULDoorAndPro_True
        # FromTo = FromTo.drop(['UL_to_LD'])
        # print(FromTo_v1)
        FromTo = pd.merge(ULDoorAndPro, LDdoorAndPro, on=['Pro', 'Count'])  # Shortcut to above stuff
        print(FromTo)
        # FromTo = FromTo.drop(['UL_to_LD', 'Count','LD_to_UL'])

        distance = pd.DataFrame(index=FromTo.index.values, columns=['Distance'])
        distance = distance.fillna(0)

        for b in range(len(FromTo)):
            # print(type(FromTo.loc[b,'ULDoor']))
            if int(FromTo.loc[b, 'ULDoor']) in EvenDoors and int(FromTo.loc[b, 'LdDoor']) in EvenDoors:
                x = abs(EvenDoors.index(int(FromTo.loc[b, 'ULDoor'])) - EvenDoors.index(int(FromTo.loc[b, 'LdDoor'])))
                if x < 1:
                    distance.loc[b] = 0
                else:
                    distance.loc[b] = DoorWidth * x + DoorSpace * x + 2 * Y
            elif int(FromTo.loc[b, 'ULDoor']) in OddDoors and int(FromTo.loc[b, 'LdDoor']) in OddDoors:
                x = abs(OddDoors.index(int(FromTo.loc[b, 'ULDoor'])) - OddDoors.index(int(FromTo.loc[b, 'LdDoor'])))
                if x < 1:
                    distance.loc[b] = 0
                else:
                    distance.loc[b] = DoorWidth * x + DoorSpace * x + 2 * Y
            elif int(FromTo.loc[b, 'ULDoor']) in SideDoors and int(FromTo.loc[b, 'LdDoor']) in SideDoors:
                distance.loc[b] = None
            else:
                if int(FromTo.loc[b, 'ULDoor']) in OddDoors and int(FromTo.loc[b, 'LdDoor']) in EvenDoors:
                    x = abs(
                        OddDoors.index(int(FromTo.loc[b, 'ULDoor'])) - EvenDoors.index(int(FromTo.loc[b, 'LdDoor'])))
                    distance.loc[b] = DoorWidth * x + DoorSpace * x + 2 * Y + DockWidth
                elif int(FromTo.loc[b, 'ULDoor']) in EvenDoors and int(FromTo.loc[b, 'LdDoor']) in OddDoors:
                    x = abs(
                        EvenDoors.index(int(FromTo.loc[b, 'ULDoor'])) - OddDoors.index(int(FromTo.loc[b, 'LdDoor'])))
                    distance.loc[b] = DoorWidth * x + DoorSpace * x + 2 * Y + DockWidth

            ## x = max(x1, x2)

        print(distance)

        FromTo['Distance'] = distance * 2
        speed = 26000  # (feet per hour | Avg speed of a forklift

        WgtPerPiece = FromTo['Wgt_y'] / FromTo['Pcs_y']
        h = WgtPerPiece.mean()
        print(h)

        c = FromTo['c_ij'] = FromTo['Distance'] / (
                h * speed)  # Cost in man hours to move a pound of freight from door i to door j

        # FromTo now contains c_ij and f_ij. To get sum_i (sum_j(c_ij*f_ij)), add up the columns fo these sections
        labor_cost_travel_df = FromTo['c_ij'] * FromTo['Wgt_y']
        return labor_cost_travel_df.sum()

def main():
    root = tkinter.Tk()
    root.configure()
    location = LocMonND(root)
    root.mainloop()
if __name__ == "__main__": main()
