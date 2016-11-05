import sys
import re
import subprocess

# does not match the output 100%. 
# I argue that a lines with only <...> calls contain 
# newlines which should be printed regardless

def command(match):
    # get the first group
    string = match.group(1)
    if string.startswith("!"):
        # we start a subprocess, remove the "!" using string slicing,
        # and split the arguments for security
        # we also need to decode the output from bytes to utf-8
        return subprocess.check_output(string[1:].split())).decode("utf-8")
    else:
        return open(string).read()

for line in sys.stdin:
    print(re.sub(r"<(.*?)>", command, line.strip()).strip())
       
"""
you should be using the subprocess module for system calls, 
as other methods are deprecated.

another method of doing this would be
p = subprocess.run(string[1:].split(), stdout=subprocess.PIPE)
return p.stdout.decode("utf-8")

check_output just makes this a bit easier, useful to remember this syntax in
these cases
"""
