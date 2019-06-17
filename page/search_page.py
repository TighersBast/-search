import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):

    search_edit_text = By.ID, "android:id/search_src_text"

    back_button = By.XPATH, "//*[@content-desc='收起']"

    @allure.step(title="正在输入")
    def input_search(self, value):
        allure.attach("输⼊", value, allure.attach_type.TEXT)
        self.input(self.search_edit_text, value)
        allure.attach("截图",self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title="点击返回")
    def click_back(self):
        self.click(self.back_button)