import random

class Perceptron:

    def __init__(self, num_inputs, learning_rate=0.01):

        self.weights = [random.uniform(-0.5, 0.5) for _ in range(num_inputs)]
        self.threshold = random.uniform(-0.5, 0.5)
        self.learning_rate = learning_rate

    def net(self, inputs):

        return sum(w * x for w, x in zip(self.weights, inputs)) - self.threshold

    def step(self, inputs):

        return 1 if self.net(inputs) > 0 else 0

    def update(self, inputs, target):

        out = self.step(inputs)
        error = target - out

        if error != 0:
            for i in range(len(self.weights)):
                self.weights[i] += self.learning_rate * error * inputs[i]

            self.threshold -= self.learning_rate * error
        return error