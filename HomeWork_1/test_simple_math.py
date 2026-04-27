import pytest
from simple_math import SimpleMath


@pytest.fixture
def math():
    """Фикстура, возвращающая экземпляр SimpleMath."""
    return SimpleMath()


class TestSquare:
    def test_square_positive(self, math):
        assert math.square(2) == 4

    def test_square_negative(self, math):
        assert math.square(-3) == 9

    def test_square_zero(self, math):
        assert math.square(0) == 0

    def test_square_large(self, math):
        assert math.square(10) == 100


class TestCube:
    def test_cube_positive(self, math):
        assert math.cube(3) == 27

    def test_cube_negative(self, math):
        assert math.cube(-3) == -27

    def test_cube_zero(self, math):
        assert math.cube(0) == 0

    def test_cube_large(self, math):
        assert math.cube(10) == 1000
