from lazydag2 import Graph


def f1(high, low):
    return high + low


def f2(f1, f5):
    return f1 + f5


def f3(f1, f2):
    return f1 * f2


def f4(high, f1):
    return high - f1


def f5(low):
    return 2 * low


if __name__ == "__main__":

    """
    When we need f3 to update and only high updated,
    we need to recompute f1, f2, f3, but not f5, f4.
    """

    g = Graph()

    g.add_node("high")
    g.add_node("low")

    g.add_node_fn(f1)
    g.add_node_fn(f2)
    g.add_node_fn(f3)
    g.add_node_fn(f4)
    g.add_node_fn(f5)

    g.set_value("high", 2)
    g.set_value("low", 1)

    print(g.exec("f3"))

    g.set_value("high", 3)
    print(g.exec("f3"))
    print(g.exec("f3"))

    print(g.exec("f5"))

    print(g.exec("f4"))
