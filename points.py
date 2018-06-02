import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import seaborn as sns
interactive(True)

# Get the CSV files
jams=pd.read_csv("stat_exports/jams.csv")
penalties=pd.read_csv("stat_exports/penalties.csv")
bouts=pd.read_csv("stat_exports/bouts.csv")
skater_jams=pd.read_csv("stat_exports/skater_jams.csv")
team_bouts=pd.read_csv("stat_exports/team_bouts.csv")
teams=pd.read_csv("stat_exports/teams.csv")
skaters=pd.read_csv("stat_exports/skaters.csv")

# Find the points scored by each team in each jam
points=skater_jams.loc[skater_jams["points"]>0]
points1=pd.merge(points, skaters, left_on = "skater_id", right_on = "id")
points2=pd.merge(points1, teams, left_on = "team_id", right_on = "id")
points3=points2[["jam_id", "skater_id", "name", "team_id", "team_name", "points"]]
points4=points3.sort_values("jam_id")
print(points4.sample(3))

# Find the points scored by each team in seperate data sets
GJPoints=points4[["jam_id", "points"]].loc[points4["team_id"]== 2]
print(GJPoints.sample(3))

DJPoints=points4[["jam_id","points"]].loc[points4["team_id"]== 1]
print(DJPoints.sample(3))


# Graph 2: Points/Jam
f, ax=plt.subplots(figsize=(12,6))
ax.scatter(x=DJPoints["jam_id"], y=DJPoints["points"], label= "Denver", color="blue")
ax.scatter(x=GJPoints["jam_id"], y=GJPoints["points"], label= "Gotham", color="red")
ax.legend(title="Points" )
ax.set_ylabel ("Number of Points")
ax.set_xlabel ("Jam Number")
plt.title('Denver vs. Gotham Points Scored Per Jam')
plt.show()
