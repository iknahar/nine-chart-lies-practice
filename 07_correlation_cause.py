import numpy as np
from honest_data import make_students
#
df = make_students()
hard = df[(df["course"] == "hard") & df["uses_app"]]
#
r = np.corrcoef(np.log(hard["minutes"]), hard["score"])[0, 1]
print(f"all hard-course users: r = {r:.2f}")
#
# now hold motivation still and look again
for level, grp in hard.groupby("motivation"):
    r = np.corrcoef(np.log(grp["minutes"]), grp["score"])[0, 1]
    print(f"{level:>4} motivation: r = {r:+.2f}")
