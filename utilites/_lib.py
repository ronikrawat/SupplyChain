from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from random import randrange

driver = webdriver.Chrome()


class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, xpath):
        self.driver.find_element(*xpath).click()

    def send_text(self, xpath, value):
        self.driver.find_element(*xpath).send_keys(value)

    def select_item(self, xpath, value):
        select = Select(self.driver.find_element(*xpath))
        select.select_by_visible_text(value)

    def move_curser(self, xpath):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*xpath)).perform()

    def screenshot(self):
        self.driver.save_screenshot(f"./Screenshot/SS{randrange(1, 999)}.png")
