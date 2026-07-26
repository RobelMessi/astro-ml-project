import pandas as pd

#Series = A Pandas 1-D labeled array that can hold any data type
#         Think of it like a single column in a spreadsheet (1-D)

data = [100, 202, 204, 209, 203]

series = pd.Series(data) #converts it to a series
series = pd.Series(data, index = ["a", "b", "c", "d", "e"]) #labeling indexes by letters
print(series)
print(series.loc["a"]) #returns the value of the label
series.loc["c"] = 200 #changing the value
print(series)
#Can also look up a value using integer position *iloc*
print(series.iloc[0]) #prints the first value

print(series[series>=200]) #print values that are greater than or equal too 200

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
series = pd.Series(calories)
series.loc["Day 3"] +=600
print(series[series>=2000])
print(series)