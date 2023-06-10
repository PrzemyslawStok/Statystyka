import numpy as np
from matplotlib import pyplot as plot


def simplePlot():
    X = np.linspace(0, 2 * np.pi, 100)
    print(X)
    Y = np.sin(X)

    plot.plot(X, Y)
    plot.show()


def hist_fun0(array_height: np.ndarray, n: int = 2) -> np.ndarray:
    for i in range(n):
        x = 20 * i
        y = 0.5 * x ** 2 + 1
        array_height = np.concatenate([array_height, np.random.normal(x, size=5000)])

    return array_height


def gauss_fun(mu: float, sigma: float) -> (np.ndarray, np.ndarray):
    X = np.linspace(-5 * mu, +5 * mu, 10_000)
    Y = np.zeros(len(X))

    return (X, Y)


def distNormal():
    array_height = np.random.normal(150, size=10_000)
    array_height = np.concatenate([array_height, np.random.normal(180, size=5000)])

    print(array_height)

    array_height = np.zeros([0])
    array_height = hist_fun0(array_height, n=5)

    Y = array_height
    X = np.arange(0, len(array_height))

    plot.scatter(X, Y)
    plot.show()

    # print(np.sort(array_height))

    plot.hist(array_height, bins=100)
    plot.show()

    X, Y = gauss_fun(167, 0.2)
    plot.scatter(X,Y)
    plot.show()

    print(f"average: {np.average(array_height)}")
    print(f"median: {np.median(array_height)}")


if __name__ == '__main__':
    # simplePlot()
    # array_height = np.random.randint(160, 195, 100)
    distNormal()
