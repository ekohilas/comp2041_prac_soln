import sys

# the readlines method 
# converts stdin into a list
lines = sys.stdin.readlines()
for line in lines:
    if line.startswith("#"):
        # we take a string slice of 
        # everything after the first character
        line_number = int(line[1:]) - 1
        print(lines[line_number].strip())
    else:
        print(line.strip())

# by using startswith and string sclicing, we
# can avoid regex, which should always be the case
