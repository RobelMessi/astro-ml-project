import pandas as pd

df = pd.read_csv("exoplanets.csv")

# Filtering = Keeping the rows that match a condition

discovery = df[df["year_discovered"]<2004] #filtering out any planets discovered past the year 2004
distance_from_earth =df[(df["distance_ly"]<150) | (df["distance_ly"]>300)] #filtering out any planets with a distance less than 150 light years away
#print(discovery)
print(distance_from_earth)