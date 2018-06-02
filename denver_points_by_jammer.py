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

# Gather skater information
jammer_stats=pd.merge(skaters, teams, left_on = "team_id", right_on = "id")
jammer_stats.columns=["skater_id", "skater_name", "team_id", "position", "team_id", "team_name"]
jammer_stats

#Gypin
gypin_points=pd.merge(jammer_stats, skater_jams, left_on = "skater_id", right_on = "skater_id")
gypin_points=gypin_points.loc[gypin_points["skater_name"]=="Gypin"]
gypin_points=gypin_points[["skater_name","position", "jam_id", "points"]]
print(gypin_points)

#Klein
klein_points=pd.merge(jammer_stats, skater_jams, left_on = "skater_id", right_on = "skater_id")
klein_points=klein_points.loc[klein_points["skater_name"]=="Klein"]
klein_points=klein_points[["skater_name","position", "jam_id", "points"]]
print(klein_points)

#Wilhelm
wilhelm_points=pd.merge(jammer_stats, skater_jams, left_on = "skater_id", right_on = "skater_id")
wilhelm_points=wilhelm_points.loc[wilhelm_points["skater_name"]=="Wilhelm"]
wilhelm_points=wilhelm_points[["skater_name","position", "jam_id", "points"]]
print(wilhelm_points)

#Cotten
cotten_points=pd.merge(jammer_stats, skater_jams, left_on = "skater_id", right_on = "skater_id")
cotten_points=cotten_points.loc[cotten_points["skater_name"]=="Cotten"]
cotten_points=cotten_points[["skater_name","position", "jam_id", "points"]]
print(cotten_points)

# Scald Eagle
eagle_points=pd.merge(jammer_stats, skater_jams, left_on = "skater_id", right_on = "skater_id")
eagle_points=eagle_points.loc[eagle_points["skater_name"]=="Scald Eagle"]
eagle_points=eagle_points[["skater_name","position", "jam_id", "points"]]
print(eagle_points)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(x=cotten_points['jam_id'],y=cotten_points['points'], label="Cotten", color="orange")
ax.scatter(x=gypin_points['jam_id'],y=gypin_points['points'], label="Gypin", color="green")
ax.scatter(x=klein_points['jam_id'],y=klein_points['points'], label="Klein", color="blue")
ax.scatter(x=eagle_points['jam_id'],y=eagle_points['points'], label="Scald Eagle", color="purple")
ax.scatter(x=wilhelm_points['jam_id'],y=wilhelm_points['points'], label="Wilhelm", color="red")
ax.legend(title="Jammer Name")
ax.set_ylabel ("Points")
ax.set_xlabel ("Jam Number")
plt.title('Denver Jammer Points per Jam')
