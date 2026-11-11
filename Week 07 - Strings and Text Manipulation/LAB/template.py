"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Data Science
Date  :

Run it:   python template.py

Reads my_survey_lines.txt, cleans and parses every raw survey response, flags
the negative ones, and prints a summary at the end.
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Turn one messy raw survey line into a clean dict of survey/id/rating/age."""
    line = raw_line.strip()
    survey_part, rest = line.split(",", 1)

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())

    return {"survey": survey_part.strip().lower(),
            "id": int(fields["id"]),
            "rating": fields["rating"],
            "age": fields["age"]}


def status_of(rating, flag_below=3):
    """Return FLAGGED for a negative response (rating below 3), otherwise OK."""
    if rating < flag_below:
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT
# The raw responses live in my_survey_lines.txt - deliberately messy: extra
# spaces, mixed case, uneven spacing round the "=" signs.
with open("my_survey_lines.txt") as f:
    raw_records = [line for line in f if line.strip()]


# =============================================================== PROCESS + OUTPUT
responses = 0
flagged = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["rating"])

    responses += 1
    if status == "FLAGGED":
        flagged += 1

    print(f"{record['survey']} #{record['id']:<4} rating={record['rating']:.0f} "
          f"age={record['age']:.0f}  {status}")

print()
print(f"{responses} responses, {flagged} flagged")
