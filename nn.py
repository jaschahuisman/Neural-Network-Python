from matrix import Matrix

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
