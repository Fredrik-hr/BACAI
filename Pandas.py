# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 08:28:09 2024

@author: 1119f
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#Repetering Numpy
# =============================================================================
# import numpy as np
# 
# a = np.array([[1.2, 2.5],[3.2, 1.8],[1.1, 4.3]])
# 
# print(a)
# 
# b = np.array([[4.1, 2.6]])
# 
# c = np.append(a,b,axis=0)
# 
# print(c)
# 
# d = np.array([[7.8],[6.1],[5.4]])
# 
# print(np.append(a,d,axis=1))
# 
# print(np.insert(a,1,b,axis=0))
# 
# print(np.delete(a,1,axis=0))
# 
# h = np.resize(a,new_shape=(2,3))
# 
# print(h)
# =============================================================================


#Pandas Series
# =============================================================================
# obj = Series([4 ,7, -5, 3])
# 
# print(obj)
# print(type(obj))
# 
# print(obj.index)
# print(obj.values)
# =============================================================================


#How to use Series
# =============================================================================
# sdata = {"Texas":10,"Ohio":20,"Oregon":15,"Utah":18}
# states = ["Texas","Ohio","Oregon","Iowa"]
# 
# #Sets sdata as the data input and states as the index
# obj1 = Series(sdata, index=states)
# print(obj1)
# 
# #Changing the index names in states
# obj1.index = ["Florida","New York","Kentucky","Georgia"]
# print(obj1)
# =============================================================================


#This will not work, because the index is immutable by itself. I must change all if i whant to change an index
# =============================================================================
# obj1.index[2] = "California"
# print(obj1)
# =============================================================================


#Activity 1, squeres the integers in the Series
# =============================================================================
# integers = np.random.randint(1,101,size=10)
# 
# obj2 = Series(integers, index=range(1,11))
# 
# squered_int = obj2**2
# 
# greater = squered_int[squered_int>500].tolist()
# 
# print(greater)
# =============================================================================


#How to frame data with DataFrame
# =============================================================================
# data = {"state":["Ohio","Ohio","Ohio","Nevada","Nevada"],
#         "year":[2000,2001,2002,2001,2002],
#         "pop":[1.5,1.7,3.6,2.4,2.9]}
# 
# frame = DataFrame(data)
# print(frame)
# =============================================================================


#Further on how to use DataFrame and change index names
# =============================================================================
# data = {"state":["Ohio","Ohio","Ohio","Nevada","Nevada"],
#          "year":[2000,2001,2002,2001,2002],
#          "pop":[1.5,1.7,3.6,2.4,2.9]}
# 
# frame2 = DataFrame(data, columns=["year","state","pop","debt","H"], index=["A","B","C","D","E"])
# print(frame2)
# print(frame2["state"])
# =============================================================================


#Activity 2
# =============================================================================
# data2 = {'price':[1600.20,1610.02,1618.07,1624.40,1626.15,1626.15,1626.15],
#          'factor_1':[1.255,1.258,1.249,1.253,1.258,1.263,1.264,],
#          'factor_2':[1.548,1.554,1.552,1.556,1.552,1.558,1.572]
#          }
# 
# frame3 = DataFrame(data2)
# mean_facror_1 = frame3["factor_1"].mean()
# std_factor_1 = frame3["factor_1"].std()
# 
# mean_fac_2 =frame3["factor_2"].mean()
# std_fac_2 = frame3["factor_2"].std()
# 
# print(frame3)
# print("Mean for factor 1: ", mean_facror_1,", std for factor 1: ", std_factor_1)
# print(f"Mean for factor 1: {mean_fac_2}, std for factor 2: {std_fac_2}")
# =============================================================================


