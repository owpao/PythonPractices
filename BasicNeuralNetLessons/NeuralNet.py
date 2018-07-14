import numpy

def NeuralNet(m1, m2, w1, w2, bias):
    z = m1 * w1 + m2 * w2 + bias
    return sigmoid(z)

def sigmoid(x):
    return 1/(1 + numpy.exp(-x))

# random measurements
w1 = numpy.random.randn()
w2 = numpy.random.randn()
b = numpy.random.randn()

print(NeuralNet(1, 2.5, w1, w2, b))

# no connections yet
# still have to teach the system