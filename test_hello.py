from hello import greetings, add, subtract


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9


def test_hello_greetings():
    assert greetings() == "Template repo"
