import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TrianglePage(BasePage):
    SIDE_A_INPUT_LOCATOR = (By.CSS_SELECTOR, ".js_a")
    SIDE_B_INPUT_LOCATOR = (By.CSS_SELECTOR, ".js_b")
    SIDE_C_INPUT_LOCATOR = (By.CSS_SELECTOR, ".js_c")
    SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-submit")
    SUBMIT_BUTTON1_LOCATOR = (By.XPATH, "//button[contains(@class, 'btn-submit')]")
    SUBMIT_BUTTON2_LOCATOR = (By.XPATH, "//button[contains(text(), 'Показать')]")

    RESULT_TEXT = (By.CSS_SELECTOR, ".info.logg")

    @allure.step("Заполняем длину сторон треугольника")
    def enter_sides(self, a, b, c):
        self.send_keys_in_input_field(self.SIDE_A_INPUT_LOCATOR, str(a))
        self.send_keys_in_input_field(self.SIDE_B_INPUT_LOCATOR, str(b))
        self.send_keys_in_input_field(self.SIDE_C_INPUT_LOCATOR, str(c))

    @allure.step("Наводим мышь и кликаем на кнопку Показать")
    def hover_and_click_button_show(self):
        self.hover_and_click(self.SUBMIT_BUTTON2_LOCATOR)

    @allure.step("Кликаем на кнопку Показать")
    def click_button_show(self):
        self.scroll_to_element(self.SUBMIT_BUTTON_LOCATOR)
        self.click(self.SUBMIT_BUTTON1_LOCATOR)

    @allure.step("Получаем результат работы алгоритма.")
    def get_result(self):
        return self.get_text(self.RESULT_TEXT)

    @allure.step("Наводим мышь и нажимаем Ввод")
    def hover_button_show_and_press_enter(self):
        self.hover_and_press_enter(self.SUBMIT_BUTTON2_LOCATOR)

    def wait_for_button_show(self):
        self.wait_for(self.SUBMIT_BUTTON_LOCATOR)

    def input_is_not_focused(self, locator=SIDE_C_INPUT_LOCATOR):
        """Проверяет, что элемент не в фокусе"""
        current_active_element = self.driver.execute_script("return document.activeElement")
        target_element = self.wait_for(locator)
        return current_active_element != target_element

    def click_button_after_wait_for_lost_fokus(self):
        """Нажимает кнопку Показать, после проверки, что поле С не в фокусе"""
        try:
            self.click_button_show()
            self.input_is_not_focused()
            self.hover_and_click_button_show()
        except TimeoutException:
            pass  # Можно залогировать ошибку, если нужно: print("Кнопка не была нажата из-за тайм-аута")
        finally:
            self.press_key_enter()
