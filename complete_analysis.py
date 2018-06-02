import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import seaborn as sns
interactive(True)

# Get the CSV files
jams=pd.read_csv("stat_exports/jams.csv")
penalties=pd.read_csv("stat_exports/penalties.csv")
# bouts=pd.read_csv("stat_exports/bouts.csv")
skater_jams=pd.read_csv("stat_exports/skater_jams.csv")
# team_bouts=pd.read_csv("stat_exports/team_bouts.csv")
teams=pd.read_csv("stat_exports/teams.csv")
skaters=pd.read_csv("stat_exports/skaters.csv")

# Find the penalties by for each skater on each team for each jam
jampenalties=pd.merge(jams, penalties, left_on="id", right_on="jam_id")
jampenalties2=pd.merge(jampenalties, skaters, left_on="skater_id", right_on="id")
jampenalties3=pd.merge(jampenalties2, teams, left_on='team_id', right_on="id")
df=jampenalties3[["jam_number", "name", "position", "team_name"]].sort_values("jam_number")
print(df.sample(3))

dfgroup=df.groupby(["jam_number", "team_name"])[["name"]].count()
print(dfgroup.sample (3))

df1 = dfgroup.reset_index()
print(df1.sample(3))


# Graph 1: Penalties
redblue= ["red", "blue"]
sns.set_palette(redblue)

f, ax=plt.subplots(figsize=(12,6))
sns.barplot(x="jam_number", y="name" , hue="team_name", data=df1 )
ax.set_yticks([0,1,2,3,4])
ax.legend(title="Team Name")
ax.set_ylabel ("Number of Penalties")
ax.set_xlabel ("Jam Number")
plt.title('Denver vs. Gotham Penalties Accrued Per Jam')
plt.show()

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

# Calculate the total points scored by each team
GJPoints["GScore"]=GJPoints.points.cumsum()
print(GJPoints.sample(3))

DJPoints["DScore"]=DJPoints.points.cumsum()
print(DJPoints.sample(3))


# Graph 3: Score
f, ax=plt.subplots(figsize=(12,6))
plt.plot(DJPoints.jam_id, DJPoints.DScore , label = "Denver", color='blue')
plt.plot(GJPoints.jam_id, GJPoints.GScore, label = "Gotham", color='red')
plt.xlabel('Jam Number')
plt.ylabel('Score')
plt.title('Denver vs. Gotham Score')
plt.legend(title="Team Score" )
plt.show()
