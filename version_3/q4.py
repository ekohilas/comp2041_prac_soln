import sys

for line in sys.stdin:
    data = line.strip().split("|")
    # here re-set the name field by 
    # spliting on commas, reversing it, and then joining it with spaces
    data[2] = " ".join(reversed(data[2].split(", ")))
    print("|".join(data))
