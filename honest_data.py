import numpy as np
import pandas as pd
#
def make_students(n=4000, seed=8):
    rng = np.random.default_rng(seed)
    # half the students sit the hard course, half the easy one
    hard = rng.random(n) < 0.5
    # struggling students go looking for help, so the app skews hard
    uses_app = rng.random(n) < np.where(hard, 0.75, 0.25)
    # motivation is invisible in real life; here we get to peek
    drive = rng.choice([-1, 0, 1], n)
    # the app is worth +3 points, the hard course costs 18
    score = (np.where(hard, 58, 76) + 3 * uses_app
             + 6 * drive + rng.normal(0, 7, n))
    # minutes per week: keen students use it more, a few use it a lot
    minutes = np.exp(3.0 + 0.9 * drive + rng.normal(0, 0.9, n))
    minutes = np.where(uses_app, np.maximum(minutes.round(), 1), 0)
    # happier users stick around; unhappy ones quietly uninstall
    happy = np.clip(np.round(3.0 + 1.1 * rng.normal(0, 1, n)), 1, 5)
    stayed = rng.random(n) < ((happy - 1) / 4) ** 2
    return pd.DataFrame({
        "course": np.where(hard, "hard", "easy"),
        "uses_app": uses_app,
        "motivation": np.array(["low", "mid", "high"])[drive + 1],
        "score": score.clip(0, 100).round(1),
        "minutes": minutes,
        "happy": happy.astype(int),
        "stayed": stayed & uses_app,
    })
#
def yearly_users():
    # monthly active users each year, in thousands; 2020 is lockdown
    users = [41, 44, 71, 38, 45, 52, 55, 58, 61]
    return pd.Series(users, index=range(2018, 2027), name="users_k")
#
if __name__ == "__main__":
    df = make_students()
    print(df.head())
    print(df.groupby(["course", "uses_app"])["score"].mean().round(1))
    print(yearly_users())
