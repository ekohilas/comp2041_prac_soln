import sys

l = []
# we can use a list sclice [1:] 
# to remove the first argument
for arg in sys.argv[1:]:
    if arg not in l:
        l.append(arg)

print(" ".join(l))
    
    

    
