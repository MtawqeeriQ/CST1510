"""
RECORD CHECK  -  AI / Data Science lane  (Threshold version)
=============================================================

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.

Lane: AI / Data Science
  - dataset name   (text)
  - rows loaded    (number)
  - rows expected  (number)

Threshold: write status_of(percent), calculate difference and percent inline,
call status_of for the status, and print a bordered report including it.
Every function you write gets a one-line docstring.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).

def status_of(percent):
    """Return OVER LIMIT, WARNING, or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Dataset name: ")
loaded = float(input("Rows loaded: "))
expected = float(input("Rows expected: "))


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.

difference = loaded - expected
percent = (loaded / expected) * 100
status = status_of(percent)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  Rows loaded : {loaded}")
print(f"  Rows expected : {expected}")
print(f"  Difference  : {difference}")
print(f"  Percent     : {percent}")
print(f"  Status      : {status}")
print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [x] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [x] Check every function does one job - status_of only returns a status,
#        nothing prints inside it
