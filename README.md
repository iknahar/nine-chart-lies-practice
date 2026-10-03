# Nine chart lies, practice code

Companion code for the article *Nine Ways People Lie With Statistics And Never Get Caught*.

Every script starts from the same honest, simulated dataset of 4,000 students and a revision app.
Each one builds a misleading "slide version" of a chart next to the honest version, so you can see
exactly which line of code does the lying.

## What is true in the data

- The app adds **+3 points** to an exam score.
- The hard course costs **18 points**.
- Motivation drives both app minutes and exam scores.
- About **31%** of app users are still around six months later, and they are the happy ones.

Every chart below is someone trying to make those four facts look like something else.

## Setup

```bash
pip install -r requirements.txt
```

```bash
python 01_truncated_axis.py
```

## The scripts

| File | Trick | What to look for |
|---|---|---|
| `honest_data.py` | none | the rules that generate the data |
| `01_truncated_axis.py` | bars that start at 75 | `set_ylim(75, 81)` |
| `02_baseline_year.py` | a flattering start year | growth printed from every start year |
| `03_mean_vs_median.py` | mean on lopsided data | mean 38 min, median 20 min |
| `04_percent_of_percent.py` | relative vs absolute change | -20% and -1 point are the same event |
| `05_survivorship.py` | a survey only stayers saw | 3.9 vs 3.0 out of 5 |
| `06_simpson.py` | Simpson's paradox | loses overall, wins in each course |
| `07_correlation_cause.py` | a confounder | r = 0.32 overall, about 0 within groups |
| `08_deleted_uncertainty.py` | a missing range | +4.6 points, range -2.2 to +11.3 |
| `09_selective_significance.py` | twenty tests, one winner | the owl mascot, p = 0.0084 |
| `audit.py` | the defence | flags truncated bars, flipped axes, missing error bars |

## Exercises

1. In `01_truncated_axis.py`, change the lower limit from 75 to 70. How much taller does the app bar look now?
2. In `02_baseline_year.py`, find the start year that makes growth look smallest without going negative.
3. In `03_mean_vs_median.py`, remove the top 1% of users. How far does the mean move? The median?
4. In `honest_data.py`, change `0.75, 0.25` to `0.5, 0.5` and rerun `06_simpson.py`. Does the paradox survive?
5. In `08_deleted_uncertainty.py`, change both sample sizes from 15 to 150. Does the range still cross zero?
6. In `09_selective_significance.py`, try seeds 0 to 49. In how many runs does at least one feature pass 0.05?

<details>
<summary>Answers</summary>

1. With a floor of 70 the app bar looks about 1.6 times taller instead of 4 times taller. The gap is still 3.6 points.
2. 2025, at +5%. Every start year tells a true story, which is the point.
3. The mean falls from about 38 to 35 minutes, the median from 20 to 19. A handful of heavy users was holding the mean up.
4. No. When both groups sit in the courses in the same proportions, the overall gap points the same way as the course gaps.
5. With 150 per group the range shrinks to about +1.2 to +5.0 points. It no longer crosses zero.
6. 28 of the 50 seeds produce at least one false winner. The formula 1 - 0.95^20 predicts about 64%, and fifty runs is a small sample.

</details>

## License

MIT
