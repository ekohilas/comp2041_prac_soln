# q4 without the use of datetime
# I had to result to this as I couldn't figure out how to use the 
# datetime/time libaries. Don't result to doing things manually when a
# thoroughly tested libary already exists
# this doesn't handle the 00 -> 12am edgecase

import sys

for line in sys.stdin:
    date = line.split()
    if line.strip():
        time = date[3].split(":")
        if int(time[0]) < 12:
            string = "am"
        else:
            time[0] = str(int(time[0]) - 12)
            string = "pm"
        print("{} {} {:>2} {}{} {} {}".format(
            date[0],
            date[1],
            date[2],
            ":".join(time),
            string,
            date[4],
            date[5]))
    #if else exists to avoid problems with empty lines
    else:
        print()

