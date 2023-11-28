import numpy as np
from Gradient import find_min_f

# MSR
"beata_alfa are a vector whose last component is alpha and the other"
" components are beta and t are a matrix each row is x_i respectively "


class MSR:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f(self, beata_alfa):
        beata, alfa = np.array(list(beata_alfa[:-1])), np.array(list(beata_alfa[-1:]))
        print(beata,alfa)
        return (self.x*beata+alfa-self.y).sum()





        # return (np.reshape((beata * self.x + alfa).sum(axis=1), (len(self.x), 1)) - self.y).sum()





_2= np.array([7])
# print(_2)
_1 = 6
# x_1 = np.array([i for i in range(-100, 110, 10)])
# y_1 = np.array([3 * i - 5 for i in x_1])
# print(_2*y_1)
# print(6*x_1)

# model = MSR(x, y)

# print(find_min_f(model.f, 2))

# print(float((np.reshape((beta * x + alfa).sum(axis=1), (len(x), 1)) - y).sum()))
# print(y)

# print(a*array)
# print(a*array-array_1)


# print((a*array).sum(axis=1))
# splits = [7, 1]
# beata, alfa = np.array_split(a, splits)
# print(beata)
# array = np.arange(10)

# splits = [3, 7]

# print(arrays)
# [[0 1 2]
#  [3 4 5 6 7 8 9]]
# a = np.array([i for i in range(-100, 110, 100)])
x = np.array([i for i in range(-100, 110, 10)])
y = np.array([3 * i - 5 for i in x])



# model = MSR(x,y)
# print(find_min_f(model.f,2))
# print(x)
alfa = np.array([1])
beta = np.array([ 2])
# print(x)
# print(y)
# print((x*beta+alfa-y).sum())
# print((x*beta+alfa-y)**2)
print(((x*beta+alfa-y)**2).sum())
