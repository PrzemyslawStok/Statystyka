import numpy as np
from matplotlib import pyplot as plot


def simplePlot():
    X = np.linspace(0, 2 * np.pi, 100)
    print(X)
    Y = np.sin(X)

    plot.plot(X, Y)
    plot.show()

def distNormal():
    array_height = np.random.normal(167, size=1000)
    array_height = np.concatenate([array_height, np.random.normal(180, size=100)])

    # print(array_height)

    Y = array_height
    X = np.arange(0, len(array_height))

    plot.plot(X, Y)
    plot.show()

    # print(np.sort(array_height))

    plot.hist(array_height, bins=1000)
    plot.show()

    print(f"average: {np.average(array_height)}")
    print(f"median: {np.median(array_height)}")


if __name__ == '__main__':
    # simplePlot()
    # array_height = np.random.randint(160, 195, 100)
    distNormal()
