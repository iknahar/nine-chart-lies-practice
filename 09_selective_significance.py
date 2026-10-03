import numpy as np
from scipy import stats
from honest_data import make_students
#
FEATURES = ["dark mode", "streaks", "badges", "reminders",
            "flashcards", "timer", "leaderboard", "sounds",
            "owl mascot", "quizzes", "notes", "widgets",
            "offline", "voice", "emoji", "themes",
            "sharing", "calendar", "hints", "stickers"]
#
df = make_students()
users = df[(df["course"] == "hard") & df["uses_app"]]
rng = np.random.default_rng(14)
#
pvals = {}
for name in FEATURES:
    # each feature is switched on at random: it cannot matter
    on = rng.random(len(users)) < 0.5
    pvals[name] = stats.ttest_ind(users["score"][on],
                                  users["score"][~on]).pvalue
#
hits = {k: round(float(p), 4) for k, p in pvals.items() if p < 0.05}
print("under 0.05:", hits)
print("bonferroni cut:", 0.05 / len(FEATURES))