#Read CSV in python and extract information from the DataFrame
# =============================================================================
# df_grades = pd.read_csv("Grades_Short.csv")
# 
# print(df_grades)
# 
# #df_grades.index = range(1,8)
# 
# #Get column names
# print("Column names: ",df_grades.columns)
# 
# #Get row names
# print("Row range: ",df_grades.index)
# 
# #Get column data
# print(df_grades["Name"])
# 
# #Storeing the column and slicing the data
# name = df_grades["Name"]
# print("Name number 2 on the list is ", name[2])
# print(f"Name number 1,2,3 is: \n{name[1:4]}") #Prints name 1-3
# print(name[[1,2,4]])
# 
# #Getting the names without variable
# print("First name is ", df_grades.loc[0,"Name"])
# fist_name = df_grades.loc[0,"Name"]
# print(f"Prints the fist name with hlep from a variable: {fist_name}")
# 
# #Getting the whole fist row
# fist_row = df_grades.loc[0,:]
# print(f"Prints the whole fist row: \n {fist_row}")
# 
# #Getting one specific chunk
# slice_one = df_grades.loc[0:2,"Name":"Mini_Exam2"]
# print(f"Printing first defined chunk: \n {slice_one}")
# 
# #Get multiple columns
# print(df_grades[["Name","Grade","Mini_Exam3"]])
# 
# #Displays the first n rows, n is 5 if not defined
# print(df_grades.head())
# 
# #Displays the last n rows, n is 5 if not defined
# print(df_grades.tail())
# 
# #Dimension of DataFrame
# print("Dimension: ",df_grades.shape)
# 
# #How each column is stored
# print("Stoerd: ",df_grades.dtypes)
# 
# #Mean column  Final
# print(f"Mean final: {df_grades["Final"].mean()}")
# 
# #Creating a new column and changing a value
# df_grades["New_column"] = 1
# df_grades.loc[0,"New_column"] = 10
# print(df_grades.head(2))
# 
# #Adds column
# df_grades["Final_Percentage"] = df_grades["Final"]/36
# df_final_and_fp = df_grades.loc[0:7,"Final":"Final_Percentage"]
# print(df_final_and_fp)
# 
# #Deleting column
# del df_grades["New_column"]
# print(df_grades.head(2))
# 
# #Delete multiple columns (Axis = 1 delete specified columns)(Axis = 0 delete specified rows)
# df_grades.drop(["Final_Percentage","Grade"], axis=1, inplace=True)
# print(df_grades.head(2))
# =============================================================================


#Activity 3
# =============================================================================
# df_values = pd.read_csv("values.csv")
# 
# #I can check if python is able to read the file with the head function
# print(f"{df_values.head(2)}")
# print(df_values.shape)
# 
# mean_fac_1 = df_values["factor_1"].mean()
# std_fac_1 = df_values["factor_1"].std()
# 
# print(f"mean: {mean_fac_1}")
# print(f"std: {std_fac_1}")
# 
# factor_1 = df_values["factor_1"]
# factor_2 = df_values["factor_2"]
# 
# df_values.insert(3, "factor 1 * 3", factor_1[0:7]*3)
# df_values.insert(5, "factor 2 * 3", factor_2[0:7]*3)
# 
# print(df_values)
# 
# #One way to write a DataFrame to a csv file
# df_values.to_csv("Your_name.csv")
# 
# #2nd way to write a DataFrame to a csv file
# with open("Your_name_2.csv","w") as file:
#     file.write(f"{df_values}")
#     file.close()
# =============================================================================
    


#Parking.CSV
# =============================================================================
# #Index_col=0 drops det fisrt column
# df_parking = pd.read_csv("Parking.csv", index_col=0)
# print(df_parking.head())
# print(df_parking.shape)
# print(df_parking.dtypes)
# 
# #Reassign Issue Date
# df_parking["Issue__Date"] = pd.to_datetime(df_parking["Issue_Date"])
# 
# df_parking["DOW"] = df_parking["Issue_Date"].dt.weekday_name
# df_parking["Month"] = df_parking["Issue_Date"].dt.month
# 
# print(df_parking.head())
# 
# =============================================================================


#
df_missing = pd.read_csv("Missing_Data.csv", na_values=["NaN",-1,"Not available"])
print(df_missing.head())



mean_temp = df_missing["Temp"].mean()
df_missing.fillna({"Temp": mean_temp}, inplace=False)
print(df_missing)

















