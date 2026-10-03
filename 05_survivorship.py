from honest_data import make_students
#
df = make_students()
users = df[df["uses_app"]]
# the survey link went out inside the app, so only stayers saw it
survey = users[users["stayed"]]
#
print(f"survey says : {survey['happy'].mean():.1f} / 5")
print(f"every user  : {users['happy'].mean():.1f} / 5")
print(f"stayed      : {users['stayed'].mean():.0%} of users")
#
# who vanished, by how happy they were
share = users.groupby("happy")["stayed"].mean()
print(share.round(2))
