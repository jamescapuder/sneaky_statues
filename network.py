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

def main():
    weights1 = np.random.uniform(-1, 1, (17, 17))
    weights2 = np.random.uniform(-1, 1, (17, 17))
    weights3 = np.random.uniform(-1, 1, (1, 17))
    bias1 = np.zeros((17, 1))
    bias2 = np.zeros((17, 1))
    bias3 = np.zeros((17, 1))
    inputs = np.random.uniform(-1, 1, (17, 1))
    layer1 = Layer(weights1, bias1, sigmoid)
    layer2 = Layer(weights2, bias2, sigmoid)
    output_layer = Layer(weights3, bias3, sigmoid)
    out1 = layer1.output(inputs)
    out2 = layer2.output(out1)
    final = output_layer.output(out2)
    print(final)

if __name__ == "__main__":
    main()






































































