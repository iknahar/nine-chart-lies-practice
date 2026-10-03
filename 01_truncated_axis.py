import matplotlib.pyplot as plt
from honest_data import make_students
#
df = make_students()
easy = df[df["course"] == "easy"]
# one number per group: the average exam score
avg = easy.groupby("uses_app")["score"].mean()
labels = ["no app", "app"]
#
fig, (lie, truth) = plt.subplots(1, 2, figsize=(10, 4))
lie.bar(labels, avg.values, color=["grey", "crimson"])
lie.set_ylim(75, 81)          # the whole trick lives on this line
lie.set_title("Slide version")
truth.bar(labels, avg.values, color=["grey", "crimson"])
truth.set_ylim(0, 100)        # bars measure length, so start at zero
truth.set_title("Honest version")
fig.savefig("01_truncated_axis.png", dpi=120)
#
gap = avg[True] - avg[False]
print(f"real gap: {gap:.1f} points")
