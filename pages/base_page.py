from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from config.links import Links


class BasePage:
    TRIANGLE_PAGE = Links.TRIANGLE_PAGE

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            self.driver, 5, poll_frequency=1,
            ignored_exceptions=[NoSuchElementException, TimeoutException])

    def open(self):
        if self.driver.current_url != self.TRIANGLE_PAGE:  # Проверяем, находимся ли уже на нужной странице
            self.driver.get(self.TRIANGLE_PAGE)

    def send_keys_in_input_field(self, locator, text):
        '''Очишает поле ввода и вносит значение '''
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        '''Кликает на доступный элемент'''
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, locator):
        """Получает текст из элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def scroll_to_element(self, locator):
        """Скролит экран к элементу"""
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    def hover_and_click(self, locator):
        """Навести курсор на элемент и кликнуть"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def hover_and_press_enter(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        element.send_keys(Keys.RETURN)

    def press_key_enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.RETURN).perform()

    def wait_for(self, locator: tuple[str, str]):
        """Ждет, пока элемент станет кликабельным"""
        return self.wait.until(EC.element_located_to_be_selected(locator))

    def input_is_not_focused(self, locator=None):
        """Проверяет, что элемент не в фокусе"""
        current_active_element = self.driver.execute_script("return document.activeElement")
        target_element = self.wait_for(locator)
        return current_active_element != target_element
