from triangle.triangle import Triangle
import pytest

class TestTrianglePytest:

    def test_triangle_eq(self):
        first = Triangle(8, 9, 7)
        second = Triangle(7, 8, 9)
        assert first == second

    def test_triangle_ne(self):
        first = Triangle(8, 9, 7)
        second = Triangle(7, 8, 6)
        assert first != second

    def test_triangle_lt(self):
        first = Triangle(7, 8, 9)
        second = Triangle(9, 10, 11)
        assert first < second

    def test_triangle_gt(self):
        first = Triangle(7, 8, 9)
        second = Triangle(9, 7, 6)
        assert first > second

    def test_triangle_le(self):
        first = Triangle(7, 8, 9)
        second = Triangle(8, 9, 7)
        assert first <= second

    def test_triangle_ge(self):
        first = Triangle(7, 8, 9)
        second = Triangle(8, 7, 9)
        assert first >= second

    def test_triangle_perimetr(self):
        first = Triangle(8, 9, 7)
        assert first.perimetr() == 24

    def test_triangle_square(self):
        second = Triangle(7, 9, 8)
        assert second.square() == 26.832815729997478


if __name__ == '__main__':
    pytest.main()
