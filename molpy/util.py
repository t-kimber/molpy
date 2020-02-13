import numpy as np


def read_xyz(filename):
    """
    Reads an XYZ file of a molecule.

    Parameters
    ----------
    filename: str
        The name of the file that will be read.

    Returns
    -------
    ndarray: the symbols and the geometry for the atoms of the molecule in the XYZ file.
    """

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
        The distance between the first and second points.

    Notes
    -----
    Link to the `wiki page <https://en.wikipedia.org/wiki/Euclidean_distance>`_
    """

    point1 = np.asarray(point1)
    point2 = np.asarray(point2)
    return np.linalg.norm(point1 - point2)
