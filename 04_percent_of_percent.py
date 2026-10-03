# a £100 jacket: 50% off, then an extra 20% off the new price
price = 100 * (1 - 0.50) * (1 - 0.20)
print(f"you pay £{price:.0f}, a total of {1 - price / 100:.0%} off")
#
# bowel cancer per 1,000 people, low vs high processed meat
low, high = 56 / 1000, 66 / 1000
relative = (high - low) / low         # change compared with the start
points = (high - low) * 100           # plain subtraction of percentages
print(f"relative: {relative:+.0%}")
print(f"absolute: {points:+.1f} percentage points")
print(f"people:   {66 - 56} extra cases per 1,000")
