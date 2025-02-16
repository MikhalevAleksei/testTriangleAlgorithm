import allure
import pytest

from pages.triangle_page import TrianglePage

@allure.epic("Тесты треугольника")
@allure.feature("Тест алгоритма создания треугодьника")
@allure.story("Тесты cоздания треугодьников с разными длинами сторон и типами данных.")
class TestTriangle:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = TrianglePage(driver)
        self.page.open()

    @allure.title("Создаем равносторонний треугольник со сторонами a=5, b=5, c=5")
    def test_equilateral_triangle(self):
        self.page.enter_sides(5, 5, 5)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()

        assert "Это равносторонний треугольник" in result, f"Expected 'Это равносторонний треугольник', got: {result}"

    @allure.title("Создаем прямоугольный треугольник со сторонами a=3, b=4, c=5")
    def test_right_triangle(self):
        self.page.enter_sides(3, 4, 5)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()

        assert "Это прямоугольный треугольник" in result, f"Expected 'Это прямоугольный треугольник', got: {result}"
