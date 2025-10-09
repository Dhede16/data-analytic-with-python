import pandas as pd 
import matplotlib.pyplot as plt

data1 = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
data2 = pd.DataFrame(data1)
data3 = data2.groupby(["Occupation"])["Sleep Duration"].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))

ax.set_title("Average sleep quality by Occupation", fontsize = 14)
ax.set_xlabel("Occupation", fontsize = 11)
ax.set_ylabel("Sleep Duration", fontsize = 11)
ax.set_ylim(1, 10)
ax.tick_params(axis = "x", rotation = 20, labelsize = 8)
ax.bar(data3["Occupation"], data3["Sleep Duration"], color="#BDE3C3")

plt.grid(axis = "y", ls = "--", alpha = 0.6)
plt.tight_layout()
plt.show()