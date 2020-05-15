from matrix import Matrix
import math

def sigmoid(x):
    return 1  / (1 + math.exp(-x))

def dsigmoid(y):
    # return sigmoid(x) * (1 + math.exp(sigmoid(-x)))
    return y * (1 - y)

class NeuralNetwork:
    # Initialization
    def __init__ (self, input_nodes:int, hidden_nodes:int, output_nodes:int):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        
        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.hidden_nodes, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()
        self.learning_rate = 0.1

    def feedforward(self, input_array: list):
        # Generate input outputs
        inputs = Matrix.fromArray(input_array)
        hidden = Matrix.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        hidden.map(sigmoid)

        # Generate hidden outputs
        outputs = Matrix.multiply(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.map(sigmoid)

        # Return outputs to call
        return outputs.toArray()

    def train(self, inputs_array: list, targets_array: list):
        # Generate input outputs
        targets = Matrix.fromArray(targets_array)
        inputs = Matrix.fromArray(inputs_array)
        hidden = Matrix.multiply(self.weights_ih, inputs) 
        hidden.add(self.bias_h)
        hidden.map(sigmoid)

        # Generate hidden outputs
        outputs = Matrix.multiply(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.map(sigmoid)

       
        # Calculate the output errors
        output_errors = Matrix.subtract(targets, outputs)

        # Calculate Gradient
        gradients = Matrix.s_map(outputs, dsigmoid)
        gradients = Matrix.multiply(gradients, output_errors)
        gradients.s_multiply(self.learning_rate)
       
        # Calculate Delta's
        transposed_hidden = Matrix.transpose(hidden)
        weight_ho_deltas = Matrix.multiply(gradients, transposed_hidden)
        
        # Adjust weights (hidden->outputs) by delta's
        self.weights_ho.add(weight_ho_deltas)
        # Adjust bias by it's delta's (gradients)
        self.bias_o.add(gradients)
        
        # Calculate hidden layer errors
        transposed_w_ho = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.subtract(transposed_w_ho, output_errors)

        # Calculate hidden gradient
        hidden_gradient = Matrix.s_map(hidden, dsigmoid)
        hidden_gradient.multiply(hidden_errors)
        hidden_gradient.multiply(self.learning_rate)

        # Calculate inputs->hidden Delta's
        transposed_inputs = Matrix.transpose(inputs)
        weight_ih_deltas = Matrix.multiply(hidden_gradient, transposed_inputs)
        
        # Adjust weights (inputs->hidden) by delta's
        self.weights_ih.add(weight_ih_deltas)
        # Adjust bias by it's delta's (gradients)
        self.bias_h.add(hidden_gradient)


class Tdata:
    def __init__(self, input_array, targets_array):
        self.inputs = input_array
        self.targets = targets_array

a = [
    Tdata([1,0],[1]),
    Tdata([0,1],[1]),
    Tdata([1,1],[0]),
    Tdata([0,0],[0]),
    ]

nn = NeuralNetwork(2, 2, 1)

for i in a:
    nn.train(i.inputs, i.targets)

