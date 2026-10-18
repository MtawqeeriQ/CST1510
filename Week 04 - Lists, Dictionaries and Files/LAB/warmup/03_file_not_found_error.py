# FIXED - was broken on purpose.
# Last line of the original error:
#   FileNotFoundError: [Errno 2] No such file or directory: 'records.txt'
# The file it asked for does not exist (in this folder). Two fixes:
# point at a file that does exist, and catch the error anyway so a bad
# path prints a clear message instead of crashing (Topic 4).

# Fix 1: a file that does exist - records_sample.txt is one folder up
# Fix 2: try/except FileNotFoundError, so even a wrong path cannot crash it
try:
    with open("../records_sample.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("../records_sample.txt not found - check the path")

# The original line, now caught instead of crashing:
try:
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("records.txt not found")
