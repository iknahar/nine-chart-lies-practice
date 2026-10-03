import matplotlib.pyplot as plt
from honest_data import yearly_users
#
users = yearly_users()
#
# the same series, read from every possible starting year
for start in users.index[:-1]:
    change = users[2026] / users[start] - 1
    print(f"since {start}: {change:+.0%}")
#
fig, (lie, truth) = plt.subplots(1, 2, figsize=(10, 4))
lie.plot(users.loc[2021:], marker="o", color="crimson")
lie.set_title("Slide version: since 2021")
truth.plot(users, marker="o", color="grey")
truth.axvspan(2019.5, 2020.5, alpha=0.2)  # shade the odd year
truth.set_title("Honest version: every year")
fig.savefig("02_baseline_year.png", dpi=120)
