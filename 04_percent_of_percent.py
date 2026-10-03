# fail rate last year and this year, out of 1,000 students each
before, after = 50 / 1000, 40 / 1000
#
points = (after - before) * 100       # a plain subtraction
relative = (after - before) / before  # change measured against before
#
print(f"absolute: {points:+.1f} percentage points")
print(f"relative: {relative:+.0%}")
print(f"students: {50 - 40} fewer fails out of 1,000")
#
# the 1995 pill numbers, same arithmetic
old, new = 1 / 7000, 2 / 7000
print(f"pill relative: {(new - old) / old:+.0%}")
print(f"pill absolute: 1 extra case per {1 / (new - old):,.0f}")
