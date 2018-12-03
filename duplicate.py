
x = [
    1111,1111]

print "Duplicates: %s" % (len(x) != len(set(x)))

j = set([])
for val in x:
    j.add(str(val))

print(j)
