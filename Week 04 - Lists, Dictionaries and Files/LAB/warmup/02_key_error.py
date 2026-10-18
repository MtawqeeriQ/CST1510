# FIXED - was broken on purpose.
# Last line of the original error:
#   KeyError: 'status'
# The dict only has "label", "value" and "limit" - asking for a key that is
# not there raises KeyError. Two fixes: add the key, or use .get() with a
# default so a missing key returns something safe instead of crashing.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}

# print(record["status"])                # <- broken: "status" is not a key yet
record["status"] = "OK"                  # fix 1: add the key
print(record["status"])

print(record.get("owner", "n/a"))        # fix 2: .get() default for keys that may be missing
