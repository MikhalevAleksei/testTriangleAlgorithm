import allure
import pytest

from pages.triangle_page import TrianglePage


@allure.epic("Тесты треугольника")
@allure.feature("Тест алгоритма создания треугодьника")
@allure.story("Тесты cоздания треугодьников с разными длинами сторон и типами данных.")
class TestTriangle:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        if not hasattr(self, "page"):  # Создаем объект страницы только один раз
            self.page = TrianglePage(driver)
            self.page.open()

    @allure.title("Создаем равносторонний треугольник со сторонами a=5, b=5, c=5")
    def test_equilateral_triangle(self):
        self.page.enter_sides(5, 5, 5)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Это равносторонний треугольник"
        assert expected_message in result, f"Expected {expected_message}, got: {result}"

    @allure.title("Создаем прямоугольный треугольник со сторонами a=3, b=4, c=5")
    def test_right_triangle(self):
        self.page.enter_sides(3, 4, 5)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Это прямоугольный треугольник"
        assert expected_message in result, f"Expected {expected_message}, got: {result}"

    @allure.title("Создаем остроугольный треугольник со сторонами a=4, b=5, c=6")
    def test_scalene_triangle(self):
        self.page.enter_sides(4, 5, 6)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Это остроугольный треугольник"
        assert expected_message in result, f"Expected {expected_message}, got: {result}"

    @allure.title("Создаем тупоугольный треугольник со сторонами a=2, b=3, c=4")
    def test_obtuse_triangle(self):
        self.page.enter_sides(2, 3, 4)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()

        assert "Это тупоугольный треугольник" in result, f"Expected 'Это тупоугольный треугольник', got: {result}"

    @allure.title("Проверяем невозможность создания треугольника со сторонами типа string a=a, b=b, c=c")
    def test_not_a_triangle(self):
        self.page.enter_sides('a', 'b', "c")
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Это НЕ треугольник"
        assert expected_message in result, f"Expected {expected_message}, got: {result}"

    @allure.title("Проверяем невозможность создания треугольника со сторонами a=5, b=5, c=10")
    def test_impossible_triangle(self):
        self.page.enter_sides(1, 2, 10)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Одна сторона больше суммы двух других или равна ей"
        assert expected_message in result, f"Expected {expected_message} got: {result}"

    @allure.title("Проверяем невозможность создания треугольника с отрицательным значением сторон a=-3, b=5, c=4")
    def test_negative_triangle(self):
        self.page.enter_sides(-3, 5, 4)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Это НЕ треугольник"
        assert expected_message in result, f"Expected {expected_message} got: {result}"

    @allure.title("Проверяем невозможность создания треугольника с пустыми полями значения сторон a='', b='', c=''")
    def test_empty_triangle(self):
        self.page.enter_sides('', '', '')
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Задайте все стороны"
        assert expected_message in result, f"Expected {expected_message} got: {result}"

    @allure.title(
        "Проверяем невозможность создания треугольника с пробелами в полях значения сторон a=' ', b=' ', c=' '")
    def test_triangle_with_spaces(self):
        self.page.enter_sides(' ', ' ', ' ')
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Это НЕ треугольник"
        assert expected_message in result, f"Expected {expected_message} got: {result}"

    @allure.title("Проверяем невозможность создания треугольника с нулями в полях значения сторон a=0, b=0, c=0")
    def test_zero_triangle(self):
        self.page.enter_sides(0, 0, 0)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Это НЕ треугольник"
        assert expected_message in result, f"Expected {expected_message} got: {result}"

    @allure.title("Проверяем невозможность создания треугольника с одним незаполненным полем значения сторон ")
    @pytest.mark.parametrize("side", (
            [("", "b", "c"),
             ("a", "", "c"),
             ("a", "b", "")])
    )
    def test_one_empty_side(self, side):
        self.page.enter_sides(*side)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Задайте все стороны"
        assert expected_message in result, f"Expected {expected_message} got: {result}"

    @allure.title(
        "Проверяем невозможность создания треугольника с вводом больших значений в  поля значениями сторон ")
    def test_large_number_input(self):
        self.page.enter_sides(1234509876, 1234509876, 1234509876)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Числа слишком большие"
        assert expected_message in result, f"Expected {expected_message} got: {result}"

    @allure.title("Проверяем невозможность создания треугольника с попыткой SQL Injection")
    def test_sql_injection(self):
        self.page.enter_sides("Select", 25, 6)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "SQL-инъекции это плохо! Так не получится"
        assert expected_message in result, f"Expected {expected_message} got: {result}"

    @allure.title("Проверяем невозможность создания треугольника с попыткой XSS Injection")
    def test_xss_injection(self):
        self.page.enter_sides("<script>", 25, 6)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "XSS это плохо! Так не получится"
        assert expected_message in result, f"Expected {expected_message} got: {result}"

    @allure.title("Проверяем невозможность создания треугольника с попыткой Case Insensitive XSS ")
    def test_case_insensitive_xss(self):
        self.page.enter_sides("<SCRIPT>", 25, 6)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "XSS это плохо! Так не получится"
        assert expected_message in result, f"Expected {expected_message} got: {result}"

    @allure.title("Проверяем невозможность создания треугольника  с нецелыми числами в полях значения сторон ")
    def test_non_integer_input(self):
        self.page.enter_sides(1.5, 2, 2.5)
        self.page.click_button_after_wait_for_lost_fokus()
        result = self.page.get_result()
        expected_message = "Это прямоугольный треугольник"
        assert expected_message in result, f"Expected {expected_message} got: {result}"
