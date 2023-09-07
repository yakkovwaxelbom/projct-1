import random
import matplotlib.pyplot as plt


class RandomWolk:
    def __init__(self, dimensions, steps):
        self.dim = dimensions
        self.step = steps
        self.coordinate_system = [[0 for step in range(self.step + 1)] for dim in range(self.dim)]
        # print(self.coordinate_system)

    def walk(self):
        for step in range(self.step):
            random_dim = random.randint(0, self.dim - 1)  # The range includes the last member
            for dim in range(self.dim):
                if dim == random_dim:
                    self.move(dim, step)
                else:
                    self.stay_put(dim, step)
        print(self.coordinate_system)
        # x = [i for i in range(self.step + 1)], self.coordinate_system[0]
        # print(x)

    def move(self, dim, step):
        direction = 1
        coin_flip = random.random()
        if coin_flip < 0.5:
            direction = -1
        self.coordinate_system[dim][step + 1] = self.coordinate_system[dim][step] + direction

    def stay_put(self, dim, step):  # לברר למה זה נצרך
        self.coordinate_system[dim][step + 1] = self.coordinate_system[dim][step]

    def dis_play(self):

        if self.dim == 1:
            plt.plot([i for i in range(self.step + 1)], self.coordinate_system[0])
            plt.show()
        elif self.dim == 2:
            plt.plot(self.coordinate_system)
            plt.show()
# elif self.dim == 3:
# pass
# else:
# pass

drunk = RandomWolk(2, 4)
drunk.walk()
drunk.dis_play()


