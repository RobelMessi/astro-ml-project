import pandas as pd

#DataFrame = A tabular data structure with rows AND columns (2 Dimensional)
#            Similar to an Excel spreadsheet

data = {"Name" : ["Robel", "Nahom", "Eden"], 
        "Age" :[18, 15, 5]}

df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])
print(df.loc["Employee 3"])
print(df.iloc[0])

# Add a new column
df["Job"] = ["Physicist", "Mathematician", "Doctor"]
print(df)

#Add new rows
new_rows = pd.DataFrame([{"Name" : "Emmanuel", "Age": 10, "Job": "Athlete"},
                       {"Name" : "Noah", "Age": 11, "Job": "Athlete"}], index = ["Employee 4", "Employee 5"], )
df = pd.concat([df, new_rows]) #adds the new row to the original dataframe
print(df)