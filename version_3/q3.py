import sys

# we use list slicing and list unpacking for our arguments
fi, string = sys.argv[1:]

for line in open(fi):
    if string in line:
        # we don't need regex for this, we can just use the replace method
        # you can also alternatively replace with "(" + string + ")"
        print(line.strip().replace(string, "({})".format(string)))
