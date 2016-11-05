import re
import sys

def round_match(match):
    # group 0 is the entire match
    return str(round(float(match.group(0))))

for line in sys.stdin:
    # re.sub will do a regex replacement with specified string.
    # to do additional expressions, we can pass in a function that will 
    # handle the match and return a replacement string
    print(re.sub(r"\d+.\d+", round_match, line.strip()))

# you could replace the function with a lambda but why
# note: the round function behaves unexpectadly with
# floating point errors, you could do it andrews's way as
#   return str(int(float(match.group(0) + 0.5)))
