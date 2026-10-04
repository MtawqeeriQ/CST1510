"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  IT
Date  :

Run it:   python template.py

Target:  Threshold (pass standard)
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Hostname: ")
value = float(input("GB used: "))
limit = float(input("GB total: "))


# ================================================================== PROCESS
# 2. Decide a status and store it in a variable called status.
#
#    Threshold : if / else  -> "OVER LIMIT" or "OK"
#
#    Used is over the total only when it is strictly greater.

status = ""

if value > limit:
    status = "OVER LIMIT"
else:
    status = "OK"


# =================================================================== OUTPUT
# 3. Print the report: the three values you were given, plus status,
#    inside a border.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  Used        : {value:g}")
print(f"  Total       : {limit:g}")
print(f"  Status      : {status}")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
