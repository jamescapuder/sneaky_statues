#pylint: disable=E1101

import numpy as np

import game

class Layer():

    def __init__(self, weights, bias, funct):
        self.weights = np.asmatrix(weights)
        self.bias = np.asmatrix(bias)
        if self.bias.shape[1] > self.bias.shape[0]:
            self.bias = self.bias.transpose()
        self.fun_vector = np.vectorize(funct)

    def feed(self, inputs):
        inputs = np.asmatrix(inputs)
        if inputs.shape[1] > inputs.shape[0]:
            inputs = inputs.transpose()
        outputs = self.weights * inputs + self.bias
        return self.fun_vector(outputs)


# activation function
def hardlim(x):
    if x >= 0:
        return 1
    else:
        return -1

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def normalize(x):
    return x / x.max(axis=0)

#---------------------------------------------------------------------------------------------------

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


def random_network():
    weights1 = np.random.uniform(-.3, .7, (17, 17))
    weights2 = np.random.uniform(-.3, .7, (17, 17))
    weights3 = np.random.uniform(-.3, .7, (1, 17))
    bias1 = np.random.uniform(0, 0, (17, 1))
    bias2 = np.random.uniform(0, 0, (17, 1))
    bias3 = np.random.uniform(0, 0, (17, 1))
    layer_1 = Layer(weights1, bias1, sigmoid)
    layer_2 = Layer(weights2, bias2, sigmoid)
    layer_3 = Layer(weights3, bias3, sigmoid)
    return (layer_1, layer_2, layer_3, 0)

def find_fitness(net):
    results = game.comp_stomp(net)
    fitness = 0
    if results[0] == 1:
        fitness = 1 - (results[1]/50)
    return fitness

def acc_fitness(population):
    total = 0
    for net in population:
        net[3] = find_fitness(net)
        total += net[3]
    for net in population:
        net[3] = net[3] / total
    population.sort(key=lambda x: x[3], reverse=True)
    population = [sum(population[i+1:])for i, j in enumerate(population[:-1])]
    return population

def select_best(population):
    best = []
    while len(best) < 7:
        rand = np.random.uniform()
        for i, net in enumerate(list(population)):
            if net[3] > rand:
                best.append(population.pop(i))
    return best, population

def breed(population):
    new_population = []
    for net1, net2 in zip(population, population[:1]):
        layer1 = crossover(net1[0], net2[0])
        layer2 = crossover(net1[1], net2[1])
        layer3 = crossover(net1[2], net2[2])
        new_population.append((layer1, layer2, layer3, 0))

        
def train():
    population = []
    for i in range(16):
        population.append(random_network())
    population = acc_fitness(population)
    best, worst = select_best(population)


#---------------------------------------------------------------------------------------------------

def save_network(fname, **matrices):
    np.savez(fname, **matrices)

def load_network(fname):
    data = np.load(fname)
    layer1 = Layer(data['weights1'], data['bias1'], sigmoid)
    layer2 = Layer(data['weights2'], data['bias2'], sigmoid)
    layer3 = Layer(data['weights3'], data['bias3'], sigmoid)
    return layer1, layer2, layer3






















































