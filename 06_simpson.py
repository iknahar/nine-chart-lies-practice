from honest_data import make_students
#
df = make_students()
#
overall = df.groupby("uses_app")["score"].mean()
print("overall:", overall.round(1).to_dict())
#
by_course = df.pivot_table(index="course", columns="uses_app",
                           values="score", aggfunc="mean")
print(by_course.round(1))
#
# the hidden ingredient: who is in which course
mix = df.groupby("uses_app")["course"].value_counts(normalize=True)
print(mix.round(2))
