from linear_regression import StupidFunction


def test_output():
    a = 'horses'
    b = 'cars'
    truth = StupidFunction(a, b)
    assert truth == 'horses are stupid and so are cars'
