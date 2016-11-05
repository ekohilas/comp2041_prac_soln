import sys
import time

for line in sys.stdin:
    line = line.strip().split()
    # we parse the the line for time
    t = time.strptime(line[3], "%H:%M:%S")
    # create a new time string format
    # lower to change AM to am
    new_time = time.strftime("%I:%M:%S%p", t).lower()
    # printing with format because .join removes 
    # the whitespace padding on the date
    # :>2 left aligned by 2
    print("{} {} {:>2} {} {} {}".format(
        line[0],
        line[1],
        line[2],
        new_time,
        line[4],
        line[5]))

    


