import numpy
print("Creating 5X2 array using numpy.arange")
sampleArray = numpy.arange(100, 200,10,dtype='i')
sampleArray = sampleArray.reshape(5,2)
print (sampleArray)