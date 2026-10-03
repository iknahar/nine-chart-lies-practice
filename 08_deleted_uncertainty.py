from scipy import stats
from honest_data import make_students
#
df = make_students()
hard = df[df["course"] == "hard"]
# a small pilot: 15 app users and 15 non-users, picked at random
app = hard[hard["uses_app"]].sample(15, random_state=38)["score"]
non = hard[~hard["uses_app"]].sample(15, random_state=38)["score"]
#
gap = app.mean() - non.mean()
test = stats.ttest_ind(app, non)
low, high = test.confidence_interval(0.95)
#
print(f"slide says : +{gap:.1f} points")
print(f"95% range  : {low:+.1f} to {high:+.1f} points")
print(f"p-value    : {test.pvalue:.2f}")
