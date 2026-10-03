import matplotlib.pyplot as plt
from honest_data import make_students
#
df = make_students()
mins = df.loc[df["uses_app"], "minutes"]
#
mean, median = mins.mean(), mins.median()
below = (mins < mean).mean()
print(f"mean {mean:.0f} min, median {median:.0f} min")
print(f"{below:.0%} of users sit below the mean")
#
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(mins, bins=60, color="grey")
ax.axvline(mean, color="crimson", label="mean")
ax.axvline(median, color="teal", label="median")
ax.legend()
fig.savefig("03_mean_vs_median.png", dpi=120)
