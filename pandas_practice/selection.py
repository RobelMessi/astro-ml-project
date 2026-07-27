import pandas as pd

df = pd.read_csv("exoplanets.csv", index_col = "name") #can search data using the name, label of each row is now the name

# Selection By Column
#print(df["mass_earth"])
#print(df["radius_earth"])
#print(df[["name", "distance_ly", "year_discovered"]])

#Selection by Rows
print(df.loc["Proxima Centauri b", ["distance_ly", "year_discovered"]]) #python list of all the columns you would like to display
print(df.loc["Kepler-186 f" : "HD 209458 b"]) #range of rows you would like to display using indexing
print(df.iloc[0:5, 0:3]) #given the first five rows and the first 3 columns

star = input("Enter a Star name: ")
try:
    print(df.loc[star])
except KeyError:
    print(f"{star} not found")
