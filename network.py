import numpy as np

class Layer():

    def __init__(self, weights, bias, funct):
        self.weights = np.asmatrix(weights)
        self.bias = np.asmatrix(bias)
        if self.bias.shape[1] > self.bias.shape[0]:
            self.bias = self.bias.getT()
        self.fun_vector = np.vectorize(funct)

    def output(self, inputs):
        inputs = np.asmatrix(inputs)
        if self.weights.shape[1] != inputs.shape[0]:
            inputs = inputs.getT()
        outputs = self.weights * inputs + self.bias
        return self.fun_vector(outputs)
