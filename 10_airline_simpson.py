import pandas as pd
#
# real 1987 data: delayed and total flights per airport, two airlines
rows = [
    ("Alaska", "LA", 62, 559), ("Alaska", "PHX", 12, 233),
    ("Alaska", "SD", 20, 232), ("Alaska", "SF", 102, 605),
    ("Alaska", "SEA", 305, 2146),
    ("America West", "LA", 117, 811), ("America West", "PHX", 415, 5255),
    ("America West", "SD", 65, 448), ("America West", "SF", 129, 449),
    ("America West", "SEA", 61, 262),
]
df = pd.DataFrame(rows, columns=["airline", "airport", "late", "flights"])
#
# delay rate at each airport: Alaska wins every single one
df["late_pct"] = (100 * df["late"] / df["flights"]).round(1)
print(df.pivot(index="airport", columns="airline", values="late_pct"))
#
# overall delay rate: add up first, then divide
total = df.groupby("airline")[["late", "flights"]].sum()
print((100 * total["late"] / total["flights"]).round(1))
#
# the reason: where each airline actually flies
share = df.pivot(index="airport", columns="airline", values="flights")
print((100 * share / share.sum()).round(0))
