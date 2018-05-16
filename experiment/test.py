import numpy

xlist = [[1, 2, 3, 4]]
for i,x in enumerate(xlist):
    xlist[i] = numpy.array(x)
print(xlist[0])
