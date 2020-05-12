class NeuralNetwork():
    # Initialization
    def __init__ (self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
    
    # Test
    def test(self):
        print(self.input_nodes)
        print(self.hidden_nodes)
        print(self.output_nodes)