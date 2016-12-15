
import itertools
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


# activation functions
def hardlim(x):
    if x >= 0:
        return 1
    else:
        return -1

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def normalize(x):
    return x / x.max(axis=0)

#----------------------------------------------------------------------------------------

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
    return [layer_1, layer_2, layer_3, 0]

def breed(population):
    new_population = []
    for net1, net2 in zip(population, population[::-1]):
        layer1 = crossover(net1[0], net2[0])
        layer2 = crossover(net1[1], net2[1])
        layer3 = crossover(net1[2], net2[2])
        new_population.append([layer1, layer2, layer3, 0])

def crossover(parent_1, parent_2):
    weights_1 = parent_1.weights
    weights_2 = parent_2.weights
    shape_1 = weights_1.shape
    shape_2 = weights_2.shape
    flat_weights_1 = np.asarray(weights_1).ravel()
    flat_weights_2 = np.asarray(weights_2).ravel()
    cross_point = np.random.randint(1, flat_weights_1.size - 1)
    new_1 = np.concatenate([flat_weights_1[:cross_point], flat_weights_2[cross_point:]])
    new_2 = np.concatenate([flat_weights_2[:cross_point], flat_weights_1[cross_point:]])
    new_1 = new_1.reshape(shape_1)
    new_2 = new_2.reshape(shape_2)
    parent_1.weights = new_1
    parent_2.weights = new_2
    return parent_1, parent_2

        
def gen_pop(size):
    pop = []
    for i in range(size):
        pop.append(random_network())
    return pop
    
def rate_and_sort(pop):
    for net1, net2 in itertools.combinations(pop, 2):
        results = game.comp_stomp(net1, net2)
        net1[3] += results["one"]
        net2[3] += results["two"]
    pop.sort(key=lambda x: x[3])
    return pop

def select(pop):
    return pop[int(len(pop)/2):]

def cross(selected):
    index = 0
    for layer1, layer2 in zip(selected[0][:3], selected[1][:3]):
        newlayer1, newlayer2 = crossover(layer1, layer2)
        selected[0][index] = newlayer1
        selected[1][index] = newlayer2
        index += 1
    return selected 

def main():
    POPSIZE = 4
    GENERATIONS = 16
    pop = gen_pop(POPSIZE)
    gen = 1
    while(gen < GENERATIONS):
        print("Generation", gen)
        pop = rate_and_sort(pop)
        selected = select(pop)
        next_pop = []
        next_pop.extend(cross(selected))
        next_pop.extend(gen_pop(int(POPSIZE/2)))
        pop = next_pop
        gen += 1
    print("Final Generation")
    pop = rate_and_sort(pop)
    best = pop[-1]
    best = best[:3]
    np.savez("pop"+str(POPSIZE)+"_gen"+str(GENERATIONS), weights1=best[0].weights, weights2=best[1].weights, weights3=best[2].weights, bias1=best[0].bias, bias2=best[1].bias, bias3=best[2].bias)

#-------------------------------------------------------------------------------------

def save_network(fname, **matrices):
    np.savez(fname, **matrices)

def load_network(fname):
    data = np.load(fname)
    layer1 = Layer(data['weights1'], data['bias1'], sigmoid)
    layer2 = Layer(data['weights2'], data['bias2'], sigmoid)
    layer3 = Layer(data['weights3'], data['bias3'], sigmoid)
    return layer1, layer2, layer3


if __name__ == "__main__":
    main()
