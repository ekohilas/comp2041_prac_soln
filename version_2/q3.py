import sys

d = {}
# we use list slicing 
# to remove the first argument
args = sys.argv[1:]
for arg in args:
    if arg not in args:
        d[arg] = 0
    d[arg] += 1

# we print the maximal element of the dictionay with the value as the key
# if multiple values are the same, we use the elements inverted index instead
print(max(d, key = lambda x: (d[x], len(args) - args.index(x))))

"""
functions like sort and max can take a function as a key.
that function takes in a single element and returns a corresponding item for 
the function to order with instead.
we could also do soemthing like

def invert(i):
    return 1/i

l = [1, 2, 3] 
sorted(l, key=invert)

in our case, it is convention to a lambda function
a lambda is a one line anonymous function which lies in the same scope.
it makes it easy for us to order how we wish

for example, the above could also be done as

l = [1, 2, 3] 
sorted(l, key = lambda i: 1/i)

In python, the returned key can also be a tuple.
In this case, if two elements are the same, 
python will then order on the second elements, and so on.

This is handy in our case as we want to find the max value, and then the first
appearing max.
"""
