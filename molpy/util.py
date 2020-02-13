import numpy as np


def read_xyz(filename):

    with open(filename, "r") as handle:
        data = handle.readlines()

    data = data[2:]
    data = [x.split() for x in data]
    #print(data)
    symbols = [x[0] for x in data]
    xyz = np.array([[float(y) for y in x[1:]] for x in data])

    return {"symbols": np.array(symbols), "geometry": xyz}


def distance(point1, point2):
    """
    Calculate the euclidian distance between two points.

    Parameters
    ----------
    point1: array_like
        The first point.
    point2: array_like
        The second point.

    Returns
    -------
    float
        The distance between point1 and point 2.
    """

    point1 = np.asarray(point1)
    point2 = np.asarray(point2)
    return np.linalg.norm(point1 - point2)
