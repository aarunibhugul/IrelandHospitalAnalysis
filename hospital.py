import pandas as pd
from datetime import datetime

df = pd.read_csv("BI.csv")
df['Admission Date'] =pd.to_datetime(df["Admission date and time"])
df['Discharge Date'] =pd.to_datetime(df["Discharge Date and Time"])
df["duration"] =  df['Discharge Date'] - df['Admission Date']
year_row = []
t2012_count = 0
t2013_count = 0
t2014_count = 0
t2015_count = 0
t2016_count = 0
for i,row in df.iterrows():
    if (row["Admission Date"] >= datetime(2012, 7, 9)) and (row["Admission Date"] <= datetime(2012, 12, 12)):
        year_row.append(2012)
        t2012_count= t2012_count+1
    elif (row["Admission Date"] > datetime(2013, 1, 1)) and (row["Admission Date"] <= datetime(2013, 12, 12)):
        year_row.append(2013)
        t2013_count= t2013_count+1
    elif (row["Admission Date"] > datetime(2014, 1, 1)) and (row["Admission Date"] <= datetime(2014, 12, 12)):
        year_row.append(2014)
        t2014_count= t2014_count+1
    elif (row["Admission Date"] > datetime(2015, 1, 1)) and (row["Admission Date"] <= datetime(2015, 12, 12)):
        year_row.append(2015)
        t2015_count= t2015_count+1
    else:
        year_row.append(2016)
        t2016_count= t2016_count+1
df['year'] = year_row
age = []
for i,row in df.iterrows():
    if (row['Age']>= 18):
        age.append("Adult")
    else:
        age.append("Child")
df["Age Group"] = age
print(df["Age Group"])


df.loc["Admission date and time"] = 

# The attached file is a sample dataset showing a list of all inpatients that were discharged from a hospital in the years 2013, 2014 and 2015. Each row represents 1 discharge. One of the most important variables for hospitals is Length of Stay (LOS). LOS is the number days a patient spends in hospital. Patients staying longer than necessary can lead to hospitals requiring additional beds, and can also lead to increased numbers of patients on trolleys due to reduced bed availability.
#
#
#
# The points we would like you to cover in your analysis of the dataset are (but not limited to):
#
# Activity (i.e. the number of discharges)
# Length of Stay
# What areas would you target in an attempt to reduce Length of Stay and why?
# Number of beds required to house the patients in this dataset (hint: there are 365 days in the year)
# How many patients were in the hospital at 5am on 30/09/2014
# Create a field that groups patients into adult and child categories
# Predict the hospital’s bed requirement if the average age of patients increased by 20%
