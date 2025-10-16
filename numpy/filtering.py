import numpy as np

rng = np.random.default_rng(0)
arr = rng.integers(0, 20, size=12)  # random ints in [0, 20)

mask = (arr % 2 == 0) & (arr > 10)  # even and > 10
selected = arr[mask]                # filtered view

print("arr:", arr)
print("selected (even & > 10):", selected)

# Replace non-matching elements with -1 (in place on a copy)
arr2 = arr.copy()
arr2[~mask] = -1
print("arr2 with others set to -1:", arr2)
