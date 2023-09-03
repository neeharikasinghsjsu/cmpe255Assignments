from calculator import Calculator

def test_addition():
    calculator = Calculator()
    result = calculator.add(5)
    assert result == 5, f'Expected 5, got {result}'
    result = calculator.add(3)
    assert result == 8, f'Expected 8, got {result}'

def test_subtraction():
    calculator = Calculator()
    result = calculator.subtract(5)
    assert result == -5, f'Expected -5, got {result}'
    result = calculator.subtract(3)
    assert result == -8, f'Expected -8, got {result}'

def test_multiplication():
    calculator = Calculator()
    result = calculator.multiply(5)
    assert result == 0, f'Expected 0, got {result}'
    result = calculator.multiply(3)
    assert result == 0, f'Expected 0, got {result}'

def test_division():
    calculator = Calculator()
    result = calculator.divide(5)
    assert result == 0, f'Expected 0, got {result}'
    result = calculator.divide(3)
    assert result == 0, f'Expected 0, got {result}'


def test_clear():
    calculator = Calculator()
    result = calculator.clear()
    assert result is None, f'Expected None, got {result}'
    result = calculator.clear()
    assert result is None, f'Expected None, got {result}'


