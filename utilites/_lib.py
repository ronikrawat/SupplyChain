from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
    NoSuchElementException,
)
from random import randrange
from time import sleep


def _wait(func):
    def wrapper(*args, **kwargs):
        driver = args[0].driver
        if len(args) > 1:
            locator = args[1]
            wait = WebDriverWait(driver, 5)
            v = visibility_of_element_located(locator)
            print(f"waiting for {args[1]} to appear")
            try:
                wait.until(v)
            except TimeoutException:
                s = SeleniumWrapper(driver)
                s.scroll_to_end()
                try:
                    wait.until(v)
                except TimeoutException:
                    print(f"Timeout again after scrolling for {locator}.")
                    return False
        return func(*args, **kwargs)

    return wrapper


def __wait(cls):
    for key, value in cls.__dict__.items():
        if callable(value) and key != "__init__":
            setattr(cls, key, _wait(value))
    return cls


@__wait
class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, xpath):
        try:
            self.driver.find_element(*xpath).click()
        except ElementClickInterceptedException:
            self.scroll_to_end()
            self.click_element(xpath)

    def send_text(self, xpath, value):
        self.driver.find_element(*xpath).send_keys(value)

    def select_item(self, xpath, value):
        select = Select(self.driver.find_element(*xpath))
        select.select_by_visible_text(value)

    def move_curser(self, xpath):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*xpath)).perform()

    def screenshot(self):
        self.driver.save_screenshot(
            f"..\Screenshot\SS{randrange(1, 999)}.png"
        )

    def alert_box_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def alert_box_accept(self):
        alert = self.driver.switch_to.alert.accept()

    def page_down(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.PAGE_DOWN).perform()

    def scroll_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def clear_text(self, xpath):
        self.driver.find_element(*xpath).clear()

    def read_text(self, xpath):
        return self.driver.find_element(*xpath).text

    def check_element(self, xpath):
        # try:
        element = self.driver.find_element(*xpath)
        return element.is_displayed()
        # except NoSuchElementException:
        #     print(f"Element {xpath} not found.")
        #     return False
        # except TimeoutException:
        #     print(f"Timeout while trying to check if {xpath} is displayed.")
        #     return False
