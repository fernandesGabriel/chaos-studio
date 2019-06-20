from random import randint
import numpy


def random_int(min: int, max: int):
    return randint(min, max)


def distributed_coordinates(n, conf):
    x = numpy.random.normal(conf['x'], conf['std_deviation'], n)
    y = numpy.random.normal(conf['y'], conf['std_deviation'], n)

    response = []
    for i in range(n):
        response += [[x[random_int(0, n-1)], y[random_int(0, n-1)]]]

    return numpy.array(response)


def random_coordinates(n, x1, y1, sigma1, x2, y2, sigma2):
    conf_1 = {
        'x': x1,
        'y': y1,
        'std_deviation': sigma1
    }
    conf_2 = {
        'x': x2,
        'y': y2,
        'std_deviation': sigma2
    }

    points_1 = distributed_coordinates(n, conf_1)
    points_2 = distributed_coordinates(n, conf_2)

    coordinates = numpy.zeros((n, 2, 2))

    coordinates[:, 0] = points_1
    coordinates[:, 1] = points_2

    response = []
    for i in range(n):
        response += [(coordinates[i, 0][0], coordinates[i, 0][1]),
                     (coordinates[i, 1][0], coordinates[i, 1][1])]

    return response