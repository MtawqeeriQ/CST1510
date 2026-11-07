"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  IT
Date  :

Run it:   python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv().

df = pd.read_csv("my_servers.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (used_gb / total_gb) * 100, then a "status"
#    column with .apply() and a lambda.

df["percent"] = (df["used_gb"] / df["total_gb"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT
# 3. Print it, show the rows that are not OK, count per status, save both
#    the CSV and the chart.

print(df)

print("\nNot OK:")
print(df[df["status"] != "OK"])

print("\nBy status:")
print(df["status"].value_counts())

df.to_csv("my_servers_report.csv", index=False)

df["status"].value_counts().plot(kind="bar", title="Servers by status")
plt.tight_layout()
plt.savefig("my_servers_status.png")
plt.show()

print("\nSaved my_servers_report.csv and my_servers_status.png")


# ==========================================================================
# 4. Before you finish:
#    [x] Run it and check the percent/status columns by hand for one row
#    [x] Check you used & (not "and") if you combined more than one condition
#    [x] Check every column your code refers to actually exists - watch case
