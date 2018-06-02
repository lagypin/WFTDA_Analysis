import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import seaborn as sns
interactive(True)

# Get the CSV files
jams=pd.read_csv("stat_exports/jams.csv")
penalties=pd.read_csv("stat_exports/penalties.csv")
teams=pd.read_csv("stat_exports/teams.csv")
skaters=pd.read_csv("stat_exports/skaters.csv")


jampenalties=pd.merge(jams, penalties, left_on="id", right_on="jam_id")
jampenalties2=pd.merge(jampenalties, skaters, left_on="skater_id", right_on="id")
jampenalties3=pd.merge(jampenalties2, teams, left_on='team_id', right_on="id")
df=jampenalties3[["jam_number", "name", "position", "team_name"]].sort_values("jam_number")
print(df.sample(3))

dfgroup=df.groupby(["jam_number", "team_name"])[["name"]].count()
print(dfgroup.sample (3))

df1 = dfgroup.reset_index()
print(df1.sample(3))



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
