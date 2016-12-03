#pylint: disable=E1101

import numpy as np

class Layer():

    def __init__(self, weights, bias, funct):
        self.weights = np.asmatrix(weights)
        self.bias = np.asmatrix(bias)
        if self.bias.shape[1] > self.bias.shape[0]:
            self.bias = self.bias.transpose()
        self.fun_vector = np.vectorize(funct)

    def output(self, inputs):
        inputs = np.asmatrix(inputs)
        if inputs.shape[1] > inputs.shape[0]:
            inputs = inputs.transpose()
        outputs = self.weights * inputs + self.bias
        return self.fun_vector(outputs)


def hardlim(x):
    if x >= 0:
        return 1
    else:
        return -1

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def normalize(x):
    return x / x.max(axis=0)

def crossover(parent_1, parent_2):
    if parent_1.shape != parent_2.shape:
        raise ValueError('Cannot cross matrices of different sizes.')
    shape = parent_1.shape
    parent_1 = parent_1.flatten()
    parent_2 = parent_2.flatten()
    cross_point = np.random.randint(1, parent_1.size - 1)
    child_1 = np.concatenate([parent_1[:cross_point], parent_2[cross_point:]])
    child_2 = np.concatenate([parent_2[:cross_point], parent_1[cross_point:]])
    return child_1.reshape(shape), child_2.reshape(shape)

def main():
    weights1 = np.random.uniform(-1, 1, (3, 3))
    weights2 = np.random.uniform(-1, 1, (3, 3))
    weights3 = np.random.uniform(-1, 1, (1, 3))
    bias1 = np.zeros((3, 1))
    bias2 = np.zeros((3, 1))
    bias3 = np.zeros((3, 1))
    inputs = np.random.uniform(-1, 1, (3, 1))    
    layer1 = Layer(weights1, bias1, sigmoid)
    layer2 = Layer(weights2, bias2, sigmoid)
    output_layer = Layer(weights3, bias3, hardlim)
    out1 = layer1.output(inputs)
    out2 = layer2.output(out1)
    final = output_layer.output(out2)
    print(final)

if __name__ == "__main__":
    main()






































































