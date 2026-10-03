from matplotlib.container import BarContainer, ErrorbarContainer
#
def audit_axes(ax):
    # the three lies a machine can spot from the chart alone
    flags = []
    has_bars = any(isinstance(c, BarContainer) for c in ax.containers)
    bottom, top = ax.get_ylim()
    if has_bars and min(bottom, top) > 0:
        flags.append(f"bars start at {min(bottom, top):g}, not zero")
    if bottom > top:
        flags.append("y axis runs upside down")
    if not any(isinstance(c, ErrorbarContainer) for c in ax.containers):
        flags.append("no error bars anywhere")
    return flags
#
QUESTIONS = [
    "Where does the y axis start, and is it a bar chart?",
    "Why does the time window start in that year?",
    "Mean or median, and how lopsided is the data?",
    "Percent or percentage points, and from what base?",
    "Who was left out of the sample before counting?",
    "Would splitting the groups flip the result?",
    "Was anything assigned at random, or just observed?",
    "Where are the error bars or the range?",
    "How many things were tested before this one?",
]
#
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # rebuild slide one exactly as the deck drew it
    fig, ax = plt.subplots()
    ax.bar(["no app", "app"], [76.2, 79.8])
    ax.set_ylim(75, 81)
    for flag in audit_axes(ax):
        print("FLAG:", flag)
    for i, q in enumerate(QUESTIONS, 1):
        print(f"{i}. {q}")
