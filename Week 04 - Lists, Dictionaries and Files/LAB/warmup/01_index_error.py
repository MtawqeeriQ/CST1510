# FIXED - was broken on purpose.
# Last line of the original error:
#   IndexError: list index out of range
# A 3-item list has positions 0, 1, 2 - len(labels) - 1 is the last one.

labels = ["R-001", "R-002", "R-003"]

# print(labels[3])          # <- this was the broken line: no position 3
print(labels[len(labels) - 1])   # last valid index, or simply labels[-1]
