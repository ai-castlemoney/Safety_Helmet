class BaseLayer:
    def __init__(self, name=""):
        self.name = name

    def __repr__(self):
        return f"{self.name}Layer"

class ActivationLayer(BaseLayer):
    def __init__(self, size):
        super().__init__("Activation")
        self.size = size

class FCLayer(BaseLayer):
    def __init__(self, size):
        super().__init__("FullyConnected")
        self.size = size

print(FCLayer())